def simulador(nome_ficheiro):
    open('nome_ficheiro','w')
    if type(Months)==int:
        EscapeGoat=simular_populacoes(Months,Eco)
        nome_ficheiro.write(EscapeGoat)
        nome_ficheiro.close()
        open('nome_ficheiro','r')
        FinalAnswer=nome_ficheiro.read()
        nome_ficheiro.close()
    elif Months=="q" or Months=="Q":
        FinalAnswer="Simulador Terminado."
    elif type(Months)!=int and not Months=="q" and not Months=="Q":
        FinalAnswer="Caracter inválido!"

    return FinalAnswer
print(simulador('Ecosystem.txt'))
