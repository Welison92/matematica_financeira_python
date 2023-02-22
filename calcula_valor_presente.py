f = 10000  # valor futuro
i = 0.10  # taxa de desconto
t = 1  # tempo em anos

d = f * i * t  # cálculo do desconto
vp = f - d  # cálculo do valor presente

print("O valor presente após o desconto é R$", vp)
