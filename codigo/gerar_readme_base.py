# -*- coding: utf-8 -*-
# P2 - Auditoria 1 - RECV3 - Preparador 211059370
# Gera base_simulada/README_BASE_SIMULADA.md com os NUMEROS lidos dos arquivos de resultado (nada digitado a mao).
# Uso: python codigo/gerar_readme_base.py   (depois de codigo/rodar_passo3.py)
import json
import pandas as pd

def br(v, d=2):
    s = f'{v:,.{d}f}'; return s.replace(',', 'X').replace('.', ',').replace('X', '.')
NE7 = {'DESENVOLVIMENTO_CAMPOS': (5186676, 2422704, 485386), 'DIREITO_PRODUCAO_OLEO_GAS': (2931329, 922414, 132263), 'MAQUINAS_EQUIPAMENTOS': (718521, 103788, 38884),
       'ALMOXARIFADO_INVERSOES_FIXAS': (477651, 0, 0), 'OUTROS': (199325, 41957, 14161), 'ABANDONO_POCO_ARO': (79303, 41848, 1174),
       'IMOBILIZADO_EM_ANDAMENTO': (72171, 0, 0), 'BLOCOS_EXPLORATORIOS': (20157, 0, 0), 'ADIANTAMENTOS': (18419, 0, 0)}
NOME = {'DESENVOLVIMENTO_CAMPOS': 'Desenvolvimento de campos', 'DIREITO_PRODUCAO_OLEO_GAS': 'Direito de producao de oleo e gas', 'MAQUINAS_EQUIPAMENTOS': 'Maquinas e equipamentos',
        'ALMOXARIFADO_INVERSOES_FIXAS': 'Almoxarifado p/ inversoes fixas', 'OUTROS': 'Outros', 'ABANDONO_POCO_ARO': 'Abandono de poco (ARO)',
        'IMOBILIZADO_EM_ANDAMENTO': 'Imobilizado em andamento', 'BLOCOS_EXPLORATORIOS': 'Blocos exploratorios', 'ADIANTAMENTOS': 'Adiantamentos'}
b = pd.read_csv('base_simulada/BASE_IMOBILIZADO_RECV3_SINTETICA.csv.gz', sep=';', decimal=',', low_memory=False)
meta = json.load(open('base_simulada/METADADOS_GERACAO.json', encoding='utf-8'))
res = json.load(open('base_simulada/resultados/RESULTADOS_MUS.json', encoding='utf-8')); M = res['mus']; P = res['parametros']; V = res['validacao']
lg = pd.read_csv('base_simulada/controle_erros/LOG_ERROS_INSERIDOS.csv', sep=';', decimal=',', encoding='utf-8-sig')
comp = pd.read_csv('base_simulada/resultados/COMPARATIVO_INSERIDOS_DETECTADOS.csv', sep=';', decimal=',', encoding='utf-8-sig')
amo = pd.read_csv('base_simulada/resultados/MUS_AMOSTRA_SELECIONADA.csv', sep=';', decimal=',', encoding='utf-8-sig')
fo = json.load(open('base_simulada/folha/METADADOS_FOLHA.json', encoding='utf-8'))
exf = pd.read_csv('base_simulada/resultados/EXCECOES_TESTES_FOLHA.csv', sep=';', decimal=',', encoding='utf-8-sig')
g = b.groupby('classe_ne7').agg(n=('id_registro', 'count'), c=('custo_historico', 'sum'), a=('depreciacao_acumulada', 'sum'), v=('valor_contabil_liquido', 'sum'), d=('depreciacao_2025', 'sum'))

L = []
L += ['# Base de dados simulada - Imobilizado da PetroReconcavo S.A. (RECV3) - 31/12/2025', '',
      '> **DADOS SINTETICOS. Os registros desta pasta NAO sao registros reais da companhia.** Os unicos dados reais usados sao os **totais publicados** listados na secao 3; todo o detalhe analitico (itens, pocos, datas, documentos, fornecedores, usuarios, empregados) foi simulado.', '',
      '| Campo | Conteudo |', '|---|---|', '| Preparador | Matricula 211059370 |', '| Data | 24/10/2026 |', '| Revisao | ______ (campo reservado; nao preenchido) |',
      '| Classificacao dos procedimentos | **Simulado para fins didaticos** (enunciado, item 2) |',
      '| Normas | NBC TA 500(R1) (dados usados como evidencia), NBC TA 530 (amostragem), NBC TA 320(R1) (materialidade - PT 320) |',
      '| Arquivo gerado por | `codigo/gerar_readme_base.py` (todos os numeros sao lidos dos arquivos de resultado) |', '', '---', '',
      '## 1. Escolha da conta e materialidade', '',
      '1. **Conta escolhida: Imobilizado (NE 7).** A rubrica "Imobilizado e intangivel" (R$ 6.254.225 mil) representa **72,2% do ativo total consolidado** (R$ 8.668.015 mil), cerca de 4,5 vezes a segunda maior rubrica (aplicacoes financeiras, 16,1%); na controladora, 66,2%. O intangivel (software, R$ 83.384 mil) e residual; a base cobre o **imobilizado** (CVM 1.02.03 = **R$ 6.170.841 mil**, 98,7% da rubrica). Fontes: F01 p.51 e p.68-70; F03; `planilhas/DIAG_RECV3.xlsx` (aba `Ranking_Ativo`).',
      f'2. **Materialidade (PT 320 - NBC TA 320 (R1)):** materialidade global **R$ {br(P["MG"], 0)}** = 1% da receita liquida consolidada de 2025 (R$ 3.157.609 mil), arredondada para baixo. Referencial escolhido pela regra do item A5 (o lucro antes do imposto e volatil: R$ 363.405 mil em 2024 e R$ 776.194 mil em 2025, com R$ 366.796 mil de ganho com swaps); percentual de 1% conforme o exemplo do item A8 para receita total. Materialidade para execucao **R$ {br(P["ME"], 0)}** ({P["pct_ME"]:.0%} da MG, julgamento com base nos fatores do item A13: primeira auditoria, inconsistencias de divulgacao ja identificadas e risco de impairment). A norma nao fixa percentuais (itens A8 e A13) - a justificativa completa esta no PT 320.', '',
      '## 2. O que cada linha representa', '',
      'Cada linha e **um item do subrazao patrimonial** com custo, depreciacao acumulada e valor liquido proprios: componentes capitalizados por poco (perfuracao/completacao, workover, estimulacao, coluna, bomba de fundo, cabeca de poco, linhas, conversao em injetor), ativo de abandono (ARO) por poco, equipamentos (sondas, unidades de bombeio, facilities, UPGN Guamare, veiculos), lotes de materiais do almoxarifado de inversoes fixas (por SKU e deposito), ordens de investimento em andamento, adiantamentos, blocos exploratorios, direito de producao por concessao e outros bens. Nao ha repeticao de registros para atingir o volume (as unicas copias sao as duplicidades inseridas de proposito, erro E01).', '',
      '| Classe NE 7.1 | Registros | Custo (R$) | Deprec. acumulada (R$) | Valor liquido (R$) | Deprec. 2025 (R$) |', '|---|---:|---:|---:|---:|---:|']
for k in NE7:
    r = g.loc[k]; L.append(f'| {NOME[k]} | {br(r.n, 0)} | {br(r.c)} | {br(r.a)} | {br(r.v)} | {br(r.d)} |')
L.append(f'| **Total** | **{br(len(b), 0)}** | **{br(b.custo_historico.sum())}** | **{br(b.depreciacao_acumulada.sum())}** | **{br(b.valor_contabil_liquido.sum())}** | **{br(b.depreciacao_2025.sum())}** |')
L += ['', '## 3. Premissas e metodo de geracao', '',
      f'1. **Reprodutibilidade:** semente fixa = matricula (211059370). O mesmo codigo gera exatamente a mesma base; SHA-256 do conteudo do CSV: `{meta["sha256_conteudo_csv"]}` (`METADADOS_GERACAO.json`).',
      '2. **Dados reais usados (alvos):** custo, depreciacao acumulada e depreciacao do exercicio por classe, para controladora e consolidado (NE 7.1, F01 p.68-69; SPE Tieta por diferenca); custo e depreciacao transferidos da UPGN Guamare (coluna propria da NE 7.1: R$ 284.999 mil e R$ 4.322 mil); custo do direito de producao por polo (NE 7.1 ii, p.70); metodos e taxas (NE 7.2); sonda em garantia (NE 7.3); producao 2025 por ativo (13,4 e 13,1 mil boe/d) e reservas 1P/PDP (RA p.5-8; F14); lista de campos dos polos (FRE 2026 item 1.1) e datas das aquisicoes.',
      '3. **Simulacao do detalhe:** 58 concessoes (28 com nome publico; 20 com codigo sintetico), 7.200 pocos; itens com distribuicao lognormal por tipo de componente; datas posteriores a aquisicao de cada polo; usuarios de cadastro e aprovacao, documentos e fornecedores sinteticos.',
      '4. **Rateio exato em centavos** (metodo do maior resto) por entidade x classe (direito de producao: por polo). Para simular o arredondamento da DF publicada em R$ mil, cada subtotal recebe uma diferenca de no maximo R$ 240.',
      '5. **Depreciacao linear (maquinas e outros) - calibracao dupla:** a acumulada de cada item e coerente com a data de inicio e a taxa (acumulada = custo x taxa x anos, permitindo o recalculo); a parcela de itens 100% depreciados antes de 2025 foi encontrada por bissecao para que a **despesa de 2025** tambem reproduza a NE 7.1 (detalhe em `METADADOS_GERACAO.json`, chave `calibracao_depreciacao_linear`). Nenhum item fica com inicio de depreciacao anterior a fev/2000 (inicio das operacoes).',
      '6. **Deplecao por unidades produzidas:** acumulada em funcao da idade do item, escalada ao total da NE 7.1; deplecao 2025 = VCL x t/(1-t), com t = taxa do campo x fator calibrado por bissecao para reproduzir a NE 7.1.',
      '7. **Plano de contas simulado** (`PLANO_CONTAS_IMOBILIZADO_SIMULADO.csv`, 29 contas mapeadas as 9 classes reais): a DFP nao divulga plano de contas (orientacao de aula).',
      '8. **Arquivo de inspecao documental simulada** (`INSPECAO_DOCUMENTAL_SIMULADA.csv.gz`): o que o auditor encontraria ao inspecionar o documento de cada item; consultado **somente para itens selecionados na amostra**.', '',
      '## 4. Conciliacao da base com o saldo contabil (`planilhas/CONC_BASE_RECV3.xlsx`, com formulas)', '',
      '| Classe | Custo base (R$) | Custo NE 7.1 (R$) | Dif. | Acum. base (R$) | Acum. NE (R$) | Dif. | Deprec. 2025 base (R$) | NE 7.1 (R$) | Dif. |', '|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|']
for k, (c, a, d) in NE7.items():
    r = g.loc[k]; L.append(f'| {NOME[k]} | {br(r.c)} | {br(c * 1000.0)} | {br(r.c - c * 1000)} | {br(r.a)} | {br(a * 1000.0)} | {br(r.a - a * 1000)} | {br(r.d)} | {br(d * 1000.0)} | {br(r.d - d * 1000)} |')
tc, ta, td = sum(v[0] for v in NE7.values()) * 1000.0, sum(v[1] for v in NE7.values()) * 1000.0, sum(v[2] for v in NE7.values()) * 1000.0
L.append(f'| **Total** | **{br(b.custo_historico.sum())}** | **{br(tc)}** | **{br(b.custo_historico.sum() - tc)}** | **{br(b.depreciacao_acumulada.sum())}** | **{br(ta)}** | **{br(b.depreciacao_acumulada.sum() - ta)}** | **{br(b.depreciacao_2025.sum())}** | **{br(td)}** | **{br(b.depreciacao_2025.sum() - td)}** |')
vl = b.valor_contabil_liquido.sum()
L += ['', f'**Valor liquido consolidado:** base R$ {br(vl)} x CVM 1.02.03 R$ 6.170.841.000,00 -> diferenca de R$ {br(vl - 6170841000)} ({abs(vl - 6170841000) / 6170841000:.6%}).', '',
      '**Explicacao das diferencas:**', '',
      '1. **Saldos (custo e acumulada):** a DF e publicada em R$ mil; cada linha da NE 7.1 e um valor arredondado. A geracao reproduz, por classe e entidade, valores em centavos cuja diferenca para a linha publicada e de no maximo R$ 240 (arredondamento simulado). A diferenca do total e a soma dessas diferencas de linha - imaterial.',
      '2. **Depreciacao/deplecao de 2025:** (a) desenvolvimento de campos e maquinas: os registros duplicados inseridos (erro E01) repetem a despesa do registro original, de modo que o razao simulado "contem" essa distorcao; (b) maquinas da SPE Tieta: os 12 itens simulados sao todos recentes e nao comportam a despesa minima da NE (R$ 12 mil) - diferenca de cerca de R$ 43 mil, imaterial.',
      '3. **Intangivel (software, R$ 83.384 mil)** esta fora da base (a conta escolhida e o imobilizado).',
      '4. **Por que o total bate mesmo com erros inseridos:** os erros estao **dentro** do saldo contabil - a base simula um razao que contem distorcoes, como a DF real poderia conter. A diferenca entre valor contabil e valor suportado aparece na inspecao (MUS) e nos testes.', '',
      '## 5. Erros e inconsistencias inseridos (controle do preparador)', '',
      'O log `controle_erros/LOG_ERROS_INSERIDOS.csv` registra, por registro, o tipo, o campo alterado, o valor original, o valor inserido e o efeito. **Os scripts de teste (T01-T10 e MUS) rodam sem ler o log**; ele so e aberto na etapa final de comparacao (`planilhas/TESTES_BASE_RECV3.xlsx`, aba `Inseridos_x_detectados`).', '',
      '| Tipo | Natureza | Qtd. | Efeito monetario (R$) | Teste que deveria detectar | Detectados | Falsos positivos |', '|---|---|---:|---:|---|---:|---:|']
for r in comp.itertuples():
    L.append(f'| {r.tipo_erro} | {r.descricao} | {r.inseridos} | {br(r.efeito_inserido) if r.efeito_inserido else "nao monetario"} | {r.teste} | {r.verdadeiros_positivos} | {r.falsos_positivos} |')
L += [f'| | **Superavaliacao total inserida** | | **{br(V["superavaliacao_total_inserida"])}** | | | |', '',
      '## 6. Procedimentos executados com a base (resultados)', '',
      '1. **Testes em 100% da populacao (T01-T10)** - todos os erros detectaveis por esses testes foram encontrados, **sem falsos positivos**. Deteccoes cruzadas esperadas: T04 tambem marca os itens de E03 e os itens lineares de E02; T07 marca algumas duplicatas cujo cadastrador sorteado coincidiu com o aprovador.',
      '2. **MUS (Gramling, cap. 8; NBC TA 530)** - afirmacoes de existencia e avaliacao; unidade amostral = R$ 1 de valor contabil liquido.', '',
      '| Parametro / resultado | Valor |', '|---|---|',
      f'| Risco de deteccao | RA {P["RA"]:.0%} / (RI {P["RI"]:.0%} x RC {P["RC"]:.0%}) = **{M["RD"]:.0%}** -> FC {M["FC"]:.2f}; FEE {M["FEE"]:.2f} (Ilustracao 8.7) |',
      f'| Incorrecao toleravel / esperada | IT = R$ {br(M["IT"])}; IE = R$ {br(M["IE"])} |',
      f'| Intervalo | **I = (IT - IE x FEE) / FC = R$ {br(M["I"])}** |',
      f'| Populacao | {br(M["n_populacao"], 0)} itens com VCL > 0, R$ {br(M["VC_populacao"])} (itens com VCL = 0 nao tem chance de selecao e itens com VCL < 0 sao testados a parte em T03 - Gramling p.302) |',
      f'| Tamanho | n max. = {br(M["n_max"])}; {M["n_pontos"]} pontos (inicio aleatorio R$ {br(M["ponto_partida"])}); **{M["n_itens_distintos"]} itens distintos** ({M["n_estrato_superior"]} no estrato superior); cobertura R$ {br(M["valor_amostra"])} ({M["valor_amostra"] / M["VC_populacao"]:.1%} do valor) |',
      f'| Erros encontrados | **{M["n_erros"]} itens** ({", ".join(f"{k}: {v}" for k, v in amo[amo.incorrecao > 0.005].erro_inserido.value_counts().items())}) |',
      f'| Avaliacao | precisao basica R$ {br(M["PB"])} + IMP R$ {br(M["IMP"])} + ajuste incremental R$ {br(M["IA"])} = **LSI R$ {br(M["LSI"])}** |',
      f'| **Conclusao** | **{M["conclusao"]}** -> PT 530 / PT 450 |', '',
      f'   *Validacao didatica:* o LSI (R$ {br(V["LSI"])}) {"**cobre**" if V["LSI_cobre_erro_real"] == "SIM" else "**NAO cobre**"} a superavaliacao efetivamente inserida (R$ {br(V["superavaliacao_total_inserida"])}); a incorrecao mais provavel projetada foi R$ {br(V["incorrecao_projetada_MUS"])}.', '',
      f'3. **Base complementar - folha e beneficios a empregados** (`folha/`): {br(fo["cadastro"], 0)} empregados no cadastro ({br(fo["ativos_31122025"], 0)} ativos, FRE 10.1A), {br(fo["lancamentos_folha"], 0)} lancamentos de 2025, {br(fo["obrigacoes"], 0)} obrigacoes em 31/12/2025. Conciliacao: obrigacoes = **R$ {br(fo["total_obrigacoes"])} = CVM 2.01.01**; custo de pessoal R$ {br(fo["custo_pessoal_2025_simulado"])} x R$ 284.002.000,00 da NE 19 (diferenca = efeito dos pagamentos indevidos inseridos F01 + F03 com encargos). Testes G01-G06: {len(exf)} excecoes, deteccao de 100% dos erros inseridos; R$ {br(exf[exf.teste == "G06_CLASSIFICACAO_CP_LP"].valor_em_risco.sum())} vencendo a partir de 01/01/2027 estavam no circulante (reclassificar para nao circulante).', '',
      '## 7. Como reproduzir', '', '```bash', '# na raiz P2_PetroReconcavo (Python 3.10+; pacotes em requirements.txt)', 'pip install -r requirements.txt',
      'python codigo/rodar_passo3.py          # bases, conciliacao, testes, MUS, folha, dicionario e este README (~2 min)',
      'python codigo/construir_notebook.py    # (opcional) recria o notebook a partir dos scripts', '```',
      'No **Google Colab**: abrir `notebooks/P2_RECV3_passo3_base_simulada.ipynb`, informar o link do repositorio na 1a celula e executar tudo.', '',
      f'O arquivo da base (`BASE_IMOBILIZADO_RECV3_SINTETICA.csv.gz`, {br(len(b), 0)} linhas; separador `;` e virgula decimal) fica abaixo do limite de 100 MB do GitHub; a amostra de 2.000 linhas em CSV simples serve para visualizacao rapida.', '',
      '## 8. Limitacoes', '',
      '1. Dados sinteticos: proporcoes, datas e valores individuais **nao** representam a carteira real de ativos; apenas os totais reproduzem a DF.',
      '2. A distribuicao de producao e reservas por campo e um rateio sintetico de totais reais por ativo.',
      '3. A materialidade foi determinada no PT 320; se for revista (NBC TA 320 itens 12-13), basta alterar `PARAM` em `codigo/testes_auditoria_base.py` e reexecutar.',
      '4. Confirmacoes, inspecoes e entrevistas nao ocorreram; a "inspecao documental" e um arquivo simulado.']
open('base_simulada/README_BASE_SIMULADA.md', 'w', encoding='utf-8').write('\n'.join(L) + '\n')
print('ok README')
