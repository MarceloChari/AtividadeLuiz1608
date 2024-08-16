def calcular_juros_atraso(valor_principal, taxa_juros_anual, dias_atraso):#criaçaõ da função por def, que vai calcular os juros do atraso do usuário/cliente, por ser função, é necessário que nos parenteses estejam as variáveis que vão ser definididas posterorimente no código.

    taxa_juros_diaria = taxa_juros_anual / 365 / 100 #calcula a taxa de juros diárias, recebendo o valor igual à taxa de juros anual, divida por 365, divido por 100( em Python, a barra significa divisão). Assim recebendo um valor para essa nova variável criada.

    juros = valor_principal * taxa_juros_diaria * dias_atraso #aqui acontece a criação da variável juros, que vai ser calculada usando a multiplicação( em python, representada por asterísco) das 3 variáveis, valor principal, taxa de juros diarias e dias de atrasos, retornando o valor do juros.

    valor_total = valor_principal + juros#o valor total é definidido pelo valor principal mais o valor do juros, assim voltando o valor ao código.
    return valor_total, juros#como é uma função, precisa de um return, e as variáveis que retornam é o valor total e o juros, que foram calculados.

valor_principal = 1000.00#aqui no código, o valor principal foi definido como 1000.00.
taxa_juros_anual = 5.0#aqui o valor da taxa de juros anual foi definida como 5.0
dias_atraso = 30#o total de dias de atraso foi definido como 30.
valor_total, juros = calcular_juros_atraso(valor_principal, taxa_juros_anual, dias_atraso)#aqui recebe os valores que foram calculados na variável anterior.
print(f"Valor total a ser pago: R${valor_total:.2f}")#vai dar print(mostrar na tela) o valor total a ser pago.
print(f"Valor dos juros: R${juros:.2f}")#aqui vai mostrar na tela o valor dos juros.