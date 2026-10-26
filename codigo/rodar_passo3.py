# -*- coding: utf-8 -*-
# P2 - Auditoria 1 - RECV3 - Preparador 211059370
# Reproduz TODO o passo 3, na ordem: gera bases simuladas -> conciliacao/testes/MUS -> folha -> dicionario.
# Uso (na raiz P2_PetroReconcavo):  python codigo/rodar_passo3.py
import subprocess, sys, time
ETAPAS = ['codigo/gerar_base_imobilizado.py', 'codigo/testes_auditoria_base.py', 'codigo/gerar_base_folha.py', 'codigo/testes_folha.py', 'codigo/gerar_dicionario.py', 'codigo/gerar_readme_base.py']
for e in ETAPAS:
    t = time.time(); print(f'\n===== {e} =====', flush=True)
    r = subprocess.run([sys.executable, e])
    if r.returncode != 0:
        sys.exit(f'Falhou: {e}')
    print(f'----- ok ({time.time() - t:.0f}s)')
print('\nPasso 3 reproduzido com sucesso.')
