# Dicionario de variaveis - bases simuladas (DADOS SINTETICOS)

Preparador: matricula 211059370. Gerado por `codigo/gerar_dicionario.py`, que tambem confere se cada variavel documentada existe no arquivo.

## Arquivos

| Arquivo | Linhas | Conteudo |
|---|---:|---|
| `base_simulada/BASE_IMOBILIZADO_RECV3_SINTETICA.csv.gz` | 532.598 | Base obrigatoria: subrazao analitico do imobilizado em 31/12/2025 - 1 linha = 1 item patrimonial/componente capitalizado |
| `base_simulada/INSPECAO_DOCUMENTAL_SIMULADA.csv.gz` | 532.598 | Resultado SIMULADO da inspecao de documentos (usado so para itens selecionados na amostra) |
| `base_simulada/PARAMETROS_CAMPOS_SIMULADOS.csv` | 58 | Cadastro das 58 concessoes com producao e reservas (rateio sintetico de totais reais) |
| `base_simulada/PLANO_CONTAS_IMOBILIZADO_SIMULADO.csv` | 29 | Plano de contas analitico SIMULADO do imobilizado |
| `base_simulada/CADASTRO_POCOS_SIMULADO.csv` | 7.200 | Cadastro sintetico de pocos |
| `base_simulada/controle_erros/LOG_ERROS_INSERIDOS.csv` | 1.301 | Log de controle dos erros inseridos na base do imobilizado (nao usado pelos testes) |
| `base_simulada/folha/CADASTRO_EMPREGADOS_SIMULADO.csv` | 1.942 | Base complementar: cadastro de empregados |
| `base_simulada/folha/FOLHA_PAGAMENTOS_2025_SIMULADA.csv` | 61.426 | Base complementar: lancamentos da folha de 2025 |
| `base_simulada/folha/OBRIGACOES_TRABALHISTAS_31122025_SIMULADAS.csv` | 9.160 | Base complementar: obrigacoes trabalhistas em 31/12/2025 |
| `base_simulada/controle_erros/LOG_ERROS_INSERIDOS_FOLHA.csv` | 90 | Log de controle dos erros inseridos na base de folha |

## BASE_IMOBILIZADO_RECV3_SINTETICA.csv.gz

| Variavel | Tipo | Descricao | Dominio / regra | Real ou simulado |
|---|---|---|---|---|
| `id_registro` | texto | Identificador unico do registro no subrazao | IMB-0000001 a IMB-0532598 (sequencial apos embaralhamento) | SIMULADO |
| `entidade` | texto | Entidade do grupo titular do item | PETRORECONCAVO (controladora) | SPE_TIETA (controlada 100%) | Estrutura REAL (NE 1); alocacao SIMULADA |
| `polo` | texto | Polo/ativo de producao | REMANSO, REMANSO_BT_REC, MIRANGA, POTIGUAR, TIETA, MIDSTREAM_RN | Polos REAIS (NE 7.1 ii; FRE 1.1) |
| `campo` | texto | Concessao (campo) ou local do item | 58 concessoes (nomes publicos quando disponiveis; "POT-CONC-xx (SINTETICO)" nos demais), blocos e UPGN Guamare | Parcialmente REAL |
| `uf` | texto | Unidade da federacao | BA, SE, RN | REAL por polo |
| `poco_id` | texto | Poco vinculado (classes desenvolvimento e ARO) | PRS-Cnn-nnnn; vazio nas demais classes | SIMULADO |
| `classe_ne7` | texto | Classe do imobilizado conforme NE 7.1 | 9 classes da NE 7.1 (maquinas, andamento, direito de producao, desenvolvimento, blocos, ARO, almoxarifado, adiantamentos, outros) | Classes REAIS |
| `conta_custo` | texto | Conta analitica de custo (plano simulado) | ver PLANO_CONTAS_IMOBILIZADO_SIMULADO.csv | SIMULADO |
| `descricao_conta` | texto | Descricao da conta de custo | texto do plano simulado | SIMULADO |
| `conta_depreciacao` | texto | Conta redutora de depreciacao/deplecao | 1.2.03.9x.001; vazio para itens que nao depreciam | SIMULADO |
| `descricao_conta_depreciacao` | texto | Descricao da conta redutora | texto | SIMULADO |
| `tipo_item` | texto | Natureza do componente/item | ex.: PERFURACAO E COMPLETACAO; UNIDADE DE BOMBEIO MECANICO; TUBO DE REVESTIMENTO (LOTE) | SIMULADO |
| `origem` | texto | Origem do registro | AQUISICAO_PETROBRAS, AQUISICAO_MAHA, AQUISICAO_BRAVA_JOA, RODADA_ANP, CAPEX_PROPRIO, COMPRA_MATERIAL, ARO_REMENSURACAO | Origens REAIS (NE 7, FRE 1.1); alocacao SIMULADA |
| `data_aquisicao` | data | Data de aquisicao/capitalizacao/entrada em estoque | AAAA-MM-DD; posterior a aquisicao do polo | SIMULADO |
| `data_inicio_depreciacao` | data | Inicio da depreciacao/deplecao | Linear: coerente com a acumulada (acumulada = custo x taxa x anos); UoP: = data de aquisicao | SIMULADO |
| `metodo_depreciacao` | texto | Metodo de depreciacao | LINEAR | UOP_1P | UOP_PDP | NAO_DEPRECIA (NE 7.2) | Metodos REAIS |
| `taxa_anual_linear` | decimal | Taxa anual (itens lineares) | Maquinas 10%; outros 4% a 20% (NE 7.2) | Taxas REAIS |
| `taxa_uop_campo_2025` | decimal | Taxa de unidades produzidas do campo em 2025 | producao 2025 / (reservas 31/12/2025 + producao 2025) | SIMULADO (a partir de totais reais) |
| `custo_historico` | moeda (R$) | Custo historico do item | Rateio exato em centavos por entidade x classe; soma = NE 7.1 (arredondamento) | Totais REAIS; itens SIMULADOS |
| `depreciacao_acumulada` | moeda (R$) | Depreciacao/deplecao acumulada (valor positivo da conta redutora) | Soma por entidade x classe = NE 7.1 | Totais REAIS; itens SIMULADOS |
| `valor_contabil_liquido` | moeda (R$) | Custo - depreciacao acumulada | soma consolidada = R$ 6.170.841 mil (CVM 1.02.03) | Total REAL; itens SIMULADOS |
| `depreciacao_2025` | moeda (R$) | Depreciacao/deplecao reconhecida em 2025 | UoP calibrada a NE 7.1; linear derivada das datas | SIMULADO |
| `status` | texto | Situacao do item | EM_OPERACAO, EM_CONSTRUCAO, EM_ESTOQUE, ADIANTAMENTO, EXPLORACAO, BAIXADO | SIMULADO |
| `data_baixa` | data | Data da baixa (se baixado) | vazio quando nao baixado | SIMULADO |
| `documento_origem` | texto | Documento que suporta o registro | NF-/OI-/CTR-/CCV-/MEM-/ANP- + numero | SIMULADO |
| `fornecedor_id` | texto | Fornecedor/contraparte | FORN-nnnnn; PETROBRAS; VENDEDORES_MAHA; ANP; 3R POTIGUAR (BRAVA); N/A (ESTIMATIVA) | SIMULADO (contrapartes reais nas aquisicoes) |
| `centro_custo` | texto | Centro de custo | CC-<polo>-<classe> | SIMULADO |
| `garantia_judicial` | texto | Bem dado em garantia judicial | S/N (uma sonda = S, NE 7.3) | Fato REAL; item SIMULADO |
| `usuario_cadastro` | texto | Usuario que cadastrou (maker) | USR001-USR028 | SIMULADO |
| `usuario_aprovacao` | texto | Usuario que aprovou (checker) | USR001-USR028; deve ser diferente do maker | SIMULADO |
| `data_cadastro_sistema` | data | Data de inclusao no sistema (trilha) | AAAA-MM-DD | SIMULADO |
| `data_ultima_alteracao` | data | Data da ultima alteracao (trilha de auditoria) | AAAA-MM-DD | SIMULADO |
| `natureza_dado` | texto | Marcador de dado sintetico | SINTETICO | Marcador |

## INSPECAO_DOCUMENTAL_SIMULADA.csv.gz

| Variavel | Tipo | Descricao | Dominio / regra | Real ou simulado |
|---|---|---|---|---|
| `id_registro` | texto | Chave para a base | igual a base | SIMULADO |
| `documento_origem` | texto | Documento inspecionado | igual a base | SIMULADO |
| `documento_localizado` | texto | Documento foi localizado? | S/N | SIMULADO |
| `data_documento` | data | Data constante do documento | AAAA-MM-DD | SIMULADO |
| `valor_liquido_suportado` | moeda (R$) | Valor liquido suportado pela evidencia (valor auditado no MUS) | <= valor contabil | SIMULADO |
| `observacao_inspecao` | texto | Resultado da inspecao | texto | SIMULADO |
| `natureza_dado` | texto | Marcador | SINTETICO | Marcador |

## PARAMETROS_CAMPOS_SIMULADOS.csv

| Variavel | Tipo | Descricao | Dominio / regra | Real ou simulado |
|---|---|---|---|---|
| `campo` | texto | Nome da concessao | 58 concessoes | Parcialmente REAL |
| `polo` | texto | Polo | 5 polos | REAL |
| `entidade` | texto | Titular | PETRORECONCAVO | SPE_TIETA | REAL |
| `ativo` | texto | Ativo (agrupamento do RA) | BAHIA | POTIGUAR | REAL |
| `uf` | texto | UF | BA, SE, RN | REAL |
| `data_aquisicao_polo` | data | Data de aquisicao/inicio do polo | FRE 1.1 | REAL (aproximada) |
| `n_pocos` | inteiro | Pocos simulados no campo | total 7.200 | SIMULADO |
| `producao_2025_boe` | inteiro | Producao 2025 do campo | rateio de 13,4 mil boe/d (Bahia) e 13,1 mil boe/d (Potiguar) - RA | Total REAL; rateio SIMULADO |
| `reservas_1P_31122025_boe` | inteiro | Reservas provadas 1P | rateio de 87,3 MMboe (Bahia) e 56,1 MMboe (Potiguar) - RA/NSAI | Total REAL; rateio SIMULADO |
| `reservas_PDP_31122025_boe` | inteiro | Reservas PDP | rateio proporcional de 61,4 MMboe (RA) | Total REAL; rateio SIMULADO |
| `taxa_uop_1P_2025` | decimal | Taxa UoP 1P | producao/(reserva+producao) | SIMULADO |
| `taxa_uop_PDP_2025` | decimal | Taxa UoP PDP | producao/(reserva+producao) | SIMULADO |
| `situacao_concessao` | texto | Situacao | PRODUCAO | REAL (NE 17.1) |
| `natureza_dado` | texto | Marcador | texto | Marcador |

## PLANO_CONTAS_IMOBILIZADO_SIMULADO.csv

| Variavel | Tipo | Descricao | Dominio / regra | Real ou simulado |
|---|---|---|---|---|
| `conta_custo` | texto | Codigo da conta | 1.2.03.xx.xxx | SIMULADO |
| `descricao_conta` | texto | Descricao | texto | SIMULADO |
| `classe_ne7` | texto | Classe da NE 7.1 | 9 classes | REAL |
| `conta_depreciacao` | texto | Conta redutora | 1.2.03.9x.001 | SIMULADO |
| `natureza_dado` | texto | Marcador | texto | Marcador |

## CADASTRO_POCOS_SIMULADO.csv

| Variavel | Tipo | Descricao | Dominio / regra | Real ou simulado |
|---|---|---|---|---|
| `poco_id` | texto | Identificador do poco | PRS-Cnn-nnnn | SIMULADO |
| `campo` | texto | Campo | 58 concessoes | Parcialmente REAL |
| `polo` | texto | Polo | 5 polos | REAL |
| `entidade` | texto | Titular | 2 entidades | REAL |
| `uf` | texto | UF | BA/SE/RN | REAL |
| `data_entrada` | data | Entrada do poco no grupo | aquisicao do polo ou perfuracao posterior | SIMULADO |
| `origem_poco` | texto | Origem | ADQUIRIDO_COM_O_POLO | PERFURADO_PELO_GRUPO | SIMULADO |
| `natureza_dado` | texto | Marcador | SINTETICO | Marcador |

## LOG_ERROS_INSERIDOS.csv

| Variavel | Tipo | Descricao | Dominio / regra | Real ou simulado |
|---|---|---|---|---|
| `seq` | inteiro | Sequencial | 1..n | Controle |
| `tipo_erro` | texto | Tipo do erro inserido | E01 a E11 | Controle |
| `descricao` | texto | Natureza do erro | texto | Controle |
| `campo_alterado` | texto | Variavel alterada | texto | Controle |
| `valor_original` | texto | Valor antes da insercao | texto | Controle |
| `valor_inserido` | texto | Valor inserido | texto | Controle |
| `id_registro` | texto | Registro afetado | IMB-... | Controle |
| `efeito_monetario_R$` | moeda (R$) | Efeito no valor liquido (+ superavaliacao; - subavaliacao; 0 = nao monetario) | R$ | Controle |

## CADASTRO_EMPREGADOS_SIMULADO.csv

| Variavel | Tipo | Descricao | Dominio / regra | Real ou simulado |
|---|---|---|---|---|
| `matricula` | texto | Matricula do empregado | M00001... | SIMULADO |
| `entidade` | texto | Empregador | 2 entidades | SIMULADO |
| `cpf_simulado` | texto | CPF ficticio (nao e CPF real) | SIM-nnnnnnnnn | SIMULADO |
| `nivel` | texto | Nivel hierarquico | LIDERANCA (249) | NAO_LIDERANCA (1.503) entre os ativos | Quantidades REAIS (FRE 10.1A) |
| `lotacao` | texto | Lotacao | sede e polos | SIMULADO |
| `data_admissao` | data | Admissao | AAAA-MM-DD | SIMULADO |
| `data_desligamento` | data | Desligamento (vazio = ativo em 31/12/2025) | AAAA-MM-DD | SIMULADO |
| `salario_base_mensal` | moeda (R$) | Salario base | calibrado a despesa de pessoal da NE 19 | SIMULADO |
| `banco_agencia_conta` | texto | Conta bancaria ficticia | bbb-aaaa-ccccccc | SIMULADO |
| `contrato_trabalho_arquivado` | texto | Contrato arquivado | S/N | SIMULADO |
| `usuario_cadastro` | texto | Maker (RH) | RH01-RH08 | SIMULADO |
| `usuario_aprovacao` | texto | Checker (RH) | RH01-RH08, diferente do maker | SIMULADO |
| `data_ultima_alteracao_salarial` | data | Trilha: ultima alteracao salarial | AAAA-MM-DD | SIMULADO |
| `pct_ultimo_reajuste` | decimal | Ultimo reajuste (%) | 0 a 65% | SIMULADO |
| `aprovador_reajuste` | texto | Alcada que aprovou o reajuste | GERENCIA_RH | DIRETORIA_PESSOAS (acima de 30% exige diretoria) | SIMULADO |
| `natureza_dado` | texto | Marcador | SINTETICO | Marcador |

## FOLHA_PAGAMENTOS_2025_SIMULADA.csv

| Variavel | Tipo | Descricao | Dominio / regra | Real ou simulado |
|---|---|---|---|---|
| `id_lancamento` | texto | Id do lancamento | FOL-nnnnnnn | SIMULADO |
| `competencia` | texto | Competencia | 2025-01 a 2025-12; 2025-13 = 13o | SIMULADO |
| `matricula` | texto | Matricula paga | chave do cadastro | SIMULADO |
| `rubrica` | texto | Rubrica | SALARIO, ADICIONAL_PERICULOSIDADE, HORAS_EXTRAS, 13O_SALARIO, FERIAS_+1/3, PLR_2024_PAGA, VERBAS_RESCISORIAS | SIMULADO |
| `valor_bruto` | moeda (R$) | Valor bruto | R$ | SIMULADO |
| `data_pagamento` | data | Data do pagamento | AAAA-MM-DD | SIMULADO |
| `conta_credito` | texto | Conta creditada | conta do cadastro | SIMULADO |
| `encargos_patronais` | moeda (R$) | INSS patronal + FGTS (36,8%) | R$ | SIMULADO |
| `beneficios` | moeda (R$) | Beneficios (11,5% da folha bruta) | R$ | SIMULADO |
| `natureza_dado` | texto | Marcador | SINTETICO | Marcador |

## OBRIGACOES_TRABALHISTAS_31122025_SIMULADAS.csv

| Variavel | Tipo | Descricao | Dominio / regra | Real ou simulado |
|---|---|---|---|---|
| `id_obrigacao` | texto | Id da obrigacao | PROV-nnnnnn | SIMULADO |
| `matricula` | texto | Empregado | chave do cadastro | SIMULADO |
| `tipo_obrigacao` | texto | Natureza | salario de dezembro, encargos, ferias, PLR 2025, outras, bonus de retencao | SIMULADO |
| `valor` | moeda (R$) | Saldo em 31/12/2025 | soma = R$ 88.753 mil (CVM 2.01.01) | Total REAL; itens SIMULADOS |
| `data_vencimento` | data | Vencimento | ate 31/12/2026 = circulante; a partir de 01/01/2027 = nao circulante | SIMULADO |
| `classificacao_registrada` | texto | Classificacao no balanco | CIRCULANTE | SIMULADO |
| `natureza_dado` | texto | Marcador | SINTETICO | Marcador |

## LOG_ERROS_INSERIDOS_FOLHA.csv

| Variavel | Tipo | Descricao | Dominio / regra | Real ou simulado |
|---|---|---|---|---|
| `tipo_erro` | texto | Tipo | F01 a F06 | Controle |
| `chave` | texto | Matricula ou id_obrigacao afetado | texto | Controle |
| `descricao` | texto | Natureza do erro | texto | Controle |
| `efeito_monetario_R$` | moeda (R$) | Efeito monetario | R$ | Controle |
