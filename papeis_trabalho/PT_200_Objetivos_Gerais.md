# PT 200 – Objetivos gerais do auditor e condução da auditoria

| Campo | Conteúdo |
|---|---|
| **Código** | PT 200 |
| **Norma e itens** | NBC TA 200 (R1), itens 11, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23 e 24 |
| **Versão consultada** | NBC TA 200 (R1), de 19/08/2016 (consolidado da disciplina), vigente para 2025 |
| **Preparador** | Matrícula 211059370 – 24/10/2026 |
| **Revisão** | ______ (campo reservado; não preenchido) |
| **Classificação** | Realizado com evidência pública (análise) + planejado por falta de acesso (declarações de independência da equipe real) |

## 1. Objetivo
Documentar como o dossiê atende aos objetivos gerais do auditor (item 11):
- **(a)** obter segurança razoável de que as DFs como um todo estão livres de distorção relevante, por fraude ou erro;
- **(b)** apresentar relatório.

O objetivo (b) está **fora do escopo da P2**, porque a fase de relatório fica para a P3.

## 2. Requisitos e como foram atendidos

| Requisito (NBC TA 200) | Exigência | Atendimento neste dossiê |
|---|---|---|
| **Item 14 – ética e independência** | Cumprir exigências éticas, inclusive independência | Declaração do preparador na seção 3 abaixo. No trabalho real, a independência da EY consta do relatório (F01 p.44-45) e o FRE 9.1 (F12 p.305) mostra os honorários: só auditoria e revisão de ITR, **sem serviços não relacionados à auditoria** |
| **Item 15 – ceticismo profissional** | Planejar e executar reconhecendo que pode haver distorção relevante | Exemplos concretos na seção 4 |
| **Item 16 – julgamento profissional** | Exercer julgamento no planejamento e na execução | Escolha do referencial de materialidade (PT 320), avaliação de riscos (PT 315), escolha da estimativa (PT 540) e desenho do MUS (PT 530) |
| **Item 17 – evidência e risco de auditoria** | Obter evidência apropriada e suficiente para reduzir o risco a nível baixo aceitável | Modelo RA = RI × RC × RD (seção 5); limitação de acesso no PT 500 |
| **Itens 18 e 19 – observar todas as NBC TA relevantes e entender o texto inteiro** | Aplicar as normas em vigor cujas circunstâncias existem | Matriz de cobertura das normas (`matriz_cobertura/`): EC e 200 a 600, com versões e itens. Os PTs citam os itens efetivamente aplicados |
| **Item 20 – declarar conformidade** | Não declarar conformidade sem cumprir as NBC TA | **O dossiê não declara conformidade nem emite opinião** (é didático) |
| **Item 21 – objetivos de cada NBC TA** | Usar os procedimentos das normas e avaliar se a evidência é suficiente | Cada PT traz objetivo, procedimentos e conclusão, distinguindo realizado, planejado e simulado |
| **Itens 22 e 23 – exigências relevantes** | Cumprir cada exigência, salvo norma ou requisito condicional não aplicável | Quando um requisito não se aplica, o PT traz a análise (enunciado, item 2). Exemplo: PT 402, PT 600 (auditores de componentes) |
| **Item 24 – objetivo não cumprido** | Avaliar o impacto e documentar como assunto significativo | Assunto significativo documentado: **não acesso a evidências internas**. Sem acesso, não seria possível obter segurança razoável sobre várias afirmações. Em trabalho real, isso exigiria avaliar modificação de opinião (NBC TA 705); aqui é tratado como limitação didática (PT 500, conclusão integrada) |

## 3. Ética e independência (item 14) – declaração do preparador
- O preparador declara não ter vínculo com a PetroReconcavo, a EY, a Deloitte, a NSAI ou as partes relacionadas mapeadas (PERBRAS, PetroSantander) e não prestar serviços a essas entidades. ☐ **Confirmar** (campo a ser marcado pelo próprio aluno, inclusive quanto à posse de ações RECV3).
- Nenhum contato foi feito com a empresa, auditores, clientes ou fornecedores em nome da UnB (enunciado, item 1).
- **Uso de IA:** registrado em `docs/USO_DE_IA.md`. A responsabilidade pelo julgamento e pelas conclusões é do preparador.

## 4. Ceticismo profissional (item 15) – exemplos concretos aplicados
1. **Impairment.** A NE 3.4 afirma que não houve indicativos. Mesmo assim, foi comparado o valor de mercado (R$ 3,3 bi) com o PL (R$ 4,33 bi), o que indica impairment pelo CPC 01, item 12(d) (DIAG, achado 1; PT 315 e PT 540).
2. **Consistência interna da DF.** Divergências entre a tabela e o texto da NE 9 (séries da 4ª emissão) e entre a NE 9 e a NE 25 (datas e taxas) (PT 450).
3. **"Evento subsequente" da NE 25.** Os fatos descritos são anteriores à data do balanço (PT 560).
4. **Dados da companhia × dados da CVM.** Conciliação PDF × CVM sem diferenças (PT 500). Comparativos de 2024 × DFP 2024 sem diferenças (PT 510).
5. **Base simulada.** Os testes rodaram "às cegas", sem ler o log de erros (PT 530).

## 5. Risco de auditoria (item 17; definições do item 13)
- **Fórmula:** RA = RI × RC × RD. **RA aceito: 5%** (segurança razoável, alta).
- **Imobilizado:** RI = 100% (estimativas de unidades produzidas, impairment, capitalização) e RC = 100% (controles não testados por falta de acesso), logo **RD = 5%**. Isso exige procedimentos substantivos extensos: MUS com fator de confiabilidade 3,00 (PT 530).
- **Outras contas:** riscos avaliados no PT 315 e respostas no PT 330.
- **Limitações inerentes:** fraude, julgamento, estimativas e teste por amostragem. Elas impedem que a segurança seja absoluta (segurança razoável ≠ garantia).

## 6. Referências cruzadas
PT EC · PT 210 · PT 220 · PT 315 · PT 320 · PT 330 · PT 500 · PT 530 · matriz de cobertura · `docs/USO_DE_IA.md`.

## 7. Conclusão e limitações
Os princípios da NBC TA 200 (ética, ceticismo, julgamento, evidência e risco) orientaram todos os PTs.

**Limitação central (item 24):** sem acesso a registros e pessoas da entidade, o objetivo de obter segurança razoável **não pode ser cumprido** por este trabalho. O dossiê documenta riscos, procedimentos realizados com evidência pública, procedimentos planejados e procedimentos simulados, **sem afirmar ter emitido opinião profissional independente**.
