def calcular_area_comodos():#criação da função de calcular a área de comodos.

    total_area = 0#vai pré definir o valor total da área como 0.

    while True:#criação de um laço de repetiçaõ, usando enquanto for verdadeiro.

        largura = float(input("Digite a largura do cômodo (em metros): "))#vai pedir ao usuário, por meio do input(colocando float antes para definir o tipo da variável como float), o valor em metros da largura do comodo que quer calcular.
        comprimento = float(input("Digite o comprimento do cômodo (em metros): "))#vai realizar a mesma coisa, mas pedindo o comprimento ao usuário.

        area_comodo = largura * comprimento#vai definir o valor da área do comodo como largura vezes o comprimento( usando asterísco, faz multiplicação.
        print(f"A área deste cômodo é: {area_comodo:.2f} metros quadrados.")#vai mostrar na tela por meio do print, o valor da área do comodo.

        total_area += area_comodo#usando o mais igual, ele vai dar o valor de total_area somando o valor por area de comodos, quanto mais valores o usuário dar para diferentes area de comodos, o valor total vai ir somando.

        mais_comodos = input("Deseja adicionar mais cômodos? (s/n): ").strip().lower()#vai mostrar na tela se o usuário deseja adicionar mais comodos para calcular, no qual o código vai pegar do usuário o que ele digitar.
        if mais_comodos != 's':#se o usuário não digitar "s", o código vai quebrar e vai acabar o laço de repetição.
            break

    return total_area#vai retornar o valor da área total.

area_total = calcular_area_comodos()#aqui vai receber o valor da área total, que foi definida na função calcular área de comodos.
print(f"A área total da casa é: {area_total:.2f} metros quadrados.")#vai mostrar na tela o valor da área total.