# Registra um acesso a fonte publica com data/hora de Brasilia (UTC-3) em fontes/log_acessos.csv
# Uso: python codigo/log_acesso.py "Pagina" "URL" "Finalidade" ["Obs"]
import csv, sys, os, datetime
agora = datetime.datetime.utcnow() - datetime.timedelta(hours=3)
arq = 'fontes/log_acessos.csv'; novo = not os.path.isfile(arq)
with open(arq, 'a', newline='', encoding='utf-8') as f:
    w = csv.writer(f)
    if novo: w.writerow(['Data','Hora (Brasilia)','Pagina','URL','Finalidade','Observacao'])
    a = sys.argv[1:] + [''] * (4 - len(sys.argv[1:]))
    w.writerow([agora.strftime('%d/%m/%Y'), agora.strftime('%H:%M:%S'), a[0], a[1], a[2], a[3]])
print('registrado', agora.strftime('%d/%m/%Y %H:%M:%S'))
