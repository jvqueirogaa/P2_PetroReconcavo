# PT 265 – Comunicação de deficiências de controle interno

| Campo | Conteúdo |
|---|---|
| **Código** | PT 265 |
| **Norma e itens** | NBC TA 265, itens 6 (definições), 7, 8, 9, 10 (a)–(b), 11 (a)–(b) e A5 a A11 (avaliação da significância) |
| **Versão consultada** | NBC TA 265 (consolidado da disciplina) |
| **Preparador** | Matrícula 211059370 – 24/10/2026 |
| **Revisão** | ______ (campo reservado; não preenchido) |
| **Classificação** | **[SIMULADO]** deficiências D01 a D06, identificadas nas bases sintéticas · **[REALIZADO]** D07, a partir de inconsistências públicas · **[PLANEJADO]** minuta de comunicação, não enviada |

## 1. Objetivo
Comunicar adequadamente aos responsáveis pela governança e à administração as deficiências de controle interno identificadas durante a auditoria que, no julgamento do auditor, tenham importância suficiente (objetivo da norma).

**Ressalva importante (item 11(b)(ii)).** O trabalho considerou o controle interno para planejar procedimentos, e não para opinar sobre a sua eficácia. Nenhum controle real da PetroReconcavo foi testado: não houve acesso a sistemas nem a pessoas (PT 315 e PT 330). As deficiências D01 a D06 derivam de **dados sintéticos** e ilustram como o auditor aplicaria a norma.

## 2. Identificação (item 7) e avaliação da significância (item 8; A5 a A11)

Critérios aplicados (A6 e A7):
- probabilidade de a deficiência levar a distorção relevante;
- suscetibilidade do ativo a perda ou fraude;
- subjetividade e complexidade do valor;
- valores expostos;
- volume de atividade;
- importância do controle para o processo de relatório financeiro;
- causa e frequência das exceções;
- interação com outras deficiências.

Indicadores do A7 considerados: evidência de aspectos ineficazes do ambiente de controle; ausência de processo de avaliação de riscos; distorções detectadas pelo auditor e não evitadas pelo controle.

| Ref. | Deficiência | Origem / evidência | Valor exposto | Significativa? (item 8) | Justificativa |
|---|---|---|---:|---|---|
| **D01** | **Ausência de segregação no cadastro do imobilizado** (*maker-checker*): cadastros sem aprovador ou com aprovador igual ao cadastrador | [SIMULADO] T07 – 627 registros (`TESTES_BASE_RECV3.xlsx`, aba `Excecoes_detalhe`) | Indireto; os itens duplicados (T01, R$ 6,74 mi) passaram pelo mesmo cadastro | **Sim** | Controle-chave da existência no imobilizado (72% do ativo); volume alto; interage com D03, D04 e D05; erros detectados pelo auditor e não pelo controle (A7) |
| **D02** | **Folha de pagamento:** pagamento a matrículas inexistentes no cadastro, CPF ou conta bancária duplicados, pagamento após desligamento, falta de *maker-checker* e reajustes acima da alçada | [SIMULADO] G01 (6; R$ 680.767), G02 (18), G03 (8; R$ 37.918), G04 (30), G05 (12) – `TESTES_FOLHA_RECV3.xlsx` | R$ 718.685 pagos indevidamente | **Sim** | Os indícios de empregado fictício envolvem **fraude** (NBC TA 240) e indicam falha do ambiente de controle (A7). A relevância é qualitativa, mesmo com valor abaixo da ME |
| **D03** | Baixas não refletidas no subrazão (itens com status "BAIXADO" ainda com saldo) | [SIMULADO] T05 – 63 itens | R$ 2.553.788 | Não, individualmente | Abaixo da ME; com D01, D04 e D05 contribui para o conjunto (item 8: "em conjunto") |
| **D04** | Corte da capitalização: itens com data de aquisição posterior a 31/12/2025 | [SIMULADO] T02 – 46 itens | R$ 2.502.284 | Não, individualmente | Idem |
| **D05** | Cadastro mestre sem validação: campos fora das 58 concessões (T08) e datas anteriores à constituição da companhia (T10) | [SIMULADO] T08 – 35 itens (R$ 1.234.406); T10 – 30 itens | R$ 1.234.406 | Não, individualmente | Falha de validação automática (controle de aplicação de TI) |
| **D06** | Monitoramento de recuperabilidade insuficiente: almoxarifado sem movimento há mais de 5 anos e obras paradas há mais de 2 anos sem avaliação | [SIMULADO] T06 – 95 itens (R$ 281.274); T09 – 45 itens (R$ 1.134.210) | R$ 1.415.484 | Não, individualmente | Afeta a estimativa de *impairment* (PT 540) |
| **D07** | **Revisão das divulgações:** inconsistências nas notas publicadas (séries da 4ª emissão na NE 9.1 × texto e NE 25; datas e taxas divergentes; NE 25 "Evento subsequente" com fatos anteriores ao balanço; três equivalências em US$ para a UPGN; NE 16.2 com AGO de "24/04/2024" para a remuneração de 2025; blocos da SPE Tiêta "reduzidos a R$ 0" na NE 17.2 × R$ 10.604 mil na NE 7.1) | [REALIZADO] leitura crítica da DFP (F01 p.72-75, 79-80, 91, 101; NE 7.1 e 17.2) – DIAG `Achados_Preliminares` | Divulgação (sem efeito no resultado) | Não (outra deficiência – item 10(b)) | As inconsistências são **fatos públicos**. A falha do controle de revisão é **inferência**, sem teste direto |

**Conjunto (item 8).** D01, D03, D04 e D05 têm a mesma causa provável: o ciclo cadastro → capitalização → baixa do imobilizado não tem revisão independente. Em conjunto, os valores expostos somam **R$ 6,29 mi** (D03 + D04 + D05), além dos R$ 6,74 mi de duplicidades que passaram pelo D01. Por isso, o conjunto também é tratado como **deficiência significativa**.

## 3. Destinatários e forma (itens 9 e 10)

| Deficiência | Governança (CAE) – item 9, por escrito | Administração – item 10 |
|---|---|---|
| D01, D02 e conjunto D01+D03+D04+D05 (significativas) | Sim | Sim, por escrito (10(a)) |
| D03 a D07 (outras) | Não obrigatório | Sim (10(b)); por escrito ou verbalmente, com documentação |

**Exceção do item 10(a) e A20.** A comunicação de D02 diretamente à administração pode não ser apropriada se os indícios de fraude envolverem a própria administração. Nesse caso, comunica-se primeiro ao CAE (NBC TA 240, itens 41 a 43).

## 4. Minuta de comunicação por escrito (item 11)

> **[MINUTA DIDÁTICA – NÃO ENVIADA – DEFICIÊNCIAS IDENTIFICADAS EM DADOS SINTÉTICOS]**
> Ao Comitê de Auditoria Estatutário e à Diretoria da PetroReconcavo S.A.
>
> **Contexto (item 11(b)).**
> (i) O objetivo da nossa auditoria foi expressar opinião sobre as demonstrações financeiras de 31/12/2025.
> (ii) A auditoria incluiu a consideração do controle interno relevante para elaborá-las, para planejar procedimentos adequados às circunstâncias, **mas não para expressar opinião sobre a eficácia do controle interno**.
> (iii) Os assuntos abaixo se limitam às deficiências que identificamos e que julgamos importantes o suficiente para comunicar.
>
> **Deficiências significativas (item 11(a)).**
> 1. **Cadastro do imobilizado sem segregação de funções.** 627 registros foram cadastrados e aprovados pelo mesmo usuário ou ficaram sem aprovação. *Efeito possível:* registro de ativos inexistentes ou duplicados (identificamos 160 duplicidades, R$ 6,7 mi), baixas não registradas e corte incorreto. *Recomendação:* exigir aprovação sistêmica por usuário distinto, com relatório de exceções revisado mensalmente pela controladoria.
> 2. **Folha de pagamento.** Identificamos pagamentos a 6 matrículas inexistentes no cadastro, 8 pagamentos após o desligamento, 18 cadastros com CPF ou conta bancária repetidos e 12 reajustes acima da alçada. *Efeito possível:* desembolsos indevidos (R$ 718,7 mil no exercício) e risco de fraude. *Recomendação:* conciliação mensal folha × cadastro × ponto, bloqueio sistêmico de pagamento a desligados e trilha de auditoria das alterações cadastrais.
>
> **Outras deficiências (item 10(b)):** D03 a D07, conforme anexo.
>
> Local e data: ______ · Auditor: ______

## 5. Referências cruzadas
PT 240 (fraude: D02) · PT 315 (entendimento dos controles e R05/R06) · PT 330 (abordagem substantiva) · PT 450 (distorções originadas) · PT 540 (D06) · PT 260 (comunicação à governança) · PT 530 (MUS) · `TESTES_BASE_RECV3.xlsx` · `TESTES_FOLHA_RECV3.xlsx` · DIAG `Achados_Preliminares`.

## 6. Conclusão e limitações
- **Deficiências significativas:** duas (D01 e D02), mais o conjunto D01+D03+D04+D05, todas originadas de dados **sintéticos**.
- **Outras deficiências:** cinco (D03 a D07). D07 se apoia em inconsistências reais e públicas, mas a falha do controle é inferida.

**Limitação:** não houve teste de controles reais nem acesso a sistemas. As deficiências simuladas **não** representam a situação da PetroReconcavo.
