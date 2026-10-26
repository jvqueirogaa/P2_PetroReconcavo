# PT 230 – Documentação de auditoria: índice, convenções, versões e arquivo

| Campo | Conteúdo |
|---|---|
| **Código** | PT 230 |
| **Norma e itens** | NBC TA 230 (R1), itens 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, A1, A21 e A23 |
| **Versão consultada** | NBC TA 230 (R1), de 19/08/2016 (consolidado da disciplina) |
| **Preparador** | Matrícula 211059370 – 24/10/2026 |
| **Revisão** | ______ (campo reservado; não preenchido) |
| **Classificação** | Realizado (organização do próprio dossiê) |

## 1. Objetivo
Preparar documentação suficiente para que um **auditor experiente, sem envolvimento anterior**, entenda (item 8):
- (a) a natureza, a época e a extensão dos procedimentos;
- (b) os resultados e a evidência obtida;
- (c) os assuntos significativos e os julgamentos feitos.

Também definir a montagem e a guarda do arquivo (itens 14 a 16).

## 2. Índice do dossiê (arquivo de auditoria)

| Código | Título | Norma | Arquivo |
|---|---|---|---|
| — | README do repositório (identificação, organização, reprodução) | — | `README.md` |
| REG | Registro de fontes (URL, data e hora de acesso, documento, página, exercício, hash) | NBC TA 500/230 | `planilhas/REG_FONTES_RECV3.xlsx` |
| DIAG | Diagnóstico da companhia (DFs, AV/AH, ranking do ativo, NE 7, debêntures, estimativas, indicadores, grupo, achados) | NBC TA 315/520 | `diagnostico/ETAPA2_Diagnostico_RECV3.md`; `planilhas/DIAG_RECV3.xlsx` |
| BASE | Base simulada do imobilizado + folha (README, dicionário, conciliação, testes, MUS) | NBC TA 500/530 | `base_simulada/`; `planilhas/CONC_BASE_RECV3.xlsx`; `planilhas/TESTES_BASE_RECV3.xlsx`; `planilhas/TESTES_FOLHA_RECV3.xlsx`; `notebooks/` |
| PT EC | Caracterização do trabalho de asseguração | EC | `papeis_trabalho/PT_EC_Estrutura_Conceitual.md` |
| PT 200 | Objetivos gerais, ética, ceticismo, risco | 200 | `PT_200_Objetivos_Gerais.md` |
| PT 210 | Termos do trabalho e precondições | 210 | `PT_210_Termos_do_Trabalho.md` |
| PT 220 | Gestão da qualidade | 220 | `PT_220_Gestao_da_Qualidade.md` |
| PT 230 | Documentação (este PT) | 230 | `PT_230_Documentacao.md` |
| PT 240 | Fraude | 240 | `PT_240_Fraude.md` |
| PT 250 | Leis e regulamentos | 250 | `PT_250_Leis_e_Regulamentos.md` |
| PT 260 | Comunicação com a governança | 260 | `PT_260_Comunicacao_Governanca.md` |
| PT 265 | Deficiências de controle | 265 | `PT_265_Deficiencias_Controle.md` |
| PT 300 | Planejamento (estratégia, plano, cronograma, programas por ciclo) | 300 | `PT_300_Planejamento.md` |
| PT 315 | Identificação e avaliação de riscos (matriz conta × afirmação) | 315 | `PT_315_Riscos.md` |
| PT 320 | Materialidade | 320 | `PT_320_Materialidade.md`; `planilhas/PT320_MATERIALIDADE_RECV3.xlsx` |
| PT 330 | Respostas aos riscos | 330 | `PT_330_Respostas.md` |
| PT 402 | Organizações prestadoras de serviços | 402 | `PT_402_Prestadoras_Servicos.md` |
| PT 450 | Avaliação das distorções | 450 | `PT_450_Distorcoes.md` |
| PT 500 | Evidência | 500 | `PT_500_Evidencia.md` |
| PT 501 | Itens específicos (estoques, litígios, segmentos) | 501 | `PT_501_Itens_Especificos.md` |
| PT 505 | Confirmações externas | 505 | `PT_505_Confirmacoes_Externas.md` |
| PT 510 | Saldos iniciais (auditoria inicial) | 510 | `PT_510_Saldos_Iniciais.md` |
| PT 520 | Procedimentos analíticos | 520 | `PT_520_Analiticos.md`; `planilhas/PT520_ANALITICOS_RECV3.xlsx` |
| PT 530 | Amostragem (MUS na base simulada) | 530 | `PT_530_Amostragem.md` |
| PT 540 | Estimativas (provisão para abandono, com sensibilidade) | 540 | `PT_540_Estimativas.md`; `planilhas/PT540_ARO_SENSIBILIDADE_RECV3.xlsx` |
| PT 550 | Partes relacionadas | 550 | `PT_550_Partes_Relacionadas.md` |
| PT 560 | Eventos subsequentes | 560 | `PT_560_Eventos_Subsequentes.md` |
| PT 570 | Continuidade operacional | 570 | `PT_570_Continuidade.md` |
| PT 580 | Representações formais | 580 | `PT_580_Representacoes_Formais.md` |
| PT 600 | Auditoria de grupos | 600 | `PT_600_Grupos.md` |
| CONC | Conclusão integrada | — | `PT_999_Conclusao_Integrada.md` |
| MAT | Matriz de cobertura das normas | todas | `matriz_cobertura/MATRIZ_COBERTURA_NORMAS.xlsx` |
| IA | Registro de uso de IA | 220/230 | `docs/USO_DE_IA.md` |

## 3. Convenções

| Convenção | Regra |
|---|---|
| **Código de PT** | "PT" + número da NBC TA (ex.: PT 315). PT 999 = conclusão integrada |
| **Fontes** | F01 a F39 (registro de fontes). Página = **página do PDF**, não a impressa. Ex.: "F01 p.69" = NE 7.1 consolidada |
| **Referência cruzada** | `→ PT xxx §n` (seção n do PT de destino). Riscos: `R01…` (PT 315); respostas: `P01…` (PT 330); deficiências: `D01…` (PT 265); distorções: `M01…` (PT 450) |
| **Rótulos de procedimento** (enunciado, item 2) | **[REALIZADO]** com evidência pública · **[PLANEJADO]** por falta de acesso · **[SIMULADO]** para fins didáticos, com dados sintéticos |
| **Valores** | R$ mil nas tabelas da DF; R$ (centavos) na base simulada |
| **Dados sintéticos** | Coluna `natureza_dado = SINTETICO`; arquivos em `base_simulada/` |
| **Preparador e revisão** | Todo PT traz matrícula, data e campo de revisão **em branco** (sem revisão simulada – itens 9(b) e 9(c)) |

## 4. Itens 9 a 11 – como o dossiê atende
- **9(a) Características dos itens testados:** `id_registro` da base, listas de exceções e amostra MUS (`base_simulada/resultados/`).
- **9(b) Quem executou e quando:** cabeçalho de cada PT.
- **9(c) Quem revisou, quando e extensão:** campo de revisão (não preenchido, porque não houve revisão de terceiros).
- **10 Discussões com administração e governança:** **não houve contato** (vedado pelo enunciado). As comunicações são minutas (PT 260 e PT 580).
- **11 Informações inconsistentes com a conclusão:** documentadas onde ocorreram. Ex.: NE 3.4 × valor de mercado (PT 540); NE 9 × NE 25 (PT 450).

## 5. Item 12 – requisito não atendido
Requisitos que dependem de acesso, como confirmação externa, observação de inventário e indagação, não foram atendidos. **Procedimentos alternativos possíveis com fontes públicas** e a razão estão em cada PT (PT 501, PT 505, PT 500).

## 6. Controle de versões
- **Ferramenta:** Git/GitHub; cada alteração gera *commit* com data e descrição.
- **Versão de entrega:** **v1.0, de 25/10/2026** (*tag* no repositório).
- **Alterações relevantes já registradas antes da entrega:**
  - materialidade provisória (R$ 35.000 mil) substituída pela do PT 320 (R$ 31.500 mil), com todos os testes reexecutados;
  - calibração da depreciação linear da base simulada.
- **Reprodutibilidade:** scripts em `codigo/`, semente fixa e *hash* do conteúdo da base em `base_simulada/METADADOS_GERACAO.json`.

## 7. Montagem e guarda do arquivo (itens 14 a 16; A21 e A23)
- **Montagem:** até **60 dias** após a data do relatório (A21). Neste dossiê, a montagem coincide com a entrega (*tag* v1.0).
- **Após a montagem:** nada é apagado antes do fim do período de guarda (item 15). Alterações posteriores exigem registro do motivo, da data e do autor (item 16), feito pelo histórico do Git.
- **Guarda:** em geral, **mínimo de 5 anos** da data do relatório (A23). O repositório público e o histórico do Git servem de trilha.

## 7A. Item 13 – procedimentos após a data do relatório
Em circunstâncias excepcionais, procedimentos novos ou conclusões diferentes após a data do relatório exigem documentar:
- (a) as circunstâncias;
- (b) os procedimentos, a evidência e o efeito no relatório;
- (c) quando e por quem as alterações foram feitas e revisadas.

**Aplicação neste dossiê:** a leitura de fatos posteriores a 18/03/2026 (PT 560, seção 4) é **acadêmica**. Não alterou nenhuma conclusão e está documentada com data e fonte no próprio PT 560 e no REG_FONTES.

## 8. Conclusão
O dossiê está organizado de forma que um auditor experiente sem envolvimento anterior possa reexecutar e entender os procedimentos (item 8): os índices, códigos, fontes, scripts e a base são reproduzíveis.
