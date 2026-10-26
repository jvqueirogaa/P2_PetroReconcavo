# Dossiê de auditoria – PetroReconcavo S.A. (RECV3) – exercício de 2025

**P2 – Auditoria 1 (UnB, 2026.2)** · Preparador: **matrícula 211059370** · Versão de entrega: **v1.0 – 25/10/2026**

> Trabalho **acadêmico e didático**. Usa só fontes públicas e dados **sintéticos** identificados como tais. **Não** contém opinião de auditoria e **não** representa trabalho profissional independente. Nenhuma empresa, auditor, cliente ou fornecedor foi contatado.

## 1. O que está aqui
| Entregável exigido | Onde |
|---|---|
| Dossiê em PDF com referências cruzadas | [`dossie/DOSSIE_P2_RECV3_211059370.pdf`](dossie/DOSSIE_P2_RECV3_211059370.pdf) |
| Papéis de trabalho (EC + NBC TA 200 a 600 + conclusão integrada) | [`papeis_trabalho/`](papeis_trabalho/) – índice no [PT 230](papeis_trabalho/PT_230_Documentacao.md) |
| Matriz de cobertura das normas (itens de requisito × PT) e registro das versões das normas | [`matriz_cobertura/MATRIZ_COBERTURA_NORMAS.xlsx`](matriz_cobertura/MATRIZ_COBERTURA_NORMAS.xlsx) |
| Relação de fontes (URL, data e hora de acesso, documento, página, exercício, hash) | [`planilhas/REG_FONTES_RECV3.xlsx`](planilhas/REG_FONTES_RECV3.xlsx) |
| Base simulada (≥ 500 mil linhas) da conta de maior materialidade do ativo (imobilizado), com dicionário, conciliação, log de erros e testes | [`base_simulada/`](base_simulada/) – ver [`README_BASE_SIMULADA.md`](base_simulada/README_BASE_SIMULADA.md) |
| Código e notebook (seções de simulação e de scripts, comentados) | [`codigo/`](codigo/) · [`notebooks/P2_RECV3_passo3_base_simulada.ipynb`](notebooks/P2_RECV3_passo3_base_simulada.ipynb) |
| Planilhas editáveis (com fórmulas) | [`planilhas/`](planilhas/) |
| Programas de auditoria por ciclo (receitas, disponibilidades, estoques, imobilizado, passivos, estimativas, benefícios a empregados) | [PT 300, seção 6](papeis_trabalho/PT_300_Planejamento.md) |
| Conclusão integrada (sem opinião) | [PT 999](papeis_trabalho/PT_999_Conclusao_Integrada.md) |
| Registro do uso de IA (prompts e checklist de conferência) | [`docs/USO_DE_IA.md`](docs/USO_DE_IA.md) |

## 2. Estrutura do repositório
```
README.md                 este arquivo
dossie/                   dossiê em PDF (gerado a partir dos PTs) + gerador
papeis_trabalho/          PT_EC, PT_200 ... PT_600, PT_999 (Markdown)
matriz_cobertura/         matriz de cobertura + itens de requisito extraídos das normas
planilhas/                REG_FONTES, DIAG, CONC_BASE, TESTES_BASE, TESTES_FOLHA, PT320, PT520, PT540
base_simulada/            base do imobilizado (csv.gz, 532.598 linhas), amostra, dicionário, plano de contas,
                          poços, inspeção documental, controle_erros/ (log), folha/, resultados/
diagnostico/              diagnóstico da companhia (etapa 2)
fontes/                   documentos originais (DFP, DF 2024, ITRs, FRE, fatos relevantes, atas, certificação
                          de reservas, relatórios fiduciários), dados abertos da CVM e JSON da B3
codigo/                   scripts Python (reprodução integral)
notebooks/                notebook executado (Colab/Jupyter)
docs/                     uso de IA
```

## 3. Convenções
- **Classificação de procedimentos** (enunciado): **[REALIZADO]** com evidência pública · **[PLANEJADO]** por falta de acesso · **[SIMULADO]** para fins didáticos.
- **Fontes:** F01 a F39 (`REG_FONTES`). "F01 p.69" = página **do PDF** da DFP 2025.
- **Códigos:** riscos R01 a R17 (PT 315) · respostas P01 a P17 (PT 330) · deficiências D01 a D07 (PT 265) · distorções M01 a M12 e D-I1 a D-I5 (PT 450) · confirmações C01 a C09 (PT 505).
- **Preparador e revisão:** todo PT traz matrícula e data. O campo de revisão fica **em branco** (não se simula revisão de terceiros).

## 4. Como reproduzir
Requisitos: Python 3.10+.
```bash
pip install -r requirements.txt
python codigo/rodar_passo3.py            # gera a base simulada, os testes, o MUS, a folha, o dicionário e o README da base
python codigo/pt320_materialidade.py     # PT 320 (planilha com fórmulas)
python codigo/pt520_analiticos.py        # PT 520 (planilha com fórmulas)
python codigo/pt540_aro_sensibilidade.py # PT 540 (planilha com fórmulas + JSON)
python codigo/gerar_matriz_cobertura.py  # matriz de cobertura
python dossie/gerar_dossie.py            # dossiê em PDF (requer: markdown, playwright + Chromium)
```
- **Semente fixa:** 211059370 (matrícula). O *hash* SHA-256 do conteúdo da base está em `base_simulada/METADADOS_GERACAO.json`.
- As planilhas trazem **fórmulas**. Ao abrir no Excel ou no LibreOffice, os valores são recalculados.
- Etapas 1 e 2 (`etapa1_registro_fontes.py`, `etapa2_diagnostico.py`) leem os arquivos já baixados em `fontes/`. Os *downloads* originais foram feitos pelo navegador (datas e horas no `REG_FONTES`).
- No Google Colab: abrir o notebook, enviar a pasta do repositório (ou cloná-lo) e executar as células em ordem.

## 5. Resumo dos números-chave
| Item | Valor | PT |
|---|---|---|
| Conta de maior materialidade do ativo | Imobilizado e intangível – R$ 6.254.225 mil (72,2% do ativo) | DIAG; PT 315 |
| Materialidade global / execução / trivial | R$ 31.500 / 20.475 / 1.575 mil (NBC TA 320: 1% da receita líquida) | PT 320 |
| Base simulada | 532.598 registros; conciliada com a NE 7.1; 11 tipos de erro inseridos (log separado) | PT 530 |
| MUS | I = R$ 5.733.000; 1.076 pontos / 772 itens; LSI de R$ 50,4 mi > IT | PT 530 |
| Riscos significativos | *Impairment*, provisão para abandono, receita (fraude presumida), burla de controles | PT 315 |

## 6. Limitações
Ver o [PT 999, seção 5](papeis_trabalho/PT_999_Conclusao_Integrada.md). Em resumo: sem acesso à entidade, todos os testes de detalhes dos riscos significativos, as confirmações, as indagações e as inspeções estão **planejados**. A base e os erros são **sintéticos**.
