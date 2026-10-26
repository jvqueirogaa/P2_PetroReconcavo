# PT 450 – Avaliação das distorções identificadas

| Campo | Conteúdo |
|---|---|
| **Código** | PT 450 |
| **Norma e itens** | NBC TA 450 (R1), itens 4 (definições), 5, 6 (a)–(b), 7, 8, 9, 10, 11 (a)–(b), 12, 13, 14 e 15 (a)–(c); A2 (trivial), A4 e A5 (divulgação), A6 (factual / julgamento / projetada), A8, A9 |
| **Versão consultada** | NBC TA 450 (R1), de 19/08/2016, com a Revisão NBC 3 (consolidado da disciplina) |
| **Preparador** | Matrícula 211059370 – 24/10/2026 |
| **Revisão** | ______ (campo reservado; não preenchido) |
| **Classificação** | **[SIMULADO]** distorções de valor (bases sintéticas: imobilizado e folha) · **[REALIZADO]** distorções de divulgação na DFP publicada · **[PLANEJADO]** comunicação e pedido de correção |

## 1. Objetivo
Avaliar o efeito das distorções identificadas na auditoria e o efeito das distorções não corrigidas sobre as DFs (objetivo da norma).

## 2. Referenciais (PT 320; item 15(a))
| Parâmetro | R$ |
|---|---:|
| Materialidade global (MG) | 31.500.000 |
| Materialidade para execução (ME) = incorreção tolerável do imobilizado (IT) | 20.475.000 |
| **Claramente trivial (item 5; A2)** | **1.575.000** (5% da MG) |
| Materialidade específica – remuneração e partes relacionadas | 1.500.000 |
| *Covenants* e sensibilidade da provisão para abandono | Qualitativa |

**Regra de acumulação (item 5; A2 a A5):**
- acumula-se toda distorção de valor acima de R$ 1.575.000 **e**, por prudência, toda distorção de mesma natureza cuja soma supere esse limite;
- distorções de **divulgação** são acumuladas por natureza (A4), sem soma aritmética (A5);
- distorções que indicam **fraude** são acumuladas qualquer que seja o valor (A3 e NBC TA 240).

## 3. Quadro de distorções acumuladas (item 15(b))

### 3.1 Imobilizado – distorções de valor [SIMULADO]
Os testes de 100% (T01 a T10) foram executados **às cegas**, antes de ler o log de erros inseridos (PT 530). Os valores abaixo são os **observados pelo auditor**, depurados de dupla contagem: o item que já sai do saldo por existência (T01, T02, T05, T08) não é contado de novo na avaliação (T04).

| Ref. | Distorção | Tipo (A6) | Itens | Efeito no valor líquido do imobilizado (R$) | Fonte |
|---|---|---|---:|---:|---|
| M01 | Registros duplicados (T01) | Factual | 160 | +6.737.989 (superavaliação) | `EXCECOES_TESTES_POPULACAO.csv` |
| M02 | Itens com aquisição após 31/12/2025 (corte – T02) | Factual | 46 | +2.502.284 | idem |
| M03 | Itens baixados ainda com saldo (T05) | Factual | 63 | +2.553.788 | idem |
| M04 | Itens em campo fora das 58 concessões, sem documento (T08) | Factual | 35 | +1.234.406 | idem |
| M05 | Depreciação acumulada **menor** que o recálculo (T04, diferenças positivas) | Factual (recálculo) | 70 | +1.511.552 | idem |
| M06 | Depreciação acumulada **maior** que o recálculo, inclusive os 40 itens com valor líquido negativo (T03 ∩ T04) | Factual (recálculo) | 40 | **−1.940.768** (subavaliação) | idem |
| | **Subtotal factual** | | **414** | **+12.599.251** | |
| M07 | Almoxarifado sem movimento há mais de 5 anos (T06): perda estimada pelo valor líquido integral | Julgamento (depende da avaliação de recuperabilidade) | 95 | +281.274 (exposição máxima) | idem |
| M08 | Obras paradas há mais de 2 anos (T09) | Julgamento | 45 | +1.134.210 (exposição máxima) | idem |
| | **Subtotal de julgamento** | | **140** | **+1.415.484** | |
| M09 | **Projeção do MUS** – custo acima do suportado por documento (estrato inferior) | **Projetada** (NBC TA 530, item 14) | 2 erros na amostra | **+4.227.739** | seção 3.2 |
| | **Total de distorções de valor acumuladas no imobilizado** | | | **+18.242.474** | |

**M10 – Blocos exploratórios da SPE Tiêta (exposição em investigação; [REALIZADO]).**
- A NE 17.2 informa os 3 blocos REC-T da SPE Tiêta como "valor reduzido a R$ 0". Porém, o consolidado menos a controladora mostra **R$ 10.604 mil** em blocos exploratórios (NE 7.1: 20.157 − 9.553).
- **Não** é tratada como distorção enquanto não houver evidência: o saldo pode se referir a outro direito. A inconsistência foi aberta pelo item 11 do PT 500 (I5).
- **Se** o saldo se referir aos blocos zerados, haveria superavaliação potencial de até R$ 10.604 mil.

### 3.2 Por que a projeção do MUS exclui as duplicidades (julgamento documentado)
- A amostra MUS (772 itens; I = R$ 5.733.000) encontrou 5 diferenças:
  - **3 duplicidades** (*tainting* 1,0), que são itens da mesma população que o **T01 já cobriu em 100%** e que já estão integralmente em M01;
  - **2 diferenças de suporte documental** (*taintings* 0,630 e 0,107).
- Projetar as duplicidades contaria duas vezes a mesma classe de erro, já quantificada exatamente. Pelo A6, a distorção projetada é a melhor estimativa para a parte da população **não** testada integralmente.
- Por isso, a projeção relevante para o quadro é só a das 2 diferenças de suporte:
  - IMP = 0,630135 × 5.733.000 + 0,107305 × 5.733.000 = **R$ 4.227.739**;
  - ajuste incremental (Ilustração 8.7, coluna RD 5%): 0,630135 × 0,75 × 5.733.000 + 0,107305 × 0,55 × 5.733.000 = **R$ 3.047.769**;
  - **LSI ajustado** = precisão básica 17.199.000 + 4.227.739 + 3.047.769 = **R$ 24.474.508**.
- O LSI do PT 530 com as 5 diferenças é de R$ 50.382.308. **Nos dois cálculos o LSI supera a IT** (R$ 20.475.000). Pela NBC TA 530, item 15, e pelo Gramling, o resultado **não permite aceitar** o saldo sem trabalho adicional (seção 4).

### 3.3 Folha de pagamento e obrigações trabalhistas [SIMULADO]
| Ref. | Distorção | Tipo | Valor (R$) | Observação |
|---|---|---|---:|---|
| M11 | Obrigações com vencimento a partir de 01/01/2027 apresentadas no **circulante** (G06) | Factual – classificação | 1.887.634 | Abaixo do trivial em valor. Acumulada pela natureza: afeta a classificação circulante × não circulante. Efeito na liquidez corrente < 0,01x. Não afeta *covenants* |
| M12 | Pagamentos a matrículas inexistentes (G01: 6) e após desligamento (G03: 8) | Factual – **indício de fraude** | 718.685 (732.640 com encargos) | Abaixo do trivial, mas acumulada pela **natureza** (A3; NBC TA 240, item 36). Ver PT 240 e PT 265 (D02) |

### 3.4 Distorções de divulgação na DFP publicada [REALIZADO] (A4 e A5 – acumuladas por natureza)
| Ref. | Distorção | Fonte | Avaliação qualitativa |
|---|---|---|---|
| D-I1 | Valores das séries da 4ª emissão aparentemente trocados na tabela da NE 9.1 (1ª série 225.208 / 2ª 525.492) × texto da NE 9 e NE 25 (R$ 525 mi / R$ 225 mi) | F01 p.72, 74-75, 101 | Afeta o entendimento do custo por série. O total (R$ 750 mi) está correto |
| D-I2 | Data de liquidação (18/12 × 29/12/2025) e taxas da 4ª emissão (7,40% × 7,4564% e 7,2833%) divergentes | F01 NE 9 × NE 25 | Divergência factual entre notas |
| D-I3 | NE 25 "Evento subsequente" descreve fatos anteriores ao balanço (liquidação e swaps de dezembro) | F01 p.101; PT 560 | Rótulo inadequado. Só o swap de 12/01/2026 é subsequente |
| D-I4 | Saldo a pagar pela UPGN (R$ 18.515 mil) com três equivalências em US$ (3.559; 9.952; cerca de 3.365 pela PTAX) | F01 NE 11 e NE 21 | Afeta a divulgação de risco cambial (NE 21) |
| D-I5 | NE 16.2: AGO de "24 de abril de **2024**" fixando a remuneração de 2025 | F01 p.91 | Trivial (erro de data). Comparada com a materialidade específica de remuneração, não muda valores |

## 4. Consideração durante a auditoria (itens 6 e 7)
- **Item 6(a) – natureza indica mais distorções?** **Sim.** As distorções M01 a M05 vêm de falhas sistêmicas de controle (D01 do PT 265: cadastro sem segregação) e afetam várias classes. Pelo A7, isso indica que podem existir outras distorções da mesma origem.
- **Item 6(b) – o conjunto se aproxima da materialidade?** **Sim.** O total de R$ 18.242.474 equivale a **89% da ME** e 58% da MG. Somada a exposição M10 (R$ 10.604 mil), chegaria a 92% da MG. Pelo A8, o risco de que distorções não detectadas levem o conjunto acima da materialidade **não é aceitavelmente baixo**.
- **Revisão da estratégia (PT 300 e PT 330):**
  - (i) pedir à administração que examine **toda** a classe "custo capitalizado com suporte documental" (origem das diferenças do MUS) – A9;
  - (ii) ampliar a inspeção documental ao estrato inferior;
  - (iii) resolver a exposição M10 antes da conclusão.
- **Item 7 [SIMULADO como premissa didática]:** se a administração examinar a população e corrigir as distorções, o auditor deve reexecutar os testes. Na base, isso equivale a rodar novamente T01 a T10 e o MUS sobre a base corrigida.

## 5. Comunicação e correção (itens 8 e 9) [PLANEJADO]
- **Item 8:** todas as distorções acumuladas (M01 a M12 e D-I1 a D-I5) seriam comunicadas tempestivamente ao diretor financeiro, com pedido de correção.
- **Premissa didática do dossiê:** a administração **corrige** as distorções factuais M01 a M06, M11 e D-I1 a D-I5, e **não corrige** M07 e M08 (discorda da perda) nem a distorção projetada M09.
- **Item 9:** as razões da recusa seriam obtidas e documentadas (por exemplo, "avaliação de recuperabilidade do almoxarifado em andamento").

## 6. Avaliação do efeito das distorções não corrigidas (itens 10 e 11)
- **Item 10 – a materialidade continua apropriada?** **Sim.** A MG foi calculada sobre a receita líquida **efetiva** de 2025 (R$ 3.157.609 mil). As distorções não alteram a receita de forma significativa.

**Item 11(a) – magnitude e natureza:**

| Cenário | Distorções de valor não corrigidas (R$) | % ME | % MG |
|---|---:|---:|---:|
| A – antes de qualquer correção (M01 a M09 + M11) | 20.130.108 | 98,3% | 63,9% |
| **B – após a premissa do item 5 (só M07, M08 e M09 não corrigidas)** | **5.643.223** | **27,6%** | **17,9%** |
| C – B + exposição M10, se confirmada | 16.247.223 | 79,4% | 51,6% |

**Fatores qualitativos considerados:**
- as distorções **não** alteram o cumprimento de *covenants* (DL/EBITDA de 1,06x contra limite de 3,0x – PT 570), **não** transformam lucro em prejuízo e **não** afetam a remuneração variável de forma identificável;
- **porém**, M12 indica fraude (desvio de ativos na folha) → mesmo sendo pequena, exige avaliação da integridade e da extensão (PT 240);
- D-I1 a D-I4 são distorções de divulgação na mesma emissão de debêntures. **Em conjunto**, prejudicam a compreensão da dívida e por isso foram tratadas como correção necessária (premissa: corrigidas).

**Avaliação no cenário B:** as distorções não corrigidas **não são relevantes**, individualmente ou em conjunto, para as DFs como um todo, **desde que**:
- (i) o trabalho adicional da seção 4 reduza o LSI do MUS abaixo da IT;
- (ii) a exposição M10 seja resolvida sem distorção;
- (iii) a investigação de M12 não revele fraude mais ampla.

Se o LSI continuar acima da IT, o saldo do imobilizado **não poderá ser aceito** com base na amostra (NBC TA 530, item 15).

- **Item 11(b) – distorções de períodos anteriores:** nenhuma identificada (comparativos sem diferença – PT 510).

## 7. Comunicação à governança e representação (itens 12 a 14)
- **Itens 12 e 13 [PLANEJADO]:** a lista de distorções não corrigidas (M07, M08, M09) vai ao CAE, com o pedido de correção (PT 260, item 16(e)). Não há distorção não corrigida **individualmente relevante**.
- **Item 14:** o demonstrativo de ajustes não registrados é anexado à carta de representação (PT 580, item 6).

## 8. Referências cruzadas
PT 320 (referenciais) · PT 530 (MUS: LSI de R$ 50.382.308; ajuste do item 3.2) · PT 240 (M12) · PT 265 (D01, D02 e D07) · PT 500 (I1 a I6) · PT 540 (M07 e M08 – recuperabilidade) · PT 560 (D-I3) · PT 550 (D-I5) · PT 570 · PT 580 · PT 260 · `TESTES_BASE_RECV3.xlsx` · `TESTES_FOLHA_RECV3.xlsx`.

## 9. Conclusão e limitações
- As distorções de valor acumuladas no imobilizado sintético (R$ 18,2 mi) **se aproximam da ME** e exigem revisão da estratégia (item 6). O LSI do MUS supera a IT.
- Na premissa didática de correção das distorções factuais, as não corrigidas (R$ 5,6 mi) **não são relevantes**, condicionadas às três ressalvas da seção 6.

**Limitações:**
- as distorções de valor são de **dados sintéticos** (não representam a PetroReconcavo);
- as de divulgação são reais, mas a classificação como distorção depende de confirmação com a companhia;
- a premissa de correção é **didática**, não um fato.

*Este PT avalia distorções; não expressa opinião sobre as DFs.*
