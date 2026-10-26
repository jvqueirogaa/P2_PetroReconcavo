# -*- coding: utf-8 -*-
# =============================================================================
# P2 - AUDITORIA 1 (UnB 2026.2) - PetroReconcavo S.A. (RECV3) - exercicio 2025
# Preparador: matricula 211059370
#
# >>> SECAO DE SIMULACAO - BASE COMPLEMENTAR (folha e beneficios a empregados) <<<
# Complementa a base obrigatoria (imobilizado). Atende a orientacao de aula sobre beneficios a empregados:
# circulante (vence ate 31/12/2026) x nao circulante (a partir de 01/01/2027); riscos de empregado ficticio,
# cadastro duplicado e pagamento sem vinculo; controle maker-checker e trilha de alteracoes.
#
# !!! DADOS SINTETICOS. Nenhum empregado, CPF ou conta bancaria e real. !!!
# Ancoras REAIS: quadro de 1.752 empregados (249 em lideranca) em 31/12/2025 - FRE 2026 item 10.1A (F13);
# obrigacoes sociais e trabalhistas consolidadas R$ 88.753 mil (CVM 2.01.01, F03);
# despesa de pessoal consolidada 2025 R$ 284.002 mil (F01 NE 19, p.93);
# provisao para PLR inferida do IR diferido: R$ 11.054 mil / 34% = R$ 32.512 mil (F01 NE 10.2, p.77) - estimativa do preparador.
# Uso:  python codigo/gerar_base_folha.py
# =============================================================================
import os, json
import numpy as np
import pandas as pd

SEED = 211059370 + 7
rng = np.random.default_rng(SEED)
OUT = 'base_simulada/folha'; CTRL = 'base_simulada/controle_erros'
os.makedirs(OUT, exist_ok=True); os.makedirs(CTRL, exist_ok=True)
DB = pd.Timestamp('2025-12-31')
ATIVOS, LIDER = 1752, 249
OBRIG_TRAB = 88_753_000.00                  # CVM 2.01.01 consolidado (R$)
DESP_PESSOAL = 284_002_000.00               # NE 19 consolidado (R$)
PLR_PROV = round(11_054_000 / 0.34, 2)      # inferencia a partir do IR diferido (NE 10.2)
ENC_INSS, ENC_FGTS = 0.288, 0.08            # encargos patronais simulados (INSS+RAT+terceiros; FGTS)

# ---------------------------------------------------------------- 1) cadastro de empregados
n_desl = 190                                 # desligados ao longo de 2025 (turnover simulado)
N = ATIVOS + n_desl
lider = np.zeros(N, bool); lider[rng.choice(ATIVOS, LIDER, replace=False)] = True; lider[ATIVOS:] = rng.random(n_desl) < 0.08
polos = rng.choice(['SEDE SALVADOR', 'BAHIA - REMANSO', 'BAHIA - MIRANGA', 'BAHIA - SAO ROQUE (UTG)', 'POTIGUAR - MOSSORO', 'TIETA'], N, p=[.14, .22, .22, .08, .31, .03])
cad = pd.DataFrame({
    'matricula': [f'M{i:05d}' for i in range(1, N + 1)],
    'entidade': np.where(polos == 'TIETA', 'SPE_TIETA', 'PETRORECONCAVO'),
    'cpf_simulado': [f'SIM-{x:09d}' for x in pd.unique(rng.integers(100_000_000, 999_999_999, N * 2))[:N]],
    'nivel': np.where(lider, 'LIDERANCA', 'NAO_LIDERANCA'),
    'lotacao': polos,
    'data_admissao': pd.Timestamp('2000-03-01') + pd.to_timedelta((rng.beta(2.8, 1.3, N) * (pd.Timestamp('2025-11-30') - pd.Timestamp('2000-03-01')).days).astype(int), unit='D'),
    'data_desligamento': pd.NaT,
    'salario_base_mensal': np.where(lider, rng.lognormal(np.log(19000), 0.45, N), rng.lognormal(np.log(6200), 0.40, N)),
    'banco_agencia_conta': [f'{b}-{a:04d}-{c:07d}' for b, a, c in zip(rng.choice(['001', '104', '237', '341', '033', '756'], N), rng.integers(1, 9999, N), rng.integers(1, 9_999_999, N))],
    'contrato_trabalho_arquivado': 'S',
})
cad.loc[ATIVOS:, 'data_desligamento'] = pd.Timestamp('2025-01-10') + pd.to_timedelta(rng.integers(0, 345, n_desl), unit='D')
cad.loc[ATIVOS:, 'data_admissao'] = np.minimum(cad.loc[ATIVOS:, 'data_admissao'], cad.loc[ATIVOS:, 'data_desligamento'] - pd.Timedelta(days=200))
usr = [f'RH{i:02d}' for i in range(1, 9)]
cad['usuario_cadastro'] = rng.choice(usr, N)
cad['usuario_aprovacao'] = [usr[(usr.index(u) + int(o)) % len(usr)] for u, o in zip(cad.usuario_cadastro, rng.integers(1, len(usr), N))]
cad['data_ultima_alteracao_salarial'] = (cad.data_admissao + pd.to_timedelta(rng.integers(0, 900, N), unit='D')).clip(upper=DB)
cad['pct_ultimo_reajuste'] = np.round(rng.normal(0.055, 0.025, N).clip(0, 0.18), 4)
cad['aprovador_reajuste'] = rng.choice(['GERENCIA_RH', 'DIRETORIA_PESSOAS'], N, p=[.85, .15])

# ---------------------------------------------------------------- 2) folha de pagamentos 2025 (competencias jan-dez + 13o + ferias + PLR)
linhas = []
for comp in range(1, 13):
    ini = pd.Timestamp(2025, comp, 1); fim = ini + pd.offsets.MonthEnd(0)
    ativo = (cad.data_admissao <= fim) & (cad.data_desligamento.isna() | (cad.data_desligamento >= ini))
    c = cad[ativo]
    adic = rng.choice([0.0, 0.30], len(c), p=[.45, .55])                 # adicional de periculosidade (campo)
    he = rng.gamma(1.2, 0.04, len(c))
    for rub, mult in (('SALARIO', 1.0), ('ADICIONAL_PERICULOSIDADE', adic), ('HORAS_EXTRAS', he)):
        v = c.salario_base_mensal.values * mult
        m = v > 0
        linhas.append(pd.DataFrame({'competencia': f'2025-{comp:02d}', 'matricula': c.matricula.values[m], 'rubrica': rub, 'valor_bruto': v[m],
                                    'data_pagamento': (fim + pd.Timedelta(days=5)).date(), 'conta_credito': c.banco_agencia_conta.values[m]}))
ativos_dez = cad[cad.data_desligamento.isna()]
linhas.append(pd.DataFrame({'competencia': '2025-13', 'matricula': ativos_dez.matricula, 'rubrica': '13O_SALARIO', 'valor_bruto': ativos_dez.salario_base_mensal,
                            'data_pagamento': pd.Timestamp('2025-12-19').date(), 'conta_credito': ativos_dez.banco_agencia_conta}))
fer = cad.sample(frac=0.92, random_state=SEED)
linhas.append(pd.DataFrame({'competencia': rng.choice([f'2025-{m:02d}' for m in range(1, 13)], len(fer)), 'matricula': fer.matricula, 'rubrica': 'FERIAS_+1/3',
                            'valor_bruto': fer.salario_base_mensal * 4 / 3, 'data_pagamento': None, 'conta_credito': fer.banco_agencia_conta}))
plr = cad[cad.data_admissao < pd.Timestamp('2025-01-01')]
linhas.append(pd.DataFrame({'competencia': '2025-03', 'matricula': plr.matricula, 'rubrica': 'PLR_2024_PAGA', 'valor_bruto': plr.salario_base_mensal * rng.uniform(1.2, 2.6, len(plr)),
                            'data_pagamento': pd.Timestamp('2025-03-28').date(), 'conta_credito': plr.banco_agencia_conta}))
rescis = cad[cad.data_desligamento.notna()]
linhas.append(pd.DataFrame({'competencia': rescis.data_desligamento.dt.strftime('%Y-%m'), 'matricula': rescis.matricula, 'rubrica': 'VERBAS_RESCISORIAS',
                            'valor_bruto': rescis.salario_base_mensal * rng.uniform(1.5, 4.0, len(rescis)), 'data_pagamento': (rescis.data_desligamento + pd.Timedelta(days=10)).dt.date,
                            'conta_credito': rescis.banco_agencia_conta}))
folha = pd.concat(linhas, ignore_index=True)
folha['data_pagamento'] = folha.data_pagamento.fillna(pd.Timestamp('2025-06-30').date())

# calibracao: custo total do ano (bruto + encargos + beneficios + variacao de provisoes) = despesa de pessoal da NE 19
BENEF = 0.115                                # beneficios (saude, alimentacao, previdencia) sobre a folha bruta - premissa simulada
bruto = folha.valor_bruto.sum()
k = (DESP_PESSOAL - PLR_PROV * (1 + ENC_INSS + ENC_FGTS)) / (bruto * (1 + ENC_INSS + ENC_FGTS + BENEF))
folha['valor_bruto'] = (folha.valor_bruto * k).round(2)
cad['salario_base_mensal'] = (cad.salario_base_mensal * k).round(2)
folha['encargos_patronais'] = (folha.valor_bruto * (ENC_INSS + ENC_FGTS)).round(2)
folha['beneficios'] = (folha.valor_bruto * BENEF).round(2)

# ---------------------------------------------------------------- 3) obrigacoes trabalhistas em 31/12/2025 (por empregado) - total = CVM 2.01.01
prov = []
ad = cad[cad.data_desligamento.isna()].copy()
sal_dez = ad.salario_base_mensal
meses_fer = rng.integers(0, 12, len(ad)) + 1
for tipo, v, venc in (('SALARIO_DEZ_A_PAGAR', sal_dez * (1 + 0.55 * 0.30), pd.Timestamp('2026-01-05')),
                      ('INSS_FGTS_DEZ_A_RECOLHER', sal_dez * (ENC_INSS + ENC_FGTS), pd.Timestamp('2026-01-20')),
                      ('FERIAS_PROPORCIONAIS_+1/3', sal_dez * 4 / 3 * meses_fer / 12, pd.Timestamp('2026-06-30')),
                      ('ENCARGOS_SOBRE_FERIAS', sal_dez * 4 / 3 * meses_fer / 12 * (ENC_INSS + ENC_FGTS), pd.Timestamp('2026-06-30'))):
    prov.append(pd.DataFrame({'matricula': ad.matricula, 'tipo_obrigacao': tipo, 'valor': np.asarray(v, float), 'data_vencimento': venc}))
w = ad.salario_base_mensal * np.where(ad.nivel == 'LIDERANCA', 2.5, 1.0)
prov.append(pd.DataFrame({'matricula': ad.matricula, 'tipo_obrigacao': 'PLR_2025_PROVISIONADA', 'valor': w / w.sum() * PLR_PROV, 'data_vencimento': pd.Timestamp('2026-03-31')}))
prov = pd.concat(prov, ignore_index=True)
resto = OBRIG_TRAB - prov.valor.sum()
assert resto > 0, resto
n_out = 400; idx = rng.choice(len(ad), n_out, replace=False)
prov = pd.concat([prov, pd.DataFrame({'matricula': ad.matricula.values[idx], 'tipo_obrigacao': 'OUTRAS (ENCARGOS S/ PLR, RESCISOES, BENEFICIOS A PAGAR)',
                                      'valor': rng.dirichlet(np.ones(n_out)) * resto, 'data_vencimento': pd.Timestamp('2026-02-28')})], ignore_index=True)
prov['valor'] = prov.valor.round(2)
prov.loc[prov.valor.idxmax(), 'valor'] += round(OBRIG_TRAB - prov.valor.sum(), 2)   # fecha exatamente em centavos
prov['classificacao_registrada'] = 'CIRCULANTE'

# ---------------------------------------------------------------- 4) erros inseridos (log separado)
LOG = []
def log(tipo, ids, desc, efeito=0.0):
    for i, e in zip(ids, np.broadcast_to(efeito, len(ids))):
        LOG.append({'tipo_erro': tipo, 'chave': i, 'descricao': desc, 'efeito_monetario_R$': float(e)})
# F01 - empregado ficticio: pagamentos para matriculas que nao existem no cadastro
fic = [f'M{N + i:05d}' for i in range(1, 7)]
lf = []
for m in fic:
    s = float(rng.uniform(9000, 16000)); conta = f'341-{rng.integers(1, 9999):04d}-{rng.integers(1, 9_999_999):07d}'
    for comp in range(4, 13):
        lf.append(dict(competencia=f'2025-{comp:02d}', matricula=m, rubrica='SALARIO', valor_bruto=round(s, 2), data_pagamento=(pd.Timestamp(2025, comp, 1) + pd.offsets.MonthEnd(0) + pd.Timedelta(days=5)).date(),
                       conta_credito=conta, encargos_patronais=0.0, beneficios=0.0))
lf = pd.DataFrame(lf); folha = pd.concat([folha, lf], ignore_index=True)
for m in fic: log('F01', [m], 'Empregado ficticio: pagamentos de salario a matricula inexistente no cadastro', lf[lf.matricula == m].valor_bruto.sum())
# F02 - cadastro duplicado: mesmo CPF e/ou mesma conta bancaria para matriculas diferentes
src = rng.choice(len(ad), 9, replace=False)
dst = rng.choice(np.setdiff1d(np.arange(len(ad)), src), 9, replace=False)
for s_, d_ in zip(src[:5], dst[:5]):
    cad.loc[cad.matricula == ad.matricula.iloc[d_], 'cpf_simulado'] = ad.cpf_simulado.iloc[s_]; log('F02', [ad.matricula.iloc[d_]], 'CPF identico ao de outra matricula')
for s_, d_ in zip(src[5:], dst[5:]):
    cad.loc[cad.matricula == ad.matricula.iloc[d_], 'banco_agencia_conta'] = ad.banco_agencia_conta.iloc[s_]
    folha.loc[folha.matricula == ad.matricula.iloc[d_], 'conta_credito'] = ad.banco_agencia_conta.iloc[s_]
    log('F02', [ad.matricula.iloc[d_]], 'Conta bancaria de credito identica a de outra matricula')
# F03 - pagamento apos o desligamento (sem vinculo empregaticio)
dl = cad[cad.data_desligamento.notna() & (cad.data_desligamento < pd.Timestamp('2025-09-01'))].sample(8, random_state=SEED)
for _, r in dl.iterrows():
    comp = r.data_desligamento.month + 2
    lp = dict(competencia=f'2025-{comp:02d}', matricula=r.matricula, rubrica='SALARIO', valor_bruto=r.salario_base_mensal,
              data_pagamento=(pd.Timestamp(2025, comp, 1) + pd.offsets.MonthEnd(0) + pd.Timedelta(days=5)).date(), conta_credito=r.banco_agencia_conta,
              encargos_patronais=round(r.salario_base_mensal * (ENC_INSS + ENC_FGTS), 2), beneficios=0.0)
    folha = pd.concat([folha, pd.DataFrame([lp])], ignore_index=True)
    log('F03', [r.matricula], 'Salario pago apos a data de desligamento', r.salario_base_mensal)
# F04 - cadastro sem aprovacao ou aprovado pelo proprio cadastrador (maker-checker)
ix = rng.choice(len(cad), 30, replace=False)
cad.loc[cad.index[ix[:15]], 'usuario_aprovacao'] = ''
cad.loc[cad.index[ix[15:]], 'usuario_aprovacao'] = cad.loc[cad.index[ix[15:]], 'usuario_cadastro'].values
log('F04', cad.matricula.iloc[ix].tolist(), 'Cadastro de empregado sem aprovacao independente (maker-checker)')
# F05 - reajuste salarial acima de 30% sem aprovacao da diretoria (trilha de alteracoes)
ix = rng.choice(np.where(cad.data_desligamento.isna())[0], 12, replace=False)
cad.loc[cad.index[ix], 'pct_ultimo_reajuste'] = np.round(rng.uniform(0.32, 0.65, 12), 4); cad.loc[cad.index[ix], 'aprovador_reajuste'] = 'GERENCIA_RH'
cad.loc[cad.index[ix], 'data_ultima_alteracao_salarial'] = pd.Timestamp('2025-08-01') + pd.to_timedelta(rng.integers(0, 120, 12), unit='D')
log('F05', cad.matricula.iloc[ix].tolist(), 'Reajuste salarial > 30% sem aprovacao da Diretoria (alcada)')
# F06 - obrigacao com vencimento apos 31/12/2026 registrada como CIRCULANTE (classificacao)
iv = prov[prov.tipo_obrigacao.str.startswith('OUTRAS')].sample(25, random_state=SEED).index
prov.loc[iv, 'tipo_obrigacao'] = 'BONUS DE RETENCAO DIFERIDO'; prov.loc[iv, 'data_vencimento'] = pd.Timestamp('2027-03-31') + pd.to_timedelta(rng.integers(0, 300, 25), unit='D')
log('F06', [f'PROV-{i:06d}' for i in iv], 'Obrigacao com vencimento a partir de 01/01/2027 classificada no circulante', prov.loc[iv, 'valor'].values)

prov.insert(0, 'id_obrigacao', [f'PROV-{i:06d}' for i in prov.index])
for df in (cad, folha, prov): df['natureza_dado'] = 'SINTETICO'
folha.insert(0, 'id_lancamento', [f'FOL-{i:07d}' for i in range(1, len(folha) + 1)])
cad.to_csv(f'{OUT}/CADASTRO_EMPREGADOS_SIMULADO.csv', index=False, sep=';', decimal=',', encoding='utf-8-sig', date_format='%Y-%m-%d')
folha.to_csv(f'{OUT}/FOLHA_PAGAMENTOS_2025_SIMULADA.csv', index=False, sep=';', decimal=',', encoding='utf-8-sig')
prov.to_csv(f'{OUT}/OBRIGACOES_TRABALHISTAS_31122025_SIMULADAS.csv', index=False, sep=';', decimal=',', encoding='utf-8-sig', date_format='%Y-%m-%d')
pd.DataFrame(LOG).to_csv(f'{CTRL}/LOG_ERROS_INSERIDOS_FOLHA.csv', index=False, sep=';', decimal=',', encoding='utf-8-sig')
custo = folha.valor_bruto.sum() + folha.encargos_patronais.sum() + folha.beneficios.sum() + PLR_PROV * (1 + ENC_INSS + ENC_FGTS)
meta = dict(cadastro=len(cad), ativos_31122025=int(cad.data_desligamento.isna().sum()), lancamentos_folha=len(folha), obrigacoes=len(prov),
            total_obrigacoes=float(prov.valor.sum()), custo_pessoal_2025_simulado=float(custo), plr_inferida=PLR_PROV, erros=pd.DataFrame(LOG).tipo_erro.value_counts().sort_index().to_dict())
json.dump(meta, open(f'{OUT}/METADADOS_FOLHA.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(meta)
