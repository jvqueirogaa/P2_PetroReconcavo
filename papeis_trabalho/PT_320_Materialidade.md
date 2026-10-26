# PT 320 – Materialidade no planejamento e na execução da auditoria

| Campo | Conteúdo |
|---|---|
| **Código** | PT 320 |
| **Norma e itens** | NBC TA 320 (R1), itens 8, 9, 10, 11, 12, 13, 14, A4, A5, A6, A8, A11, A12, A13 e A14; NBC TA 450 (R1), item 5 e A2 |
| **Versão da norma consultada** | NBC TA 320 (R1), de 19/08/2016, aplicável a períodos findos em 31/12/2016 ou depois (consolidado da disciplina) |
| **Entidade / período** | PetroReconcavo S.A. – DF individuais e consolidadas de 31/12/2025 |
| **Preparador** | Matrícula 211059370 – 24/10/2026 |
| **Revisão** | ______ (campo reservado; não preenchido) |
| **Classificação** | Realizado com evidência pública (cálculo sobre a DF publicada) |
| **Planilha** | `planilhas/PT320_MATERIALIDADE_RECV3.xlsx` (fórmulas editáveis), gerada por `codigo/pt320_materialidade.py` |

## 1. Objetivo
Aplicar o conceito de materialidade no planejamento e na execução da auditoria (item 8). Para isso, determinar:
- a **materialidade para as demonstrações como um todo** (item 10);
- as **materialidades específicas**, quando aplicáveis (item 10);
- a **materialidade para execução** (itens 9 e 11);
- o limite abaixo do qual as distorções são **claramente triviais** (NBC TA 450, item 5).

## 2. Afirmações e riscos considerados
A materialidade não se refere a uma afirmação específica. Ela é a referência para (i) avaliar riscos e definir natureza, época e extensão dos procedimentos (item 11) e (ii) avaliar as distorções (NBC TA 450). Riscos que afetam o julgamento:
- volatilidade do resultado por derivativos;
- primeira auditoria (PT 510);
- inconsistências de divulgação já identificadas (DIAG-RECV3, achados 2 a 5);
- risco significativo de impairment (PT 315).

## 3. População, fontes e critérios
DRE, BP e notas da DFP 2025 consolidada (F01 p.51-56; NE 20 p.94; NE 16.2 p.91), comparadas com os dados abertos da CVM (F03). Os valores estão em R$ mil.

## 4. Procedimentos executados

### 4.1 Escolha do referencial (itens A4 e A5)
O item A4 lista os fatores para escolher o referencial. A análise para a PetroReconcavo:

| Fator do A4 | Análise |
|---|---|
| (a) Elementos das DCs | Receita líquida R$ 3.157.609; LAIR R$ 776.194; PL R$ 4.330.716; ativo R$ 8.668.015 |
| (b) Itens que atraem a atenção dos usuários | Companhia listada (Novo Mercado): investidores olham produção, receita, EBITDA e lucro. Debenturistas (R$ 3,1 bi) olham os *covenants* de dívida líquida/EBITDA |
| (c) Natureza, setor e ambiente | E&P de campos maduros *onshore*, intensivo em capital, com receita atrelada ao Brent e ao dólar (97% da receita bruta – NE 21) |
| (d) Estrutura societária e financiamento | Sem controlador. Dívida relevante em debêntures, com *swaps* para dólar |
| (e) **Volatilidade do referencial** | **O LAIR passou de R$ 363.405 (2024) para R$ 776.194 (2025), +114%.** A variação vem do resultado de *swaps*: −R$ 368.547 em 2024 e +R$ 366.796 em 2025 (NE 20). **A receita líquida variou só −3,3%.** |

**Conclusão.** O item A5 diz que o LAIR é o referencial usual, mas que, *"quando o lucro antes do imposto de operações em continuidade é volátil, outros referenciais podem ser mais apropriados, como lucro bruto ou receita total"*. O LAIR da companhia é volátil por causa dos derivativos, então foi escolhida a **receita líquida consolidada de 2025**.

### 4.2 Percentual (item A8)
O A8 diz que o percentual é questão de julgamento e que o percentual sobre o LAIR é *"normalmente maior"* que o aplicado à receita. Como exemplo, cita **5% do LAIR** e **1% da receita total**, admitindo percentuais maiores ou menores. Foi adotado **1% da receita líquida**: 1% × R$ 3.157.609 = **R$ 31.576**.

### 4.3 Teste de razoabilidade (itens A6 e A4(d))

| Referencial | Base | % | Resultado |
|---|---:|---:|---:|
| **Receita líquida 2025 (escolhido)** | 3.157.609 | 1% | **31.576** |
| LAIR 2025 como divulgado | 776.194 | 5% | 38.810 |
| LAIR normalizado – média 2024-2025 (A6) | 569.800 | 5% | 28.490 |
| LAIR 2025 sem o resultado de *swaps* (A6) | 409.398 | 5% | 20.470 |
| Ativo total (A4(d)) | 8.668.015 | 0,5% | 43.340 |

O valor escolhido fica dentro da faixa formada pelos referenciais alternativos. A diferença para o LAIR normalizado pela média (A6) é de cerca de 11%.

### 4.4 Determinação

| Medida | Valor (R$ mil) | Fundamento |
|---|---:|---|
| **Materialidade global (MG)** | **31.500** | Item 10. Os R$ 31.576 foram arredondados para baixo (conservador) |
| **Materialidade para execução (ME)** | **20.475** (65% da MG) | Itens 9 e 11 e A13 (abaixo) |
| **Limite de distorção claramente trivial** | **1.575** (5% da MG) | NBC TA 450, item 5 e A2: magnitude *"totalmente diferente (menor)"* |
| **Materialidade específica – remuneração da administração e partes relacionadas** | **1.500** (ME específica: 975) | Item 10 e A11 (1º tópico). A remuneração total é de R$ 30.694 (NE 16.2) |
| **Materialidade específica – índices dos *covenants*** | Qualitativa | Item 10 e A11. Qualquer distorção que mude o cumprimento de *covenant* é relevante, seja qual for o valor |
| **Materialidade específica – sensibilidade da provisão para abandono** | Qualitativa | A11 (2º tópico): análise de sensibilidade de estimativas com alta incerteza (PT 540) |

**Materialidade para execução (A13).** A norma diz que ela *"não é um cálculo mecânico simples e envolve o exercício de julgamento profissional"*, influenciado pelo entendimento da entidade e pelas distorções de auditorias anteriores. **A norma não fixa percentual.** Os 65% foram definidos considerando:
1. **Primeira auditoria** (troca Deloitte → EY): não há histórico de distorções conhecido pelo auditor atual (PT 510).
2. **Expectativa de distorções:** o diagnóstico já mostrou inconsistências de divulgação (séries da 4ª emissão, NE 25, valores em dólar da UPGN) e um indicativo de impairment não tratado.
3. **Muitas estimativas relevantes:** reservas e depleção por unidades produzidas, provisão para abandono e derivativos.

Esses fatores pedem margem maior para distorções não detectadas, por isso o percentual ficou abaixo de patamares mais altos de execução.

### 4.5 Revisão (itens 12, 13 e A14)
A MG foi calculada sobre o **resultado efetivo do exercício encerrado** (DF publicada), não sobre projeções. Por isso não se aplica o caso do A14 (resultado efetivo diferente do previsto). **Gatilho de revisão:** ajustes que mudem a receita ou informações novas, como os achados do PT 450. Se houver revisão, a ME e os procedimentos são reavaliados (item 13) e o MUS é reprocessado (parâmetro `PARAM` do script).

## 5. Evidências e referências cruzadas
- **F01:** DRE p.52, BP p.51, NE 20 p.94, NE 16.2 p.91.
- **F03:** dados abertos da CVM.
- **DIAG-RECV3:** aba `Indicadores` (EBITDA) e aba `Achados_Preliminares`.
- **Uso nos outros PTs:** PT 530 (IT = ME = R$ 20.475 mil no MUS), PT 450 (acumulação acima de R$ 1.575 mil), PT 520 (limite de investigação ≤ ME), PT 315 e PT 330 (natureza, época e extensão).

## 6. Documentação exigida pelo item 14

| Item 14 | Registro |
|---|---|
| (a) materialidade para as DCs como um todo | R$ 31.500 mil (seção 4.4) |
| (b) materialidades específicas | Remuneração e partes relacionadas R$ 1.500 mil; *covenants* e sensibilidade da provisão para abandono: qualitativas |
| (c) materialidade para execução | R$ 20.475 mil (específica: R$ 975 mil) |
| (d) revisões | Nenhuma até 24/10/2026. Na versão preliminar do passo 3 havia uma MG provisória de R$ 35.000 mil, **substituída** por este PT antes da execução final dos testes (todos os testes foram reexecutados) |

## 7. Conclusão e limitações
A materialidade foi determinada de acordo com os itens 10 e 11 da NBC TA 320. Os percentuais aplicados seguem os exemplos do item A8 e o julgamento previsto no A13; a norma não fixa percentuais obrigatórios.

**Limitações:**
- não houve indagação à governança (A12);
- não se conhecem as distorções de auditorias anteriores (A13), porque não há acesso aos papéis da Deloitte (PT 510).
