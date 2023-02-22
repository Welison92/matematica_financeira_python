fcl1 = 100000  # fluxo de caixa livre do ano 1
fcl2 = 120000  # fluxo de caixa livre do ano 2
fcl3 = 150000  # fluxo de caixa livre do ano 3
tma = 0.12  # taxa mínima de atratividade

vp1 = fcl1 / (1 + tma)  # valor presente do fluxo de caixa do ano 1
vp2 = fcl2 / (1 + tma) ** 2  # valor presente do fluxo de caixa do ano 2
vp3 = fcl3 / (1 + tma) ** 3  # valor presente do fluxo de caixa do ano 3

vp_total = vp1 + vp2 + vp3  # valor presente total dos fluxos de caixa

print(f"O valor da empresa pelo fluxo de caixa descontado é R$ {vp_total:.2f}")
