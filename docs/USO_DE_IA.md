# Registro de uso de inteligência artificial (IA)

**Trabalho:** P2 – Auditoria 1 (CCA0024, UnB 2026.2) – dossiê de auditoria da PetroReconcavo S.A. (RECV3)
**Aluno / preparador:** matrícula 211059370
**Ferramenta de IA:** Claude (Anthropic), usado pelo aplicativo Claude com acesso à pasta do trabalho no computador do aluno.
**Ferramentas de execução:** Python 3 (pandas, numpy, openpyxl), Jupyter/Google Colab e LibreOffice (recálculo das fórmulas das planilhas).

> Em aula, o professor orientou que se pode usar IA para gerar a base e executar os procedimentos, desde que (1) o código seja entregue, (2) a ferramenta seja explicada, (3) o passo a passo seja registrado e (4) o aluno confira e justifique os resultados. Este arquivo atende os itens (2) a (4); o item (1) está nas pastas `codigo/` e `notebooks/`.

## 1. Divisão de papéis

| Etapa | O que a IA fez | O que o aluno fez / deve fazer |
|---|---|---|
| Roteiro | Propôs o roteiro dos 27 PTs a partir do enunciado, do plano de ensino e das normas | Definiu a ordem de execução e os pontos de parada para conferência |
| 1 – Fontes | Localizou e baixou os documentos (RI, CVM, B3), montou o registro com URL, data, hora, página e hash | Pediu a inclusão da hora de acesso; conferir os links e as páginas citadas |
| 2 – Diagnóstico | Extraiu as DFs, recalculou a NE 7, os covenants e os indicadores, e listou achados como hipóteses | Confirmou que a conta escolhida é a de maior materialidade; revisar os achados |
| 3 – Base simulada | Escreveu os geradores, os testes, o MUS (seguindo o material do Gramling enviado pelo professor), a conciliação, o dicionário e o notebook | Enviou o material de MUS e as notas da aula; **conferir os itens da seção 3** |
| Revisão do passo 3 | Refez a materialidade seguindo a NBC TA 320 (itens 10, 11, A4–A8, A13; NBC TA 450 A2) e corrigiu a calibração da depreciação linear; reexecutou todos os testes | **Questionou a materialidade provisória de R$ 35 mi** ("não é algo que você pode simplesmente fazer uma média da sua cabeça") e exigiu que toda decisão seguisse o texto das NBC TA |
| 4 – Papéis de trabalho | Redigiu os PTs EC e 200 a 600, cada um amarrado aos itens de requisito da norma (lidos do consolidado da disciplina); gerou as planilhas PT 320, PT 520 e PT 540 com fórmulas | Conferir cada PT contra a norma e os números contra as fontes (checklist da seção 3) |
| 5 – Montagem | Gerou a matriz de cobertura (itens de requisito × PT), o PT 999 (conclusão sem opinião), o dossiê em PDF com referências cruzadas e o README | Criar o repositório no GitHub, subir os arquivos e enviar o link |

## 2. Principais instruções (prompts) dadas pelo aluno

Transcrição resumida das instruções, em ordem cronológica:
1. "Antes de começarmos a executar qualquer coisa vamos montar um roteiro de cada passo que devemos fazer" (com o enunciado da P2 anexado).
2. "Pode começar a etapa 1!"
3. "Você criou o registro de fontes com os horários de acessos, sites e tudo mais? (...) Verificou se houve mudança de nome empresarial? (...) Você conferiu se o imobilizado é a conta de maior materialidade? Se for pode seguir pode executar toda a segunda parte."
4. Envio das notas da aula (Granola), com o pedido de comparar com o enunciado e o plano de ensino e tirar dicas novas.
5. "Coloquei o arquivo com a explicação do MUS na pasta (...) executa até o passo 3, depois disso vou conferir tudo."
6. "Como você definiu essa materialidade de 35 milhões? Qual foi sua conta e seus parâmetros? Usou a NBC TA 320 como base? Onde está documentado isso da depreciação? (...) mapeie todos os papéis de trabalho (...) e me diga quais são os mais simples e os mais complexos."
7. "Sim, adote a materialidade da NBC TA 320 e corrija a depreciação. (...) as NBC TAs são a sua principal fonte de como fazer esses papéis de trabalho, qualquer coisa que você for fazer busque na norma NBC TA qual a forma correta de fazer. (...) é imprescindível que siga o que está escrito na norma."

**Técnicas de *prompt* usadas:** norma como fonte primária (cada procedimento ancorado no item da NBC TA); contexto completo (enunciado, plano de ensino, normas e material de MUS na pasta); execução por etapas com pontos de conferência; exigência de rastreabilidade (fonte, página, hora); separação explícita entre real e simulado; instrução para não apresentar como realizado o que não foi realizado.

## 3. Checklist de conferência do aluno (preencher)

| # | Conferência | Como conferir | OK? | Observação do aluno |
|---|---|---|---|---|
| 1 | A base tem pelo menos 500.000 linhas, cada uma um item distinto | `base_simulada/DICIONARIO_VARIAVEIS.md` (contagem) ou abrir a amostra de 2.000 linhas | ☐ | |
| 2 | O total da base bate com a NE 7.1 / CVM 1.02.03 (diferença só de arredondamento) | `planilhas/CONC_BASE_RECV3.xlsx`, aba `Conc_classe` | ☐ | |
| 3 | Os parâmetros do MUS estão de acordo com o Gramling (RD, FC, FEE, I, n) | `planilhas/TESTES_BASE_RECV3.xlsx`, aba `MUS_parametros`, comparada com a Ilustração 8.7 | ☐ | |
| 4 | A avaliação do MUS (PB + IMP + IA = LSI) e a conclusão estão corretas | aba `MUS_avaliacao` (fórmulas editáveis) | ☐ | |
| 5 | Concorda com a materialidade da NBC TA 320 (MG R$ 31,5 mi = 1% da receita líquida, A5/A8; ME 65%, A13; trivial 5%, NBC TA 450 A2) | `planilhas/PT320_MATERIALIDADE_RECV3.xlsx` e PT 320; para mudar, alterar `PARAM` em `codigo/testes_auditoria_base.py` e reexecutar | ☐ | |
| 6 | Os testes foram executados antes da leitura do log de erros | `codigo/testes_auditoria_base.py`: o log só é lido na seção (4) | ☐ | |
| 7 | Os resultados são reproduzíveis | Rodar `python codigo/rodar_passo3.py` e conferir os totais em `METADADOS_GERACAO.json` | ☐ | |
| 8 | Todo arquivo simulado está identificado como SINTÉTICO | Coluna `natureza_dado` e cabeçalhos das planilhas | ☐ | |
| 9 | Os textos e conclusões foram revisados e reescritos com as palavras do aluno (o professor verifica similaridade) | Revisão dos PTs | ☐ | |
| 10 | Cada PT cita os itens de requisito da norma e a matriz mostra 100% de cobertura | `matriz_cobertura/MATRIZ_COBERTURA_NORMAS.xlsx`, abas `Matriz_por_norma` e `Itens_requisitos` | ☐ | |
| 11 | Os números dos PTs batem com as fontes (amostra: PT 540 provisão para abandono R$ 145.192; PT 520 royalties R$ 198.434; PT 600 SPE Tiêta R$ 879.674) | Páginas do F01 indicadas em cada PT | ☐ | |
| 12 | Nenhum PT apresenta confirmação, entrevista ou inspeção como realizada, nem simula revisão de terceiros | Busca por "[REALIZADO]" nos PTs; campo "Revisão" em branco | ☐ | |
| 13 | O PT 999 não emite opinião | Ler a seção 3 do PT 999 | ☐ | |

## 4. Limites do uso de IA neste trabalho

1. A IA não contatou a empresa, os auditores ou terceiros, nem enviou solicitações reais (confirmações ou e-mails).
2. Nenhum procedimento que dependesse de acesso interno foi apresentado como realizado. Esses procedimentos aparecem como "planejado por falta de acesso".
3. A IA não emite opinião de auditoria. O trabalho é didático e **não** constitui opinião profissional independente.
4. Os números extraídos das fontes públicas foram conferidos por recálculo (Python e fórmulas do Excel). O aluno deve revisar por amostragem as páginas citadas no registro de fontes.
