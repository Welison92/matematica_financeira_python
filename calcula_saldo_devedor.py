pv = 10000  # valor presente do empréstimo
n = 12  # número de períodos
i = 0.01  # taxa de juros por período
pmt = (pv * i) / (1 - (1 + i) ** -n)  # valor da parcela
saldo = pv
for periodo in range(1, n+1):
    juros = saldo * i
    amortizacao = pmt - juros
    saldo -= amortizacao

print("O saldo devedor após", n, "períodos é R$", saldo)
