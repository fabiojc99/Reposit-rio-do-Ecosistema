    Pco0=50
    Pcomax=1000
    Mco=2
    Plo0=5
    Plomax=100
    Mlo=0.0005
    EcosystemPython=open( 'Ecosystem.txt','w')  #Os ficheiros vão são ser utilizados mais à frente noutra etapa, muito provavelmente.
    FinalReturn=""
    if Iteration==0:
        EcosystemPython.write(('Mês '+str(Iteration)+' : '+str(50000) +' cenouras,'+str(50)+' coelhos,'+str(5)+' lobos')+('\n'))
        Iteration+=1
    while Iteration<=num_meses and not Iteration==0:
        CenourasIntermidiate=evoluir_populacao_cenouras (Pce0,Rce,Pcemax,Mce,Pco0)
        CoelhosIntermidiate=evoluir_populacao_coelhos (Pco0,Pce0,Mce,Pcomax,Mco,Plo0)
        LobosIntermidiate=evoluir_populacao_lobos (Plo0,Pco0,Mco,Plomax,Mlo)
        Pce0=CenourasIntermidiate
        Pco0=CoelhosIntermidiate
        Plo0=LobosIntermidiate
        param[Iteration] = 'Mês '+str(Iteration)+' : '+str(Pce0) +' cenouras,'+str(Pco0)+' coelhos,'+str(Plo0)+' lobos'
        EcosystemPython.write(('Mês '+str(Iteration)+' : '+str(Pce0) +' cenouras,'+str(Pco0)+' coelhos,'+str(Plo0)+' lobos')+('\n'))
        Iteration+=1
    for Iteration2 in param:
        param[Iteration2]
        FinalReturn+=param[Iteration2]+"\n"
    EcosystemPython.close()    
    return FinalReturn
print(simular_populacoes (Months,Eco))

#Aqui começa a Etapa 5
#Aqui começa a Etapa 6
#Aqui começa a Etapa 7
def simulador(nome_ficheiro):
    open('nome_ficheiro','w') 
    if type(Months)==int:
        EscapeGoat=simular_populacoes(Months,Eco) #Existe algo problema com o Ficheiro
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
#Aqui começa a Etapa 8
#Aqui começa a Etapa 9
