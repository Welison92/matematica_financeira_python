principal = 10000  # valor principal do empréstimo
taxa = 0.01  # taxa de juros por período
n = 12  # número de períodos
pmt = (principal * taxa) / (1 - (1 + taxa) ** -n)  # valor da parcela mensal

saldo_devedor = principal
pagamento_total = 0

print("Mês\t\tPagamento\t\tJuros\t\tAmortização\t\tSaldo Devedor")

for i in range(n):
    juros = saldo_devedor * taxa
    amortizacao = pmt - juros
    saldo_devedor -= amortizacao
    pagamento_total += pmt
    print(f"{i + 1}\t\tR${pmt:.2f}\t\tR${juros:.2f}\t\tR${amortizacao:.2f}\t\tR${saldo_devedor:.2f}")

print(f"\nO valor total pago é R${pagamento_total:.2f}.")
print(f"O valor total dos juros é R${pagamento_total - principal:.2f}.")
