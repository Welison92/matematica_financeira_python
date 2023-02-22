ebitda = 100000  # lucro antes dos juros, impostos, depreciação e amortização
capex = 20000  # investimento em bens de capital
nwc = 5000  # variação no capital de giro
tx = 0.30  # taxa de imposto de renda
tma = 0.12  # taxa mínima de atratividade

fcl = ebitda * (1 - tx) + capex - nwc  # cálculo do fluxo de caixa livre

print("O fluxo de caixa livre é R$", fcl)
