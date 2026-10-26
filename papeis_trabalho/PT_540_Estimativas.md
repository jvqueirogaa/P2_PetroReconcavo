# PT 540 – Auditoria de estimativas contábeis e divulgações relacionadas

| Campo | Conteúdo |
|---|---|
| **Código** | PT 540 |
| **Norma e itens** | NBC TA 540 (R2), itens 13 (entendimento), 14 (revisão retrospectiva), 15 (especialistas), 16 e 17 (riscos), 18 a 20 (respostas), 22 a 26 (teste do processo da administração: método, premissas, dados, estimativa pontual e incerteza), 27 a 29 (estimativa ou intervalo do auditor), 30, 32 (tendenciosidade), 33 a 36 (avaliação), 37 (representações), 38 (comunicação) e 39 (documentação) |
| **Versão consultada** | NBC TA 540 (R2) (consolidado da disciplina) |
| **Preparador** | Matrícula 211059370 – 24/10/2026 |
| **Revisão** | ______ (campo reservado; não preenchido) |
| **Classificação** | **[REALIZADO]** entendimento, revisão retrospectiva, recálculo da movimentação e do *unwinding*, indicadores de *impairment* · **[SIMULADO]** sensibilidade sobre cronograma sintético calibrado · **[PLANEJADO]** teste dos modelos internos |
| **Papéis de suporte** | `planilhas/PT540_ARO_SENSIBILIDADE_RECV3.xlsx` (fórmulas) · `planilhas/PT540_resultados.json` · `codigo/pt540_aro_sensibilidade.py` |

## 1. Objetivo
Obter evidência apropriada e suficiente de que as estimativas contábeis e as divulgações relacionadas são **razoáveis** no contexto do CPC (objetivo da norma; item 35).

## 2. Inventário das estimativas e entendimento (item 13) – [REALIZADO]

| # | Estimativa | Valor (R$ mil) | Requisito do CPC | Método da administração | Incerteza (item 16(a)) | Complexidade / subjetividade (16(b)) | Risco |
|---|---|---:|---|---|---|---|---|
| E1 | **Provisão para abandono de poços (ARO)** | **145.192** | CPC 25; ICPC 12 | Valor presente dos custos futuros: taxa nominal de 10,56% e inflação de 3,56% (NE 3.3); revisão anual | **Alta:** horizonte de décadas; custos e época incertos | Alta: modelo e premissas econômicas | **Significativo (R02)** – PAA da EY |
| E2 | **Recuperabilidade do imobilizado (*impairment*)** | Imobilizado e intangível de 6.254.225 | CPC 01 (R1) | A NE 3.4 informa revisão anual e **ausência de indicativos** | Alta (preço do Brent, reservas, taxas) | Alta | **Significativo (R01)** |
| E3 | **Reservas → depleção por unidades produzidas** | Depleção, amortização e depreciação de 721.077 (NE 19) | CPC 27; NE 3.2 | Taxa por campo = produção / reservas remanescentes (certificação NSAI – PRMS) | Média | Alta (especialista) | Elevado (R01/R06) |
| E4 | IR diferido (passivo líquido) | 52.211 | CPC 32 | Projeção de lucro tributável e incentivo SUDENE | Média | Média | Normal |
| E5 | Valor justo dos derivativos (*swaps*, NDF, *collar*) | Ativos 35.055; passivos 88.449 | CPC 46/48 | Modelos de mercado (nível 2) | Baixa-média | Média | Normal (PT 505 – C02) |
| E6 | Créditos de gás de 2022 em disputa | 55.917 | CPC 48 (perda esperada) | Expectativa de recebimento; arbitragem na CCI | **Alta** (resultado da mediação) | Alta (jurídico) | Elevado (R09) |
| E7 | Pagamento baseado em ações | 7.320 (despesa) | CPC 10 | Valor justo na outorga (inclui condição de TSR) | Baixa | Média | Normal |
| E8 | Recuperabilidade do almoxarifado e das obras paradas | [SIMULADO] exposição de 1.415 (T06, T09) | CPC 01 | — | Média | Baixa | PT 450 (M07, M08) |

**Controles (item 13(i)):** os controles da administração sobre as estimativas (revisão pelo CAE, aprovação das premissas, uso do especialista NSAI) não foram testados. Abordagem substantiva (PT 330).

**Especialistas (item 15):** E1 e E2 exigem especialista em modelos financeiros e em engenharia de reservas na equipe. A EY usou "especialistas de modelos financeiros" (F01, PAA).

## 3. Revisão retrospectiva (item 14; A55 a A60) – [REALIZADO]

| Teste | Esperado (estimativa de 2024) | Realizado em 2025 | Leitura |
|---|---:|---:|---|
| *Unwinding* 2025 = saldo de 2024 × taxa de 2024 (136.972 × 10,92%) | 14.957 | 14.958 (NE 13.1) | **Coerente:** a mecânica do desconto está correta (item 23(c)) |
| **Baixas de 2025 × parcela circulante prevista em 31/12/2024** | **342** | **14.856** | **Desembolsos 43,4 vezes maiores** que o previsto como circulante. A estimativa de **época** em 2024 falhou |
| Baixas de 2025 × parcela circulante de 31/12/2025 | 4.728 | (14.856 em 2025) | Se o ritmo de 2025 se repetir em 2026, o **circulante de 2025 pode estar subestimado** (classificação – PT 450) |
| Movimentos de estimativa | 2024: **reversão de 67.369** (−36% do saldo de 2023) · 2025: constituição de 8.383 | — | Revisões grandes e em direções opostas: **volatilidade** da estimativa, sem padrão único de viés |

A revisão **não** questiona o julgamento de 2024 com as informações daquela época (item 14). Ela serve para calibrar o risco de 2025: a estimativa da **época dos abandonos** tem histórico de erro relevante.

## 4. E1 – Provisão para abandono (ARO): respostas (itens 18 a 29)

**Abordagem escolhida (item 18):** (b) testar o processo da administração e (c) desenvolver um **intervalo** do auditor. Como o risco é significativo e a abordagem é só substantiva, os procedimentos incluem **testes de detalhes** (item 20).

| Item | Exigência | Procedimento | Situação |
|---|---|---|---|
| 23(a) | Método apropriado | Valor presente de custos futuros, com a contrapartida no ativo (ICPC 12) – NE 13 | **[REALIZADO]** método coerente com o CPC |
| 23(c) | Exatidão matemática | Movimentação: 136.972 + 8.383 − 265 + 14.958 − 14.856 = **145.192** (sem diferença); *unwinding* recalculado | **[REALIZADO]** |
| 24(a)(b) | Premissas apropriadas; tendenciosidade | **Taxa real implícita:** 6,76% em 2025 contra 7,00% em 2024 (queda de 0,24 p.p.), o que **aumenta** o passivo. A direção não indica viés para reduzir a provisão. A taxa nominal deve ser confrontada com a curva de títulos públicos de longo prazo em 31/12/2025, e a inflação com a expectativa de mercado de longo prazo | **[REALIZADO]** direção · **[PLANEJADO]** comparação com curvas externas |
| 24(c) | Consistência com outras áreas | A época dos abandonos deve ser consistente com a vida das reservas usada na depleção (E3) e no *impairment* (E2): 1P de 143,3 MMboe ÷ produção de cerca de 9,7 MMboe/ano ≈ 14,8 anos | **[REALIZADO]** referência usada no cronograma sintético · **[PLANEJADO]** conciliar com os cronogramas internos |
| 25 | Dados (custos por poço, número de poços, sondas) | Inventário de poços (base simulada: 7.200 registros ARO, `CADASTRO_POCOS_SIMULADO.csv`); custos unitários de abandono × contratos de sonda (PERBRAS – PT 550) | **[SIMULADO]** / **[PLANEJADO]** |
| 26 | A administração entendeu e tratou a incerteza? | A NE 3.3 descreve as premissas, mas **não traz análise de sensibilidade** | **[REALIZADO]** ver seção 4.2 |
| 28 e 29 | Intervalo do auditor | Seção 4.1 | **[SIMULADO]** |

### 4.1 Sensibilidade – [SIMULADO para fins didáticos]
**Método.** A companhia não divulga o cronograma de desembolsos. O script cria um cronograma **sintético** em moeda de 31/12/2025:
- 2026 = parcela circulante publicada;
- 2027 a 2050 com perfil triangular e pico em 2040 (vida das reservas);
- calibrado para que o valor presente com as premissas da NE 3.3 reproduza **exatamente R$ 145.192 mil**;
- total não descontado: R$ 336.882 mil.

| Cenário | Provisão (R$ mil) | Δ (R$ mil) | % da ME (20.475) | % da MG (31.500) |
|---|---:|---:|---:|---:|
| Base (10,56% / 3,56%) | 145.192 | — | — | — |
| Taxa de desconto **+1 p.p.** | 130.572 | −14.620 | 71,4% | 46,4% |
| Taxa de desconto **−1 p.p.** | 161.994 | +16.802 | 82,1% | 53,3% |
| Inflação **+1 p.p.** | 163.032 | +17.840 | 87,1% | 56,6% |
| Inflação **−1 p.p.** | 129.513 | −15.679 | 76,6% | 49,8% |
| Pior combinação (taxa −1 p.p. e inflação +1 p.p.) | 182.362 | **+37.170** | **181,5%** | **118,0%** |
| **Custos +1%** (sensibilidade de 1%) | 146.644 | +1.452 | 7,1% | 4,6% |
| Custos +10% | 159.711 | +14.519 | 70,9% | 46,1% |
| Abandonos antecipados em 2 anos | 164.703 | +19.511 | 95,3% | 61,9% |
| Premissas de 2024 sobre o mesmo cronograma | 141.301 | −3.891 | 19,0% | 12,4% |

**Intervalo do auditor (item 29(a)):** cenários individuais de ±1 p.p. → **R$ 129,5 mi a R$ 164,7 mi**. A amplitude de cerca de R$ 35 mi supera a **MG**. A estimativa pontual da administração (R$ 145,2 mi) fica **dentro** do intervalo. A combinação extrema (R$ 182,4 mi) é descartada como base do intervalo: o item 29(a) exige que o intervalo inclua só valores suportados por evidência e razoáveis. O choque simultâneo e oposto de 1 p.p. em taxa e inflação é pouco plausível, porque as duas variáveis tendem a andar juntas.

**Leitura.** O valor da provisão é **altamente sensível**: um único ponto percentual em uma premissa movimenta 71% a 87% da ME. Isso confirma o **risco significativo (R02)** e torna as premissas e a época os pontos centrais dos testes de detalhes (item 20). A sensibilidade de 1% nos custos é pequena (R$ 1,5 mi; abaixo do trivial).

### 4.2 Divulgação da incerteza (itens 26(b), 27 e 36)
- O CPC 26, item 125, exige divulgar as fontes de incerteza com risco significativo de ajuste relevante no próximo exercício, inclusive a **sensibilidade** quando aplicável (item 129).
- A NE 3.3 lista as premissas, mas não quantifica a sensibilidade, embora ±1 p.p. mova a provisão em valores próximos à ME.
- **Item 27(a):** solicitar à administração a inclusão da análise de sensibilidade da taxa, da inflação e da época **[PLANEJADO]**.
- Se não for incluída, avaliar se a divulgação é suficiente para a apresentação adequada (item 36(a)). A materialidade específica para essa divulgação é **qualitativa** (PT 320, A11).
- **Item 27(c):** a ausência de sensibilidade, somada à falha histórica de época (seção 3), é **outra deficiência** a comunicar (PT 265, item 10(b)).

### 4.3 Outras divulgações relacionadas às estimativas (item 31)
Além da incerteza (itens 26(b) e 29(b)), foram avaliadas:
- a descrição do método e das bases de mensuração (NE 3.3 e NE 13);
- a movimentação (NE 13.1, conferida);
- a classificação circulante × não circulante (4.728 / 140.464), que pode estar subestimada no circulante (seção 3).

Para E2, falta a divulgação do indicativo e das premissas (CPC 01, item 134), recomendada (seção 5).

## 5. E2 – Recuperabilidade do imobilizado (R01) – [REALIZADO] indicadores / [PLANEJADO] teste

| Indicador (CPC 01, itens 12 a 14) | Evidência | Leitura |
|---|---|---|
| **12(d) – valor contábil do PL maior que o valor de mercado** | Valor de mercado de R$ 3,3 bi (ações a R$ 11,32 em 31/12/2025 – RA) × PL de R$ 4,33 bi → **0,77x** | **Indicativo externo presente** |
| 12(a)/(b) – queda de preços e ambiente adverso | Brent médio de US$ 69,10 (−14%); lucro operacional −24%; 1S26 com lucro −29,9% (ITR 2T26) | Reforça o indicativo |
| Folga indicativa (PV-10 1P) | PV-10 1P da NSAI = US$ 1,9 bi × PTAX 5,5024 = **R$ 10,45 bi** contra R$ 6,25 bi de imobilizado e intangível → folga de **1,67x**. O valor recuperável só ficaria abaixo do contábil se o PV-10 caísse **40,2%** (1 − 6,254/10,455) | Folga **aparente** relevante. Porém, o PV-10 é **antes de impostos**, usa taxa de 10% e o cenário de preços da certificadora; **não** é o valor em uso do CPC 01 |
| Declaração da administração | NE 3.4: não identificou indicativos | **Inconsistente** com o indicador 12(d) |

**Avaliação (itens 24(b), 32 e 33):**
- A administração **não reconhece** um indicativo que o próprio CPC 01 lista. Esse julgamento pode indicar **tendenciosidade** (item 32), porque evita a formalização do teste e a divulgação das premissas (CPC 01, item 134).
- **Resposta [PLANEJADO]:** solicitar o teste de recuperabilidade por unidade geradora de caixa (Ativo Bahia × Ativo Potiguar), ou pelo menos a análise formal do indicativo, com fluxos pós-impostos, taxa pré-impostos equivalente e cenário de preços de mercado.
- **Resposta [SIMULADO]:** se o teste não for fornecido, desenvolver estimativa pontual a partir do PV-10 ajustado por impostos (alíquota efetiva com SUDENE) e por cenário de Brent 10% menor (item 28).
- **Divulgação:** recomendar a divulgação do indicativo e da conclusão (PT 260; minuta, seção 2).

## 6. E3 – Reservas e depleção (item 30 e NBC TA 500, item 8)
- Especialista da administração: NSAI (PT 500, seção 3).
- **[REALIZADO]** 1P de 143,3 MMboe (Bahia 87,3; Potiguar 56,1).
- **[PLANEJADO]** recálculo da taxa de depleção por campo: produção do ano ÷ (reservas finais + produção). A base sintética usa taxas calibradas por campo (`PARAMETROS_CAMPOS_SIMULADOS.csv`) e reproduz a depleção da NE 7.1 (PT 530 e `CONC_BASE_RECV3.xlsx`).

## 7. Tendenciosidade da administração (item 32) – resumo
| Indicador | Direção | Conclusão |
|---|---|---|
| Mudança da taxa real (E1) | Aumenta o passivo | Não indica viés para reduzir |
| Reversão de 36% em 2024 e baixas 43 vezes acima do circulante previsto (E1) | Misto | Volatilidade, não viés demonstrado |
| Não reconhecimento do indicativo de *impairment* (E2) | Evita teste e divulgação | **Possível indicador de viés** → PT 240 (item 33(b)) e PT 260 |

## 8. Avaliação final (itens 33 a 36), representações (37), comunicação (38) e documentação (39)
- **Item 33(a):** os riscos R01 e R02 continuam **significativos**.
- **Item 33(c):** a evidência pública **não é suficiente** para concluir sobre E1 e E2. Faltam modelos internos, curvas externas e o teste de recuperabilidade.
- **Item 35:** a estimativa pontual de E1 está **dentro** do intervalo do auditor (simulado). E2 está **pendente**.
- **Item 37:** representação no PT 580, item 8.
- **Item 38 (NBC TA 260, item 16(a)):** aspectos qualitativos comunicados ao CAE: indicativo de *impairment*, sensibilidade da provisão para abandono e falha histórica na estimativa de época.
- **Item 39:** documentação neste PT e na planilha de suporte, incluindo os julgamentos significativos (cronograma sintético, descarte do cenário combinado).

## 9. Referências cruzadas
PT 315 (R01, R02, R06, R09) · PT 320 (A11 – materialidade qualitativa da sensibilidade) · PT 330 · PT 240 (item 33(b)) · PT 450 (M07, M08; classificação do circulante da provisão) · PT 500 (NSAI) · PT 505 (C02, C05) · PT 510 (provisão para abandono de 2024) · PT 530 · PT 560 (P5) · PT 570 · PT 580 · PT 260 · PT 265.

## 10. Conclusão e limitações
- **E1 (provisão para abandono):** movimentação e *unwinding* conferem. As premissas mudaram na direção de **aumentar** o passivo. A sensibilidade (simulada) mostra que ±1 p.p. movimenta 71% a 87% da ME, e a divulgação **não traz sensibilidade**. A estimativa de época falhou em 2024.
- **E2 (*impairment*):** há um **indicativo externo não tratado** pela administração. A folga aparente pelo PV-10 (1,67x) não substitui o teste do CPC 01.

**Limitação:** o cronograma de desembolsos é **sintético**. Os valores de sensibilidade são ilustrativos e servem para dimensionar o risco e planejar os testes. Não são números da companhia.
