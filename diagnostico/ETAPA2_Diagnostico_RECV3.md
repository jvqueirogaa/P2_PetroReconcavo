# Etapa 2 — Diagnóstico da companhia (base para PT 315, 320, 520, 540, 550, 570 e 600)

| Campo | Conteúdo |
|---|---|
| Companhia | PetroReconcavo S.A. (RECV3) — CNPJ 03.342.704/0001-30 — código CVM 25780 |
| Exercício | 2025 (comparativo 2024) — DFs individuais e consolidadas |
| Preparador | Matrícula 211059370 — 22/10/2026 |
| Revisão | ______ (campo reservado; não preenchido) |
| Natureza dos procedimentos | **Realizado com evidência pública** (leitura, recálculo e análise de documentos públicos). Nenhuma informação interna foi utilizada. |
| Papéis de suporte | `planilhas/DIAG_RECV3.xlsx` (21 abas) · `planilhas/REG_FONTES_RECV3.xlsx` · `codigo/etapa2_diagnostico.py` |

> Convenção: **F01** = DFP 2025 em PDF (páginas do PDF); **F03/F04** = dados abertos CVM 2025/2024; **F07** = DF 2024; **F12/F13** = FRE 2025/2026; **F14** = certificação de reservas NSAI. A lista completa está no registro de fontes.

---

## 1. Entendimento da entidade

1. **Atividade.** A companhia opera e produz em campos maduros *onshore* de petróleo e gás. São 58 concessões na Bahia, em Sergipe e no Rio Grande do Norte, 14 delas em consórcio (F01 NE 1, p.57). Toda a receita vem de um único segmento, E&P (NE 23, p.101).
2. **Controle.** Não há acionista nem grupo controlador (NE 1). Os acionistas fundadores PERBRAS e PetroSantander continuam como partes relacionadas prestadoras de serviço (NE 16, p.90-91).
3. **Grupo.** É formado pela controladora e pela SPE Tiêta Ltda. (100%; ex-Maha Energy Brasil Ltda.), além de dois acordos de operação em conjunto (JOA) celebrados em 2025:
   - **Midstream da Brava (UPGN Guamaré):** 50%, por US$ 65 milhões, concluída em 30/09/2025.
   - **Farm-out para a Mandacaru:** 50% de 7 concessões no RN, concluído em 10/10/2025 (NE 7, p.70-71).
   - Aba `Grupo_Componentes`.
4. **Desempenho em 2025:**
   - Produção média de 26,5 mil boe/dia (+1%).
   - Brent médio de US$ 69,10/bbl (-14%).
   - Receita líquida de R$ 3,16 bi (-3,3%) e lucro operacional de R$ 722 mi (-24%).
   - Lucro líquido de R$ 638 mi (+46%), puxado pelo resultado de swaps (+R$ 352 mi) (F01 RA p.4-5; DRE p.52; NE 20 p.94).
5. **Estrutura de relatório financeiro:** práticas contábeis adotadas no Brasil e IFRS, com DVA como informação suplementar. A administração autorizou a emissão em 18/03/2026 (NE 2.1, p.57).
6. **Auditoria.** A EY é a auditora de 2025 e sucedeu a Deloitte, que auditou até 2024 e saiu por término de contrato (F07 p.37).
   - Opinião de 2025 sem modificação.
   - PAA único: provisão para abandono de poços (F01 p.44-50).
   - Na prática, isso torna 2025 uma **auditoria inicial** (PT 510).

## 2. Conta de maior materialidade do ativo (item 3 do enunciado)

| # | Rubrica (consolidado, R$ mil) | 31/12/2025 | % ativo |
|---|---|---:|---:|
| 1 | **Imobilizado e intangível (NE 7)** | **6.254.225** | **72,2%** |
| 2 | Aplicações financeiras (CP) | 1.395.510 | 16,1% |
| 3 | Contas a receber de clientes (CP) | 253.967 | 2,9% |
| 4 | Caixa e equivalentes | 229.508 | 2,6% |
| — | Ativo total | 8.668.015 | 100% |

1. **Imobilizado e intangível** é a maior rubrica nos dois exercícios: 74,8% do ativo em 2024. Ela é cerca de **4,5 vezes** a segunda maior. Na controladora, representa 66,2% do ativo. Aba `Ranking_Ativo`.
2. O intangível (software) é residual: R$ 83.384. O **imobilizado** propriamente dito (R$ 6.170.841, conta CVM 1.02.03) responde por 98,7% da rubrica. O recálculo da NE 7.1 fecha **sem diferença** com a CVM e com o balanço (aba `NE7_Imobilizado`).
3. Composição do imobilizado líquido em 2025:

| Classe | Valor líquido | % |
|---|---:|---:|
| Desenvolvimento de campos (UoP – PDP) | 2.763.972 | 44,8% |
| Direito de produção de óleo e gás (UoP – 1P) | 2.008.915 | 32,6% |
| Máquinas e equipamentos (inclui UPGN Guamaré) | 614.733 | 10,0% |
| Almoxarifado para inversões fixas | 477.651 | 7,7% |
| Outros, em andamento, ARO, blocos, adiantamentos | 305.570 | 4,9% |
| **Total** | **6.170.841** | 100% |

4. **Decisão.** A base simulada (Etapa 3) será um **subrazão analítico do imobilizado**, com registros por poço, componente e campo. Os parâmetros sairão da NE 7, dos polos (NE 7.1 ii) e das reservas (F14). O alvo de conciliação é R$ 6.170.841 mil, com custo de R$ 9.703.552 mil e depreciação acumulada de R$ 3.532.711 mil.

## 3. Endividamento, liquidez e continuidade (insumo PT 570)

1. **Debêntures** (4 emissões, todas com swap para dólar): saldo de **R$ 3.105.016**, contra R$ 1.792.321 em 2024. Em 2025 entraram a 3ª emissão (R$ 500 mi) e a 4ª (R$ 750 mi). Não há vencimento relevante de principal antes de 2028 (NE 9, p.72-75).
2. **Covenants recalculados por mim** (aba `NE9_Debentures`). Todos são cumpridos com folga:

| Covenant | Limite | Recálculo | Divulgado |
|---|---|---:|---:|
| Dívida líquida / EBITDA | ≤ 3,00x | 1,06x | 1,10x |
| PV-10 1P / dívida bruta | ≥ 1,50x | 3,37x | — |
| Caixa livre | ≥ R$ 100 mi | R$ 1.630 mi | — |

3. **Liquidez:** corrente de 3,48x e imediata de 2,62x. O endividamento geral é de 50,0% do ativo e a cobertura de juros de 5,1x (aba `Indicadores`).
4. **Ponto de atenção:** o fluxo de caixa livre simplificado ficou **negativo em R$ 135 mi**, contra +R$ 1,03 bi em 2024. O capex foi de R$ 1,64 bi, incluindo o midstream. Também houve **R$ 300 mi de dividendos** declarados em 18/12/2025 com base na Lei 15.270/2025 (R$ 200 mi a longo prazo). Não vejo indício de incerteza relevante sobre continuidade, mas o tema será documentado no PT 570.
5. **Limitação:** as escrituras não estão no site de RI. As definições contratuais de dívida líquida e EBITDA ainda precisam ser confirmadas nos relatórios do agente fiduciário (F31–F34).

## 4. Estimativas contábeis (insumo PT 540)

1. **Provisão para abandono de poços (ARO):** R$ 145.192.
   - Taxa nominal de 10,56% e inflação de 3,56%; em 2024, 10,92% e 3,66% (NE 3.3, p.61; NE 13, p.82-83).
   - É o PAA do auditor, e **será a estimativa selecionada para o PT 540**, com análise de sensibilidade.
2. **Reservas e depleção por unidades produzidas:** a depleção de 2025 foi de R$ 618.823. Depende da certificação da NSAI: 1P de 143,3 MMboe e PV-10 1P de US$ 1,9 bi (NE 3.2; F14).
3. **Impairment:** a companhia declara não ter identificado indicativos (NE 3.4, p.62). Porém, o **valor de mercado (R$ 3,3 bi) é menor que o PL (R$ 4,33 bi)**, numa relação de 0,77x. O CPC 01, item 12(d), trata isso como indicativo. Isso foi classificado como **risco significativo** para os PTs 315 e 540.
4. **Outras estimativas:** IR diferido (passivo líquido de R$ 52.211), valor justo de derivativos e créditos de gás em disputa (R$ 55.917). Aba `Estimativas`.

## 5. Receita, clientes, litígios e partes relacionadas

1. **Receita bruta de R$ 3,71 bi:** petróleo responde por 57% e gás e subprodutos por 42%. 97% está atrelada ao dólar (NE 18, p.93; NE 21, p.97).
2. **Concentração:** três clientes somam 83% da receita (22%, 28% e 33%) (NE 21, p.97). A receita foi o PAA da auditora anterior. Esses pontos alimentam o risco de fraude na receita (PT 240) e as confirmações externas (PT 505).
3. **Litígios:**
   - Perda provável de R$ 47.946, em grande parte regulatória (ANP / Programa Exploratório Mínimo da SPE Tiêta, coberto por fiança das vendedoras).
   - Perda possível de R$ 181.206.
   - **Arbitragem confidencial na CCI** sobre contratos de venda de gás, suspensa para mediação (NE 12, p.80-82). Vai para os PTs 501 e 250.
4. **Partes relacionadas:** PERBRAS (sondas e serviços, R$ 4.509) e PetroSantander (assistência técnica, R$ 961). A remuneração da administração foi de R$ 30.694 (NE 16, p.90-91). Vai para o PT 550.

## 6. Consistência com o exercício anterior (insumo PT 510)

1. Comparei os valores de 2024 apresentados na DFP 2025 com a DFP 2024 (versão 2) nos dados da CVM: balanço, DRE e DFC, consolidado e controladora. Encontrei **zero diferenças** (aba `Comparativos_2024`), ou seja, não houve reapresentação dos comparativos.
2. A DFP 2024 foi reentregue no mesmo dia (versões 1 e 2), mas a CVM só publica a versão 2. O motivo continua **pendente** para o PT 510.

## 7. Achados preliminares (hipóteses a investigar, não constatações)

A aba `Achados_Preliminares` tem 11 itens, com fonte e página. Os principais:

1. **Indicativo de impairment não tratado nas notas** (valor de mercado abaixo do PL; Brent -14%). Vai para os PTs 540, 315 e 330.
2. **Inconsistências de divulgação na 4ª emissão:**
   - Na tabela da NE 9.1, os rótulos das séries parecem trocados em relação ao texto e à NE 25.
   - As datas de liquidação divergem (18/12 contra 29/12/2025).
   - As taxas também divergem (7,40% contra 7,4564% e 7,2833%).
   - Vai para os PTs 450 e 500.
3. **A NE 25 ("Evento subsequente") descreve fatos anteriores ao balanço.** Só o swap de 12/01/2026 é de fato um evento subsequente. Vai para o PT 560.
4. **Valores a pagar pela UPGN Guamaré** aparecem com três equivalências em dólar diferentes: US$ 3.559, US$ 9.952 e cerca de US$ 3.365 pela PTAX. Vai para os PTs 450 e 500.
5. **As transferências do imobilizado não zeram** (custo -R$ 81.390), sem quantificação na nota. Vai para os PTs 520 e 500.

## 8. Limitações

1. Usei apenas fontes públicas. Não tive acesso a razão contábil, contratos, escrituras, laudos internos de impairment ou ARO, nem a sistemas.
2. As páginas citadas seguem a numeração do PDF, não a impressa.
3. Os indicadores são cálculos meus e podem diferir das definições contratuais e gerenciais.
4. Os achados da seção 7 são **hipóteses**. Ainda precisam de procedimentos adicionais para virar constatações.

## 9. Próximos passos

1. **Etapa 3:** gerar a base simulada do imobilizado, com no mínimo 500.000 linhas, dicionário de variáveis, conciliação com R$ 6.170.841 mil e registro dos erros inseridos.
2. Na sequência, elaborar os PTs (blocos A a E), usando este diagnóstico como referência cruzada **DIAG-RECV3**.
