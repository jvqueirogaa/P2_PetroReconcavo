# PT 220 – Gestão da qualidade do trabalho de auditoria

| Campo | Conteúdo |
|---|---|
| **Código** | PT 220 |
| **Norma e itens** | NBC TA 220 (R3), itens 13 a 41 (responsabilidade do sócio; requisitos éticos 16 a 21; aceitação 22 a 24; recursos 25 a 28; direção, supervisão e revisão 29 a 34; consulta 35; revisão de qualidade 36; diferenças de opinião 37; monitoramento 38; responsabilidade geral 40; documentação 41) |
| **Versão consultada** | NBC TA 220 (R3), de 18/11/2021 – "Gestão de Qualidade da Auditoria de Demonstrações Contábeis" (consolidado da disciplina) |
| **Preparador** | Matrícula 211059370 – 24/10/2026 |
| **Revisão** | ______ (campo reservado; não preenchido) |
| **Classificação** | Planejado (estrutura de qualidade de um trabalho real) + realizado (controles aplicados a este dossiê) |

## 1. Objetivo
Planejar a gestão da qualidade no nível do trabalho:
- direção, supervisão e revisão;
- consultas;
- recursos;
- registro de conflitos e riscos à qualidade.

O objetivo é dar segurança razoável de que o trabalho cumpre as normas e de que o relatório é apropriado.

## 2. Plano de qualidade do trabalho (equipe hipotética de um trabalho real)

| Requisito | Exigência | Plano para a auditoria da PetroReconcavo 2025 |
|---|---|---|
| Itens 13 a 15 – responsabilidade do sócio | Sócio assume a responsabilidade geral, cria o ambiente de qualidade e supervisiona tarefas delegadas | Sócio responsável define o tom (ceticismo e consulta) no *kick-off* e aprova o plano de auditoria (PT 300) |
| Itens 16 a 21 – requisitos éticos | Entender exigências éticas e independência; tratar ameaças; confirmar antes de datar o relatório | Declarações anuais de independência da equipe; verificação de participações em RECV3 e de relação com PERBRAS e PetroSantander (PT 550); rodízio de sócio; avaliação de serviços não auditoria (F12 9.1: só auditoria e revisão) |
| Itens 22 a 24 – aceitação | Confirmar que as políticas de aceitação foram seguidas | PT 210 (precondições) e PT 510 (comunicação com o antecessor; anuência da Deloitte) |
| Itens 25 a 28 – recursos | Recursos suficientes e apropriados, inclusive especialistas e tempo | Especialistas: (i) engenharia de reservatórios, para avaliar a certificação NSAI e a depleção por unidades produzidas; (ii) modelos financeiros, para a provisão para abandono (a EY usou "especialistas de modelos financeiros", F01 p.46); (iii) derivativos e valor justo; (iv) TI (ITGC do ERP); (v) tributário (SUDENE, Lei 15.270/2025). Ferramenta de análise de dados para testes em 100% da população |
| Itens 29 a 34 – direção, supervisão e revisão | Natureza, época e extensão da revisão; revisão das DFs e do relatório antes de datá-lo | Revisão em camadas: preparador → sênior → gerente → sócio, com prioridade para riscos significativos (impairment, provisão para abandono, receita/fraude, saldos iniciais). Revisão das DFs antes da data do relatório (item 33) |
| Item 35 – consultas | Consultar sobre assuntos difíceis ou controversos | Consultas previstas: (a) indicativo de impairment × NE 3.4; (b) tratamento do farm-out Mandacaru no imobilizado (NE 7.4, julgamento com o CPC 31); (c) divulgações inconsistentes da 4ª emissão |
| Item 36 – revisão de qualidade do trabalho (EQR) | Obrigatória quando exigida pela política da firma; tipicamente para entidades listadas | **Aplicável** (companhia listada): revisor de qualidade independente da equipe, antes da data do relatório |
| Item 37 – diferenças de opinião | Seguir as políticas da firma; não datar o relatório antes de resolver | Registro de divergências e resolução documentada (PT 230) |
| Item 38 – monitoramento | Considerar informações do monitoramento da firma | Considerar resultados de inspeções internas e externas (CFC, CVM) |
| Itens 40 e 41 – responsabilidade geral e documentação | Sócio conclui sobre o envolvimento suficiente; documentar | Checklist de encerramento (PT 230) |

## 3. Conflitos e riscos à qualidade identificados

| # | Risco à qualidade | Origem | Resposta |
|---|---|---|---|
| Q1 | Primeira auditoria: falta de conhecimento histórico | Troca de auditor (PT 510) | Mais tempo de planejamento, leitura dos PAAs de 2024 (receita) e de 2025 (provisão para abandono), procedimentos sobre saldos iniciais |
| Q2 | Estimativas técnicas além da competência contábil | Reservas e provisão para abandono | Especialistas (itens 25 e 26; NBC TA 620) |
| Q3 | Pressão de prazo | Entrega em 25/10/2026 (contexto acadêmico); no real, prazo CVM de 3 meses | Priorizar riscos significativos; registrar o que ficou planejado |
| Q4 | Uso de IA na elaboração | Ferramenta Claude | Registro de prompts, conferência pelo preparador e reprodutibilidade (`docs/USO_DE_IA.md`) |
| Q5 | Equipe de uma pessoa (aluno): revisão independente impossível | Trabalho individual | **Campo de revisão mantido em branco** (enunciado, item 4); não há simulação de assinatura ou revisão de terceiros |
| Q6 | Conflito de interesse | — | Nenhum conflito identificado; confirmar a declaração do PT 200 |

## 4. Controles de qualidade efetivamente aplicados a este dossiê (realizado)
1. Recálculo independente de todos os números extraídos das fontes: Python e fórmulas recalculadas no LibreOffice; conciliação PDF × CVM.
2. Reexecução completa da base simulada e dos testes, com o mesmo resultado (hash SHA-256 do conteúdo).
3. Conferência das páginas citadas no registro de fontes (correções registradas na Etapa 1).
4. Separação explícita entre os rótulos "realizado", "planejado" e "simulado" em cada PT.

## 5. Referências cruzadas
PT 200 · PT 210 · PT 230 · PT 300 · PT 510 · PT 540 · `docs/USO_DE_IA.md`.

## 6. Conclusão e limitações
O plano de qualidade do trabalho foi desenhado de acordo com os itens 13 a 41 da NBC TA 220 (R3). Como é um trabalho individual e acadêmico, **não há revisão por terceiros**. O campo de revisão permanece em branco e não foi simulado.
