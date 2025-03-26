quant_maxima = 1000
quant_min = 800
quant_media = (quant_maxima + quant_min) / 2
quant_atual = int(input("Digite a quantidade atual em estoque "))
print(f"A média é {quant_media}")
if quant_atual >= quant_media:
    print("Não efetuar compra")
else : 
    print("Efetuar compra")