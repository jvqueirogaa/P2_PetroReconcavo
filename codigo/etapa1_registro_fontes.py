# -*- coding: utf-8 -*-
"""
Etapa 1 - Registro de fontes publicas (P2 Auditoria 1 - UnB 2026.2)
Preparador: matricula 211059370 | Companhia: PetroReconcavo S.A. (RECV3)
Gera planilhas/REG_FONTES_RECV3.xlsx com: registro de fontes (URL, acesso, doc,
paginas, exercicio, hash SHA-256), identificacao da companhia, conciliacao
preliminar PDF x dados abertos CVM e pendencias.
Uso: python codigo/etapa1_registro_fontes.py   (executar na raiz P2_PetroReconcavo)
"""
import hashlib, os, csv, subprocess
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

ACESSO = "22/10/2026"
RI = "https://ri.petroreconcavo.com.br/Download.aspx?Arquivo="
F = "fontes/originais/"

# (id, origem, documento, exercicio/data-base, publicacao, url, arquivo, paginas, uso/PTs, obs)
FONTES = [
 ("F01","RI (espelho do documento CVM)","Demonstracoes Financeiras 2025 (DFP) - Relatorio da Administracao, declaracoes, relatorio do Comite de Auditoria, relatorio do auditor (EY), DFs individuais e consolidadas e NEs 1 a 25","2025 (comparativo 2024)","18/03/2026",RI+"uXlsREfF5W0EAwolNEO+XA==",F+"RECV3_DFP2025_DF_4T25.pdf",
  "RA p.4-30; Decl. diretores p.31-35; Comite Aud. p.38-42; Relatorio auditor p.44-50 (PAA ARO p.46; Outros assuntos - valores correspondentes p.47; assinatura p.50); BP p.51; DRE p.52; DRA p.53; DMPL p.54; DFC p.55; DVA p.56; NE1-2 p.57; NE3 p.60 (3.3 ARO p.61); NE4 p.63; NE5 p.64; NE6-7 p.65-70; NE8-9 p.71-75 (covenants p.75); NE10 p.76; NE11 p.79; NE12 p.80; NE13 p.82; NE14 p.83; NE15 p.86; NE16 p.90; NE17 p.91; NE18 p.92; NE19 p.93; NE20-21 p.94; NE22 p.100; NE23-25 p.101",
  "Base de todos os PTs (EC a 600); base simulada (NE7)","Paginas = paginacao do PDF (nao a paginacao impressa). Auditor: Ernst & Young Auditores Independentes S/S Ltda., CRC SP-015199/O; socio Daniel de Araujo Peixoto, CRC BA-025348/O; Salvador, 18/03/2026; opiniao sem modificacao; PAA unico: provisao para abandono de pocos (R$ 145.192 mil)."),
 ("F02","CVM - RAD/ENET","DFP 31/12/2025 - versao 1 (ID_DOC 155475), recebida em 18/03/2026","2025","18/03/2026","http://www.rad.cvm.gov.br/ENETCONSULTA/frmDownloadDocumento.aspx?CodigoInstituicao=1&NumeroSequencialDocumento=155475","fontes/cvm_dados_abertos/RECV3_dfp_cia_aberta_2025.csv","n/a (registro do documento)","PT 500 (fonte primaria regulatoria); PT 230","Link obtido no indice dfp_cia_aberta_2025.csv dos dados abertos da CVM."),
 ("F03","CVM - Dados Abertos","Dados estruturados DFP 2025 (BPA, BPP, DRE, DRA, DMPL, DFC-MI, DVA; ind. e con.) filtrados por CD_CVM 025780","2025 e 2024","arquivo atualizado em 18/10/2026","https://dados.cvm.gov.br/dados/CIA_ABERTA/DOC/DFP/DADOS/dfp_cia_aberta_2025.zip","fontes/cvm_dados_abertos/_brutos/CVM_dfp_cia_aberta_2025.zip","n/a (tabular)","PT 500 (conciliacao PDF x CVM); PT 520 (analiticos); PT 320","Filtro reproduzivel no codigo; zip original preservado."),
 ("F04","CVM - Dados Abertos","Dados estruturados DFP 2024 (versoes 1 e 2, ID_DOC 145557 e 145562)","2024 e 2023","arquivo atualizado em 18/10/2026","https://dados.cvm.gov.br/dados/CIA_ABERTA/DOC/DFP/DADOS/dfp_cia_aberta_2024.zip","fontes/cvm_dados_abertos/_brutos/CVM_dfp_cia_aberta_2024.zip","n/a (tabular)","PT 510 (saldos iniciais); PT 520","DFP 2024 reapresentada no mesmo dia (versao 2) - avaliar motivo no PT 510."),
 ("F05","CVM - Dados Abertos","Cadastro de companhias abertas (cad_cia_aberta.csv) - registro da PetroReconcavo","situacao em 22/10/2026","arquivo atualizado em 22/10/2026","https://dados.cvm.gov.br/dados/CIA_ABERTA/CAD/DADOS/cad_cia_aberta.csv","fontes/cvm_dados_abertos/RECV3_cad_cia_aberta.csv","n/a (tabular)","Identificacao; PT EC; PT 210","CD_CVM 25780; Categoria A; registro CVM 30/04/2021; constituicao 21/07/1999; situacao ATIVO; denominacao social PETRORECONCAVO S.A. (sem registro de denominacao anterior no cadastro)."),
 ("F06","B3 - Listados","Ficha da companhia (API publica Empresas Listadas - GetDetail codeCVM 25780)","situacao em 21/10/2026","n/a",
  "https://sistemaswebb3-listados.b3.com.br/listedCompaniesProxy/CompanyCall/GetDetail/eyJjb2RlQ1ZNIjoiMjU3ODAiLCJsYW5ndWFnZSI6InB0LWJyIn0=","fontes/b3/B3_GetDetail_RECV_25780_acesso_2026-10-22.json","n/a (JSON)","Identificacao; PT 250 (Novo Mercado); PT 315","Segmento NOVO MERCADO; codigo unico RECV3 (ISIN BRRECVACNOR3); inicio de cotacao 05/05/2021; escriturador Itau."),
 ("F07","RI (espelho do documento CVM)","Demonstracoes Financeiras 2024 (DF 4T24) - inclui relatorio do auditor anterior (Deloitte)","2024 (comparativo 2023)","19/03/2025",RI+"JwXPUOtd5ZECodkfTV4TrQ==",F+"RECV3_DF_4T24.pdf",
  "Comite de Auditoria (substituicao Deloitte -> EY) p.37; relatorio do auditor p.42-45 (assinatura p.45); BP p.46; NE7 p.63",
  "PT 510 (saldos iniciais / auditor anterior); PT 520; PT 200 (independencia/rodizio)","Auditor 2024: Deloitte Touche Tohmatsu Auditores Independentes Ltda., CRC 2SP011609/O-8 F BA; Marcelo de Figueiredo Seixas, CRC 1PR045179/O-9; 19/03/2025; opiniao sem modificacao; PAA: reconhecimento de receita de venda de petroleo, gas e subprodutos."),
 ("F08","RI","Release de resultados 4T25 e 2025","2025","18/03/2026",RI+"6mYV+T95PqHeU+9kSEJfwg==",F+"RECV3_Release_4T25.pdf","a referenciar por PT (28 p.)","PT 315; PT 520 (dados operacionais: producao, preco, lifting cost)","Informacao nao auditada (gerencial)."),
 ("F09","RI (espelho CVM - ITR)","Informacoes Trimestrais 1T26 (com relatorio de revisao)","1T26 (31/03/2026)","mai/2026",RI+"DBmAmh0RbkL27/eBIRLh/g==",F+"RECV3_ITR_1T26.pdf","a referenciar (38 p.)","PT 560 (eventos subsequentes); PT 570","Posterior ao encerramento - revisao, nao auditoria."),
 ("F10","RI (espelho CVM - ITR)","Informacoes Trimestrais 2T26 (com relatorio de revisao)","2T26 (30/06/2026)","ago/2026",RI+"+ngsiaFkjuI6qhdMTmMn0g==",F+"RECV3_ITR_2T26.pdf","a referenciar (40 p.)","PT 560; PT 570","ITR 3T26 ainda nao publicado na data de acesso (periodo de silencio comunicado em 16/10/2026)."),
 ("F11","RI","Release de resultados 2T26","2T26","ago/2026",RI+"8vUBMWgMtf60nTL/r3ekcQ==",F+"RECV3_Release_2T26.pdf","a referenciar (21 p.)","PT 560; PT 570","Informacao nao auditada."),
 ("F12","RI (espelho CVM - FRE)","Formulario de Referencia 2025 - versao 11 (data no RI: 11/05/2026)","2025","11/05/2026",RI+"oPPkqtv8pKtsSV3xh0P+XQ==&IdCanal=EW7a94Xws5oTPwg03xyeFg==",F+"RECV3_FRE_2025_v2026-05-11.pdf",
  "1.1 Historico p.5-8; 2.1 Comentarios dos diretores p.92+; 4.1 Fatores de risco p.127+; 5.1 Gerenciamento de riscos p.193+; 5.2 Controles internos p.202-203; 6.5 Organograma p.216; 7.1 Administracao p.218-221; 9.1/9.2 Auditores p.305; 11.1 Regras PR p.318-320; 11.2 Transacoes PR p.321+; 12.1 Capital p.328",
  "PT 315; PT 240; PT 250; PT 260; PT 265; PT 550; PT 200/220 (honorarios e independencia)","Paginas = paginacao do PDF. Deloitte (cod. CVM 003859) contratada 01/10/2018 - servicos a partir de 01/01/2019; EY (cod. CVM 004715) contratada 10/02/2025 - servicos a partir de 01/01/2025."),
 ("F13","RI (espelho CVM - FRE)","Formulario de Referencia 2026 - versao 7 (data no RI: 28/09/2026)","2026","28/09/2026",RI+"aQdz7+zP4ReTZpwynaC0aQ==&IdCanal=EW7a94Xws5oTPwg03xyeFg==",F+"RECV3_FRE_2026_v2026-09-28.pdf",
  "1.1 Historico p.5-8; 4.1 Fatores de risco p.123+; 9.1/9.2 Auditores p.283; 11.2 Transacoes PR p.297-298",
  "Historico societario (nomes/incorporacoes); PT 550; PT 560","Versao mais recente na data de acesso."),
 ("F14","RI","Certificacao de reservas - data-base 31/12/2025 (Netherland, Sewell & Associates - NSAI)","31/12/2025","18/03/2026",RI+"emem/uzuhjQGwAdaSDA28A==&IdCanal=JH9AbY1f6b5691gLtD0/0Q==",F+"RECV3_Certificacao_Reservas_dez2025.pdf","carta/assinatura p.6; tabelas a referenciar (47 p.)","PT 540 (reservas -> deplecao UoP e ARO); PT 315; PT 500 (trabalho de especialista da administracao)","Relatorio de especialista externo; a ser avaliado como evidencia (relevancia/confiabilidade)."),
 ("F15","RI","NSAI - tabelas por ativo e total (planilha .xlsx; servida pelo RI como application/octet-stream)","31/12/2025","18/03/2026",RI+"kY3PiHiQFrxjWpZvdsAnYQ==&IdCanal=JH9AbY1f6b5691gLtD0/0Q==",F+"RECV3_NSAI_Tabelas.xlsx","abas a referenciar","PT 540; base simulada (parametros por polo/campo)","Arquivo renomeado de .pdf para .xlsx (assinatura PK/Excel 2007+)."),
 ("F16","RI (espelho CVM - Fato Relevante)","Fato Relevante - Certificacao de Reservas 2025","31/12/2025","18/03/2026",RI+"LHqYL4fJko54n4OoIj1p7Q==&IdCanal=ckeQVNzVtM/ZZ4T5tqRLLw==",F+"FR_2026-03-18_Certificacao_Reservas_2025.pdf","p.1-2","PT 540; PT 560",""),
 ("F17","RI (espelho CVM - Fato Relevante)","Fato Relevante - Reestruturacao organizacional da Diretoria Estatutaria","2026","20/02/2026",RI+"cduTGiux/Ls/UgRqChiVrA==&IdCanal=ckeQVNzVtM/ZZ4T5tqRLLw==",F+"FR_2026-02-20_Reestruturacao_Diretoria.pdf","p.1-2","PT 560; PT 315 (ambiente de controle)",""),
 ("F18","RI (espelho CVM - Fato Relevante)","Fato Relevante - Alteracoes na composicao do CA e do Comite de Pessoas e ESG","2026","02/03/2026",RI+"TJvTFP/GpwnhVVkzBzgbmQ==&IdCanal=ckeQVNzVtM/ZZ4T5tqRLLw==",F+"FR_2026-03-02_Alteracoes_Conselho.pdf","p.1-2","PT 260; PT 560",""),
 ("F19","RI (espelho CVM - Fato Relevante)","Fato Relevante - 4o Programa de Recompra de Acoes","2026","05/05/2026",RI+"nKft2JHS5ES6JsuSIqT/AQ==&IdCanal=ckeQVNzVtM/ZZ4T5tqRLLw==",F+"FR_2026-05-05_Recompra_Acoes.pdf","p.1-2","PT 560",""),
 ("F20","RI (espelho CVM - Fato Relevante)","Fato Relevante - Distribuicao de JCP (mai/2026)","2026","07/05/2026",RI+"tlX3320tjZeBAemxPviXbg==&IdCanal=ckeQVNzVtM/ZZ4T5tqRLLw==",F+"FR_2026-05-07_JCP.pdf","p.1-2","PT 560; PT 570",""),
 ("F21","RI (espelho CVM - Fato Relevante)","Fato Relevante - Distribuicao de JCP (ago/2026)","2026","06/08/2026",RI+"WreKKYArpPM8zQu1BGWUFw==&IdCanal=ckeQVNzVtM/ZZ4T5tqRLLw==",F+"FR_2026-08-06_JCP.pdf","p.1-2","PT 560",""),
 ("F22","RI (espelho CVM - Fato Relevante)","Fato Relevante - Processo de sucessao de Diretor Estatutario","2026","24/09/2026",RI+"VCa/qCWpCSSsIsgDU4PT3g==&IdCanal=ckeQVNzVtM/ZZ4T5tqRLLw==",F+"FR_2026-09-24_Sucessao_Diretor.pdf","p.1-2","PT 560; PT 260",""),
 ("F23","RI (espelho CVM - Comunicado)","Comunicado - Contratacao de swaps para a 2a serie da 4a emissao de debentures","2026","12/01/2026",RI+"asYvcV8SNmUnxWbeHrYo0Q==&IdCanal=ckeQVNzVtM/ZZ4T5tqRLLw==",F+"CM_2026-01-12_Swaps_4aEmissao.pdf","p.1-2","PT 560; PT 540 (derivativos); PT 570",""),
 ("F24","RI (espelho CVM - Comunicado)","Comunicado - Declaracao de aquisicao de participacao acionaria relevante","2026","16/01/2026",RI+"2QlRp7l2lKP0asBpmMFACw==&IdCanal=ckeQVNzVtM/ZZ4T5tqRLLw==",F+"CM_2026-01-16_Participacao_Relevante.pdf","p.1-3","PT 550 (estrutura acionaria); PT 560",""),
 ("F25","RI (espelho CVM - Comunicado)","Comunicado - Aditivos aos contratos de venda de petroleo com a Brava Energia","2026","07/05/2026",RI+"W1NWQbfWosHIwLs36hqMow==&IdCanal=ckeQVNzVtM/ZZ4T5tqRLLw==",F+"CM_2026-05-07_Aditivos_Brava.pdf","p.1-2","PT 240/315 (receita); PT 560",""),
 ("F26","RI (espelho CVM - Comunicado)","Comunicado - Contrato de venda de petroleo de longo prazo com a Brava Energia","2026","06/08/2026",RI+"gV4n6IxnHwTn4/SeVb4Jpw==&IdCanal=ckeQVNzVtM/ZZ4T5tqRLLw==",F+"CM_2026-08-06_Contrato_Brava_LP.pdf","p.1-2","PT 560; PT 570",""),
 ("F27","RI (espelho CVM - Comunicado)","Comunicado - Contratacao de longo prazo com Petrobras para processamento de gas na UTG Catu","2026","19/08/2026",RI+"a4WPrqPkkrLTgvYJh9XnHw==&IdCanal=ckeQVNzVtM/ZZ4T5tqRLLw==",F+"CM_2026-08-19_Petrobras_UTG_Catu.pdf","p.1-2","PT 560; PT 402 (servico de terceiro)",""),
 ("F28","RI (espelho CVM - Comunicado)","Comunicado - Aquisicao de blocos exploratorios em leilao da ANP","2026","07/10/2026",RI+"nm+cMiD1OdCzJUXGE43NbA==&IdCanal=ckeQVNzVtM/ZZ4T5tqRLLw==",F+"CM_2026-10-07_Blocos_ANP.pdf","p.1-2","PT 560; PT 250 (ANP)","Evento mais recente pesquisado."),
 ("F29","RI (espelho CVM - Comunicado)","Comunicado - Dados operacionais dezembro/2025","2025","08/01/2026",RI+"+G/jPefhCHfeWqsXwAQpbw==&IdCanal=ckeQVNzVtM/ZZ4T5tqRLLw==",F+"CM_2026-01-08_Dados_Operacionais_Dez2025.pdf","p.1-2","PT 520 (producao mensal)","Informacao nao auditada."),
 ("F30","RI (espelho CVM - Aviso aos Acionistas)","Aviso aos Acionistas - Aumento de capital por subscricao privada deliberado em RCA","2026","02/06/2026",RI+"hGdtLfiE9gE+UChfK0/tZw==&IdCanal=ckeQVNzVtM/ZZ4T5tqRLLw==",F+"AV_2026-06-02_Aumento_Capital.pdf","p.1-4","PT 560",""),
 ("F31","RI","Relatorio anual do Agente Fiduciario - 1a emissao de debentures","2025","30/04/2026",RI+"xGj6EJ3bkfjxS2eYwdyetg==&IdCanal=IZpef0cJIEQ7tpP+nNe5QQ==",F+"DEB_1aEmissao_RAF_2026-04-30.pdf","covenants a referenciar","PT 570 (covenants); PT 505 (fonte externa independente)","Escrituras nao disponibilizadas no RI - buscar na CVM/agente fiduciario se necessario."),
 ("F32","RI","Relatorio anual do Agente Fiduciario - 2a emissao de debentures","2025","01/05/2026",RI+"YID0Abyjn/WmywHI6qllwA==&IdCanal=IZpef0cJIEQ7tpP+nNe5QQ==",F+"DEB_2aEmissao_RAF_2026-05-01.pdf","covenants a referenciar","PT 570; PT 505",""),
 ("F33","RI","Relatorio anual do Agente Fiduciario - 3a emissao de debentures","2025","01/05/2026",RI+"XURZ6b0mXZzCP+54iasSbg==&IdCanal=IZpef0cJIEQ7tpP+nNe5QQ==",F+"DEB_3aEmissao_RAF_2026-05-01.pdf","covenants a referenciar","PT 570; PT 505",""),
 ("F34","RI","Relatorio anual do Agente Fiduciario - 4a emissao de debentures","2025","01/05/2026",RI+"72pxrqwKCe5JZZjmGNAaaQ==&IdCanal=IZpef0cJIEQ7tpP+nNe5QQ==",F+"DEB_4aEmissao_RAF_2026-05-01.pdf","covenants a referenciar","PT 570; PT 505",""),
 ("F35","RI (espelho CVM - Ata)","Ata da AGOE de 24/04/2026 (aprovacao das contas de 2025)","2025","24/04/2026",RI+"Em2YaYbBK+DFG1hf4vGo0Q==&IdCanal=cFFw6GnZKdIiBX64dUfpDA==",F+"AGOE_2026-04-24_Ata.pdf","a referenciar","PT 560; PT 260; PT 580",""),
 ("F36","RI (espelho CVM)","Proposta da Administracao - AGOE 2026","2025","15/04/2026",RI+"e0radgJeTR8MzYHA2oS9ig==&IdCanal=cFFw6GnZKdIiBX64dUfpDA==",F+"AGOE_2026_Proposta_Administracao.pdf","a referenciar","PT 560; PT 550 (remuneracao da administracao)",""),
 ("F37","RI (espelho CVM - Ata)","Ata de RCA de 17/03/2026","2026","24/03/2026",RI+"BjLAnj5yLzi/xNZtJIS8Tg==&IdCanal=cFFw6GnZKdIiBX64dUfpDA==",F+"RCA_2026-03-17_Ata.pdf","a referenciar","PT 260; PT 560","Provavel aprovacao das DFs 2025 - confirmar."),
 ("F38","RI (espelho CVM - Ata)","Ata de RCA de 24/02/2026","2026","05/03/2026",RI+"hnmL3/4jjyFKkAiAOHx1SA==&IdCanal=cFFw6GnZKdIiBX64dUfpDA==",F+"RCA_2026-02-24_Ata.pdf","a referenciar","PT 260; PT 560",""),
 ("F39","CFC (material da disciplina)","Consolidado das NBC TA (Estrutura Conceitual e NBC TA 200 a 810) - arquivo disponibilizado na pasta da disciplina","versoes vigentes para 2025 (a confirmar no site do CFC)","n/a","https://cfc.org.br/tecnica/normas-brasileiras-de-contabilidade-nbc/","../Consolidado Normas Aud1.pdf","indice p.1-2 (1.479 p.)","Todos os PTs (norma e itens)","Versoes no consolidado: EC; 200(R1); 210(R1); 220(R3); 230(R1); 240(R1); 250; 260(R2); 265; 300(R1); 315(R2); 320(R1); 330(R1); 402; 450(R1); 500(R1); 501; 505; 510; 520; 530; 540(R2); 550; 560(R1); 570; 580(R1); 600(R2)."),
]

IDENT = [
 ("Denominacao social (CVM/B3)","PETRORECONCAVO S.A. (grafia nas DFs: PetroReconcavo S.A.)","F05; F06; F01 p.57"),
 ("CNPJ","03.342.704/0001-30","F05; F06"),
 ("Codigo CVM","25780 (Categoria A; registro em 30/04/2021)","F05"),
 ("Codigo de negociacao / ISIN","RECV3 / BRRECVACNOR3 - codigo unico desde o inicio da cotacao (05/05/2021)","F06; F12 1.1"),
 ("Segmento de listagem","Novo Mercado (B3)","F06; F12 1.1"),
 ("Sede","Mata de Sao Joao - BA (Estrada do Vinte Mil, km 3,5, Estacao de Sao Roque)","F05; F01 p.57"),
 ("Constituicao / inicio da operacao","21/07/1999 / fevereiro de 2000 (Contrato de Producao com a Petrobras)","F05; F12 1.1"),
 ("Atividade","Operacao e producao de campos maduros onshore de petroleo e gas (BA, SE e RN); 58 concessoes, 14 em consorcio","F01 NE1 p.57"),
 ("Controle acionario","Sem acionista ou grupo controlador (controle difuso)","F01 NE1 p.57; F05"),
 ("Grupo (consolidacao)","Controladora + SPE Tieta Ltda. (100%; campos de Tie e Tartaruga). Ex-Maha Energy Brasil Ltda., adquirida em 28/02/2023 e renomeada","F01 NE1 e NE6 p.57/65; F13 1.1"),
 ("Alteracoes societarias relevantes","Incorporacao das subsidiarias SPE Miranga S.A., Reconcavo E&P S.A. e Potiguar E&P S.A. (proposta de 02/09/2022) e liquidacao da Reconcavo America LLC; farm-out de 50% de 7 concessoes na Bacia Potiguar para Mandacaru Energia (concluido em 10/10/2025); aquisicao de 50% dos ativos de midstream de gas da Brava Energia no RN (concluida em 30/09/2025, via JOA)","F13 1.1 p.5-8"),
 ("Alteracao de nome / codigo de negociacao","Companhia: nenhuma alteracao de denominacao social ou de ticker identificada (CVM e B3 registram apenas PETRORECONCAVO S.A. / RECV3). Controlada: Maha Energy Brasil Ltda. -> SPE Tieta Ltda.","F05; F06; F13 1.1; F01 RA"),
 ("Auditor 2025","Ernst & Young Auditores Independentes S/S Ltda. (CVM 004715) - socio Daniel de Araujo Peixoto - relatorio de 18/03/2026, sem modificacao; PAA: provisao para abandono de pocos","F01 p.44-50; F12 9.1"),
 ("Auditor 2024 (anterior)","Deloitte Touche Tohmatsu Auditores Independentes Ltda. (CVM 003859) - socio Marcelo de Figueiredo Seixas - relatorio de 19/03/2025, sem modificacao; PAA: reconhecimento de receita. Substituicao por termino de contrato (EY contratada para 2025 e 2026)","F07 p.37 e 42-45; F12 9.1"),
 ("Aprovacao das DFs 2025","Diretoria autorizou a emissao em 18/03/2026; DFP entregue a CVM em 18/03/2026 (versao 1)","F01 NE2.1 p.57; F02"),
 ("Estrutura de relatorio financeiro","Praticas contabeis adotadas no Brasil (CPC/CVM) e IFRS (IASB); DFs individuais e consolidadas; DVA como informacao suplementar","F01 NE2.1 p.57"),
]


# Hora de acesso (horario de Brasilia, UTC-3). Base: carimbo de tempo do download
# (mtime do arquivo / cabecalho do pacote .tar gerado no navegador logo apos o GET HTTP).
HORA = {
 "F01":("16:12:41","mtime do PDF baixado (Downloads)"),
 "F02":("16:32:39","indice dfp_cia_aberta_2025.csv contido no zip CVM baixado"),
 "F03":("16:32:39","cabecalho tar do zip CVM 2025"),"F04":("16:32:41","cabecalho tar do zip CVM 2024"),
 "F05":("16:32:41","cabecalho tar do cad_cia_aberta.csv"),"F06":("16:34:29","gravacao do JSON obtido da API B3"),
 "F07":("16:16:43","cabecalho tar (pacote 1)"),"F08":("16:16:43","cabecalho tar (pacote 1)"),"F09":("16:16:43","cabecalho tar (pacote 1)"),
 "F10":("16:16:43","cabecalho tar (pacote 1)"),"F11":("16:16:43","cabecalho tar (pacote 1)"),"F12":("16:16:47","cabecalho tar (pacote 1)"),
 "F13":("16:16:54","cabecalho tar (pacote 1)"),"F14":("16:16:54","cabecalho tar (pacote 1)"),"F15":("16:16:54","cabecalho tar (pacote 1)"),
 "F16":("16:16:55","cabecalho tar (pacote 1)"),"F17":("16:16:55","cabecalho tar (pacote 1)"),"F18":("16:16:56","cabecalho tar (pacote 1)"),
 "F19":("16:16:56","cabecalho tar (pacote 1)"),"F20":("16:16:57","cabecalho tar (pacote 1)"),"F21":("16:16:57","cabecalho tar (pacote 1)"),
 "F22":("16:16:58","cabecalho tar (pacote 1)"),"F23":("16:16:58","cabecalho tar (pacote 1)"),"F24":("16:16:59","cabecalho tar (pacote 1)"),
 "F25":("16:16:59","cabecalho tar (pacote 1)"),"F26":("16:17:00","cabecalho tar (pacote 1)"),"F27":("16:17:00","cabecalho tar (pacote 1)"),
 "F28":("16:17:01","cabecalho tar (pacote 1)"),"F29":("16:17:01","cabecalho tar (pacote 1)"),"F30":("16:17:02","cabecalho tar (pacote 1)"),
 "F31":("16:31:41","cabecalho tar (pacote 2)"),"F32":("16:31:42","cabecalho tar (pacote 2)"),"F33":("16:31:43","cabecalho tar (pacote 2)"),
 "F34":("16:31:44","cabecalho tar (pacote 2)"),"F35":("16:31:44","cabecalho tar (pacote 2)"),"F36":("16:31:46","cabecalho tar (pacote 2)"),
 "F37":("16:31:47","cabecalho tar (pacote 2)"),"F38":("16:31:47","cabecalho tar (pacote 2)"),
 "F39":("n/a","arquivo fornecido na pasta da disciplina (sem acesso web nesta etapa)"),
}
# Paginas de indice consultadas para localizar os documentos (nao sao evidencia em si).
LOG_INDICES = [
 ("22/10/2026","~16:07","RI - Central de Resultados","https://ri.petroreconcavo.com.br/central-de-resultados","Localizar DFP 2025, DF 2024, releases e ITRs","horario aproximado (registro da sessao)"),
 ("22/10/2026","~16:10","Dados de Mercado - RECV3 (terceiro, apoio)","https://www.dadosdemercado.com.br/acoes/recv3","Conferencia inicial de razao social/CNPJ (nao usado como evidencia)","horario aproximado"),
 ("22/10/2026","~16:15","RI - Formulario de Referencia e Formulario Cadastral","https://ri.petroreconcavo.com.br/formulario-de-referencia-e-formulario-cadastral","Localizar FRE 2025 e 2026","horario aproximado"),
 ("22/10/2026","~16:15","RI - Relatorio de Reservas","https://ri.petroreconcavo.com.br/relatorio-de-reservas","Localizar certificacao NSAI","horario aproximado"),
 ("22/10/2026","~16:15","RI - Fatos Relevantes, Comunicados e Avisos","https://ri.petroreconcavo.com.br/fatos-relevantes-comunicados-e-avisos","Localizar eventos 2026 (eventos subsequentes)","horario aproximado; pagina so exibiu itens de 2026"),
 ("22/10/2026","~16:29","RI - Debentures","https://ri.petroreconcavo.com.br/debentures","Localizar relatorios do agente fiduciario","horario aproximado; escrituras nao disponiveis"),
 ("22/10/2026","~16:29","RI - Atas e Assembleias","https://ri.petroreconcavo.com.br/atas-e-assembleias","Localizar AGOE 2026 e RCAs","horario aproximado; pagina so exibiu itens de 2026"),
 ("22/10/2026","~16:32","CVM - Dados Abertos (indices CAD e DFP)","https://dados.cvm.gov.br/dados/CIA_ABERTA/","Localizar arquivos estruturados","horario aproximado"),
]

def sha(p):
    h=hashlib.sha256()
    with open(p,'rb') as f:
        for b in iter(lambda: f.read(1<<20), b''): h.update(b)
    return h.hexdigest()

def cvm_val(arq, conta, data="2025-12-31"):
    with open(arq, encoding='utf-8') as f:
        for r in csv.DictReader(f, delimiter=';'):
            if r['CD_CONTA']==conta and r['DT_FIM_EXERC']==data and r['ORDEM_EXERC']=='ÚLTIMO':
                return float(r['VL_CONTA']), r['DS_CONTA']
    return None, None

def estilo(ws, widths):
    head=PatternFill('solid', fgColor='1F4E78'); thin=Side(style='thin', color='BFBFBF')
    for c in ws[1]:
        c.font=Font(bold=True,color='FFFFFF'); c.fill=head; c.alignment=Alignment(wrap_text=True,vertical='center')
    for row in ws.iter_rows(min_row=2):
        for c in row:
            c.alignment=Alignment(wrap_text=True,vertical='top'); c.border=Border(top=thin,bottom=thin,left=thin,right=thin)
    for i,w in enumerate(widths,1): ws.column_dimensions[get_column_letter(i)].width=w
    ws.freeze_panes='A2'

wb=Workbook()
ws=wb.active; ws.title='Registro_Fontes'
ws.append(['ID','Origem','Documento','Exercicio / data-base','Data de publicacao','Endereco eletronico (URL)','Data de acesso','Hora de acesso (Brasilia, UTC-3)','Base do horario','Arquivo local (repositorio)','Paginas / secoes utilizadas','Uso previsto (PTs)','Observacoes','SHA-256 do arquivo','Tamanho (bytes)'])
for (i,o,d,e,p,u,a,pg,uso,obs) in FONTES:
    h=sz=''
    if os.path.isfile(a): h=sha(a); sz=os.path.getsize(a)
    ws.append([i,o,d,e,p,u,ACESSO,HORA[i][0],HORA[i][1],a,pg,uso,obs,h,sz])
estilo(ws,[6,22,48,16,14,60,12,12,30,40,60,32,55,66,12])

w2=wb.create_sheet('Identificacao_Cia')
w2.append(['Item','Informacao','Fonte (ID / pagina)'])
for r in IDENT: w2.append(list(r))
estilo(w2,[34,100,30])

w3=wb.create_sheet('Conc_PDF_x_CVM')
w3.append(['Conta (consolidado, R$ mil)','Valor no PDF (F01 p.51-52)','Codigo CVM','Descricao CVM','Valor CVM (F03)','Diferenca','Status'])
B='fontes/cvm_dados_abertos/RECV3_dfp_cia_aberta_BPA_con_2025.csv'; P='fontes/cvm_dados_abertos/RECV3_dfp_cia_aberta_BPP_con_2025.csv'; R='fontes/cvm_dados_abertos/RECV3_dfp_cia_aberta_DRE_con_2025.csv'
itens=[('Ativo total',8668015,B,'1'),('Ativo circulante',2158236,B,'1.01'),('Ativo nao circulante',6509779,B,'1.02'),
       ('Imobilizado e intangivel (PDF) x Imobilizado (CVM 1.02.03)',6254225,B,'1.02.03'),('  (+) Intangivel (CVM 1.02.04)',None,B,'1.02.04'),
       ('Patrimonio liquido',4330716,P,'2.03'),('Receita liquida',3157609,R,'3.01'),('Lucro liquido do exercicio',638352,R,'3.11')]
imob=0
for nome,pdf,arq,cod in itens:
    v,ds=cvm_val(arq,cod)
    if cod=='1.02.03': imob=v
    if cod=='1.02.04':
        w3.append([nome,None,cod,ds,v,None,'soma abaixo']); 
        w3.append(['Imobilizado + intangivel (CVM)',6254225,'1.02.03+1.02.04','soma',imob+v,6254225-(imob+v),'OK' if abs(6254225-(imob+v))<1 else 'DIVERGE'])
        continue
    dif=None if pdf is None or v is None else pdf-v
    st='' if dif is None else ('OK' if (cod=='1.02.03') is False and abs(dif)<1 else ('ver linha seguinte' if cod=='1.02.03' else 'DIVERGE'))
    w3.append([nome,pdf,cod,ds,v,dif,st])
estilo(w3,[52,22,16,52,18,14,18])
w3.append([]); w3.append(['Nota: conciliacao preliminar (Etapa 1). O PDF agrega imobilizado e intangivel numa unica rubrica (NE 7); a CVM os separa. Detalhamento completo no PT 500.'])

w5=wb.create_sheet('Log_Indices')
w5.append(['Data','Hora (Brasilia)','Pagina','URL','Finalidade','Observacao'])
for r in LOG_INDICES: w5.append(list(r))
import csv as _c
if os.path.isfile('fontes/log_acessos.csv'):
    for r in list(_c.reader(open('fontes/log_acessos.csv',encoding='utf-8')))[1:]: w5.append(r)
estilo(w5,[12,14,40,70,50,40])

w4=wb.create_sheet('Pendencias')
w4.append(['#','Pendencia','Onde sera tratada'])
for r in [
 (1,'Confirmar no site do CFC a versao vigente de cada NBC TA para o exercicio 2025 (ex.: 220(R3), 600(R2), 510) e registrar resolucao/data','PT 200 / PT 230 / matriz de cobertura'),
 (2,'Identificar motivo da reapresentacao da DFP 2024 (versao 2 entregue no mesmo dia)','PT 510'),
 (3,'Escrituras de debentures nao estao no RI; covenants serao extraidos da NE 9 (F01 p.75) e dos relatorios do agente fiduciario (F31-F34)','PT 570'),
 (4,'ITR 3T26 nao publicado ate a data de acesso; data de corte da pesquisa de eventos subsequentes = 22/10/2026 (ajustar se houver nova publicacao ate a entrega)','PT 560'),
 (5,'Referenciar paginas especificas dos documentos marcados como "a referenciar" a medida que cada PT for elaborado','Todos os PTs'),
]: w4.append(list(r))
estilo(w4,[5,110,35])

os.makedirs('planilhas',exist_ok=True)
wb.save('planilhas/REG_FONTES_RECV3.xlsx'); print('ok planilhas/REG_FONTES_RECV3.xlsx')
