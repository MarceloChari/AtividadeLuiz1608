def diagnosticar_diabetes(glicemia_em_jejum, glicemia_pos_prandial):#vai criar a função de diagnosticar diabetes, recebendo o valores da glicemia em jejum e da glicemia pós prandial.

    if glicemia_em_jejum >= 126 or glicemia_pos_prandial >= 200:#vai usar condição se e senão, se a glicemia em jejum for maior ou igual a 126, ou a glicemia pos prandial for maior ou igual a 200, então vai continuar para linha de baixo.
        return "Diabetes"#caso a condição anterior passar, então vai retornar "Diabetes" como valor da função.
    elif 100 <= glicemia_em_jejum < 126 or 140 <= glicemia_pos_prandial < 200:#mesmo das linhas anteriores, usando elif(outro se), se a glicemia em jejum estar entre 100 e 126, ou a glicemia pos prandial estar entre 140 e 200, então retorna ao usuário a linha de baixo.
        return "Pré-diabetes"#vai retornar "Pré-diabetes" como valor da função.
    else:#se não estar entre as condições anteriores, então retorna a linha de baixo.
        return "Normal"#vai retornar à função o valor de normal.

glicemia_em_jejum = float(input("Digite o valor da glicemia em jejum (mg/dL): "))#vai pedir ao usuário que ele digite o valor, como variável de tipo flutuante(que pode ser número com vírgula).
glicemia_pos_prandial = float(input("Digite o valor da glicemia pós-prandial (mg/dL): "))#vai pedir ao usuário o valor da glicemia pos prandial, também recebendo valor flutuante.

resultado = diagnosticar_diabetes(glicemia_em_jejum, glicemia_pos_prandial)#o valor do resultado vai ser igual ao valor definido na função anterior.
print(f"O diagnóstico é: {resultado}")#vai imprimir na tela o valor do resultado.