def investimento_poupanca(valor_investido, saldo, objetivo, juros_mensal, valor_dolar=5.8):
    meses = 0  # Contador de meses
    while saldo < objetivo:
        saldo = saldo * (1 + juros_mensal) + valor_investido
        meses += 1

    # Calculando anos e meses
    anos = meses // 12
    meses_restantes = meses % 12
    juros_obtidos = saldo - valor_investido * meses
    saldo_em_dolar = saldo / valor_dolar

    return anos, meses_restantes, valor_investido * meses, juros_obtidos, saldo_em_dolar


valor_investido = 500  # valor mensal investido
juros_mensal = 0.0005  # juros de 0,05% ao mês
objetivo_100k = 100000  # marco de R$ 100.000
objetivo_1kk = 1000000  # marco de R$ 1.000.000
valor_dolar = 5.8  # valor do dólar hoje dia 13

#
anos_100k, meses_100k, valor_investido_100k, juros_100k, saldo_dolar_100k = investimento_poupanca(
    valor_investido, 0, objetivo_100k, juros_mensal, valor_dolar
)


anos_1kk, meses_1kk, valor_investido_1kk, juros_1kk, saldo_dolar_1kk = investimento_poupanca(
    valor_investido, 0, objetivo_1kk, juros_mensal, valor_dolar
)


print(f"Para alcançar R$ 100.000,00:")
print(f"Tempo gasto: {anos_100k} anos e {meses_100k} meses")
print(f"Valor investido: R$ {valor_investido_100k * (anos_100k * 12 + meses_100k):,.2f}")
print(f"Juros compostos obtidos: R$ {juros_100k:,.2f}")
print(f"Valor final em dólares: {saldo_dolar_100k:,.2f} Dólares")

print("\nPara alcançar R$ 1.000.000,00:")
print(f"Tempo gasto: {anos_1kk} anos e {meses_1kk} meses")
print(f"Valor investido: R$ {valor_investido_1kk * (anos_1kk * 12 + meses_1kk):,.2f}")
print(f"Juros compostos obtidos: R$ {juros_1kk:,.2f}")
print(f"Valor final em dólares: {saldo_dolar_1kk:,.2f} Dólares")
