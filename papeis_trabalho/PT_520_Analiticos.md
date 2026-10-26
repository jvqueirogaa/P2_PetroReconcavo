# PT 520 – Procedimentos analíticos

| Campo | Conteúdo |
|---|---|
| **Código** | PT 520 |
| **Norma e itens** | NBC TA 520, itens 4 (definição), 5 (a)–(d) (procedimentos analíticos substantivos), 6 (procedimento analítico próximo ao fim) e 7 (a)–(b) (investigação); A16 (limite de diferença aceitável). Avaliação de riscos: NBC TA 315, item 14(b) |
| **Versão consultada** | NBC TA 520, de 27/11/2009 (consolidado da disciplina) |
| **Preparador** | Matrícula 211059370 – 24/10/2026 |
| **Revisão** | ______ (campo reservado; não preenchido) |
| **Classificação** | **[REALIZADO]** com evidência pública (DFP 2025, DF 2024, dados abertos da CVM, relatório da administração) · **[PLANEJADO]** corroboração das explicações (item 7) |
| **Papéis de suporte** | `planilhas/PT520_ANALITICOS_RECV3.xlsx` (6 abas com fórmulas) · `codigo/pt520_analiticos.py` · DIAG (`DRE_con`, `BPA_con`, `BPP_con`, `Indicadores`) |

## 1. Objetivo
- Obter evidência relevante e confiável com procedimentos analíticos **substantivos** (item 5).
- Executar, perto do fim da auditoria, um procedimento analítico que ajude a concluir se as DFs são consistentes com o entendimento da entidade (item 6).

## 2. Procedimento analítico substantivo da receita (item 5) – aba `Receita_item5`

| Alínea | Exigência | Aplicação |
|---|---|---|
| (a) | Adequação às afirmações | Receita de *commodity* com relação previsível: **volume × preço em US$ × câmbio** (ocorrência e exatidão). Como R03 é **risco significativo**, o analítico **não basta sozinho**: a NBC TA 330, item 21, exige teste de detalhes (PT 330 – P03) |
| (b) | Confiabilidade dos dados | Volumes e preços médios do relatório da administração (informação da entidade, consistente com os dados operacionais mensais – CM de 08/01/2026). Brent e câmbio são verificáveis externamente |
| (c) | Expectativa suficientemente precisa | Modelo: petróleo 2025 = venda de 2024 × (1 + Δprodução) × (preço 2025 / preço 2024) × (1 + Δdólar). Gás 2025 = venda de 2024 × (1 + Δpreço) × (1 + Δvolume) |
| (d) | Diferença aceitável sem investigação | **50% da ME = R$ 10.238 mil**. Julgamento pelo A16: maior segurança desejada para risco significativo → limite menor que a ME |

| Produto | Registrado (R$ mil) | Esperado (R$ mil) | Diferença | Limite | Resultado |
|---|---:|---:|---:|---:|---|
| Petróleo | 2.113.133 | 2.126.322 | **−13.189 (−0,6%)** | 10.238 | **Investigar** |
| Gás e subprodutos | 1.554.086 | 1.554.946 | −860 (−0,1%) | 10.238 | Dentro do limite |

**Leitura do petróleo (item 7).**
- A diferença de 0,6% excede o limite, mas os insumos do modelo são **percentuais arredondados** do relatório da administração ("+2%", "+4%"). Cada um tem precisão de cerca de ±0,5 p.p., o que gera incerteza de cerca de ±R$ 25 mi na expectativa.
- Pelo item 5(c), a expectativa **não é precisa o bastante** para o limite escolhido.
- **Resposta [PLANEJADO]:** refazer desagregado por **mês e por ativo** (Bahia × Potiguar), com volumes vendidos e preços efetivos (desconto em relação ao Brent: US$ 3,66 na Bahia e US$ 12,87 no Potiguar), e corroborar com corte e confirmação (PT 505 – C04).

## 3. Procedimentos analíticos de avaliação de riscos e de razoabilidade (NBC TA 315, item 14(b))

### 3.1 Gastos por natureza (NE 19) – aba `Custos_NE19`
Critério de investigação: variação absoluta maior que a ME.

| Natureza | 2025 | 2024 | Var. % | Investigar? | Expectativa / explicação a obter |
|---|---:|---:|---:|---|---|
| Serviços e materiais | 720.753 | 553.842 | +30,1% | **Sim** | Cresceu muito acima da produção (+0,7%). Hipóteses: custos da UPGN (JOA a partir de out./2025) e *workover* lançado no resultado. Ligação com R06 (capitalização) |
| Outras | 10.430 | 73.920 | −85,9% | **Sim** | Composição de 2024 (itens não recorrentes?) |
| Compra/"swap" de gás | 104.707 | 61.951 | +69,0% | **Sim** | Coerente com a "maior compra de gás de terceiros" (relatório da administração) |
| Processamento de gás | 189.748 | 219.741 | −13,6% | **Sim** | Volume de gás +1%. Hipótese: compra de 50% da UPGN em 30/09/2025 (a tarifa deixa de ser paga a terceiros pela parcela própria) |
| Transporte de gás | 94.419 | 118.405 | −20,3% | **Sim** | Contratos de transporte |
| Depreciação, amortização e depleção | 721.077 | 694.816 | +3,8% | Sim (valor) | Explicada: DD&A por boe de R$ 74,55 contra R$ 72,14 (+3,3%) → **coerente** com o método de unidades produzidas (aba `DDA_boe`) |
| Pessoal | 284.002 | 274.271 | +3,5% | Não | Coerente com reajuste próximo da inflação |
| **Total** | **2.436.030** | **2.316.334** | +5,2% | | Confere com a NE 19 |

### 3.2 Royalties – aba `Royalties`
- Royalties de **R$ 198.434 mil** (NE 17.1) sobre venda bruta de petróleo e gás de R$ 3.667.219 mil = **5,41%**. A NE 17.1 divulga alíquota de **7,5% a 10%**.
- Esperado a 7,5%: R$ 275.041 mil. **Diferença de −R$ 76.607 mil (3,7 vezes a ME)** → **investigar (item 7)**.
- Explicações a corroborar **[PLANEJADO]**:
  - (i) a base é o **preço de referência da ANP × volume produzido**, e não a receita de venda;
  - (ii) parte do gás vendido é **comprado de terceiros**;
  - (iii) **redução de royalties** sobre produção incremental de campos maduros concedida pela ANP;
  - (iv) valor agregado de subprodutos processados (GLP, C5+).
- **Item 7(b):** se as explicações não forem corroboradas, a diferença indica possível **subavaliação de custos/passivo regulatório** → PT 250 (L2) e PT 450.

### 3.3 Balanço e indicadores – aba `Balanco_indicadores`
| Item | 2025 | 2024 | Leitura |
|---|---:|---:|---|
| Contas a receber CP | 253.967 | 361.095 | −30% com receita −3%. **Prazo médio de recebimento: 25,0 dias contra 34,4** → corte de dezembro (produção −0,7% no mês; Brent −8% no 4T) ou antecipação de recebíveis? Ligação com R03 |
| Juros sobre debêntures | 281.098 | 84.840 | +231% contra dívida média +73%. **Taxa efetiva aparente de 11,5%**: obter abertura (IPCA, custos de emissão, efeito dos *swaps*) |
| Fornecedores LP | 130.476 | 130.476 | **Saldo idêntico** nos dois anos → obter natureza (disputa? retenção contratual?) |
| Valor a pagar por aquisições | 18.515 | 213.077 | Parcelas da UPGN pagas. Equivalência em US$ divergente (PT 450, D-I4) |
| Margem bruta | 32,4% | 36,5% | Queda coerente com o Brent −14% |

## 4. Procedimento analítico global perto do fim (item 6) – aba `Item6_conclusao_global`
As DFs são, **em geral, consistentes** com o entendimento da entidade (preço, câmbio, volume e expansão do midstream). As exceções viram procedimentos adicionais:

| # | Ponto | Destino |
|---|---|---|
| A1 | Petróleo: expectativa imprecisa, com diferença acima do limite | PT 330 (P03) – analítico desagregado + teste de detalhes |
| A2 | Royalties abaixo da alíquota mínima divulgada (−R$ 76,6 mi contra o esperado) | PT 250 (L2), PT 330 |
| A3 | Serviços e materiais +30% | PT 330 (R06), PT 530 (capitalização × resultado) |
| A4 | Prazo de recebimento −9 dias | PT 330 (corte), PT 505 (C04) |
| A5 | Juros das debêntures | PT 505 (C03) |
| A6 | Fornecedores LP inalterados | Indagação (PT 501 – litígios?) |
| A7 | Transferências do imobilizado que não zeram (−81.390) | PT 500 (I4) |

## 5. Investigação (item 7)
- **(a)** Indagar a administração e obter evidência que corrobore as respostas **[PLANEJADO]**.
- **(b)** Se a explicação não for adequada, executar outros procedimentos (testes de detalhes). As respostas estão no PT 330.

## 6. Referências cruzadas
PT 315 (avaliação de riscos – analíticos) · PT 320 (ME e limite) · PT 330 · PT 250 · PT 450 · PT 500 · PT 505 · PT 530 · PT 540 · DIAG.

## 7. Conclusão e limitações
- O analítico substantivo da **receita de gás** fica dentro do limite.
- O da **receita de petróleo** precisa de expectativa mais precisa.
- Sete pontos foram encaminhados para investigação, sendo o principal o de **royalties**.

**Limitação:** sem dados mensais por ativo nem acesso à administração para corroborar as explicações. Os dados são públicos e agregados.
