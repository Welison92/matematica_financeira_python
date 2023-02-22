investimento = [-1000, 400, 450, 500, 600]  # fluxos de caixa do investimento
tma = 0.1  # taxa mínima de atratividade


def calcular_vpl(investimento, tma):
    vpl = 0
    for i, fluxo in enumerate(investimento):
        vp = fluxo / (1 + tma) ** i  # calcula o valor presente do fluxo de caixa
        vpl += vp  # adiciona o valor presente ao VPL
    return vpl


vpl = calcular_vpl(investimento, tma)
print(f"O valor presente líquido do investimento é R$ {vpl:.2f}")
