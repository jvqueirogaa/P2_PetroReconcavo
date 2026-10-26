# PT 500 – Evidência de auditoria

| Campo | Conteúdo |
|---|---|
| **Código** | PT 500 |
| **Norma e itens** | NBC TA 500 (R1), itens 6, 7 (com a alteração da Revisão NBC 3 sobre fonte de informação externa), 8 (a)–(c), 9 (a)–(b), 10, 11 e A14 a A25 (tipos de procedimento) |
| **Versão consultada** | NBC TA 500 (R1), de 19/08/2016, com a Revisão NBC 3 (consolidado da disciplina) |
| **Preparador** | Matrícula 211059370 – 24/10/2026 |
| **Revisão** | ______ (campo reservado; não preenchido) |
| **Classificação** | **[REALIZADO]** avaliação das fontes públicas, conciliações e recálculos · **[SIMULADO]** avaliação da base sintética como informação produzida pela entidade · **[PLANEJADO]** avaliação do especialista da administração |

## 1. Objetivo
Definir e executar procedimentos que permitam obter evidência apropriada (relevante e confiável) e suficiente para conclusões razoáveis (objetivo da norma; item 6).

## 2. Inventário de evidências e avaliação de relevância e confiabilidade (item 7; A30 a A44)

| Ref. | Fonte | Natureza (A31) | Relevância | Confiabilidade | Uso |
|---|---|---|---|---|---|
| E1 | DFP 2025 em PDF, com relatório do auditor (F01) | Externa, publicada pela entidade e auditada | Alta (objeto da auditoria) | Média-alta: documento oficial na CVM, com hash. Ainda assim, é informação produzida pela entidade | Base de todos os PTs |
| E2 | Dados abertos da CVM (F03/F04) | **Fonte de informação externa** (Revisão NBC 3) | Alta | Alta para integridade: é base estruturada independente do PDF | Conciliação PDF × CVM (DIAG) |
| E3 | Certificação de reservas da NSAI (F14) | Trabalho de **especialista da administração** (item 8) | Alta para depleção (R$ 618.823) e *impairment* | Depende da avaliação do item 8 (seção 3) | PT 540 |
| E4 | Relatórios do agente fiduciário (F31–F34) | Externa, de terceiro independente | Alta para debêntures e *covenants* | Alta | PT 505 (C03) e PT 570 |
| E5 | FRE 2025/2026, fatos relevantes e comunicados (F12, F13, FR/CM) | Produzida pela entidade (regime CVM) | Média | Média | PT 250, 550, 560 e 600 |
| E6 | Cotação e capitalização de mercado (B3) | Externa | Alta para indicativo de *impairment* | Alta | PT 315 e PT 540 |
| E7 | Bases simuladas (imobilizado e folha) | **[SIMULADO]** tratadas como informação produzida pela entidade (IPE) | Alta (didática) | Avaliada pelo item 9 (seção 4) | PT 530, 240, 265 e 450 |

**Hierarquia aplicada (A31).** Evidência externa e independente (E2, E4, E6) > documentos da entidade auditados ou registrados na CVM (E1) > informação da entidade não auditada (E5). Indagações e representações (PT 580) sozinhas não bastam (NBC TA 580, item 4).

## 3. Especialista da administração – NSAI (item 8)

| Alínea | Exigência | Procedimento | Situação |
|---|---|---|---|
| (a) | Competência, habilidades e objetividade | Natureza da firma (consultoria internacional de reservas); relação contratual com a companhia; ausência de vínculo societário | **[REALIZADO parcialmente]** o fato relevante de 18/03/2026 identifica a NSAI como "consultoria independente". **[PLANEJADO]** contrato, honorários e declaração de independência |
| (b) | Entendimento do trabalho | Critério PRMS; data de referência 31/12/2025; reservas 1P de 143,3 MMboe (Bahia 87,3 e Potiguar 56,1); premissas de preço e custo | **[REALIZADO]** leitura do relatório e do fato relevante (F14) |
| (c) | Adequação como evidência | Consistência entre as reservas usadas na depleção por unidades produzidas e as certificadas; premissas de preço × Brent da NE 3.2 | **[PLANEJADO]** recálculo da taxa de depleção por campo; **[SIMULADO]** a base usa taxas por campo calibradas à NE 7 |

## 4. Informação produzida pela entidade – a base simulada (item 9)
- **(a) Exatidão e integridade:**
  - a base concilia com a NE 7.1 por classe, em centavos, com diferença apenas de arredondamento (≤ R$ 1 mil por classe), no `CONC_BASE_RECV3.xlsx`;
  - o hash SHA-256 do conteúdo está registrado nos metadados;
  - os totais de controle (517.770 itens com valor líquido positivo; valor líquido de R$ 6.171.370.101,38) foram reproduzidos pelo script de testes.
- **(b) Precisão e detalhamento:** os 33 campos por registro (dicionário) permitem testes por item, por poço, por campo e por usuário. São suficientes para T01 a T10 e para o MUS.
- **Limitação:** a confiabilidade da base vem da construção (código reproduzível), e **não** de controles da entidade.

## 5. Seleção de itens (item 10; A52 a A56)

| Método (A52) | Aplicação |
|---|---|
| Seleção de 100% dos itens | T01 a T10 na base do imobilizado e G01 a G06 na folha (dados eletrônicos e testes automatizáveis; A53) |
| Seleção de itens específicos | Estrato superior do MUS (56 itens com valor ≥ I); itens cadastrados no fim do período (PT 240); itens com valor líquido > R$ 1 mi |
| Amostragem de auditoria | MUS com seleção sistemática e início aleatório (PT 530) |

## 6. Inconsistências entre fontes (item 11) – [REALIZADO]

| # | Inconsistência | Fontes | Modificação de procedimento | Destino |
|---|---|---|---|---|
| I1 | Séries da 4ª emissão: a tabela da NE 9.1 mostra 1ª série = 225.208 e 2ª = 525.492; o texto e a NE 25 dizem R$ 525 mi e R$ 225 mi | F01 p.72 × p.74-75 × p.101 | Conferir com a escritura e o relatório fiduciário (F34) | PT 450 (divulgação) |
| I2 | Liquidação em 18/12 × 29/12/2025; taxas de 7,40% × 7,4564% e 7,2833% | F01 NE 9 × NE 25 | Idem; confirmação C03 | PT 450 e PT 560 |
| I3 | UPGN: R$ 18.515 com três equivalências em US$ (3.559; 9.952; cerca de 3.365 pela PTAX) | F01 NE 11 e NE 21 | Recalcular pela PTAX de 31/12/2025; confirmação C06 | PT 450 |
| I4 | Transferências do imobilizado não zeram (custo −81.390; depreciação −62.640) | F01 NE 7.1 p.69 | Pedir a abertura das transferências; analítico | PT 520 |
| I5 | Blocos da SPE Tiêta "reduzidos a R$ 0" (NE 17.2) × R$ 10.604 mil no consolidado menos a controladora (NE 7.1) | F01 | Inspecionar o *impairment* dos blocos e a composição | PT 450 e PT 250 |
| I6 | NE 16.2: AGO de "24/04/2024" fixando a remuneração de 2025 | F01 p.91 × ata da AGO de 2025 | Conferir a ata | PT 550 e PT 450 |

Essas inconsistências não indicam, sozinhas, fraude. Afetam a confiabilidade da divulgação e levaram à deficiência D07 (PT 265).

## 7. Tipos de procedimento usados no dossiê (A14 a A25)

| Tipo | Exemplos | Classificação |
|---|---|---|
| Inspeção de registros e documentos | Leitura da DFP, do FRE, das atas e da certificação | REALIZADO (públicos) / PLANEJADO (contratos) |
| Inspeção de ativos tangíveis / observação | Visita aos polos e contagem do almoxarifado (PT 501) | PLANEJADO |
| Confirmação externa | C01 a C09 (PT 505) | PLANEJADO / SIMULADO |
| Recálculo | NE 7.1, *covenants*, materialidade, depreciação (T04), provisão para abandono | REALIZADO / SIMULADO |
| Reexecução | Testes T01 a T10 refeitos por script independente da geração | SIMULADO |
| Procedimentos analíticos | PT 520 | REALIZADO |
| Indagação | Pautas nos PTs 240, 250, 501 e 570 | PLANEJADO |

## 8. Referências cruzadas
PT 505 · PT 520 · PT 530 · PT 540 · PT 450 · PT 265 · PT 230 · DIAG-RECV3 · REG_FONTES.

## 9. Conclusão e limitações
A evidência pública e simulada é **apropriada** para os procedimentos marcados como realizados ou simulados. Ela **não é suficiente** para uma opinião, porque faltam evidências de fontes internas, confirmações e inspeções físicas (procedimentos planejados).
