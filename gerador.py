import string
import random

# print(string.ascii_lowercase)
# print(string.ascii_letters)

tamanho = 32

valores = string.ascii_lowercase + string.ascii_uppercase + string.ascii_letters + string.punctuation
senha = ''

for i in range(tamanho):
    senha += random.choice(valores)
    
print(senha)