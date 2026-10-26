# -*- coding: utf-8 -*-
# PT 520 - Procedimentos analiticos (NBC TA 520 itens 5(a)-(d), 6 e 7; A16 limite de diferenca aceitavel)
# Preparador: matricula 211059370 | 24/10/2026 | Revisao: ______ (nao preenchido)
# Todos os dados sao PUBLICOS (DFP 2025 F01; dados abertos CVM F03/F04; relatorio da administracao 2025) -> REALIZADO.
# Gera planilhas/PT520_ANALITICOS_RECV3.xlsx com FORMULAS (expectativa, diferenca, limite, decisao de investigar).
# Uso: python codigo/pt520_analiticos.py
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Border, Side, Alignment
from openpyxl.utils import get_column_letter

ME = 20475                      # PT 320 (R$ mil)
LIM_RS = 0.5                    # limite de diferenca aceitavel para risco significativo (receita, R03) = 50% da ME (julgamento, A16)
H = PatternFill('solid', fgColor='1F4E78'); thin = Side(style='thin', color='BFBFBF'); BD = Border(top=thin, bottom=thin, left=thin, right=thin)
NUM = '#,##0;(#,##0);-'; PCT = '0.0%'; NUM2 = '#,##0.00'
TOPO = 'PetroReconcavo S.A. - consolidado - R$ mil | Preparador: matricula 211059370 | 24/10/2026 | Revisao: ______ (nao preenchido) | REALIZADO COM EVIDENCIA PUBLICA'
wb = Workbook()
def sheet(nome, titulo, larg):
    ws = wb.create_sheet(nome) if wb.active.title != 'Sheet' else wb.active
    if ws.title == 'Sheet': ws.title = nome
    ws['A1'] = titulo; ws['A1'].font = Font(bold=True, size=13); ws['A2'] = TOPO
    for j, w in enumerate(larg, 1): ws.column_dimensions[get_column_letter(j)].width = w
    return ws
def cab(ws, r, cols):
    for j, c in enumerate(cols, 1):
        x = ws.cell(row=r, column=j, value=c); x.font = Font(bold=True, color='FFFFFF'); x.fill = H; x.border = BD; x.alignment = Alignment(wrap_text=True)
def lin(ws, r, vals, nfs=None):
    for j, v in enumerate(vals, 1):
        x = ws.cell(row=r, column=j, value=v); x.border = BD
        if nfs and j in nfs: x.number_format = nfs[j]

# ---------- Aba 1: receita - procedimento analitico SUBSTANTIVO (item 5) ----------
ws = sheet('Receita_item5', 'Analitico substantivo da receita bruta (NBC TA 520 item 5) - modelo volume x preco x cambio', [62, 16, 16, 70])
cab(ws, 4, ['Dado (item 5(b): fontes independentes / externas quando possivel)', 'Valor', '', 'Fonte'])
d = [('Venda de petroleo 2024 (R$ mil)', 2440303, 'NE 18.1 consolidado (F01)'),
     ('Venda de petroleo 2025 registrada (R$ mil)', 2113133, 'NE 18.1 consolidado (F01)'),
     ('Variacao da producao de petroleo 2025 x 2024', 0.02, 'RA 2025 (F01): "aumento de 2% na producao de petroleo"'),
     ('Preco medio de realizacao do petroleo 2024 (US$/bbl)', 73.57, 'RA 2024 (F07)'),
     ('Preco medio de realizacao do petroleo 2025 (US$/bbl)', 60.43, 'RA 2025 (F01)'),
     ('Dolar medio 2025 (R$)', 5.59, 'RA 2025 (F01)'),
     ('Variacao do dolar medio 2025 x 2024', 0.04, 'RA 2025 (F01): "aumento de 4% versus ano anterior"'),
     ('Venda de gas e subprodutos 2024 (R$ mil)', 1480337, 'NE 18.1'),
     ('Venda de gas e subprodutos 2025 registrada (R$ mil)', 1554086, 'NE 18.1'),
     ('Variacao do preco medio de realizacao do gas', 0.04, 'RA 2025: "precos medios de realizacao 4% maiores"'),
     ('Variacao do volume total de gas entregue', 0.01, 'RA 2025: "crescimento de 1% no volume total entregue"'),
     ('Materialidade para execucao (ME)', ME, 'PT 320'),
     ('% da ME como limite de diferenca aceitavel (risco significativo R03)', LIM_RS, 'Julgamento - A16 (maior seguranca desejada -> limite menor)')]
for i, (a, b, c) in enumerate(d, 5): lin(ws, i, [a, b, '', c], {2: (PCT if isinstance(b, float) and b < 1 else (NUM2 if isinstance(b, float) else NUM))})
# B5 oleo24 B6 oleo25 B7 dprod B8 p24 B9 p25 B10 usd25 B11 dusd B12 gas24 B13 gas25 B14 dpg B15 dvg B16 ME B17 pct
cab(ws, 19, ['Expectativa (item 5(c)) e comparacao', 'Valor', '', 'Formula / leitura'])
lin(ws, 20, ['Expectativa de venda de petroleo 2025', '=B5*(1+B7)*(B9/B8)*(1+B11)', '', 'Base 2024 x volume x preco US$ x cambio'], {2: NUM})
lin(ws, 21, ['Diferenca registrado - esperado (petroleo)', '=B6-B20', '', ''], {2: NUM})
lin(ws, 22, ['Expectativa de venda de gas 2025', '=B12*(1+B14)*(1+B15)', '', 'Base 2024 x preco x volume'], {2: NUM})
lin(ws, 23, ['Diferenca registrado - esperado (gas)', '=B13-B22', '', ''], {2: NUM})
lin(ws, 24, ['Limite de diferenca aceitavel (item 5(d))', '=B16*B17', '', 'Sem investigacao adicional se |diferenca| <= limite'], {2: NUM})
lin(ws, 25, ['Petroleo: investigar? (item 7)', '=IF(ABS(B21)>B24,"INVESTIGAR","Dentro do limite")', '', ''])
lin(ws, 26, ['Gas: investigar? (item 7)', '=IF(ABS(B23)>B24,"INVESTIGAR","Dentro do limite")', '', ''])
ws['A28'] = 'Adequacao (item 5(a)): relacao previsivel volume x preco para commodity; R03 e risco significativo -> o analitico NAO basta sozinho (NBC TA 330 item 21): exige tambem teste de detalhes (corte, confirmacao - PT 330/505).'
ws['A29'] = 'Confiabilidade dos dados (item 5(b)): precos e volumes do RA (informacao da entidade, consistente com dados operacionais mensais publicados - CM 08/01/2026); Brent e cambio verificaveis em fontes externas.'

# ---------- Aba 2: razoabilidade de custos (procedimentos analiticos de avaliacao de risco / item 6) ----------
w2 = sheet('Custos_NE19', 'Gastos por natureza (NE 19) - variacoes e expectativas', [44, 14, 14, 12, 14, 14, 62])
cab(w2, 4, ['Natureza (consolidado)', '2025', '2024', 'Var. %', 'Var. R$', 'Investigar? (|var| > ME)', 'Expectativa / explicacao a obter'])
cs = [('Pessoal', 284002, 274271, 'Reajuste ~ inflacao + quadro: esperado +3% a +6%'),
      ('Servicos e materiais', 720753, 553842, 'Crescimento acima da producao (+1%): ver JOA UPGN (custos da operacao) e possivel workover lancado no resultado'),
      ('Eletricidade', 71792, 72093, 'Estavel - coerente'),
      ('Vendas', 0, 3940, 'Linha sem saldo em 2025'),
      ('Outras', 10430, 73920, 'Queda de 86%: obter composicao de 2024 (itens nao recorrentes?)'),
      ('Compra/"Swap" de gas', 104707, 61951, 'Coerente com "maior compra de gas de terceiros" (RA)'),
      ('Escoamento de gas', 11408, 18713, 'Queda com nova infraestrutura propria?'),
      ('Processamento de gas', 189748, 219741, 'Queda com volume de gas +1%: hipotese = compra de 50% da UPGN em 30/09/2025 (tarifa paga a si mesma eliminada)'),
      ('Transporte de gas', 94419, 118405, 'Queda de 20%: verificar contratos'),
      ('Royalties (inclui proprietarios de terra)', 227694, 224642, 'Ver aba Royalties'),
      ('Depreciacao, amortizacao e deplecao', 721077, 694816, 'Ver aba DDA_boe')]
for i, (n, a, b, e) in enumerate(cs, 5):
    lin(w2, i, [n, a, b, f'=B{i}/C{i}-1', f'=B{i}-C{i}', f'=IF(ABS(E{i})>{ME},"SIM","nao")', e], {2: NUM, 3: NUM, 4: PCT, 5: NUM})
r = 5 + len(cs); lin(w2, r, ['Total', f'=SUM(B5:B{r-1})', f'=SUM(C5:C{r-1})', f'=B{r}/C{r}-1', f'=B{r}-C{r}', '', 'NE 19: 2.436.030 / 2.316.334'], {2: NUM, 3: NUM, 4: PCT, 5: NUM})

# ---------- Aba 3: royalties ----------
w3 = sheet('Royalties', 'Razoabilidade dos royalties (NE 17.1: 7,5% a 10% da producao bruta)', [66, 16, 70])
cab(w3, 4, ['Item', 'Valor', 'Fonte / leitura'])
rr = [('Royalties 2025 (sem proprietarios de terra)', 198434, 'NE 17.1'), ('Venda bruta de petroleo + gas 2025', '=Receita_item5!B6+Receita_item5!B13', 'NE 18.1'),
      ('Royalties / venda bruta', '=B5/B6', 'Proxy da aliquota efetiva'), ('Aliquota minima divulgada', 0.075, 'NE 17.1'),
      ('Royalties esperados a 7,5% sobre a venda bruta', '=B6*B8', 'Expectativa simples'), ('Diferenca registrada - esperada', '=B5-B9', ''),
      ('Investigar? (|dif| > ME)', f'=IF(ABS(B10)>{ME},"INVESTIGAR","Dentro do limite")', 'Item 7 da NBC TA 520')]
for i, (a, b, c) in enumerate(rr, 5): lin(w3, i, [a, b, c], {2: (PCT if i in (7, 8) else NUM)})
w3['A13'] = 'Explicacoes a corroborar (item 7(a)-(b)): (i) base de calculo = preco de referencia ANP x volume produzido, nao a receita de venda; (ii) parte do gas vendido e comprado de terceiros (sem royalty proprio);'
w3['A14'] = '(iii) reducao de royalties sobre producao incremental de campos maduros concedida pela ANP; (iv) receita de subprodutos processados (GLP, C5+) com valor agregado fora da base. Sem corroboracao, a diferenca permanece aberta (PT 250 - L2).'

# ---------- Aba 4: DD&A por boe ----------
w4 = sheet('DDA_boe', 'DD&A por boe produzido (coerencia com o metodo de unidades produzidas)', [60, 16, 16, 60])
cab(w4, 4, ['Item', '2025', '2024', 'Fonte'])
lin(w4, 5, ['Producao media (mil boe/dia)', 26.5, '=26.5/1.007', 'RA 2025: 26,5 mil boe/dia, +0,7% (CM 08/01/2026)'], {2: '0.00', 3: '0.00'})
lin(w4, 6, ['Producao anual (MMboe)', '=B5*365/1000', '=C5*366/1000', '2024 bissexto'], {2: '0.000', 3: '0.000'})
lin(w4, 7, ['DD&A (R$ mil)', 721077, 694816, 'NE 19'], {2: NUM, 3: NUM})
lin(w4, 8, ['DD&A por boe (R$)', '=B7/B6/1000', '=C7/C6/1000', ''], {2: NUM2, 3: NUM2})
lin(w4, 9, ['Variacao', '=B8/C8-1', '', 'Esperado: proximo de zero +/- capex adicionado a base depreciavel'], {2: PCT})
lin(w4, 10, ['Leitura', '=IF(ABS(B9)<=0.1,"Coerente","Investigar")', '', ''])

# ---------- Aba 5: balanco e indicadores ----------
w5 = sheet('Balanco_indicadores', 'Variacoes do balanco e indicadores (avaliacao de risco e item 6)', [54, 16, 16, 12, 16, 60])
cab(w5, 4, ['Item', '2025', '2024', 'Var. %', 'Investigar?', 'Leitura'])
bp = [('Contas a receber de clientes CP', 253967, 361095, 'Queda de 30% com receita -3%: ver prazo medio'),
      ('Contas a receber de clientes LP', 65231, 58145, 'Inclui creditos de gas em disputa (NE 5.1: 55.917)'),
      ('Imobilizado', 6170841, 5540758, 'Capex 1,64 bi incluindo UPGN; conciliado (PT 530)'),
      ('Aplicacoes financeiras (CP + LP)', 1400532, 777903, '3a e 4a emissoes de debentures'),
      ('Debentures (CP + LP)', 3105016, 1792321, '3a e 4a emissoes (R$ 1,25 bi)'),
      ('Juros sobre debentures (resultado)', 281098, 84840, 'Crescimento de 231% contra divida media +73%: obter abertura (IPCA, custos de emissao, swaps)'),
      ('Valor a pagar por aquisicoes (CP)', 18515, 213077, 'Pagamento das parcelas da UPGN; equivalencia em US$ divergente (PT 450 D-I4)'),
      ('Fornecedores LP', 130476, 130476, 'Saldo IDENTICO nos dois anos: obter natureza (disputa?)')]
for i, (n, a, b, e) in enumerate(bp, 5):
    lin(w5, i, [n, a, b, f'=B{i}/C{i}-1', f'=IF(ABS(B{i}-C{i})>{ME},"SIM","nao")', e], {2: NUM, 3: NUM, 4: PCT})
r = 5 + len(bp) + 1
cab(w5, r, ['Indicador', '2025', '2024', 'Var.', '', 'Leitura'])
lin(w5, r + 1, ['Prazo medio de recebimento (dias) = CR CP / receita bruta x 365', '=B5/3709684*365', '=C5/3836743*365', f'=B{r+1}-C{r+1}', '', 'Reducao de ~9 dias: corte de dezembro (producao -0,7% em dez.; Brent -8% no 4T) ou antecipacao?'], {2: '0.0', 3: '0.0', 4: '0.0'})
lin(w5, r + 2, ['Taxa efetiva aparente das debentures = juros / saldo medio', '=B10/((B9+C9)/2)', '', '', '', 'Comparar com IPCA + ~7% e CDI + spread das emissoes'], {2: PCT})
lin(w5, r + 3, ['Margem bruta = resultado bruto / receita liquida', '=1021436/3157609', '=1191749/3264554', f'=B{r+3}-C{r+3}', '', 'Queda coerente com Brent -14%'], {2: PCT, 3: PCT, 4: PCT})

# ---------- Aba 6: item 6 - analitico global perto do fim ----------
w6 = sheet('Item6_conclusao_global', 'Procedimentos analiticos proximo ao final (item 6) - coerencia global com o entendimento', [60, 90])
cab(w6, 4, ['Area', 'Conclusao'])
c6 = [('Receita', 'Gas: diferenca de -0,9 mi, dentro do limite. Petroleo: diferenca de -13,2 mi (-0,6%) ACIMA do limite de 10,2 mi; os insumos do modelo sao percentuais arredondados do RA (precisao de +/-0,5 p.p. cada), logo a expectativa NAO e precisa o bastante (item 5(c)) -> refazer desagregada por mes e por ativo (Bahia x Potiguar) com volumes e precos exatos e corroborar com teste de detalhes (PT 330 P03).'),
      ('Custos', 'Servicos e materiais (+30%) e outras (-86%) exigem abertura; processamento de gas em queda coerente com a compra da UPGN (hipotese).'),
      ('Royalties', 'Aliquota aparente abaixo da minima divulgada: diferenca acima da ME sem corroboracao -> procedimento adicional (item 7).'),
      ('Imobilizado/DD&A', 'DD&A por boe coerente; imobilizado conciliado com a NE 7.1; transferencias que nao zeram (PT 500 I4) pendentes.'),
      ('Financeiro', 'Juros das debentures crescem mais que a divida: obter abertura; resultado de swaps +352 mi explica o lucro liquido.'),
      ('Conclusao (item 6)', 'As DFs sao, em geral, consistentes com o entendimento da entidade, EXCETO pelos pontos acima marcados para investigacao, que alimentam o PT 330 e o PT 450.')]
for i, (a, b) in enumerate(c6, 5): lin(w6, i, [a, b])
wb.save('planilhas/PT520_ANALITICOS_RECV3.xlsx'); print('ok PT520 xlsx')
