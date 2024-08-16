def calcular_custo_viagem(distancia, custo_combustivel, consumo_veiculo, numero_pedagios,
custo_pedagio):#vai criar a função de calcular o custo da viagem, recebendo os valores das variáveis que vão ser definidas posteriormente no código.

    custo_combustivel_total = (distancia / consumo_veiculo) * custo_combustivel#vai calcular o valor total do custo de combustível pela conta da divisão da distância por consumo do carro, aí multiplicando pelo custo do combustível.

    custo_pedagio_total = numero_pedagios * custo_pedagio#vai calcular o custo total do pedágio, pela multiplicação do número de pedágios e o custo dos pedágios.

    custo_total = custo_combustivel_total + custo_pedagio_total#vai calcular o custo total, pelo custo do combústivel e de todos pedágios.

    return custo_total, custo_combustivel_total, custo_pedagio_total#vai retornar o valor do custo total, o custo do combustível total e dos pegágios no total.

distancia = float(input("Digite a distância da viagem (em km): "))#vai pedir ao usuário o valor da distância como varíavel tipo flutuante.
custo_combustivel = float(input("Digite o custo do combustível por litro (em R$): "))#vai pedir o custo do combustível.
consumo_veiculo = float(input("Digite o consumo do veículo (km por litro): "))#vai pedir o custo do consummo do veívulo
numero_pedagios = int(input("Digite o número de pedágios no percurso: "))#vai pedir o número de pedágios.
custo_pedagio = float(input("Digite o custo de um pedágio (em R$): "))#vai pedir o custo dos pedágios.

custo_total, custo_combustivel_total, custo_pedagio_total = calcular_custo_viagem(distancia,
custo_combustivel,
                                                            consumo_veiculo, numero_pedagios,
                                                            custo_pedagio)#vai receber os valores das variáveis definidas pela função anterior.

print(f"Custo total da viagem: R${custo_total:.2f}")#essas 3 últimas linhas vão imprimir o valor do custo total e custos dos combusítveis e pedágios.
print(f"Custo total com combustível: R${custo_combustivel_total:.2f}")
print(f"Custo total com pedágios: R${custo_pedagio_total:.2f}")