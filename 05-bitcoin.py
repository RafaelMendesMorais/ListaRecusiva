def calcular_investimento():
    investimentos_mensais = 250  
    marcos = [100000, 1000000]  
    cotacoes_btc = [
        307000, 360000, 317000, 355000, 353000, 369000,
        334000, 345000, 409000, 581000, 583000, 600000
    ]  # Cotações mensais do Bitcoin
    
    valor_investido = 0
    meses = 0
    marco1 = marco2 = marco_btc = False
    
    while not (marco1 and marco2 and marco_btc):
        valor_investido += investimentos_mensais
        meses += 1
        
        # Calculando Bitcoin acumulado
        mes_atual = (meses - 1) % 12  
        bitcoin_acumulado = valor_investido / cotacoes_btc[mes_atual]
        
        # Verificando marcos
        if not marco1 and valor_investido >= marcos[0]:
            print(f"Atingiu R$ {marcos[0]:,.2f} em {meses // 12} anos e {meses % 12} meses. Valor investido: R$ {valor_investido:,.2f}")
            marco1 = True
        if not marco2 and valor_investido >= marcos[1]:
            print(f"Atingiu R$ {marcos[1]:,.2f} em {meses // 12} anos e {meses % 12} meses. Valor investido: R$ {valor_investido:,.2f}")
            marco2 = True
        if not marco_btc and bitcoin_acumulado >= 1:
            print(f"Atingiu 1 BTC em {meses // 12} anos e {meses % 12} meses. Valor investido: R$ {valor_investido:,.2f}")
            marco_btc = True


calcular_investimento()
