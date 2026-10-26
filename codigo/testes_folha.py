# -*- coding: utf-8 -*-
# =============================================================================
# P2 - AUDITORIA 1 - PetroReconcavo (RECV3) - Preparador: matricula 211059370
# >>> SECAO DE SCRIPTS DE AUDITORIA - base complementar de folha (DADOS SINTETICOS) <<<
# Testes em 100% da populacao, executados antes da leitura do log de erros.
# G01 empregado ficticio | G02 CPF/conta duplicados | G03 pagamento sem vinculo (apos desligamento)
# G04 maker-checker no cadastro | G05 reajuste fora de alcada (trilha de alteracoes)
# G06 classificacao circulante x nao circulante (vence ate 31/12/2026 = circulante; a partir de 01/01/2027 = nao circulante)
# Uso: python codigo/testes_folha.py
# =============================================================================
import os
import numpy as np
import pandas as pd
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Border, Side, Alignment
from openpyxl.utils import get_column_letter

F = 'base_simulada/folha'; RES = 'base_simulada/resultados'; os.makedirs(RES, exist_ok=True)
cad = pd.read_csv(f'{F}/CADASTRO_EMPREGADOS_SIMULADO.csv', sep=';', decimal=',', parse_dates=['data_admissao', 'data_desligamento', 'data_ultima_alteracao_salarial'],
                  dtype={'usuario_aprovacao': str}).fillna({'usuario_aprovacao': ''})
fol = pd.read_csv(f'{F}/FOLHA_PAGAMENTOS_2025_SIMULADA.csv', sep=';', decimal=',')
prov = pd.read_csv(f'{F}/OBRIGACOES_TRABALHISTAS_31122025_SIMULADAS.csv', sep=';', decimal=',', parse_dates=['data_vencimento'])
OBRIG_TRAB = 88_753_000.00; DESP_PESSOAL = 284_002_000.00

exc = []
def reg(teste, chaves, detalhe, valor=0.0):
    exc.append(pd.DataFrame({'teste': teste, 'chave': list(chaves), 'detalhe': detalhe, 'valor_em_risco': np.broadcast_to(np.asarray(valor, float), len(chaves))}))
# G01 - pagamentos a matriculas inexistentes no cadastro
g1 = fol[~fol.matricula.isin(cad.matricula)].groupby('matricula').valor_bruto.sum()
reg('G01_EMPREGADO_FICTICIO', g1.index, 'Matricula paga na folha e inexistente no cadastro', g1.values)
# G02 - CPF ou conta bancaria compartilhados por matriculas distintas (marca as matriculas posteriores)
for campo, nome in (('cpf_simulado', 'CPF'), ('banco_agencia_conta', 'conta bancaria')):
    d = cad[cad.duplicated(campo, keep=False)]                        # marca TODAS as matriculas do par (ambas devem ser investigadas)
    reg('G02_CADASTRO_DUPLICADO', d.matricula, f'{nome} igual ao de outra matricula')
# G03 - salario pago em competencia posterior ao desligamento
f = fol.merge(cad[['matricula', 'data_desligamento']], on='matricula', how='inner')
f = f[(f.rubrica == 'SALARIO') & f.data_desligamento.notna() & (f.competencia.str[:7] <= '2025-12')]
f['ini_comp'] = pd.to_datetime(f.competencia + '-01', errors='coerce')
g3 = f[f.ini_comp > f.data_desligamento + pd.offsets.MonthEnd(0)].groupby('matricula').valor_bruto.sum()
reg('G03_PAGAMENTO_SEM_VINCULO', g3.index, 'Salario pago apos o desligamento', g3.values)
# G04 - maker-checker no cadastro
reg('G04_MAKER_CHECKER', cad[(cad.usuario_aprovacao == '') | (cad.usuario_aprovacao == cad.usuario_cadastro)].matricula, 'Cadastro sem aprovacao independente')
# G05 - reajuste > 30% sem aprovacao da diretoria (politica de alcadas simulada)
reg('G05_REAJUSTE_FORA_ALCADA', cad[(cad.pct_ultimo_reajuste > 0.30) & (cad.aprovador_reajuste != 'DIRETORIA_PESSOAS')].matricula, 'Reajuste > 30% aprovado abaixo da alcada')
# G06 - classificacao: vencimento a partir de 01/01/2027 registrado como circulante
g6 = prov[(prov.data_vencimento >= pd.Timestamp('2027-01-01')) & (prov.classificacao_registrada == 'CIRCULANTE')]
reg('G06_CLASSIFICACAO_CP_LP', g6.id_obrigacao, 'Vence a partir de 01/01/2027 e esta no circulante (reclassificar para nao circulante)', g6.valor.values)
excecoes = pd.concat(exc, ignore_index=True)
excecoes.to_csv(f'{RES}/EXCECOES_TESTES_FOLHA.csv', index=False, sep=';', decimal=',', encoding='utf-8-sig')
resumo = excecoes.groupby('teste').agg(qtd=('chave', 'count'), valor=('valor_em_risco', 'sum')).reset_index()

# conciliacoes
custo = fol.valor_bruto.sum() + fol.encargos_patronais.sum() + fol.beneficios.sum() + prov.loc[prov.tipo_obrigacao == 'PLR_2025_PROVISIONADA', 'valor'].sum() * (1 + 0.288 + 0.08)
conc = pd.DataFrame([
    ('Obrigacoes sociais e trabalhistas 31/12/2025 - base', prov.valor.sum()), ('CVM 2.01.01 consolidado (F03)', OBRIG_TRAB), ('Diferenca', prov.valor.sum() - OBRIG_TRAB),
    ('  dos quais vencem ate 31/12/2026 (circulante)', prov.loc[prov.data_vencimento <= '2026-12-31', 'valor'].sum()),
    ('  dos quais vencem a partir de 01/01/2027 (nao circulante)', prov.loc[prov.data_vencimento >= '2027-01-01', 'valor'].sum()),
    ('Custo de pessoal 2025 - base (bruto + encargos + beneficios + PLR provisionada c/ encargos)', custo), ('Despesa de pessoal NE 19 consolidada (F01 p.93)', DESP_PESSOAL),
    ('Diferenca', custo - DESP_PESSOAL), ('  explicada por G01 + G03 (pagamentos indevidos simulados, com encargos de G03)', np.nan)], columns=['item', 'valor_R$'])

lg = pd.read_csv('base_simulada/controle_erros/LOG_ERROS_INSERIDOS_FOLHA.csv', sep=';', decimal=',')   # lido somente agora
MAPA = {'F01': 'G01_EMPREGADO_FICTICIO', 'F02': 'G02_CADASTRO_DUPLICADO', 'F03': 'G03_PAGAMENTO_SEM_VINCULO', 'F04': 'G04_MAKER_CHECKER',
        'F05': 'G05_REAJUSTE_FORA_ALCADA', 'F06': 'G06_CLASSIFICACAO_CP_LP'}
comp = []
for t, teste in MAPA.items():
    ins, det = set(lg[lg.tipo_erro == t].chave), set(excecoes[excecoes.teste == teste].chave)
    contraparte = set()
    if t == 'F02':                                                    # a outra matricula do par nao e falso positivo: e a contraparte do cadastro duplicado
        alvo = cad[cad.matricula.isin(ins)]
        contraparte = set(cad[(cad.cpf_simulado.isin(alvo.cpf_simulado) | cad.banco_agencia_conta.isin(alvo.banco_agencia_conta)) & ~cad.matricula.isin(ins)].matricula)
    comp.append(dict(tipo_erro=t, teste=teste, inseridos=len(ins), detectados=len(det), verdadeiros_positivos=len(ins & det), contrapartes_do_par=len(det & contraparte),
                     falsos_positivos=len(det - ins - contraparte),
                     taxa_deteccao=len(ins & det) / len(ins), efeito_inserido=lg[lg.tipo_erro == t]['efeito_monetario_R$'].sum()))
comp = pd.DataFrame(comp)
print(resumo); print(conc); print(comp)

HEAD = PatternFill('solid', fgColor='1F4E78'); thin = Side(style='thin', color='BFBFBF'); BD = Border(top=thin, bottom=thin, left=thin, right=thin)
NUM = '#,##0.00;(#,##0.00);-'
def sheet(wb, nome, titulo, df, w, nf=None):
    ws = wb.create_sheet(nome); ws['A1'] = titulo; ws['A1'].font = Font(bold=True, size=13)
    ws['A2'] = 'DADOS SINTETICOS - procedimento SIMULADO PARA FINS DIDATICOS | Preparador: matricula 211059370 | 23/10/2026 | Revisao: ______'
    ws['A2'].font = Font(italic=True, size=9)
    for j, c in enumerate(df.columns, 1):
        x = ws.cell(row=4, column=j, value=c); x.font = Font(bold=True, color='FFFFFF'); x.fill = HEAD; x.border = BD; ws.column_dimensions[get_column_letter(j)].width = w[j - 1]
    for i, row in enumerate(df.itertuples(index=False), 5):
        for j, v in enumerate(row, 1):
            if isinstance(v, float) and np.isnan(v): v = None
            elif isinstance(v, np.generic): v = v.item()
            c = ws.cell(row=i, column=j, value=v); c.border = BD
            if nf and j in nf: c.number_format = nf[j]
wb = Workbook(); wb.remove(wb.active)
sheet(wb, 'Conciliacao', 'Conciliacao da base de folha com a DF (CVM 2.01.01 e NE 19)', conc, [90, 22], {2: NUM})
sheet(wb, 'Resumo_testes', 'Testes G01-G06 em 100% da populacao', resumo, [34, 10, 18], {3: NUM})
sheet(wb, 'Excecoes', 'Excecoes (detalhe)', excecoes, [30, 16, 70, 18], {4: NUM})
sheet(wb, 'Inseridos_x_detectados', 'Comparacao erros inseridos x detectados (folha)', comp, [8, 30, 10, 10, 12, 12, 12, 12, 18], {8: '0.0%', 9: NUM})
wb.save('planilhas/TESTES_FOLHA_RECV3.xlsx'); print('ok')
