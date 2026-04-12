"""
AULA: Erros e Tratamento de Exceções em Python
"""

# ===============
# TIPOS DE ERROS
# ===============

print("\n=== TIPOS DE ERROS ===")

# ValueError
try:
    int("abc")
except ValueError:
    print("ValueError: nao foi possivel converter texto em numero.")

# ZeroDivisionError
try:
    10 / 0
except ZeroDivisionError:
    print("ZeroDivisionError: nao e possivel dividir por zero.")

# TypeError
try:
    "10" + 5
except TypeError:
    print("TypeError: operacao invalida entre tipos diferentes.")

# FileNotFoundError
try:
    with open("arquivo.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("FileNotFoundError: ficheiro nao encontrado.")


# ===================
# TRY / EXCEPT BÁSICO
# ===================

print("\n=== TRY / EXCEPT ===")

try:
    numero = int(input("Digite um numero: "))
    print("Resultado:", 10 / numero)
except:
    print("Ocorreu um erro.")


# =================
# ERROS ESPECÍFICOS
# =================

print("\n=== ERROS ESPECIFICOS ===")

try:
    numero = int(input("Digite um numero: "))
    print("Resultado:", 10 / numero)

except ValueError:
    print("Erro: digite apenas numeros.")

except ZeroDivisionError:
    print("Erro: divisao por zero.")


# ===============
# ELSE E FINALLY
# ===============

print("\n=== ELSE / FINALLY ===")

try:
    numero = int(input("Digite um numero: "))
    resultado = 10 / numero

except ValueError:
    print("Erro: entrada invalida.")

except ZeroDivisionError:
    print("Erro: divisao por zero.")

else:
    print("Resultado:", resultado)

finally:
    print("Fim da execucao.")


# ================
# MULTIPLOS ERROS
# ================

print("\n=== MULTIPLOS ERROS ===")

try:
    numero = int(input("Digite um numero: "))
    print("Resultado:", 10 / numero)

except (ValueError, ZeroDivisionError):
    print("Erro: entrada invalida ou divisao por zero.")


# ======
# DEBUG
# ======

print("\n=== DEBUG ===")

try:
    numero = int(input("Digite um numero: "))
    print("Resultado:", 10 / numero)

except Exception as e:
    print("Erro detectado:", e)


# =======================
# TRACEBACK (EXPLICACAO)
# =======================

print("\n=== TRACEBACK ===")
print("Quando um erro nao tratado ocorre, o Python mostra um traceback.")
print("Leia de baixo para cima.")


# =========
# EXERCICIO
# =========

print("\n=== EXERCICIO ===")

try:
    n1 = int(input("Digite o primeiro numero: "))
    n2 = int(input("Digite o segundo numero: "))
    print("Resultado:", n1 / n2)

except ValueError:
    print("Erro: digite apenas numeros.")

except ZeroDivisionError:
    print("Erro: divisao por zero.")

finally:
    print("Programa finalizado.")
