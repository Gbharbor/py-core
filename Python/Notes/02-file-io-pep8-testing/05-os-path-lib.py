"""
AULA: Manipulação de Arquivos e Diretórios (os vs pathlib)
"""

# =======================
# OS (FORMA TRADICIONAL)
# =======================

import os

# Criar diretórios
os.mkdir("teste")
os.mkdir(os.path.join("teste", "interna"))

# Remover diretório
os.rmdir(os.path.join("teste", "interna"))

# Diretório atual
print(os.getcwd())

# Renomear arquivo
os.rename("6oslib.py", "6-oslib.py")

# Listar arquivos
print(os.listdir("docs"))

# Caminho seguro
caminho = os.path.join("teste", "arquivo.txt")
print(caminho)


# ========================
# PATHLIB (FORMA MODERNA)
# ========================

from pathlib import Path

# Criar/remover pasta
teste_folder = Path("TESTE1")

if not teste_folder.exists():
    teste_folder.mkdir()
    print("Pasta criada com sucesso")
else:
    teste_folder.rmdir()
    print("Pasta deletada com sucesso")


# Verificar existência de arquivo
eu = Path("7pathlib.py")

if eu.exists():
    print("Sim, eu existo")
else:
    print("Não, eu não existo")
    # eu.unlink()  # remove arquivo (cuidado)


# Criar outra pasta
pasta = Path("teste2")
pasta.mkdir()
