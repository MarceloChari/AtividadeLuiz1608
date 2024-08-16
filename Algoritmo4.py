def calcular_media_e_aprovacao(notas, nota_minima_aprovacao):#função para calcular a media e a aprovação de alunos, recebendo valores das notas e nota minima para aprovação.

    total_notas = 0#o valor das notas total é pré-definido como 0.

    num_alunos = len(notas)#aqui vai dar os valores dos números de alunos, por quanto de notas que foi dado.

    aprovados = []#vai gerar um vetor para receber os aprovados.

    reprovados = []#vetor para receber os reprovados.

    for aluno, nota in notas.items():#usando o para em, vai realizar a conta abaixo.
        total_notas += nota#o valor do total de notas vai ser dado somando o valor das notas que vão ser dadas pelo programa.
        if nota >= nota_minima_aprovacao:#usando o se e senão(condicional), se a nota for maior do que a nota minima de aprovação, então o resultado da linha de baixo.
            aprovados.append(aluno)#vai criar uma lista dos alunos aprovados.
        else:#se não der a condição anterior, então vai dar o valor abaixo.
            reprovados.append(aluno)#vai criar uma lista dos alunos reprovados.

    media_turma = total_notas / num_alunos#vai calcular a media da turma, por meio da divisão do total de notas pela variável de número de alunos.

    return media_turma, aprovados, reprovados#vai retornar à função, a média da turma, a lista dos aprovados e reprovados

notas = {#aqui abaixo, vai receber as notas dos alunos.
"Alice": 85,
"Bruno": 72,
"Carlos": 60,
"Diana": 95,
"Eduardo": 55
}

nota_minima_aprovacao = 70#vai receber a nota mínima para aprovação.

media_turma, aprovados, reprovados = calcular_media_e_aprovacao(notas, nota_minima_aprovacao)#vai receber os valores para as variáveis, de acordo com o resultado da função.

print(f"Média da turma: {media_turma:.2f}")#nessas 3 linhas, vai imprimir na tela a média da turma e as listas dos alunos aprovados e reprovados.
print(f"Alunos aprovados: {', '.join(aprovados)}")
print(f"Alunos reprovados: {', '.join(reprovados)}")