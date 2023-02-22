p = 1000  # valor principal
r = 0.05  # taxa de juros
t = 2  # tempo em anos

m = p * (1 + r) ** t  # cálculo do montante

j = m - p  # cálculo dos juros

print("O valor dos juros é R$", j)
