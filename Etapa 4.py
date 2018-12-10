#Aqui começa a Etapa 4
def simular_populacoes (num_meses,param):
    Iteration=0
    Pce0=50000
    Rce=1
    Pcemax=100000
    Mce=5
    Pco0=50
    Pcomax=1000
    Mco=2
    Plo0=5
    Plomax=100
    Mlo=0.0005
    EcosystemPython=open( 'Ecosystem.txt','w')
    if Iteration==0:
        EcosystemPython.write(('Mês '+str(Iteration)+' : '+str(50000) +' cenouras,'+str(50)+' coelhos,'+str(5)+' lobos')+('\n'))
        Iteration+=1
    while Iteration<=num_meses and not Iteration==0 :
        CenourasIntermidiate=evoluir_populacao_cenouras (Pce0,Rce,Pcemax,Mce,Pco0)
        CoelhosIntermidiate=evoluir_populacao_coelhos (Pco0,Pce0,Mce,Pcomax,Mco,Plo0)
        LobosIntermidiate=evoluir_populacao_lobos (Plo0,Pco0,Mco,Plomax,Mlo)
        Pce0=CenourasIntermidiate
        Pco0=CoelhosIntermidiate
        Plo0=LobosIntermidiate
        EcosystemPython.write(('Mês '+str(Iteration)+' : '+str(Pce0) +' cenouras,'+str(Pco0)+' coelhos,'+str(Plo0)+' lobos')+('\n'))
        Iteration+=1

    EcosystemPython.close()    
    param[Pce0]=int(Pce0) #Esta parte do Dicionário pode não ser utilizado na etapa 4 mas pode ser útil a posteriori
    param[Pco0]=int(Pco0)
    param[Plo0]=int(Plo0)
    EcosystemPython=open('Ecosystem.txt','r')
    FinalEcosystem=EcosystemPython.read()
    EcosystemPython.close()
    return FinalEcosystem
print(simular_populacoes (Months,Eco))
