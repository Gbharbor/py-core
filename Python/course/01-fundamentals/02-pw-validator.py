"""
Validação de Senha
"""

print("=== MODO 1: VALIDACAO DIRETA ===")

password = input("Digite uma senha: ")

if len(password) >= 8 and password != "12345678":
   print("Senha valida.")
elif len(password) < 8:
   print("Senha invalida. Deve ter pelo menos 8 caracteres.")
else:
   print("Senha invalida. Sequencia nao permitida.")


print("\n=== MODO 2: VARIAVEIS AUXILIARES ===")

password = input("Digite uma senha: ")

char_count = len(password)
is_sequence = password == "12345678"

if char_count < 8:
   print("Senha invalida. Deve ter pelo menos 8 caracteres.")
elif is_sequence:
   print("Senha invalida. Nao pode ser uma sequencia simples.")
else:
   print("Senha valida. Muito bem.")


print("\n=== MODO 3: FUNCAO ===")


def validate_password(password: str) -> bool:
   if len(password) < 8:
      return False

   if password == "12345678":
      return False

   return True


password = input("Digite uma senha: ")

if validate_password(password):
   print("Senha valida.")
else:
   print("Senha invalida.")