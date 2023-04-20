# Nome: Murilo Favoretto Finardi
# RM: 99950

tempo = float(input("Digite há quantos anos você fuma.................: "))
valor_maco = float(input("Digite quanto custa cada maço do seu cigarro.....: "))
maco_dia = float(input("Digite quantos maços de cigarro você fuma por dia: "))

maco_ano = (maco_dia * 30) * 12
montante = maco_ano * valor_maco * tempo

if montante < 20000:
    print(f"Com o valor R$ {montante:.2f}, você poderia ter dado entrada em um carro.")
elif montante >= 20000 and montante <= 50000:
    print(f"Com o valor R$ {montante:.2f}, você poderia ter comprado um carro popular usado.")
else:
    print(f"Com o valor R$ {montante:.2f}, você poderia ter comprado um carro zero.")
