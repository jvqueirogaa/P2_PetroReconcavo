# -*- coding: utf-8 -*-
# =============================================================================
# P2 - AUDITORIA 1 (UnB 2026.2) - PetroReconcavo S.A. (RECV3) - exercicio 2025
# Preparador: matricula 211059370
#
# >>> SECAO DE SIMULACAO <<<
# Gera a BASE SIMULADA (DADOS SINTETICOS) do subrazao analitico do IMOBILIZADO,
# conta de maior materialidade do ativo (72,2% do ativo consolidado - ver
# planilhas/DIAG_RECV3.xlsx, aba Ranking_Ativo).
#
# !!! OS DADOS GERADOS SAO SINTETICOS. NAO SAO REGISTROS REAIS DA COMPANHIA. !!!
# Os unicos dados REAIS usados sao os TOTAIS publicados na NE 7.1 da DFP 2025
# (F01 p.68-70), os totais operacionais do Relatorio da Administracao (producao
# e reservas por ativo, F01 p.5-8) e a lista publica de campos dos polos
# (FRE 2026 item 1.1, F13 p.5-8). Todo o detalhe analitico (itens, pocos, datas,
# fornecedores, usuarios, documentos) e simulado.
#
# Uso:  python codigo/gerar_base_imobilizado.py      (na raiz P2_PetroReconcavo)
# Reprodutivel: semente fixa = matricula (211059370).
# =============================================================================
import os, json, hashlib
import numpy as np
import pandas as pd

SEED = 211059370
rng = np.random.default_rng(SEED)
DATA_BASE = pd.Timestamp('2025-12-31')          # data do balanco
OUT = 'base_simulada'
CTRL = 'base_simulada/controle_erros'           # log dos erros inseridos (NAO usado pelos testes)
os.makedirs(OUT, exist_ok=True); os.makedirs(CTRL, exist_ok=True)

# -----------------------------------------------------------------------------
# 1) DADOS REAIS - alvos da NE 7.1 (R$ mil). Fonte: F01 p.68 (controladora) e
#    p.69 (consolidado). SPE Tieta = consolidado - controladora (inclui a
#    mais-valia de aquisicao alocada no consolidado).
#    (custo 31/12/2025, deprec/deplecao acumulada 31/12/2025, deprec 2025 = coluna "Adicoes")
# -----------------------------------------------------------------------------
NE7_CONTROLADORA = {
    'MAQUINAS_EQUIPAMENTOS': (716487, 103733, 38872),
    'IMOBILIZADO_EM_ANDAMENTO': (68419, 0, 0),
    'DIREITO_PRODUCAO_OLEO_GAS': (2851955, 850980, 131327),
    'DESENVOLVIMENTO_CAMPOS': (4018461, 1749489, 306122),
    'BLOCOS_EXPLORATORIOS': (9553, 0, 0),
    'ABANDONO_POCO_ARO': (73827, 36676, 1156),
    'ALMOXARIFADO_INVERSOES_FIXAS': (435242, 0, 0),
    'ADIANTAMENTOS': (15677, 0, 0),
    'OUTROS': (195997, 39032, 13895),
}
NE7_CONSOLIDADO = {
    'MAQUINAS_EQUIPAMENTOS': (718521, 103788, 38884),
    'IMOBILIZADO_EM_ANDAMENTO': (72171, 0, 0),
    'DIREITO_PRODUCAO_OLEO_GAS': (2931329, 922414, 132263),
    'DESENVOLVIMENTO_CAMPOS': (5186676, 2422704, 485386),
    'BLOCOS_EXPLORATORIOS': (20157, 0, 0),
    'ABANDONO_POCO_ARO': (79303, 41848, 1174),
    'ALMOXARIFADO_INVERSOES_FIXAS': (477651, 0, 0),
    'ADIANTAMENTOS': (18419, 0, 0),
    'OUTROS': (199325, 41957, 14161),
}
ENT_PR, ENT_TI = 'PETRORECONCAVO', 'SPE_TIETA'
ALVO = {ENT_PR: NE7_CONTROLADORA,
        ENT_TI: {k: tuple(NE7_CONSOLIDADO[k][i] - NE7_CONTROLADORA[k][i] for i in range(3)) for k in NE7_CONSOLIDADO}}
# Direito de producao por polo (NE 7.1 nota ii, F01 p.70) - custo, R$ mil
UPGN_CUSTO_MIL, UPGN_DEPREC_MIL = 284999, 4322     # NE 7.1, coluna 'UPGN Guamare' (maquinas): custo e depreciacao (F01 p.68-69)
DIREITO_POR_POLO = {'REMANSO': 95629, 'REMANSO_BT_REC': 1248, 'MIRANGA': 1247506, 'POTIGUAR': 1507572, 'TIETA': 79374}
# Totais operacionais reais (F01 RA p.5-8): producao media 2025 (boe/d) e reservas 31/12/2025 (MMboe)
PROD_BOED = {'BAHIA': 13400, 'POTIGUAR': 13100}
RES_1P = {'BAHIA': 87.3, 'POTIGUAR': 56.1}
RES_PDP_TOTAL = 61.4

# -----------------------------------------------------------------------------
# 2) SIMULACAO - cadastro de campos (58 concessoes, F01 NE 1) e pocos
#    Nomes reais quando publicados (FRE 2026 item 1.1 e NE 7.4); demais = codigo sintetico.
# -----------------------------------------------------------------------------
campos = []
def add(polo, ent, ativo, uf, nomes, data_aq):
    for n in nomes:
        campos.append(dict(campo=n, polo=polo, entidade=ent, ativo=ativo, uf=uf, data_aquisicao_polo=data_aq))
add('REMANSO', ENT_PR, 'BAHIA', 'BA', ['BREJINHO', 'CANABRAVA', 'CASSARONGONGO', 'FAZENDA BELEM', 'GOMO', 'MATA DE SAO JOAO',
    'NORTE FAZENDA CARUACU', 'REMANSO', 'RIO DOS OVOS', 'RIO SUBAUMA', 'SAO PEDRO', 'SESMARIA'], '2021-12-23')
add('MIRANGA', ENT_PR, 'BAHIA', 'BA', ['APRAIUS', 'BIRIBA', 'FAZENDA ONCA', 'JACUIPE', 'MIRANGA', 'MIRANGA NORTE', 'RIO PIPIRI',
    'RIACHO SAO PEDRO', 'SUSSUARANA'], '2021-12-07')
add('REMANSO_BT_REC', ENT_PR, 'BAHIA', 'BA', ['ACAJA-BURIZINHO', 'LAGOA DO PAULO NORTE', 'LAGOA DO PAULO', 'LAGOA DO PAULO SUL', 'JURITI'], '2003-06-01')
add('TIETA', ENT_TI, 'BAHIA', 'BA', ['TIE'], '2023-02-28')
add('TIETA', ENT_TI, 'BAHIA', 'SE', ['TARTARUGA'], '2023-02-28')
pot_reais = ['RIACHO DA FORQUILHA', 'SABIA', 'LIVRAMENTO', 'ACAUA', 'BAIXA DO ALGODAO', 'FAZENDA CURRAL', 'FAZENDA MALAQUIAS',
             'PAJEU', 'RIO MOSSORO', 'TRES MARIAS']
add('POTIGUAR', ENT_PR, 'POTIGUAR', 'RN', pot_reais + [f'POT-CONC-{i:02d} (SINTETICO)' for i in range(1, 21)], '2019-12-09')
campos = pd.DataFrame(campos)
assert len(campos) == 58
campos['sigla'] = [f'C{i:02d}' for i in range(1, 59)]
POCOS_POLO = {'POTIGUAR': 3500, 'REMANSO': 1550, 'MIRANGA': 1600, 'REMANSO_BT_REC': 400, 'TIETA': 150}
pesos = rng.lognormal(0, 0.8, len(campos))
campos['n_pocos'] = 0
for polo, n in POCOS_POLO.items():
    m = campos.polo == polo
    w = pesos[m.values] / pesos[m.values].sum()
    q = np.maximum(3, np.floor(w * n)).astype(int); q[np.argmax(q)] += n - q.sum()
    campos.loc[m, 'n_pocos'] = q
# producao e reservas por campo (rateio SINTETICO dos totais REAIS por ativo)
for ativo in ('BAHIA', 'POTIGUAR'):
    m = campos.ativo == ativo
    w = campos.loc[m, 'n_pocos'].values * rng.lognormal(0, 0.35, m.sum()); w = w / w.sum()
    campos.loc[m, 'producao_2025_boe'] = np.round(w * PROD_BOED[ativo] * 365)
    w2 = w * rng.lognormal(0, 0.25, m.sum()); w2 = w2 / w2.sum()
    campos.loc[m, 'reservas_1P_31122025_boe'] = np.round(w2 * RES_1P[ativo] * 1e6)
campos['reservas_PDP_31122025_boe'] = np.round(campos.reservas_1P_31122025_boe * RES_PDP_TOTAL / sum(RES_1P.values()) * rng.uniform(0.85, 1.15, 58))
campos['taxa_uop_1P_2025'] = campos.producao_2025_boe / (campos.reservas_1P_31122025_boe + campos.producao_2025_boe)
campos['taxa_uop_PDP_2025'] = campos.producao_2025_boe / (campos.reservas_PDP_31122025_boe + campos.producao_2025_boe)
campos['situacao_concessao'] = 'PRODUCAO'
campos['natureza_dado'] = 'NOMES/POLOS: publicos (F13, F01); quantidades por campo: SINTETICAS (rateio de totais reais por ativo)'

pocos = campos.loc[campos.index.repeat(campos.n_pocos), ['campo', 'sigla', 'polo', 'entidade', 'ativo', 'uf', 'data_aquisicao_polo']].reset_index(drop=True)
pocos['seq'] = pocos.groupby('campo').cumcount() + 1
pocos['poco_id'] = 'PRS-' + pocos.sigla + '-' + pocos.seq.astype(str).str.zfill(4)
# data de entrada do poco no grupo: na aquisicao do polo (pocos adquiridos) ou perfurado depois
aq = pd.to_datetime(pocos.data_aquisicao_polo)
novo = rng.random(len(pocos)) < 0.22
span = (DATA_BASE - aq).dt.days.values
pocos['data_entrada'] = aq + pd.to_timedelta(np.where(novo, (rng.beta(2.2, 1.2, len(pocos)) * span).astype(int), 0), unit='D')
pocos['origem_poco'] = np.where(novo, 'PERFURADO_PELO_GRUPO', 'ADQUIRIDO_COM_O_POLO')

# -----------------------------------------------------------------------------
# 3) SIMULACAO - plano de contas analitico do imobilizado (SINTETICO; a DFP nao divulga plano de contas)
# -----------------------------------------------------------------------------
PLANO = [
 ('1.2.03.01.001', 'Maquinas e equip. - sondas e equipamentos de perfuracao/producao', 'MAQUINAS_EQUIPAMENTOS', '1.2.03.91.001'),
 ('1.2.03.01.002', 'Maquinas e equip. - unidades de bombeio e elevacao artificial', 'MAQUINAS_EQUIPAMENTOS', '1.2.03.91.001'),
 ('1.2.03.01.003', 'Maquinas e equip. - compressores, separadores, tanques e facilities', 'MAQUINAS_EQUIPAMENTOS', '1.2.03.91.001'),
 ('1.2.03.01.004', 'Maquinas e equip. - UPGN Guamare (50% JOA Brava)', 'MAQUINAS_EQUIPAMENTOS', '1.2.03.91.001'),
 ('1.2.03.01.005', 'Maquinas e equip. - veiculos pesados e ferramentas', 'MAQUINAS_EQUIPAMENTOS', '1.2.03.91.001'),
 ('1.2.03.02.001', 'Imobilizado em andamento - projetos de facilities', 'IMOBILIZADO_EM_ANDAMENTO', ''),
 ('1.2.03.02.002', 'Imobilizado em andamento - pocos em perfuracao/completacao', 'IMOBILIZADO_EM_ANDAMENTO', ''),
 ('1.2.03.03.001', 'Direito de producao - Polo Remanso', 'DIREITO_PRODUCAO_OLEO_GAS', '1.2.03.93.001'),
 ('1.2.03.03.002', 'Direito de producao - Remanso BT-REC', 'DIREITO_PRODUCAO_OLEO_GAS', '1.2.03.93.001'),
 ('1.2.03.03.003', 'Direito de producao - Polo Miranga', 'DIREITO_PRODUCAO_OLEO_GAS', '1.2.03.93.001'),
 ('1.2.03.03.004', 'Direito de producao - Polo Potiguar', 'DIREITO_PRODUCAO_OLEO_GAS', '1.2.03.93.001'),
 ('1.2.03.03.005', 'Direito de producao - Polo Tieta (SPE Tieta)', 'DIREITO_PRODUCAO_OLEO_GAS', '1.2.03.93.001'),
 ('1.2.03.04.001', 'Desenvolvimento de campos - perfuracao e completacao', 'DESENVOLVIMENTO_CAMPOS', '1.2.03.94.001'),
 ('1.2.03.04.002', 'Desenvolvimento de campos - workover/recompletacao capitalizados', 'DESENVOLVIMENTO_CAMPOS', '1.2.03.94.001'),
 ('1.2.03.04.003', 'Desenvolvimento de campos - equipamentos de subsuperficie e cabeca de poco', 'DESENVOLVIMENTO_CAMPOS', '1.2.03.94.001'),
 ('1.2.03.04.004', 'Desenvolvimento de campos - linhas e instalacoes de superficie', 'DESENVOLVIMENTO_CAMPOS', '1.2.03.94.001'),
 ('1.2.03.04.005', 'Desenvolvimento de campos - pocos injetores e recuperacao secundaria', 'DESENVOLVIMENTO_CAMPOS', '1.2.03.94.001'),
 ('1.2.03.05.001', 'Blocos exploratorios', 'BLOCOS_EXPLORATORIOS', ''),
 ('1.2.03.06.001', 'Abandono de pocos - ativo de desmantelamento (ARO)', 'ABANDONO_POCO_ARO', '1.2.03.96.001'),
 ('1.2.03.07.001', 'Almoxarifado p/ inversoes fixas - tubulares (OCTG)', 'ALMOXARIFADO_INVERSOES_FIXAS', ''),
 ('1.2.03.07.002', 'Almoxarifado p/ inversoes fixas - hastes, bombas e componentes de elevacao', 'ALMOXARIFADO_INVERSOES_FIXAS', ''),
 ('1.2.03.07.003', 'Almoxarifado p/ inversoes fixas - equipamentos de superficie e valvulas', 'ALMOXARIFADO_INVERSOES_FIXAS', ''),
 ('1.2.03.07.004', 'Almoxarifado p/ inversoes fixas - materiais diversos', 'ALMOXARIFADO_INVERSOES_FIXAS', ''),
 ('1.2.03.08.001', 'Adiantamentos a fornecedores de imobilizado', 'ADIANTAMENTOS', ''),
 ('1.2.03.09.001', 'Outros - terrenos', 'OUTROS', ''),
 ('1.2.03.09.002', 'Outros - edificacoes e benfeitorias', 'OUTROS', '1.2.03.99.001'),
 ('1.2.03.09.003', 'Outros - moveis e utensilios', 'OUTROS', '1.2.03.99.001'),
 ('1.2.03.09.004', 'Outros - equipamentos de informatica', 'OUTROS', '1.2.03.99.001'),
 ('1.2.03.09.005', 'Outros - veiculos leves', 'OUTROS', '1.2.03.99.001'),
]
plano = pd.DataFrame(PLANO, columns=['conta_custo', 'descricao_conta', 'classe_ne7', 'conta_depreciacao'])
plano['natureza_dado'] = 'SINTETICO - plano de contas simulado; mapeado as classes reais da NE 7.1'
DESC_DEP = {'1.2.03.91.001': '(-) Depreciacao acumulada - maquinas e equipamentos', '1.2.03.93.001': '(-) Deplecao acumulada - direito de producao',
            '1.2.03.94.001': '(-) Deplecao acumulada - desenvolvimento de campos', '1.2.03.96.001': '(-) Deplecao acumulada - abandono de pocos',
            '1.2.03.99.001': '(-) Depreciacao acumulada - outros'}

# -----------------------------------------------------------------------------
# 4) SIMULACAO - geracao dos itens por classe
# -----------------------------------------------------------------------------
partes = []
def bloco(n, **cols):
    d = pd.DataFrame({k: (v if np.ndim(v) else np.repeat(v, n)) for k, v in cols.items()})
    partes.append(d); return d

def datas_unif(ini, fim, n, a=1.0, b=1.0):
    ini, fim = pd.Timestamp(ini), pd.Timestamp(fim)
    return ini + pd.to_timedelta((rng.beta(a, b, n) * (fim - ini).days).astype(int), unit='D')

# 4.1 Direito de producao: 1 registro por concessao + parcelas de ajuste de preco (earnout/ajustes)
for _, c in campos.iterrows():
    k = 1 + rng.poisson(0.4)
    bloco(k, entidade=c.entidade, polo=c.polo, campo=c.campo, uf=c.uf, poco_id='', classe_ne7='DIREITO_PRODUCAO_OLEO_GAS',
          conta_custo={'REMANSO': '1.2.03.03.001', 'REMANSO_BT_REC': '1.2.03.03.002', 'MIRANGA': '1.2.03.03.003', 'POTIGUAR': '1.2.03.03.004', 'TIETA': '1.2.03.03.005'}[c.polo],
          tipo_item=['CUSTO DE AQUISICAO DA CONCESSAO'] + ['AJUSTE DE PRECO DE AQUISICAO'] * (k - 1),
          origem={'TIETA': 'AQUISICAO_MAHA', 'REMANSO_BT_REC': 'RODADA_ANP'}.get(c.polo, 'AQUISICAO_PETROBRAS'),
          data_aquisicao=pd.Timestamp(c.data_aquisicao_polo) + pd.to_timedelta(np.r_[0, rng.integers(30, 700, k - 1)], unit='D'),
          metodo_depreciacao='UOP_1P', taxa_anual_linear=np.nan, peso=np.r_[1.0, rng.uniform(0.01, 0.05, k - 1)] * c.n_pocos * rng.uniform(0.7, 1.3))

# 4.2 Desenvolvimento de campos: componentes capitalizados por poco (perfuracao, completacao, workover, etc.)
TIPOS_DES = [('PERFURACAO E COMPLETACAO', '1.2.03.04.001', 9.0, 0.10), ('WORKOVER / RECOMPLETACAO CAPITALIZADO', '1.2.03.04.002', 6.0, 0.30),
             ('FRATURAMENTO / ESTIMULACAO CAPITALIZADA', '1.2.03.04.002', 6.3, 0.08), ('COLUNA DE PRODUCAO E HASTES', '1.2.03.04.003', 4.6, 0.20),
             ('BOMBA DE FUNDO (BM/BCP)', '1.2.03.04.003', 4.3, 0.12), ('CABECA DE POCO / ARVORE DE NATAL', '1.2.03.04.003', 4.4, 0.06),
             ('LINHA DE SURGENCIA E MANIFOLD', '1.2.03.04.004', 4.8, 0.09), ('CONVERSAO EM POCO INJETOR', '1.2.03.04.005', 5.9, 0.05)]
n_comp = 1 + rng.poisson(25.4, len(pocos))
idx = np.repeat(np.arange(len(pocos)), n_comp)
P = pocos.iloc[idx].reset_index(drop=True)
probs = np.array([t[3] for t in TIPOS_DES]); probs = probs / probs.sum()
tp = rng.choice(len(TIPOS_DES), len(P), p=probs)
ini = np.maximum(P.data_entrada.values.astype('datetime64[D]'), np.datetime64('2000-02-01'))
dias = (np.datetime64('2025-12-31') - ini).astype(int)
dt_des = ini + (rng.beta(1.6, 1.0, len(P)) * dias).astype('timedelta64[D]')
mu = np.array([TIPOS_DES[t][2] for t in tp])
bloco(len(P), entidade=P.entidade.values, polo=P.polo.values, campo=P.campo.values, uf=P.uf.values, poco_id=P.poco_id.values,
      classe_ne7='DESENVOLVIMENTO_CAMPOS', conta_custo=np.array([TIPOS_DES[t][1] for t in tp]), tipo_item=np.array([TIPOS_DES[t][0] for t in tp]),
      origem='CAPEX_PROPRIO', data_aquisicao=pd.to_datetime(dt_des), metodo_depreciacao='UOP_PDP', taxa_anual_linear=np.nan,
      peso=rng.lognormal(mu, 1.05))

# 4.3 Abandono de poco (ativo ARO): um registro por poco
bloco(len(pocos), entidade=pocos.entidade.values, polo=pocos.polo.values, campo=pocos.campo.values, uf=pocos.uf.values, poco_id=pocos.poco_id.values,
      classe_ne7='ABANDONO_POCO_ARO', conta_custo='1.2.03.06.001', tipo_item='CUSTO ESTIMADO DE ABANDONO (VALOR PRESENTE)', origem='ARO_REMENSURACAO',
      data_aquisicao=pocos.data_entrada.values, metodo_depreciacao='UOP_PDP', taxa_anual_linear=np.nan, peso=rng.lognormal(0, 0.45, len(pocos)))

# 4.4 Maquinas e equipamentos (depreciacao linear 10% a.a. - NE 7.2)
def maq(n, conta, tipo, mu, sd, d0, d1, ent=ENT_PR, origem='CAPEX_PROPRIO', polo=None):
    cc = campos[campos.entidade == ent].sample(n, replace=True, weights='n_pocos', random_state=int(rng.integers(1e9)))
    bloco(n, entidade=ent, polo=cc.polo.values if polo is None else polo, campo=cc.campo.values if polo is None else 'UPGN GUAMARE', uf=cc.uf.values if polo is None else 'RN',
          poco_id='', classe_ne7='MAQUINAS_EQUIPAMENTOS', conta_custo=conta, tipo_item=tipo, origem=origem,
          data_aquisicao=datas_unif(d0, d1, n, 1.4, 1.0), metodo_depreciacao='LINEAR', taxa_anual_linear=0.10, peso=rng.lognormal(mu, sd, n))
maq(2200, '1.2.03.01.001', 'COMPONENTE DE SONDA PROPRIA (PERFURACAO/PRODUCAO)', 11.2, 1.1, '2008-01-01', '2025-11-30')
maq(5200, '1.2.03.01.002', 'UNIDADE DE BOMBEIO MECANICO', 10.6, 0.5, '2009-01-01', '2025-11-30')
maq(8400, '1.2.03.01.003', 'COMPRESSOR/SEPARADOR/TANQUE/FACILITY', 10.4, 1.0, '2008-01-01', '2025-11-30')
maq(26000, '1.2.03.01.005', 'FERRAMENTA/EQUIPAMENTO DE CAMPO', 8.2, 1.0, '2012-01-01', '2025-11-30')
maq(850, '1.2.03.01.005', 'VEICULO PESADO / CAMINHAO SONDA', 11.0, 0.6, '2012-01-01', '2025-11-30')
maq(12, '1.2.03.01.001', 'EQUIPAMENTO DE CAMPO - SPE TIETA', 10.5, 0.8, '2023-03-01', '2025-11-30', ent=ENT_TI)
n_upgn = 3100
bloco(n_upgn, entidade=ENT_PR, polo='MIDSTREAM_RN', campo='UPGN GUAMARE', uf='RN', poco_id='', classe_ne7='MAQUINAS_EQUIPAMENTOS', conta_custo='1.2.03.01.004',
      tipo_item=rng.choice(['MODULO DE PROCESSAMENTO UPGN III', 'COMPRESSAO E RECEBIMENTO', 'ARMAZENAMENTO DE LIQUIDOS', 'GASODUTO DE INTERLIGACAO (TRECHO)',
                            'UTILIDADES E INSTRUMENTACAO', 'UPGN II (HIBERNADA)'], n_upgn, p=[.30, .18, .12, .15, .20, .05]),
      origem='AQUISICAO_BRAVA_JOA', data_aquisicao=pd.Timestamp('2025-09-30'), metodo_depreciacao='LINEAR', taxa_anual_linear=0.10, peso=rng.lognormal(11.0, 1.2, n_upgn))

# 4.5 Imobilizado em andamento
for ent, n in ((ENT_PR, 2350), (ENT_TI, 150)):
    cc = campos[campos.entidade == ent].sample(n, replace=True, weights='n_pocos', random_state=int(rng.integers(1e9)))
    bloco(n, entidade=ent, polo=cc.polo.values, campo=cc.campo.values, uf=cc.uf.values, poco_id='', classe_ne7='IMOBILIZADO_EM_ANDAMENTO',
          conta_custo=rng.choice(['1.2.03.02.001', '1.2.03.02.002'], n, p=[.55, .45]), tipo_item='ORDEM DE INVESTIMENTO EM ANDAMENTO', origem='CAPEX_PROPRIO',
          data_aquisicao=datas_unif('2024-07-01', '2025-12-20', n, 2.0, 1.0), metodo_depreciacao='NAO_DEPRECIA', taxa_anual_linear=np.nan, peso=rng.lognormal(9.6, 1.3, n))

# 4.6 Blocos exploratorios (NE 17.2) - 6 registros
for ent, polo, campo, uf, d in ((ENT_PR, 'POTIGUAR', 'BLOCO POT-T-702', 'RN', '2021-03-15'), (ENT_PR, 'POTIGUAR', 'BLOCO POT-T-742', 'RN', '2024-06-27'),
                                (ENT_PR, 'POTIGUAR', 'BLOCO POT-T-793', 'RN', '2024-06-27'), (ENT_TI, 'TIETA', 'BLOCO REC-T-129', 'BA', '2023-02-28'),
                                (ENT_TI, 'TIETA', 'BLOCO REC-T-142', 'BA', '2023-02-28'), (ENT_TI, 'TIETA', 'BLOCO REC-T-155', 'BA', '2023-02-28')):
    bloco(1, entidade=ent, polo=polo, campo=campo, uf=uf, poco_id='', classe_ne7='BLOCOS_EXPLORATORIOS', conta_custo='1.2.03.05.001',
          tipo_item='BONUS DE ASSINATURA E GASTOS EXPLORATORIOS', origem='RODADA_ANP' if ent == ENT_PR else 'AQUISICAO_MAHA',
          data_aquisicao=pd.Timestamp(d), metodo_depreciacao='NAO_DEPRECIA', taxa_anual_linear=np.nan, peso=rng.uniform(0.5, 1.5, 1))

# 4.7 Almoxarifado para inversoes fixas (lotes por SKU e deposito) - nao deprecia
TIPOS_AL = [('TUBO DE REVESTIMENTO/PRODUCAO (LOTE)', '1.2.03.07.001', 9.4, .26), ('HASTE DE BOMBEIO (LOTE)', '1.2.03.07.002', 8.6, .22),
            ('BOMBA DE FUNDO EM ESTOQUE', '1.2.03.07.002', 9.0, .12), ('VALVULA/EQUIPAMENTO DE SUPERFICIE', '1.2.03.07.003', 8.4, .18),
            ('MATERIAL DIVERSO DE INVESTIMENTO', '1.2.03.07.004', 7.2, .22)]
for ent, n in ((ENT_PR, 196000), (ENT_TI, 14000)):
    cc = campos[campos.entidade == ent].sample(n, replace=True, weights='n_pocos', random_state=int(rng.integers(1e9)))
    pr = np.array([t[3] for t in TIPOS_AL]); t = rng.choice(len(TIPOS_AL), n, p=pr / pr.sum())
    bloco(n, entidade=ent, polo=cc.polo.values, campo=cc.campo.values, uf=cc.uf.values, poco_id='', classe_ne7='ALMOXARIFADO_INVERSOES_FIXAS',
          conta_custo=np.array([TIPOS_AL[i][1] for i in t]), tipo_item=np.array([TIPOS_AL[i][0] for i in t]), origem='COMPRA_MATERIAL',
          data_aquisicao=datas_unif('2021-02-01', '2025-12-20', n, 2.6, 1.0), metodo_depreciacao='NAO_DEPRECIA', taxa_anual_linear=np.nan,
          peso=rng.lognormal(np.array([TIPOS_AL[i][2] for i in t]), 1.0))

# 4.8 Adiantamentos a fornecedores de imobilizado
for ent, n in ((ENT_PR, 1650), (ENT_TI, 150)):
    cc = campos[campos.entidade == ent].sample(n, replace=True, weights='n_pocos', random_state=int(rng.integers(1e9)))
    bloco(n, entidade=ent, polo=cc.polo.values, campo=cc.campo.values, uf=cc.uf.values, poco_id='', classe_ne7='ADIANTAMENTOS', conta_custo='1.2.03.08.001',
          tipo_item='ADIANTAMENTO CONTRATUAL A FORNECEDOR', origem='CAPEX_PROPRIO', data_aquisicao=datas_unif('2025-05-01', '2025-12-28', n, 2.0, 1.0),
          metodo_depreciacao='NAO_DEPRECIA', taxa_anual_linear=np.nan, peso=rng.lognormal(8.9, 1.1, n))

# 4.9 Outros (terrenos, edificacoes, moveis, TI, veiculos leves)
TIPOS_OU = [('TERRENO', '1.2.03.09.001', 11.5, .003, 0.0), ('EDIFICACAO / BENFEITORIA', '1.2.03.09.002', 10.4, .06, 0.04),
            ('MOVEL E UTENSILIO', '1.2.03.09.003', 7.0, .45, 0.10), ('EQUIPAMENTO DE INFORMATICA', '1.2.03.09.004', 7.6, .43, 0.20),
            ('VEICULO LEVE', '1.2.03.09.005', 11.2, .057, 0.20)]
for ent, n in ((ENT_PR, 74000), (ENT_TI, 1200)):
    cc = campos[campos.entidade == ent].sample(n, replace=True, weights='n_pocos', random_state=int(rng.integers(1e9)))
    pr = np.array([t[3] for t in TIPOS_OU]); t = rng.choice(len(TIPOS_OU), n, p=pr / pr.sum())
    tx = np.array([TIPOS_OU[i][4] for i in t])
    bloco(n, entidade=ent, polo=cc.polo.values, campo=cc.campo.values, uf=cc.uf.values, poco_id='', classe_ne7='OUTROS',
          conta_custo=np.array([TIPOS_OU[i][1] for i in t]), tipo_item=np.array([TIPOS_OU[i][0] for i in t]), origem='CAPEX_PROPRIO',
          data_aquisicao=datas_unif('2006-01-01', '2025-11-30', n, 1.8, 1.0), metodo_depreciacao=np.where(tx > 0, 'LINEAR', 'NAO_DEPRECIA'),
          taxa_anual_linear=np.where(tx > 0, tx, np.nan), peso=rng.lognormal(np.array([TIPOS_OU[i][2] for i in t]), 0.9))

base = pd.concat(partes, ignore_index=True)
base['data_aquisicao'] = pd.to_datetime(base.data_aquisicao)

# -----------------------------------------------------------------------------
# 5) SIMULACAO - atributos de controle (cadastro, aprovacao, documentos, fornecedores)
# -----------------------------------------------------------------------------
N = len(base)
usuarios = [f'USR{i:03d}' for i in range(1, 29)]
base['usuario_cadastro'] = rng.choice(usuarios, N)
off = rng.integers(1, len(usuarios), N)
base['usuario_aprovacao'] = [usuarios[(usuarios.index(u) + o) % len(usuarios)] for u, o in zip(base.usuario_cadastro, off)]   # sempre != maker
base['data_cadastro_sistema'] = base.data_aquisicao + pd.to_timedelta(rng.integers(0, 25, N), unit='D')
base['data_cadastro_sistema'] = base.data_cadastro_sistema.where(base.data_cadastro_sistema <= DATA_BASE, DATA_BASE)
base['data_ultima_alteracao'] = base.data_cadastro_sistema + pd.to_timedelta((rng.random(N) < 0.3) * rng.integers(0, 400, N), unit='D')
base['data_ultima_alteracao'] = base.data_ultima_alteracao.where(base.data_ultima_alteracao <= DATA_BASE, DATA_BASE)
pref = base.classe_ne7.map({'ALMOXARIFADO_INVERSOES_FIXAS': 'NF', 'ADIANTAMENTOS': 'CTR', 'DIREITO_PRODUCAO_OLEO_GAS': 'CCV',
                            'ABANDONO_POCO_ARO': 'MEM', 'BLOCOS_EXPLORATORIOS': 'ANP'}).fillna('OI')
base['documento_origem'] = pref + '-' + pd.Series(rng.permutation(np.arange(1_000_000, 1_000_000 + N))).astype(str).values
base['fornecedor_id'] = 'FORN-' + pd.Series(rng.zipf(1.6, N) % 4800 + 1).astype(str).str.zfill(5).values
base.loc[base.classe_ne7 == 'DIREITO_PRODUCAO_OLEO_GAS', 'fornecedor_id'] = base.loc[base.classe_ne7 == 'DIREITO_PRODUCAO_OLEO_GAS'].apply(
    lambda r: {'AQUISICAO_PETROBRAS': 'PETROBRAS', 'AQUISICAO_MAHA': 'VENDEDORES_MAHA', 'RODADA_ANP': 'ANP'}[r.origem], axis=1)
base.loc[base.classe_ne7.isin(['ABANDONO_POCO_ARO']), 'fornecedor_id'] = 'N/A (ESTIMATIVA)'
base.loc[base.classe_ne7.isin(['BLOCOS_EXPLORATORIOS']), 'fornecedor_id'] = 'ANP'
base.loc[base.origem == 'AQUISICAO_BRAVA_JOA', 'fornecedor_id'] = '3R POTIGUAR (BRAVA)'
base['centro_custo'] = 'CC-' + base.polo.str[:3] + '-' + base.classe_ne7.str[:4]
base['status'] = base.classe_ne7.map({'IMOBILIZADO_EM_ANDAMENTO': 'EM_CONSTRUCAO', 'ALMOXARIFADO_INVERSOES_FIXAS': 'EM_ESTOQUE',
                                      'ADIANTAMENTOS': 'ADIANTAMENTO', 'BLOCOS_EXPLORATORIOS': 'EXPLORACAO'}).fillna('EM_OPERACAO')
base['data_baixa'] = pd.NaT
base['garantia_judicial'] = 'N'
i_sonda = base[(base.tipo_item.str.startswith('COMPONENTE DE SONDA'))].peso.idxmax()
base.loc[i_sonda, 'garantia_judicial'] = 'S'          # NE 7.3 - sonda dada em garantia de execucao fiscal

# -----------------------------------------------------------------------------
# 6) Funcoes de escala exata em CENTAVOS (metodo do maior resto)
# -----------------------------------------------------------------------------
def rateio_centavos(pesos, total_centavos):
    p = np.asarray(pesos, float); p = p / p.sum() * total_centavos
    piso = np.floor(p).astype(np.int64); falta = int(total_centavos - piso.sum())
    if falta > 0:
        piso[np.argsort(-(p - piso))[:falta]] += 1
    return piso

OFFSET = {}   # diferenca simulada de arredondamento (DF publicada em R$ mil): |offset| <= R$ 240 por grupo
def alvo_centavos(ent, classe, i):
    k = (ent, classe, i)
    if k not in OFFSET:
        OFFSET[k] = int(rng.integers(-240, 241)) if ALVO[ent][classe][i] != 0 else 0
    return (ALVO[ent][classe][i] * 1000 + OFFSET[k]) * 100

# -----------------------------------------------------------------------------
# 7) Duplicidades (ERRO E01) inseridas ANTES do rateio, para que o total contabil continue igual a DF
# -----------------------------------------------------------------------------
LOG = []
elig = base[base.classe_ne7.isin(['MAQUINAS_EQUIPAMENTOS', 'ALMOXARIFADO_INVERSOES_FIXAS', 'OUTROS', 'DESENVOLVIMENTO_CAMPOS']) & (base.origem != 'AQUISICAO_BRAVA_JOA')]   # UPGN preservada (totais proprios na NE 7.1)
elig = elig[elig.data_cadastro_sistema <= DATA_BASE - pd.Timedelta(days=61)]   # garante que a copia seja cadastrada DEPOIS do original
dup_src = elig.sample(160, weights=np.sqrt(elig.peso), random_state=SEED).index
dups = base.loc[dup_src].copy()
dups['usuario_cadastro'] = rng.choice(usuarios, len(dups))
dups['data_cadastro_sistema'] = (dups.data_cadastro_sistema + pd.to_timedelta(rng.integers(3, 60, len(dups)), unit='D')).clip(upper=DATA_BASE)
dups['_dup_de'] = dup_src
base['_dup_de'] = -1
base = pd.concat([base, dups], ignore_index=True)

# -----------------------------------------------------------------------------
# 8) Custo: rateio exato por entidade x classe (direito de producao: por polo)
# -----------------------------------------------------------------------------
base['custo_centavos'] = np.int64(0)
for ent in (ENT_PR, ENT_TI):
    for classe in ALVO[ent]:
        m = (base.entidade == ent) & (base.classe_ne7 == classe)
        if classe == 'DIREITO_PRODUCAO_OLEO_GAS':
            for polo, v in DIREITO_POR_POLO.items():
                mp = m & (base.polo == polo)
                if mp.any():
                    tot = (v * 1000 + int(rng.integers(-240, 241))) * 100
                    base.loc[mp, 'custo_centavos'] = rateio_centavos(base.loc[mp, 'peso'], tot)
        elif classe == 'MAQUINAS_EQUIPAMENTOS' and ent == ENT_PR:
            # UPGN Guamare: custo transferido na NE 7.1 (coluna "UPGN Guamare") = R$ 284.999 mil (F01 p.68-69) - alvo proprio
            mu = m & (base.origem == 'AQUISICAO_BRAVA_JOA'); tot_u = UPGN_CUSTO_MIL * 1000 * 100
            base.loc[mu, 'custo_centavos'] = rateio_centavos(base.loc[mu, 'peso'], tot_u)
            base.loc[m & ~mu, 'custo_centavos'] = rateio_centavos(base.loc[m & ~mu, 'peso'], alvo_centavos(ent, classe, 0) - tot_u)
        else:
            base.loc[m, 'custo_centavos'] = rateio_centavos(base.loc[m, 'peso'], alvo_centavos(ent, classe, 0))
# duplicatas precisam ter exatamente o mesmo valor do original: copia o valor e compensa a diferenca no item de maior valor da classe
for i in base.index[base._dup_de >= 0]:
    o = base.at[i, '_dup_de']; delta = base.at[o, 'custo_centavos'] - base.at[i, 'custo_centavos']
    base.at[i, 'custo_centavos'] = base.at[o, 'custo_centavos']
    m = (base.entidade == base.at[i, 'entidade']) & (base.classe_ne7 == base.at[i, 'classe_ne7']) & (base._dup_de < 0) & (~base.index.isin(base._dup_de)) & (base.origem != 'AQUISICAO_BRAVA_JOA')
    j = base.loc[m, 'custo_centavos'].idxmax(); base.at[j, 'custo_centavos'] -= delta

# -----------------------------------------------------------------------------
# 9) Depreciacao/deplecao acumulada e do exercicio
# -----------------------------------------------------------------------------
base['dep_acum_centavos'] = np.int64(0); base['dep_2025_centavos'] = np.int64(0)
base['data_inicio_depreciacao'] = pd.NaT
anos_ate_base = (DATA_BASE - base.data_aquisicao).dt.days / 365.25

# 9.1 LINEAR - calibracao dupla: (i) depreciacao acumulada = NE 7.1 e (ii) depreciacao do exercicio 2025 = coluna "Adicoes" da NE 7.1.
#     Cada item recebe uma razao r = acumulada/custo; a data de inicio da depreciacao e derivada de r (r = taxa x anos),
#     o que permite ao auditor RECALCULAR cada item. Parte dos itens mais antigos fica totalmente depreciada antes de 2025
#     (r = 1; despesa 2025 = 0) - a fracao p e achada por bissecao para que a despesa do ano bata com a NE.
#     Despesa 2025 de um item = custo x [r - max(0, r - taxa)] = custo x min(r, taxa).
CALIB_LINEAR = {}
for ent in (ENT_PR, ENT_TI):
    for classe in ('MAQUINAS_EQUIPAMENTOS', 'OUTROS'):
        m = (base.entidade == ent) & (base.classe_ne7 == classe) & (base.metodo_depreciacao == 'LINEAR')
        idx_m = base.index[m]
        c = base.loc[m, 'custo_centavos'].astype(float).values; tx = base.loc[m, 'taxa_anual_linear'].values.astype(float)
        anos = anos_ate_base[m].values.clip(min=0.02)
        fixo = (base.loc[m, 'origem'] == 'AQUISICAO_BRAVA_JOA').values
        A = float(alvo_centavos(ent, classe, 1)); D = float(alvo_centavos(ent, classe, 2))
        r = np.zeros(len(c))
        if fixo.any():                                                        # UPGN: acumulada = despesa 2025 = R$ 4.322 mil (NE 7.1)
            r[fixo] = rateio_centavos(c[fixo], UPGN_DEPREC_MIL * 1000 * 100) / c[fixo]
            A -= (c[fixo] * r[fixo]).sum(); D -= (c[fixo] * r[fixo]).sum()
        livres = np.where(~fixo)[0]
        LIM_ANOS = 25.8                                                       # inicio da operacao: fev/2000 (FRE 1.1) -> no maximo ~25,8 anos de uso
        podeF = livres[(1 / tx[livres] + 1) <= LIM_ANOS - 0.3]                # so pode estar 100% depreciado antes de 2025 quem tem vida util compativel
        ordem = podeF[np.argsort(-anos[podeF])]                               # mais antigos primeiro
        def resolver(p):
            k = int(round(p * len(ordem))); F = ordem[:k]; O = np.setdiff1d(livres, F)
            rr = np.zeros(len(c)); rr[F] = 1.0
            resto = A - c[F].sum()
            if resto <= 0 or len(O) == 0: return rr, -1.0, F, O
            nat = np.minimum(0.98, tx[O] * anos[O]); f = resto / max((c[O] * nat).sum(), 1)
            for _ in range(80):
                rO = np.minimum(0.98, nat * f); f *= resto / max((c[O] * rO).sum(), 1)
            rr[O] = np.minimum(0.98, nat * f)
            dep = (c[O] * np.minimum(rr[O], tx[O])).sum()
            return rr, dep, F, O
        lo, hi = 0.0, 1.0
        for _ in range(60):                                                   # bissecao em p (despesa decresce com p)
            p = (lo + hi) / 2; rr, dep, F, O = resolver(p)
            if dep < 0 or dep < D: hi = p
            else: lo = p
        rr, dep, F, O = resolver(lo)
        r[livres] = rr[livres]
        CALIB_LINEAR[f'{ent}|{classe}'] = dict(fracao_itens_totalmente_depreciados=round(lo, 4), despesa_alvo=D / 100, despesa_obtida=dep / 100)
        # datas coerentes com r
        anos_cont = np.where(r >= 0.999999, np.minimum(1 / tx + 1 + rng.uniform(0, 4, len(c)), LIM_ANOS), r / tx)
        base.loc[idx_m, 'data_inicio_depreciacao'] = DATA_BASE - pd.to_timedelta(np.round(anos_cont * 365.25), unit='D')
        base.loc[idx_m, 'dep_acum_centavos'] = np.round(c * r).astype(np.int64)
        base.loc[idx_m, 'dep_2025_centavos'] = np.round(c * np.where(r >= 0.999999, 0.0, np.minimum(r, tx))).astype(np.int64)
        base.loc[idx_m[fixo], 'dep_2025_centavos'] = base.loc[idx_m[fixo], 'dep_acum_centavos']

# 9.2 UNIDADES PRODUZIDAS: acumulada por idade (escala exata) e deplecao 2025 = VCL x t/(1-t), t = taxa do campo x k calibrado
tx_campo = campos.set_index('campo')
for ent in (ENT_PR, ENT_TI):
    for classe, col_tx in (('DIREITO_PRODUCAO_OLEO_GAS', 'taxa_uop_1P_2025'), ('DESENVOLVIMENTO_CAMPOS', 'taxa_uop_PDP_2025'), ('ABANDONO_POCO_ARO', 'taxa_uop_PDP_2025')):
        m = (base.entidade == ent) & (base.classe_ne7 == classe)
        if not m.any(): continue
        c = base.loc[m, 'custo_centavos'].astype(float).values
        anos = anos_ate_base[m].values.clip(min=0)
        r0 = (1 - np.exp(-0.16 * anos)) * rng.uniform(0.7, 1.3, m.sum())
        alvo_acum = alvo_centavos(ent, classe, 1); f = alvo_acum / max((c * r0).sum(), 1)
        for _ in range(60):
            r = np.minimum(0.985, r0 * f); f *= alvo_acum / max((c * r).sum(), 1)
        r = np.minimum(0.985, r0 * f)
        base.loc[m, 'dep_acum_centavos'] = rateio_centavos(np.maximum(c * r, 1e-9), alvo_acum) if alvo_acum > 0 else 0
        vcl = c - base.loc[m, 'dep_acum_centavos'].values
        t = base.loc[m, 'campo'].map(tx_campo[col_tx]).values
        frac = np.where(base.loc[m, 'data_aquisicao'].dt.year.values == 2025, (DATA_BASE - base.loc[m, 'data_aquisicao']).dt.days.values / 365.0, 1.0)
        alvo_dep = alvo_centavos(ent, classe, 2)
        lo, hi = 1e-6, 1 / max(t.max(), 1e-9) * 0.95
        for _ in range(100):                                                  # bissecao do fator k
            k = (lo + hi) / 2; tk = np.minimum(t * k, 0.9)
            tot = (vcl * tk / (1 - tk) * frac).sum()
            lo, hi = (k, hi) if tot < alvo_dep else (lo, k)
        tk = np.minimum(t * k, 0.9)
        base.loc[m, 'dep_2025_centavos'] = rateio_centavos(np.maximum(vcl * tk / (1 - tk) * frac, 1e-9), alvo_dep)
        base.loc[m, 'fator_calibracao_uop'] = k
        base.loc[m, 'data_inicio_depreciacao'] = base.loc[m, 'data_aquisicao']
base['taxa_uop_campo_2025'] = np.where(base.metodo_depreciacao == 'UOP_1P', base.campo.map(tx_campo.taxa_uop_1P_2025),
                              np.where(base.metodo_depreciacao == 'UOP_PDP', base.campo.map(tx_campo.taxa_uop_PDP_2025), np.nan))
# duplicatas: mesma acumulada do original (o erro e a duplicidade integral do registro)
for i in base.index[base._dup_de >= 0]:
    o = base.at[i, '_dup_de']
    for col in ('dep_acum_centavos', 'dep_2025_centavos', 'data_inicio_depreciacao'):
        base.at[i, col] = base.at[o, col]

def log(tipo, idx, descricao, efeito_centavos, campo_alterado='', original='', inserido=''):
    for k, i in enumerate(idx):
        LOG.append(dict(tipo_erro=tipo, id_interno=int(i), descricao=descricao, efeito_monetario_centavos=int(efeito_centavos[k]) if np.ndim(efeito_centavos) else int(efeito_centavos),
                        campo_alterado=campo_alterado, valor_original=str(original[k]) if np.ndim(original) else str(original),
                        valor_inserido=str(inserido[k]) if np.ndim(inserido) else str(inserido)))

vcl_tmp = base.custo_centavos - base.dep_acum_centavos
log('E01', base.index[base._dup_de >= 0], 'Registro duplicado (mesmo documento, fornecedor, valor e data de aquisicao do registro original)',
    vcl_tmp[base._dup_de >= 0].values, 'registro inteiro', base.loc[base._dup_de >= 0, '_dup_de'].values, 'copia')

# -----------------------------------------------------------------------------
# 10) INSERCAO DOS DEMAIS ERROS (registro no LOG; os testes NAO leem o LOG)
# -----------------------------------------------------------------------------
usado = set(base.index[base._dup_de >= 0]) | set(base._dup_de[base._dup_de >= 0]) | {i_sonda}
def escolher(mask, n, peso=None, orcamento=None, valor=None):
    """sorteio sem reposicao (ponderado pelo valor quando 'peso' e informado - metodo de Efraimidis-Spirakis);
    com 'orcamento', para quando o efeito monetario acumulado atinge o orcamento (em centavos)."""
    cand = base.index[mask & ~base.index.isin(list(usado)) & (base.origem != 'AQUISICAO_BRAVA_JOA')]   # itens da UPGN nao recebem erros
    if peso is None:
        ordem = rng.permutation(cand)
    else:
        w = np.maximum(base.loc[cand, peso].astype(float).values, 1.0)
        ordem = cand[np.argsort(-np.log(rng.random(len(cand))) / w)]
    ordem = np.asarray(ordem)
    if orcamento is not None:
        acum = np.cumsum(valor.loc[ordem[:n]].values)
        ordem = ordem[:max(1, np.searchsorted(acum, orcamento) + 1)]
    ordem = ordem[:n]
    usado.update(ordem.tolist()); return ordem

VCL = lambda: base.custo_centavos - base.dep_acum_centavos
nao_dep = base.metodo_depreciacao == 'NAO_DEPRECIA'
linear = base.metodo_depreciacao == 'LINEAR'

# E02 - corte: item capitalizado em 2026 (posterior a data-base) incluido no saldo de 31/12/2025
faixa = lambda a, b: (VCL() >= a * 100) & (VCL() <= b * 100)          # faixa de valor liquido (R$) dos itens elegiveis
base['_raiz'] = np.sqrt(base.custo_centavos.astype(float))
ix = escolher(base.classe_ne7.isin(['MAQUINAS_EQUIPAMENTOS', 'ALMOXARIFADO_INVERSOES_FIXAS', 'IMOBILIZADO_EM_ANDAMENTO', 'OUTROS', 'DESENVOLVIMENTO_CAMPOS'])
              & faixa(5_000, 400_000), 90, orcamento=250_000_000, valor=VCL(), peso='_raiz')
novas = pd.Timestamp('2026-01-02') + pd.to_timedelta(rng.integers(0, 75, len(ix)), unit='D')
log('E02', ix, 'Corte: data de aquisicao/capitalizacao posterior a 31/12/2025 (item nao existia na data-base)', VCL().loc[ix].values, 'data_aquisicao',
    base.loc[ix, 'data_aquisicao'].dt.date.values, novas.date)
base.loc[ix, 'data_aquisicao'] = novas; base.loc[ix, 'data_cadastro_sistema'] = novas; base.loc[ix, 'data_ultima_alteracao'] = novas
base.loc[ix, 'data_inicio_depreciacao'] = novas
# o saldo contabil (custo) e mantido; acumulada mantida (o erro e de existencia/corte, nao de calculo)

# E03 - depreciacao acumulada maior que o custo (valor liquido negativo) - itens lineares
ix = escolher(linear & (base.custo_centavos > 2_000_000), 40)
nova = (base.loc[ix, 'custo_centavos'] * rng.uniform(1.05, 1.6, len(ix))).round().astype(np.int64)
log('E03', ix, 'Depreciacao acumulada superior ao custo (valor contabil liquido negativo)', -(nova - base.loc[ix, 'custo_centavos']).values,
    'dep_acum_centavos', base.loc[ix, 'dep_acum_centavos'].values, nova.values)
base.loc[ix, 'dep_acum_centavos'] = nova.values

# E04 - depreciacao acumulada subavaliada (diverge do recalculo pela taxa e pela data de inicio)
ix = escolher(linear & (base.dep_acum_centavos > 500_000) & (base.origem != 'AQUISICAO_BRAVA_JOA'), 320, orcamento=150_000_000,
              valor=(base.dep_acum_centavos * 0.45), peso='dep_acum_centavos')
fator = rng.uniform(0.25, 0.65, len(ix)); nova = (base.loc[ix, 'dep_acum_centavos'] * (1 - fator)).round().astype(np.int64)
log('E04', ix, 'Depreciacao acumulada registrada a menor que o recalculo (taxa x tempo de uso)', (base.loc[ix, 'dep_acum_centavos'] - nova).values,
    'dep_acum_centavos', base.loc[ix, 'dep_acum_centavos'].values, nova.values)
base.loc[ix, 'dep_acum_centavos'] = nova.values

# E05 - item baixado (sucateado/alienado em 2025) ainda com saldo
ix = escolher(base.classe_ne7.isin(['MAQUINAS_EQUIPAMENTOS', 'OUTROS', 'DESENVOLVIMENTO_CAMPOS']) & faixa(3_000, 300_000), 130, orcamento=250_000_000, valor=VCL(), peso='_raiz')
db = pd.Timestamp('2025-01-15') + pd.to_timedelta(rng.integers(0, 340, len(ix)), unit='D')
log('E05', ix, 'Item com status BAIXADO (baixa em 2025) mantido com saldo no subrazao', VCL().loc[ix].values, 'status/data_baixa', 'EM_OPERACAO', 'BAIXADO')
base.loc[ix, 'status'] = 'BAIXADO'; base.loc[ix, 'data_baixa'] = db.values

# E06 - almoxarifado sem movimentacao ha mais de 5 anos (risco de obsolescencia/valor recuperavel)
ix = escolher(base.classe_ne7 == 'ALMOXARIFADO_INVERSOES_FIXAS', 95)
novas = datas_unif('2014-01-01', '2020-10-31', len(ix))
log('E06', ix, 'Material de almoxarifado de investimento sem movimentacao ha mais de 5 anos (indicio de obsolescencia)', 0, 'data_aquisicao',
    base.loc[ix, 'data_aquisicao'].dt.date.values, novas.date)
base.loc[ix, 'data_aquisicao'] = novas.values; base.loc[ix, 'data_cadastro_sistema'] = novas.values; base.loc[ix, 'data_ultima_alteracao'] = novas.values

# E07 - falha de segregacao (maker-checker): aprovacao ausente ou feita pelo proprio cadastrador
ix = escolher(pd.Series(True, index=base.index), 620)
metade = len(ix) // 2
log('E07', ix[:metade], 'Cadastro sem aprovacao (campo usuario_aprovacao vazio)', 0, 'usuario_aprovacao', base.loc[ix[:metade], 'usuario_aprovacao'].values, '')
log('E07', ix[metade:], 'Cadastro aprovado pelo proprio usuario que cadastrou (maker = checker)', 0, 'usuario_aprovacao', base.loc[ix[metade:], 'usuario_aprovacao'].values,
    base.loc[ix[metade:], 'usuario_cadastro'].values)
base.loc[ix[:metade], 'usuario_aprovacao'] = ''
base.loc[ix[metade:], 'usuario_aprovacao'] = base.loc[ix[metade:], 'usuario_cadastro'].values

# E08 - item vinculado a campo inexistente no cadastro de concessoes e sem documento de suporte
ix = escolher(base.classe_ne7.isin(['DESENVOLVIMENTO_CAMPOS', 'MAQUINAS_EQUIPAMENTOS']) & faixa(3_000, 150_000), 55, orcamento=120_000_000, valor=VCL(), peso='_raiz')
falsos = rng.choice(['CAMPO X-01', 'FAZENDA NOVA', 'POT-CONC-99 (SINTETICO)'], len(ix))
log('E08', ix, 'Campo nao cadastrado entre as 58 concessoes e documento de suporte inexistente (existencia)', VCL().loc[ix].values, 'campo', base.loc[ix, 'campo'].values, falsos)
base.loc[ix, 'campo'] = falsos

# E09 - superavaliacao de custo (despesa capitalizada / valor acima do documento) - so aparece na inspecao documental
VCLs = VCL()
ix = escolher(base.classe_ne7.isin(['DESENVOLVIMENTO_CAMPOS', 'MAQUINAS_EQUIPAMENTOS', 'ALMOXARIFADO_INVERSOES_FIXAS', 'IMOBILIZADO_EM_ANDAMENTO'])
              & (VCLs >= 2_000_000) & (VCLs <= 300_000_000), 400, peso='_raiz', orcamento=800_000_000, valor=VCLs * 0.4)
taint = np.where(rng.random(len(ix)) < 0.06, 1.0, rng.uniform(0.05, 0.75, len(ix)))
efeito = np.round(VCLs.loc[ix].values * taint).astype(np.int64)
log('E09', ix, 'Custo registrado acima do suportado por documento (inclui despesa de manutencao capitalizada)', efeito, 'valor suportado (arquivo de inspecao)',
    VCLs.loc[ix].values, (VCLs.loc[ix].values - efeito))
E09_SUPORTE = dict(zip(ix, VCLs.loc[ix].values - efeito))

# E10 - imobilizado em andamento parado ha mais de 2 anos (indicio de impairment / transferencia tardia)
ix = escolher(base.classe_ne7 == 'IMOBILIZADO_EM_ANDAMENTO', 45)
novas = datas_unif('2019-01-01', '2023-09-30', len(ix))
log('E10', ix, 'Ordem em andamento sem movimentacao ha mais de 2 anos', 0, 'data_aquisicao', base.loc[ix, 'data_aquisicao'].dt.date.values, novas.date)
base.loc[ix, 'data_aquisicao'] = novas.values; base.loc[ix, 'data_cadastro_sistema'] = novas.values; base.loc[ix, 'data_ultima_alteracao'] = novas.values

# E11 - data de aquisicao anterior a constituicao da companhia (21/07/1999) em item de capex proprio
ix = escolher((base.origem == 'CAPEX_PROPRIO') & (base.classe_ne7 == 'OUTROS') & linear, 30)
novas = datas_unif('1985-01-01', '1999-06-30', len(ix))
log('E11', ix, 'Data de aquisicao anterior a constituicao da companhia (21/07/1999) - erro cadastral', 0, 'data_aquisicao', base.loc[ix, 'data_aquisicao'].dt.date.values, novas.date)
base.loc[ix, 'data_aquisicao'] = novas.values

# -----------------------------------------------------------------------------
# 11) Restabelece o total EXATO da acumulada por entidade x classe (compensa E03/E04 em itens sem erro)
#     -> o total contabil da base continua igual ao saldo publicado (a DF "contem" as distorcoes simuladas)
# -----------------------------------------------------------------------------
com_erro = set(r['id_interno'] for r in LOG) | set(base._dup_de[base._dup_de >= 0])
for ent in (ENT_PR, ENT_TI):
    for classe in ALVO[ent]:
        m = (base.entidade == ent) & (base.classe_ne7 == classe)
        alvo = alvo_centavos(ent, classe, 1)
        dif = alvo - base.loc[m, 'dep_acum_centavos'].sum()
        if dif == 0: continue
        livre = m & ~base.index.isin(list(com_erro)) & (base.origem != 'AQUISICAO_BRAVA_JOA') & (base.dep_acum_centavos < 0.97 * base.custo_centavos)
        folga = (base.custo_centavos - base.dep_acum_centavos) if dif > 0 else base.dep_acum_centavos   # quanto cada item comporta
        if classe in ('MAQUINAS_EQUIPAMENTOS', 'OUTROS'):                     # lineares: so itens com r >= taxa, para nao alterar a despesa 2025 (= custo x taxa)
            tx_ = base.taxa_anual_linear.fillna(0)
            folga = ((0.97 * base.custo_centavos - base.dep_acum_centavos) if dif > 0 else (base.dep_acum_centavos - tx_ * base.custo_centavos)).clip(lower=0).apply(np.floor)
            livre = livre & (base.dep_acum_centavos >= tx_ * base.custo_centavos)
        cand = folga[livre & (folga > 0)].nlargest(5000).index
        aj = rateio_centavos(folga.loc[cand].astype(float), abs(dif)) * np.sign(dif)
        base.loc[cand, 'dep_acum_centavos'] += aj
        mm = cand[base.loc[cand, 'metodo_depreciacao'] == 'LINEAR']
        if len(mm):                                                             # mantem coerencia data de inicio x acumulada
            r = base.loc[mm, 'dep_acum_centavos'] / base.loc[mm, 'custo_centavos']
            base.loc[mm, 'data_inicio_depreciacao'] = DATA_BASE - pd.to_timedelta(np.round(r / base.loc[mm, 'taxa_anual_linear'] * 365.25), unit='D')
            base.loc[mm, 'dep_2025_centavos'] = np.round(base.loc[mm, 'custo_centavos'] * np.minimum(r, base.loc[mm, 'taxa_anual_linear'])).astype(np.int64)

# coerencia cadastral: nos itens lineares sem erro inserido, a data de aquisicao nao pode ser posterior ao inicio da depreciacao
lin_ok = (base.metodo_depreciacao == 'LINEAR') & ~base.index.isin(list(com_erro)) & (base.data_inicio_depreciacao < base.data_aquisicao)
base.loc[lin_ok, 'data_aquisicao'] = base.loc[lin_ok, 'data_inicio_depreciacao']
base.loc[lin_ok, 'data_cadastro_sistema'] = base.loc[lin_ok, ['data_cadastro_sistema', 'data_aquisicao']].min(axis=1)
base.loc[lin_ok, 'data_cadastro_sistema'] = (base.loc[lin_ok, 'data_aquisicao'] + pd.to_timedelta(rng.integers(0, 25, lin_ok.sum()), unit='D')).clip(upper=DATA_BASE)
base.loc[lin_ok, 'data_ultima_alteracao'] = base.loc[lin_ok, ['data_ultima_alteracao', 'data_cadastro_sistema']].max(axis=1)

# -----------------------------------------------------------------------------
# 12) Montagem final, identificadores e arquivos
# -----------------------------------------------------------------------------
base = base.sample(frac=1, random_state=SEED).reset_index().rename(columns={'index': 'id_interno'})   # embaralha (ordem nao revela classe)
base['id_registro'] = 'IMB-' + (base.index + 1).astype(str).str.zfill(7)
mapa_id = dict(zip(base.id_interno, base.id_registro))
base['custo_historico'] = base.custo_centavos / 100
base['depreciacao_acumulada'] = base.dep_acum_centavos / 100
base['valor_contabil_liquido'] = (base.custo_centavos - base.dep_acum_centavos) / 100
base['depreciacao_2025'] = base.dep_2025_centavos / 100
base = base.merge(plano[['conta_custo', 'descricao_conta', 'conta_depreciacao']], on='conta_custo', how='left')
base['descricao_conta_depreciacao'] = base.conta_depreciacao.map(DESC_DEP).fillna('')
base['natureza_dado'] = 'SINTETICO'
COLS = ['id_registro', 'entidade', 'polo', 'campo', 'uf', 'poco_id', 'classe_ne7', 'conta_custo', 'descricao_conta', 'conta_depreciacao',
        'descricao_conta_depreciacao', 'tipo_item', 'origem', 'data_aquisicao', 'data_inicio_depreciacao', 'metodo_depreciacao', 'taxa_anual_linear',
        'taxa_uop_campo_2025', 'custo_historico', 'depreciacao_acumulada', 'valor_contabil_liquido', 'depreciacao_2025', 'status', 'data_baixa',
        'documento_origem', 'fornecedor_id', 'centro_custo', 'garantia_judicial', 'usuario_cadastro', 'usuario_aprovacao', 'data_cadastro_sistema',
        'data_ultima_alteracao', 'natureza_dado']
saida = base[COLS].copy()
for c in ('data_aquisicao', 'data_inicio_depreciacao', 'data_baixa', 'data_cadastro_sistema', 'data_ultima_alteracao'):
    saida[c] = pd.to_datetime(saida[c]).dt.strftime('%Y-%m-%d')
saida.to_csv(f'{OUT}/BASE_IMOBILIZADO_RECV3_SINTETICA.csv.gz', index=False, sep=';', decimal=',', encoding='utf-8', compression={'method': 'gzip', 'mtime': 0})
saida.head(2000).to_csv(f'{OUT}/BASE_IMOBILIZADO_RECV3_SINTETICA_amostra_2000_linhas.csv', index=False, sep=';', decimal=',', encoding='utf-8-sig')

# Arquivo SIMULADO de resultado da inspecao documental (o "documento" que o auditor veria ao inspecionar o item)
erro_por_id = {}
for r in LOG:
    erro_por_id.setdefault(r['id_interno'], []).append(r['tipo_erro'])
sup = base[['id_interno', 'id_registro', 'documento_origem', 'fornecedor_id', 'data_aquisicao', 'custo_centavos', 'dep_acum_centavos']].copy()
sup['documento_localizado'] = 'S'; sup['valor_liquido_suportado'] = (sup.custo_centavos - sup.dep_acum_centavos) / 100
sup['data_documento'] = pd.to_datetime(sup.data_aquisicao).dt.strftime('%Y-%m-%d'); sup['observacao_inspecao'] = 'Documento confere com o registro'
dep_ok = {}
for r in LOG:
    if r['tipo_erro'] in ('E04',): dep_ok[r['id_interno']] = int(r['valor_original'])
idx_err = sup.index[sup.id_interno.isin(list(erro_por_id.keys())) | (base._dup_de >= 0)]
for k in idx_err:
    row = sup.loc[k]; tipos = erro_por_id.get(row.id_interno, [])
    if base.at[k, '_dup_de'] >= 0:
        sup.at[k, 'valor_liquido_suportado'] = 0.0; sup.at[k, 'observacao_inspecao'] = f'Documento ja vinculado ao registro {mapa_id[base.at[k, "_dup_de"]]} (duplicidade)'
    if 'E02' in tipos:
        sup.at[k, 'valor_liquido_suportado'] = 0.0; sup.at[k, 'observacao_inspecao'] = 'Documento datado de 2026: bem recebido apos a data-base'
    if 'E05' in tipos:
        sup.at[k, 'valor_liquido_suportado'] = 0.0; sup.at[k, 'observacao_inspecao'] = 'Laudo de sucateamento/baixa emitido em 2025'
    if 'E08' in tipos:
        sup.at[k, 'documento_localizado'] = 'N'; sup.at[k, 'valor_liquido_suportado'] = 0.0; sup.at[k, 'observacao_inspecao'] = 'Documento nao localizado; campo inexistente'
    if 'E09' in tipos:
        sup.at[k, 'valor_liquido_suportado'] = E09_SUPORTE[row.id_interno] / 100; sup.at[k, 'observacao_inspecao'] = 'Nota/medicao suporta valor inferior ao registrado'
    if 'E04' in tipos:
        sup.at[k, 'valor_liquido_suportado'] = (row.custo_centavos - dep_ok[row.id_interno]) / 100; sup.at[k, 'observacao_inspecao'] = 'Recalculo da depreciacao diverge do registro'
    if 'E03' in tipos:
        sup.at[k, 'valor_liquido_suportado'] = 0.0; sup.at[k, 'observacao_inspecao'] = 'Bem totalmente depreciado; acumulada excede o custo'
sup['natureza_dado'] = 'SINTETICO - resultado simulado de inspecao documental (usado apenas para itens selecionados)'
sup[['id_registro', 'documento_origem', 'documento_localizado', 'data_documento', 'valor_liquido_suportado', 'observacao_inspecao', 'natureza_dado']].to_csv(
    f'{OUT}/INSPECAO_DOCUMENTAL_SIMULADA.csv.gz', index=False, sep=';', decimal=',', encoding='utf-8', compression={'method': 'gzip', 'mtime': 0})

# Parametros e cadastros auxiliares
campos.drop(columns=['sigla']).to_csv(f'{OUT}/PARAMETROS_CAMPOS_SIMULADOS.csv', index=False, sep=';', decimal=',', encoding='utf-8-sig')
plano.to_csv(f'{OUT}/PLANO_CONTAS_IMOBILIZADO_SIMULADO.csv', index=False, sep=';', encoding='utf-8-sig')
pocos[['poco_id', 'campo', 'polo', 'entidade', 'uf', 'data_entrada', 'origem_poco']].assign(natureza_dado='SINTETICO').to_csv(
    f'{OUT}/CADASTRO_POCOS_SIMULADO.csv', index=False, sep=';', encoding='utf-8-sig')

# LOG dos erros inseridos (controle do preparador; os testes so o leem na etapa final de comparacao)
lg = pd.DataFrame(LOG); lg['id_registro'] = lg.id_interno.map(mapa_id); lg['efeito_monetario_R$'] = lg.efeito_monetario_centavos / 100
lg = lg.drop(columns=['id_interno', 'efeito_monetario_centavos']).sort_values(['tipo_erro', 'id_registro'])
lg.insert(0, 'seq', range(1, len(lg) + 1))
lg.to_csv(f'{CTRL}/LOG_ERROS_INSERIDOS.csv', index=False, sep=';', decimal=',', encoding='utf-8-sig')

meta = dict(semente=SEED, linhas=int(len(saida)), data_base='2025-12-31', gerado_por='codigo/gerar_base_imobilizado.py',
            sha256_conteudo_csv=hashlib.sha256(__import__('gzip').open(f'{OUT}/BASE_IMOBILIZADO_RECV3_SINTETICA.csv.gz', 'rb').read()).hexdigest(),   # hash do CSV descompactado (o cabecalho gzip guarda a hora)
            total_custo=float(saida.custo_historico.sum()), total_dep_acum=float(saida.depreciacao_acumulada.sum()),
            total_liquido=float(saida.valor_contabil_liquido.sum()), erros_inseridos=lg.tipo_erro.value_counts().sort_index().to_dict(),
            calibracao_depreciacao_linear=CALIB_LINEAR, offsets_arredondamento_reais={f'{k[0]}|{k[1]}|{["custo","acum","dep2025"][k[2]]}': v for k, v in OFFSET.items()})
json.dump(meta, open(f'{OUT}/METADADOS_GERACAO.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(json.dumps({k: meta[k] for k in ('linhas', 'total_custo', 'total_dep_acum', 'total_liquido', 'erros_inseridos')}, ensure_ascii=False))
