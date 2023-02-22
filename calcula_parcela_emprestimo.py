pv = 10000  # valor presente do empréstimo
n = 12  # número de períodos
i = 0.01  # taxa de juros por período

pmt = (pv * i) / (1 - (1 + i) ** -n)  # cálculo da parcela

print(f"O valor da parcela é R$ {pmt:.2f}")
