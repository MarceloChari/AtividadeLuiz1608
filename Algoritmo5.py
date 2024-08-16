def calcular_imc(peso, altura):#vai criar a função de calcular imc, recebendo as variáveis peso e altura.

    imc = peso / (altura ** 2)#vai calcular o valor do imc, pela divisão do peso pela altura elevado a 2.
    return imc#vai retornar o valor do imc

def classificar_imc(imc):#vai calcular a classificação do imc.

    if imc < 18.5:#essas linhas vão servir para classificar em qual imc se configura, pelo valor dado pelo usuário anteriormente.
        return "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    elif 30 <= imc < 34.9:
        return "Obesidade grau 1"
    elif 35 <= imc < 39.9:
        return "Obesidade grau 2"
    else:
        return "Obesidade grau 3"

def sugestao_atividade_fisica(classificacao_imc):

    if classificacao_imc == "Abaixo do peso":
            return "Sugere-se atividades de fortalecimento muscular, como musculação, e uma dieta rica em
proteínas e calorias."

    elif classificacao_imc == "Peso normal":
        return "Sugere-se a manutenção com atividades aeróbicas regulares, como caminhada, corrida leve e
natação, junto a um treino de força moderado."

    elif classificacao_imc == "Sobrepeso":
        return "Sugere-se atividades aeróbicas moderadas, como caminhada rápida, ciclismo e natação, além
de exercícios de resistência."

    elif classificacao_imc == "Obesidade grau 1":
        return "Sugere-se atividades de baixo impacto, como caminhadas, natação e hidroginástica, junto a um
programa de reeducação alimentar."

    elif classificacao_imc == "Obesidade grau 2":
        return "Sugere-se exercícios de baixo impacto com supervisão, como hidroginástica e pilates, e
acompanhamento nutricional."

    else:
        return "Sugere-se atividades físicas supervisionadas por profissionais de saúde, como hidroginástica,
fisioterapia, e consultas regulares com um nutricionista."

peso = float(input("Digite seu peso (em kg): "))#vai pedir o valor do peso ao usuário, por flutuante.
altura = float(input("Digite sua altura (em metros): "))#vai pedir o valor da altura por flutuante.

imc = calcular_imc(peso, altura)#vai receber o valor do imc definido na função anterior.
classificacao_imc = classificar_imc(imc)#vai receber o valor da classificação do imc.
sugestao = sugestao_atividade_fisica(classificacao_imc)#vai receber o valor da sugestão.

print(f"Seu IMC é: {imc:.2f}")#vai imprimir na tela o valor do imc, da classificação e da sugestão.
print(f"Classificação: {classificacao_imc}")
print(f"Sugestão de atividade física: {sugestao}")