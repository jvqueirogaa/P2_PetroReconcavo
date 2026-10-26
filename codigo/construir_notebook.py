# -*- coding: utf-8 -*-
# P2 - Auditoria 1 - RECV3 - Preparador 211059370
# Constroi o notebook (Jupyter / Google Colab) a partir dos scripts, quebrando cada script em celulas nas
# marcas de secao ("# ----" / "# ===="). Assim o codigo do notebook e IDENTICO ao dos scripts.
# Uso: python codigo/construir_notebook.py   -> notebooks/P2_RECV3_passo3_base_simulada.ipynb
import json, os, re

def md(txt): return {'cell_type': 'markdown', 'metadata': {}, 'source': txt.strip('\n').splitlines(keepends=True)}
def code(txt): return {'cell_type': 'code', 'metadata': {}, 'execution_count': None, 'outputs': [], 'source': txt.strip('\n').splitlines(keepends=True)}

def quebrar(path):
    src = open(path, encoding='utf-8').read().splitlines()
    blocos, atual = [], []
    for ln in src:
        if re.match(r'^# (-{20,}|={20,})', ln) and atual and any(x.strip() and not x.startswith('#') for x in atual):
            blocos.append('\n'.join(atual)); atual = []
        atual.append(ln)
    if atual: blocos.append('\n'.join(atual))
    return blocos

C = []
C.append(md("""
# P2 — Auditoria 1 (UnB 2026.2) — PetroReconcavo S.A. (RECV3)
## Passo 3: base de dados simulada, conciliação e procedimentos de auditoria (MUS)

**Preparador:** matrícula 211059370 · **Data:** 23/10/2026 · **Revisão:** ______ (campo reservado, não preenchido)

> ⚠️ **DADOS SINTÉTICOS.** As bases geradas neste notebook **não são registros reais** da PetroReconcavo. Os únicos dados reais usados são **totais publicados** (NE 7.1 da DFP 2025, Relatório da Administração, FRE 2026 e dados abertos da CVM), indicados como "REAL" no dicionário de variáveis.

### Ferramenta utilizada (e por quê)
* **Python 3 + pandas/numpy/openpyxl**, executável no **Google Colab** (ou Anaconda/Jupyter local). O professor indicou o Colab; outras ferramentas são aceitas desde que o código seja entregue e a ferramenta explicada.
* **IA generativa:** o código foi escrito com auxílio do **Claude (Anthropic)**, a partir dos comandos do aluno; o aluno conferiu e justificou os resultados. O registro dos prompts e das conferências está em `docs/USO_DE_IA.md`.
* O notebook tem o **mesmo código** dos scripts da pasta `codigo/` (gerado por `codigo/construir_notebook.py`).

### Como foi feito ("como fez o bolo")
1. **Escolha da conta.** O imobilizado é a conta de maior materialidade: 72,2% do ativo consolidado (`planilhas/DIAG_RECV3.xlsx`, aba `Ranking_Ativo`).
2. **Dados reais.** Totais por classe e por entidade da NE 7.1, polos, produção, reservas e quadro de pessoal.
3. **SIMULAÇÃO.** Geração de 532.598 itens patrimoniais com semente fixa (211059370). Os valores foram rateados em centavos para que os totais batam com a NE 7.1.
4. **Erros inseridos.** Inserção de erros controlados, registrados num log separado que os testes não leem.
5. **Conciliação.** Base comparada com a NE 7.1 e com a CVM.
6. **Testes em 100% da população** (T01–T10).
7. **MUS (Gramling, cap. 8):** intervalo, seleção sistemática e avaliação pelo LSI.
8. **Comparação.** Só no fim o log é aberto, para comparar inseridos × detectados.
9. **Base complementar de folha e benefícios a empregados,** com testes G01–G06.

### Organização
| Seção | Conteúdo | Natureza |
|---|---|---|
| 0 | Preparação do ambiente | — |
| A + B | Dados reais (alvos) e **SIMULAÇÃO** da base do imobilizado | **SIMULAÇÃO** |
| C | Conciliação, testes, MUS e comparação | Scripts de auditoria |
| D | **SIMULAÇÃO** da base de folha + testes | **SIMULAÇÃO** + scripts |
| E | Dicionário de variáveis (gerado e conferido) | Documentação |
"""))
C.append(md("""## 0. Preparação do ambiente
No **Colab**: rode a célula abaixo depois de trocar `URL_DO_REPOSITORIO` pelo link do GitHub. Ela clona o repositório e entra na pasta. Localmente, basta abrir o notebook na raiz `P2_PetroReconcavo`."""))
C.append(code("""# Preparacao (Colab): clona o repositorio e entra na raiz do projeto. Localmente, nao faz nada.
import os, sys
URL_DO_REPOSITORIO = 'https://github.com/USUARIO/REPOSITORIO.git'   # <- trocar pelo link do repositorio
if 'google.colab' in sys.modules and not os.path.exists('codigo'):
    os.system(f'git clone {URL_DO_REPOSITORIO} repo')
    os.chdir('repo')
    os.system('pip install -q openpyxl')
if os.path.basename(os.getcwd()) == 'notebooks':
    os.chdir('..')          # executado de dentro de notebooks/: sobe para a raiz
print('pasta de trabalho:', os.getcwd())"""))
secoes = [('codigo/gerar_base_imobilizado.py', '## A + B. Dados reais (alvos) e SIMULAÇÃO da base do imobilizado\n> 🟨 **SEÇÃO DE SIMULAÇÃO**: tudo que é gerado aqui é sintético.'),
          ('codigo/testes_auditoria_base.py', '## C. Scripts de auditoria: conciliação, testes na população, MUS e comparação\n> Procedimentos **simulados para fins didáticos** (executados sobre dados sintéticos).'),
          ('codigo/gerar_base_folha.py', '## D1. SIMULAÇÃO da base complementar de folha e benefícios a empregados\n> 🟨 **SEÇÃO DE SIMULAÇÃO**'),
          ('codigo/testes_folha.py', '## D2. Testes da folha (G01–G06): fictício, duplicado, sem vínculo, maker-checker, alçada e classificação CP/LP'),
          ('codigo/gerar_dicionario.py', '## E. Dicionário de variáveis (gerado e conferido contra os arquivos)')]
for path, titulo in secoes:
    C.append(md(titulo + f'\n\nCódigo-fonte: `{path}` (o mesmo código, dividido em células).'))
    for b in quebrar(path):
        if b.strip(): C.append(code(b))
C.append(md("""## Conclusão do passo 3 (resumo, dados sintéticos)
Os números finais estão em `base_simulada/resultados/` e nas planilhas `CONC_BASE_RECV3.xlsx`, `TESTES_BASE_RECV3.xlsx` e `TESTES_FOLHA_RECV3.xlsx`. A interpretação vai nos PTs 500, 530 e 450 (passo 4). Nenhum resultado deste notebook é uma constatação sobre a PetroReconcavo real."""))
nb = {'cells': C, 'metadata': {'kernelspec': {'display_name': 'Python 3', 'language': 'python', 'name': 'python3'}, 'language_info': {'name': 'python'},
                               'colab': {'provenance': []}}, 'nbformat': 4, 'nbformat_minor': 5}
os.makedirs('notebooks', exist_ok=True)
json.dump(nb, open('notebooks/P2_RECV3_passo3_base_simulada.ipynb', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('ok notebook com', len(C), 'celulas')
