import math

p = 1000  # valor principal
r = 0.05  # taxa de juros
m = 2000  # montante desejado

t = math.log(m / p) / math.log(1 + r)  # cálculo do tempo necessário

print(f"O tempo necessário para atingir o montante desejado é de {t:.2f} anos")
