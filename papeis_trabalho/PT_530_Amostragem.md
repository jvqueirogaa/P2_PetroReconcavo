# PT 530 – Amostragem em auditoria: MUS no imobilizado (base simulada)

| Campo | Conteúdo |
|---|---|
| **Código** | PT 530 |
| **Norma e itens** | NBC TA 530, itens 5 (definições: população, unidade de amostragem, risco de amostragem, distorção tolerável, anomalia), 6, 7, 8, 9, 10, 11, 12, 13, 14 e 15 (a)–(b); Apêndices 2 e 4. Metodologia: Gramling, cap. 8 (MUS – *monetary unit sampling*), Ilustração 8.7 |
| **Versão consultada** | NBC TA 530, de 27/11/2009 (consolidado da disciplina) |
| **Preparador** | Matrícula 211059370 – 24/10/2026 |
| **Revisão** | ______ (campo reservado; não preenchido) |
| **Classificação** | **[SIMULADO PARA FINS DIDÁTICOS]**: população, inspeção documental e erros são sintéticos |
| **Papéis de suporte** | `planilhas/TESTES_BASE_RECV3.xlsx` (abas `MUS_parametros`, `MUS_amostra`, `MUS_avaliacao`, `Inseridos_x_detectados`, com fórmulas) · `base_simulada/resultados/RESULTADOS_MUS.json` · `MUS_AMOSTRA_SELECIONADA.csv` · `codigo/testes_auditoria_base.py` · notebook, seção de scripts |

## 1. Objetivo
Dar ao auditor base razoável para concluir sobre a população do imobilizado a partir da amostra (objetivo da norma). A afirmação testada é a **existência e exatidão do valor líquido** (superavaliação), por inspeção documental.

## 2. Definição da amostra (item 6; A4 a A9)
| Elemento | Definição |
|---|---|
| Finalidade | Detectar **superavaliação** do valor contábil líquido (custo sem documento ou acima do suportado) – R05/R06 do PT 315 |
| População (item 5(a)) | Subrazão sintético do imobilizado em 31/12/2025: **532.598 registros**; valor líquido de R$ 6.170.839.319, conciliado com a NE 7.1 (`CONC_BASE_RECV3.xlsx`) |
| Estratificação / segregação | **517.770 itens com valor líquido > 0** (VC de R$ 6.171.370.101,38) entram no MUS. Os 14.828 itens com valor líquido ≤ 0 foram segregados: o MUS não seleciona valores zero ou negativos. Os 40 negativos foram testados em 100% (T03) |
| Unidade de amostragem (item 5(f)) | **R$ 1 do valor líquido** (MUS) → probabilidade de seleção proporcional ao valor |
| Distorção / incorreção tolerável (IT) | **R$ 20.475.000** = ME (PT 320). Não há materialidade específica para o imobilizado |
| Distorção esperada (IE) | 10% da IT = R$ 2.047.500 (primeira auditoria, sem histórico; julgamento) |
| Definição de distorção | Diferença entre o valor líquido registrado e o suportado pelo documento (nota/medição) e, quando inexistente, o valor integral |

**Integridade da população (A5 e NBC TA 500, item 9):** feita pela conciliação total com a NE 7.1 e pelo hash do conteúdo (PT 500, seção 4).

## 3. Tamanho da amostra (item 7; Apêndice 2) – Gramling
| Parâmetro | Valor | Fundamento |
|---|---:|---|
| Risco de auditoria (RA) | 5% | Julgamento |
| Risco inerente (RI) | 1,0 | Máximo: estimativas e capitalização (PT 315) |
| Risco de controle (RC) | 1,0 | Máximo: controles não testados (PT 330) |
| Risco de detecção (RD) = RA / (RI × RC) | 5% | Coluna de 5% da Ilustração 8.7 |
| Fator de confiabilidade (FC) | 3,00 | Ilustração 8.7 |
| Fator de expansão de erro (FEE) | 1,60 | Ilustração 8.7 |
| **Intervalo de amostragem I = (IT − IE × FEE) / FC** | **R$ 5.733.000** | (20.475.000 − 2.047.500 × 1,6) / 3 |
| n = VC / I | **1.076 pontos** | 6.171.370.101,38 / 5.733.000 |

O risco de amostragem (item 5(c)) fica limitado a 5% pelo uso do FC da coluna RD = 5%.

## 4. Seleção (item 8; Apêndice 4)
- **Seleção sistemática por intervalo monetário**, com **início aleatório** de R$ 3.429.906,84 (gerador numpy, semente registrada).
- Pontos de seleção: início + k × I, com k = 0 a 1.075.
- **1.076 pontos → 772 itens distintos.** Itens com mais de um ponto contam uma vez.
- **Estrato superior:** 56 itens com valor ≥ I (R$ 2.063,3 mi), selecionados com certeza. **Estrato inferior:** 716 itens (R$ 285,3 mi).
- Toda unidade monetária teve a mesma chance de seleção (item 8).

## 5. Execução (itens 9 a 11) – [SIMULADO]
- **Item 9:** inspeção documental simulada (`INSPECAO_DOCUMENTAL_SIMULADA.csv.gz`) para os 772 itens. O valor auditado é o valor suportado pelo documento.
- **Item 10:** não houve item em que o procedimento fosse inaplicável. Os 772 documentos foram "localizados".
- **Item 11:** nenhum item ficou sem procedimento. Pela regra do item 11, um item sem procedimento seria tratado como distorção integral.

## 6. Natureza e causa das distorções (item 12) e anomalia (item 13)

| # | Item | Estrato | Valor líquido (R$) | Auditado (R$) | Distorção (R$) | *Tainting* | Natureza e causa |
|---|---|---|---:|---:|---:|---:|---|
| 1 | IMB-0033499 | Inferior | 16.074,47 | 0,00 | 16.074,47 | 1,0000 | Documento já vinculado a outro registro → **duplicidade** (falha de cadastro – D01) |
| 2 | IMB-0262098 | Inferior | 1.479.340,84 | 0,00 | 1.479.340,84 | 1,0000 | Duplicidade |
| 3 | IMB-0468355 | Inferior | 2.947.113,56 | 0,00 | 2.947.113,56 | 1,0000 | Duplicidade |
| 4 | IMB-0469519 | Inferior | 458.332,64 | 169.521,33 | 288.811,31 | 0,6301 | Nota/medição suporta valor menor (custo acima do suportado, possivelmente manutenção capitalizada – R06) |
| 5 | IMB-0471357 | Inferior | 749.851,21 | 669.388,76 | 80.462,45 | 0,1073 | Idem |

- **Item 12:** as causas são **sistêmicas** (falha de segregação no cadastro e critério de capitalização), e não isoladas. O PT 265 trata as deficiências, e o PT 450 avalia o efeito.
- **Item 13 (anomalia):** **não se aplica.** Nenhuma distorção atende à exigência de "grau elevado de certeza" de não ser representativa, porque as duplicidades e o sobrecusto se repetem na população. Todas foram projetadas.

## 7. Projeção (item 14) e avaliação (item 15)

| Componente (Gramling) | Valor (R$) | Cálculo |
|---|---:|---|
| Precisão básica (PB) | 17.199.000,00 | FC × I = 3,00 × 5.733.000 |
| Incorreção mais provável (IMP) – estrato inferior | 21.426.739,36 | Σ *tainting* × I (5 distorções) |
| Incorreção do estrato superior | 0,00 | Nenhuma distorção nos 56 itens |
| Ajuste incremental (IA) | 11.756.568,66 | *Taintings* em ordem decrescente × fatores incrementais da coluna de 5% (0,75; 0,55; 0,46; 0,40; 0,36) × I |
| **Limite superior de incorreção (LSI)** | **50.382.308,03** | PB + IMP + IA |
| Incorreção tolerável (IT) | 20.475.000,00 | PT 320 |

**Item 15(a) – resultados.** **LSI (R$ 50,4 mi) > IT (R$ 20,5 mi)** e IMP (R$ 21,4 mi) > IT. A amostra **não fornece base razoável** para concluir que a população está livre de distorção relevante.

**Item 15(b) – a avaliação de riscos foi confirmada?** **Não.** A taxa de distorção ficou acima da esperada (IE = R$ 2,05 mi). Pelo A23 e pelo Gramling, as alternativas são:
- (i) pedir à administração que investigue e corrija a classe;
- (ii) ampliar a amostra ou os testes;
- (iii) aplicar procedimentos alternativos.

Escolhas deste dossiê:
1. Os 160 duplicados foram **identificados em 100%** pelo teste T01 (PT 450 – M01).
2. Excluídas as duplicidades já quantificadas, o LSI ajustado (só sobrecusto) é de **R$ 24.474.508**, que **ainda supera a IT** (cálculo no PT 450, seção 3.2).
3. Logo, é preciso **ampliar a inspeção documental** no estrato inferior e pedir à administração que examine a classe "custo capitalizado × documento" (NBC TA 450, item 7 e A9).

## 8. Validação didática – "a IA executa, o aluno confere e justifica"
O log de erros inseridos só foi lido **depois** dos testes, que foram executados às cegas (`Inseridos_x_detectados`):
- foram inseridos **97 erros de sobrecusto (E09), somando R$ 9,17 mi**; o MUS encontrou 2;
- outros 3 erros encontrados pelo MUS eram duplicidades (E01);
- a superavaliação total inserida na base (todos os tipos) é de **R$ 23,71 mi**, e o **LSI de R$ 50,38 mi a cobre**. Isso é coerente com a confiança de 95%: o limite superior deve ser maior que a distorção real com alta probabilidade;
- a IMP (R$ 21,4 mi) ficou **próxima** da superavaliação real (R$ 23,7 mi). A estimativa central foi boa, apesar de só 5 distorções na amostra.

**Leitura para o aluno conferir.** O MUS mostrou baixo poder para achar **muitos erros pequenos** (E09 é pulverizado). Mas o LSI cumpriu o papel de **sinalizar** que o saldo não pode ser aceito, o que é exatamente o comportamento esperado do método (Gramling, cap. 8: o MUS é eficiente para superavaliações e conservador quando há muitas distorções).

## 9. Referências cruzadas
PT 320 (IT) · PT 315 (R05, R06) · PT 330 (P05, P06) · PT 450 (M01, M09; LSI ajustado) · PT 265 (D01) · PT 500 (integridade da população) · PT 501 (almoxarifado) · Notebook, seções de simulação e de scripts · `docs/USO_DE_IA.md`.

## 10. Conclusão e limitações
Pelo MUS, o saldo do imobilizado **não pode ser aceito sem trabalho adicional**: LSI de R$ 50,4 mi (ajustado: R$ 24,5 mi) contra IT de R$ 20,5 mi.

**Limitação:** tudo é **simulado**. População, documentos e erros são sintéticos. A conclusão ilustra a técnica e **não** descreve a PetroReconcavo.
