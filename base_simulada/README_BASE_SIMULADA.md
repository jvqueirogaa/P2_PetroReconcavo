# Base de dados simulada - Imobilizado da PetroReconcavo S.A. (RECV3) - 31/12/2025

> **DADOS SINTETICOS. Os registros desta pasta NAO sao registros reais da companhia.** Os unicos dados reais usados sao os **totais publicados** listados na secao 3; todo o detalhe analitico (itens, pocos, datas, documentos, fornecedores, usuarios, empregados) foi simulado.

| Campo | Conteudo |
|---|---|
| Preparador | Matricula 211059370 |
| Data | 24/10/2026 |
| Revisao | ______ (campo reservado; nao preenchido) |
| Classificacao dos procedimentos | **Simulado para fins didaticos** (enunciado, item 2) |
| Normas | NBC TA 500(R1) (dados usados como evidencia), NBC TA 530 (amostragem), NBC TA 320(R1) (materialidade - PT 320) |
| Arquivo gerado por | `codigo/gerar_readme_base.py` (todos os numeros sao lidos dos arquivos de resultado) |

---

## 1. Escolha da conta e materialidade

1. **Conta escolhida: Imobilizado (NE 7).** A rubrica "Imobilizado e intangivel" (R$ 6.254.225 mil) representa **72,2% do ativo total consolidado** (R$ 8.668.015 mil), cerca de 4,5 vezes a segunda maior rubrica (aplicacoes financeiras, 16,1%); na controladora, 66,2%. O intangivel (software, R$ 83.384 mil) e residual; a base cobre o **imobilizado** (CVM 1.02.03 = **R$ 6.170.841 mil**, 98,7% da rubrica). Fontes: F01 p.51 e p.68-70; F03; `planilhas/DIAG_RECV3.xlsx` (aba `Ranking_Ativo`).
2. **Materialidade (PT 320 - NBC TA 320 (R1)):** materialidade global **R$ 31.500.000** = 1% da receita liquida consolidada de 2025 (R$ 3.157.609 mil), arredondada para baixo. Referencial escolhido pela regra do item A5 (o lucro antes do imposto e volatil: R$ 363.405 mil em 2024 e R$ 776.194 mil em 2025, com R$ 366.796 mil de ganho com swaps); percentual de 1% conforme o exemplo do item A8 para receita total. Materialidade para execucao **R$ 20.475.000** (65% da MG, julgamento com base nos fatores do item A13: primeira auditoria, inconsistencias de divulgacao ja identificadas e risco de impairment). A norma nao fixa percentuais (itens A8 e A13) - a justificativa completa esta no PT 320.

## 2. O que cada linha representa

Cada linha e **um item do subrazao patrimonial** com custo, depreciacao acumulada e valor liquido proprios: componentes capitalizados por poco (perfuracao/completacao, workover, estimulacao, coluna, bomba de fundo, cabeca de poco, linhas, conversao em injetor), ativo de abandono (ARO) por poco, equipamentos (sondas, unidades de bombeio, facilities, UPGN Guamare, veiculos), lotes de materiais do almoxarifado de inversoes fixas (por SKU e deposito), ordens de investimento em andamento, adiantamentos, blocos exploratorios, direito de producao por concessao e outros bens. Nao ha repeticao de registros para atingir o volume (as unicas copias sao as duplicidades inseridas de proposito, erro E01).

| Classe NE 7.1 | Registros | Custo (R$) | Deprec. acumulada (R$) | Valor liquido (R$) | Deprec. 2025 (R$) |
|---|---:|---:|---:|---:|---:|
| Desenvolvimento de campos | 189.928 | 5.186.675.801,00 | 2.422.704.184,00 | 2.763.971.617,00 | 485.531.844,42 |
| Direito de producao de oleo e gas | 76 | 2.931.328.820,00 | 922.414.031,00 | 2.008.914.789,00 | 132.262.883,00 |
| Maquinas e equipamentos | 45.780 | 718.521.296,00 | 103.787.870,00 | 614.733.426,00 | 38.928.573,72 |
| Almoxarifado p/ inversoes fixas | 210.083 | 477.650.882,00 | 0,00 | 477.650.882,00 | 0,00 |
| Outros | 75.225 | 199.325.044,00 | 41.957.074,00 | 157.367.970,00 | 14.166.748,47 |
| Abandono de poco (ARO) | 7.200 | 79.302.672,00 | 41.848.296,00 | 37.454.376,00 | 1.174.187,00 |
| Imobilizado em andamento | 2.500 | 72.171.064,00 | 0,00 | 72.171.064,00 | 0,00 |
| Blocos exploratorios | 6 | 20.156.531,00 | 0,00 | 20.156.531,00 | 0,00 |
| Adiantamentos | 1.800 | 18.418.664,00 | 0,00 | 18.418.664,00 | 0,00 |
| **Total** | **532.598** | **9.703.550.774,00** | **3.532.711.455,00** | **6.170.839.319,00** | **672.064.236,61** |

## 3. Premissas e metodo de geracao

1. **Reprodutibilidade:** semente fixa = matricula (211059370). O mesmo codigo gera exatamente a mesma base; SHA-256 do conteudo do CSV: `74914d46934f818d6c304a65e8c9f00ef97e9a4e0825825a87096d5920af7599` (`METADADOS_GERACAO.json`).
2. **Dados reais usados (alvos):** custo, depreciacao acumulada e depreciacao do exercicio por classe, para controladora e consolidado (NE 7.1, F01 p.68-69; SPE Tieta por diferenca); custo e depreciacao transferidos da UPGN Guamare (coluna propria da NE 7.1: R$ 284.999 mil e R$ 4.322 mil); custo do direito de producao por polo (NE 7.1 ii, p.70); metodos e taxas (NE 7.2); sonda em garantia (NE 7.3); producao 2025 por ativo (13,4 e 13,1 mil boe/d) e reservas 1P/PDP (RA p.5-8; F14); lista de campos dos polos (FRE 2026 item 1.1) e datas das aquisicoes.
3. **Simulacao do detalhe:** 58 concessoes (28 com nome publico; 20 com codigo sintetico), 7.200 pocos; itens com distribuicao lognormal por tipo de componente; datas posteriores a aquisicao de cada polo; usuarios de cadastro e aprovacao, documentos e fornecedores sinteticos.
4. **Rateio exato em centavos** (metodo do maior resto) por entidade x classe (direito de producao: por polo). Para simular o arredondamento da DF publicada em R$ mil, cada subtotal recebe uma diferenca de no maximo R$ 240.
5. **Depreciacao linear (maquinas e outros) - calibracao dupla:** a acumulada de cada item e coerente com a data de inicio e a taxa (acumulada = custo x taxa x anos, permitindo o recalculo); a parcela de itens 100% depreciados antes de 2025 foi encontrada por bissecao para que a **despesa de 2025** tambem reproduza a NE 7.1 (detalhe em `METADADOS_GERACAO.json`, chave `calibracao_depreciacao_linear`). Nenhum item fica com inicio de depreciacao anterior a fev/2000 (inicio das operacoes).
6. **Deplecao por unidades produzidas:** acumulada em funcao da idade do item, escalada ao total da NE 7.1; deplecao 2025 = VCL x t/(1-t), com t = taxa do campo x fator calibrado por bissecao para reproduzir a NE 7.1.
7. **Plano de contas simulado** (`PLANO_CONTAS_IMOBILIZADO_SIMULADO.csv`, 29 contas mapeadas as 9 classes reais): a DFP nao divulga plano de contas (orientacao de aula).
8. **Arquivo de inspecao documental simulada** (`INSPECAO_DOCUMENTAL_SIMULADA.csv.gz`): o que o auditor encontraria ao inspecionar o documento de cada item; consultado **somente para itens selecionados na amostra**.

## 4. Conciliacao da base com o saldo contabil (`planilhas/CONC_BASE_RECV3.xlsx`, com formulas)

| Classe | Custo base (R$) | Custo NE 7.1 (R$) | Dif. | Acum. base (R$) | Acum. NE (R$) | Dif. | Deprec. 2025 base (R$) | NE 7.1 (R$) | Dif. |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Desenvolvimento de campos | 5.186.675.801,00 | 5.186.676.000,00 | -199,00 | 2.422.704.184,00 | 2.422.704.000,00 | 184,00 | 485.531.844,42 | 485.386.000,00 | 145.844,42 |
| Direito de producao de oleo e gas | 2.931.328.820,00 | 2.931.329.000,00 | -180,00 | 922.414.031,00 | 922.414.000,00 | 31,00 | 132.262.883,00 | 132.263.000,00 | -117,00 |
| Maquinas e equipamentos | 718.521.296,00 | 718.521.000,00 | 296,00 | 103.787.870,00 | 103.788.000,00 | -130,00 | 38.928.573,72 | 38.884.000,00 | 44.573,72 |
| Almoxarifado p/ inversoes fixas | 477.650.882,00 | 477.651.000,00 | -118,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 |
| Outros | 199.325.044,00 | 199.325.000,00 | 44,00 | 41.957.074,00 | 41.957.000,00 | 74,00 | 14.166.748,47 | 14.161.000,00 | 5.748,47 |
| Abandono de poco (ARO) | 79.302.672,00 | 79.303.000,00 | -328,00 | 41.848.296,00 | 41.848.000,00 | 296,00 | 1.174.187,00 | 1.174.000,00 | 187,00 |
| Imobilizado em andamento | 72.171.064,00 | 72.171.000,00 | 64,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 |
| Blocos exploratorios | 20.156.531,00 | 20.157.000,00 | -469,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 |
| Adiantamentos | 18.418.664,00 | 18.419.000,00 | -336,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 |
| **Total** | **9.703.550.774,00** | **9.703.552.000,00** | **-1.226,00** | **3.532.711.455,00** | **3.532.711.000,00** | **455,00** | **672.064.236,61** | **671.868.000,00** | **196.236,61** |

**Valor liquido consolidado:** base R$ 6.170.839.319,00 x CVM 1.02.03 R$ 6.170.841.000,00 -> diferenca de R$ -1.681,00 (0.000027%).

**Explicacao das diferencas:**

1. **Saldos (custo e acumulada):** a DF e publicada em R$ mil; cada linha da NE 7.1 e um valor arredondado. A geracao reproduz, por classe e entidade, valores em centavos cuja diferenca para a linha publicada e de no maximo R$ 240 (arredondamento simulado). A diferenca do total e a soma dessas diferencas de linha - imaterial.
2. **Depreciacao/deplecao de 2025:** (a) desenvolvimento de campos e maquinas: os registros duplicados inseridos (erro E01) repetem a despesa do registro original, de modo que o razao simulado "contem" essa distorcao; (b) maquinas da SPE Tieta: os 12 itens simulados sao todos recentes e nao comportam a despesa minima da NE (R$ 12 mil) - diferenca de cerca de R$ 43 mil, imaterial.
3. **Intangivel (software, R$ 83.384 mil)** esta fora da base (a conta escolhida e o imobilizado).
4. **Por que o total bate mesmo com erros inseridos:** os erros estao **dentro** do saldo contabil - a base simula um razao que contem distorcoes, como a DF real poderia conter. A diferenca entre valor contabil e valor suportado aparece na inspecao (MUS) e nos testes.

## 5. Erros e inconsistencias inseridos (controle do preparador)

O log `controle_erros/LOG_ERROS_INSERIDOS.csv` registra, por registro, o tipo, o campo alterado, o valor original, o valor inserido e o efeito. **Os scripts de teste (T01-T10 e MUS) rodam sem ler o log**; ele so e aberto na etapa final de comparacao (`planilhas/TESTES_BASE_RECV3.xlsx`, aba `Inseridos_x_detectados`).

| Tipo | Natureza | Qtd. | Efeito monetario (R$) | Teste que deveria detectar | Detectados | Falsos positivos |
|---|---|---:|---:|---|---:|---:|
| E01 | Registro duplicado (mesmo documento, fornecedor, valor e data de aquisicao do registro original) | 160 | 6.737.989,18 | T01_DUPLICIDADE | 160 | 0 |
| E02 | Corte: data de aquisicao/capitalizacao posterior a 31/12/2025 (item nao existia na data-base) | 46 | 2.502.284,36 | T02_CORTE | 46 | 0 |
| E03 | Depreciacao acumulada superior ao custo (valor contabil liquido negativo) | 40 | -530.782,38 | T03_VCL_NEGATIVO | 40 | 0 |
| E04 | Depreciacao acumulada registrada a menor que o recalculo (taxa x tempo de uso) | 70 | 1.511.583,78 | T04_RECALCULO_DEPRECIACAO | 70 | 0 |
| E05 | Item com status BAIXADO (baixa em 2025) mantido com saldo no subrazao | 63 | 2.553.787,67 | T05_BAIXADO_COM_SALDO | 63 | 0 |
| E06 | Material de almoxarifado de investimento sem movimentacao ha mais de 5 anos (indicio de obsolescencia) | 95 | nao monetario | T06_ALMOX_SEM_MOVIMENTO_5A | 95 | 0 |
| E07 | Cadastro sem aprovacao (campo usuario_aprovacao vazio) | 620 | nao monetario | T07_MAKER_CHECKER | 620 | 0 |
| E08 | Campo nao cadastrado entre as 58 concessoes e documento de suporte inexistente (existencia) | 35 | 1.234.406,07 | T08_CAMPO_NAO_CADASTRADO | 35 | 0 |
| E09 | Custo registrado acima do suportado por documento (inclui despesa de manutencao capitalizada) | 97 | 9.172.612,04 | MUS (inspecao documental) | 2 | 0 |
| E10 | Ordem em andamento sem movimentacao ha mais de 2 anos | 45 | nao monetario | T09_ANDAMENTO_PARADO_2A | 45 | 0 |
| E11 | Data de aquisicao anterior a constituicao da companhia (21/07/1999) - erro cadastral | 30 | nao monetario | T10_DATA_ANTERIOR_CONSTITUICAO | 30 | 0 |
| | **Superavaliacao total inserida** | | **23.712.663,10** | | | |

## 6. Procedimentos executados com a base (resultados)

1. **Testes em 100% da populacao (T01-T10)** - todos os erros detectaveis por esses testes foram encontrados, **sem falsos positivos**. Deteccoes cruzadas esperadas: T04 tambem marca os itens de E03 e os itens lineares de E02; T07 marca algumas duplicatas cujo cadastrador sorteado coincidiu com o aprovador.
2. **MUS (Gramling, cap. 8; NBC TA 530)** - afirmacoes de existencia e avaliacao; unidade amostral = R$ 1 de valor contabil liquido.

| Parametro / resultado | Valor |
|---|---|
| Risco de deteccao | RA 5% / (RI 100% x RC 100%) = **5%** -> FC 3.00; FEE 1.60 (Ilustracao 8.7) |
| Incorrecao toleravel / esperada | IT = R$ 20.475.000,00; IE = R$ 2.047.500,00 |
| Intervalo | **I = (IT - IE x FEE) / FC = R$ 5.733.000,00** |
| Populacao | 517.770 itens com VCL > 0, R$ 6.171.370.101,38 (itens com VCL = 0 nao tem chance de selecao e itens com VCL < 0 sao testados a parte em T03 - Gramling p.302) |
| Tamanho | n max. = 1.076,46; 1076 pontos (inicio aleatorio R$ 3.429.906,84); **772 itens distintos** (56 no estrato superior); cobertura R$ 2.348.534.050,85 (38.1% do valor) |
| Erros encontrados | **5 itens** (E01: 3, E09: 2) |
| Avaliacao | precisao basica R$ 17.199.000,00 + IMP R$ 21.426.739,36 + ajuste incremental R$ 11.756.568,66 = **LSI R$ 50.382.308,03** |
| **Conclusao** | **NAO ACEITAR SEM TRABALHO ADICIONAL (LSI > IT)** -> PT 530 / PT 450 |

   *Validacao didatica:* o LSI (R$ 50.382.308,03) **cobre** a superavaliacao efetivamente inserida (R$ 23.712.663,10); a incorrecao mais provavel projetada foi R$ 21.426.739,36.

3. **Base complementar - folha e beneficios a empregados** (`folha/`): 1.942 empregados no cadastro (1.752 ativos, FRE 10.1A), 61.426 lancamentos de 2025, 9.160 obrigacoes em 31/12/2025. Conciliacao: obrigacoes = **R$ 88.753.000,00 = CVM 2.01.01**; custo de pessoal R$ 284.734.640,24 x R$ 284.002.000,00 da NE 19 (diferenca = efeito dos pagamentos indevidos inseridos F01 + F03 com encargos). Testes G01-G06: 99 excecoes, deteccao de 100% dos erros inseridos; R$ 1.887.633,53 vencendo a partir de 01/01/2027 estavam no circulante (reclassificar para nao circulante).

## 7. Como reproduzir

```bash
# na raiz P2_PetroReconcavo (Python 3.10+; pacotes em requirements.txt)
pip install -r requirements.txt
python codigo/rodar_passo3.py          # bases, conciliacao, testes, MUS, folha, dicionario e este README (~2 min)
python codigo/construir_notebook.py    # (opcional) recria o notebook a partir dos scripts
```
No **Google Colab**: abrir `notebooks/P2_RECV3_passo3_base_simulada.ipynb`, informar o link do repositorio na 1a celula e executar tudo.

O arquivo da base (`BASE_IMOBILIZADO_RECV3_SINTETICA.csv.gz`, 532.598 linhas; separador `;` e virgula decimal) fica abaixo do limite de 100 MB do GitHub; a amostra de 2.000 linhas em CSV simples serve para visualizacao rapida.

## 8. Limitacoes

1. Dados sinteticos: proporcoes, datas e valores individuais **nao** representam a carteira real de ativos; apenas os totais reproduzem a DF.
2. A distribuicao de producao e reservas por campo e um rateio sintetico de totais reais por ativo.
3. A materialidade foi determinada no PT 320; se for revista (NBC TA 320 itens 12-13), basta alterar `PARAM` em `codigo/testes_auditoria_base.py` e reexecutar.
4. Confirmacoes, inspecoes e entrevistas nao ocorreram; a "inspecao documental" e um arquivo simulado.
