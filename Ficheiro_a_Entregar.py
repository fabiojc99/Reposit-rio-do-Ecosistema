#Aqui começa a Etapa 1
#####
#####


#Pce0=50000
#Rce=1
#Pcemax=100000
#Mce = 5
#Pco0 = 50
#Pcomax = 1000
#Mco = 2
#Plo0 = 5
#Plomax = 100
#Mlo = 0.0005

Months=int(input())
Eco={"Pce0":50000,"Pco0":50,"Plo0":5}
def evoluir_populacao_cenouras (Pce,Rce,Pcemax,Mce,Pco):
    PceAfter=Pce+(Rce*Pce)*(1-(Pce/Pcemax))-(Mce*Pco)
    return round(PceAfter)

#Aqui começa a Etapa 2

def evoluir_populacao_coelhos (Pco,Pce,Mce,Pcomax,Mco,Plo):
    Nco=(Pce/Mce*Pco)
    PcoAfter=Pco+Nco*(1-(Pco/Pcomax))-(Mco*Plo)
    return round(PcoAfter)

#Aqui começa a Etapa 3
def evoluir_populacao_lobos (Plo,Pco,Mco,Plomax,Mlo):
    Nlo=(Pco/(Mco*Plo))
    PloAfter=Plo+Nlo*(1-(Plo/Plomax))-(Mlo*Plo)
    return round(PloAfter)

#Aqui começa a Etapa 4
def simular_populacoes (num_meses,param):
    Iteration=0
    Pce0=5000
    Rce=1
    Pcemax=1000000
    Mce=5
    Pco0=50
    Pcomax=1000
    Mco=2
    Plo0=5
    Plomax=100
    Mlo=0.0005
    while Iteration<num_meses: #Isto está tudo errado, volta sempre ao valor inicial Xxx0
        CenourasIntermidiate=evoluir_populacao_cenouras (Pce0,Rce,Pcemax,Mce,Pco0)
        CoelhosIntermidiate=evoluir_populacao_coelhos (Pco0,Pce0,Mce,Pcomax,Mco,Plo0)
        LobosIntermidiate=evoluir_populacao_lobos (Plo0,Pco0,Mco,Plomax,Mlo)
        Iteration+=1
        Pce0=CenourasIntermidiate
        Pco0=CoelhosIntermidiate
        Plo0=LobosIntermidiate
        print(Pce0)
        print(Pco0)
        print(Plo0)
    param[Pce0]=int(Pce0)
    param[Pco0]=int(Pco0)
    param[Plo0]=int(Plo0)
    FinalString=("Mês "+str(num_meses)," : ",str(param[Pce0])," cenouras, ",str(param[Pco0])," coelhos,",(param[Plo0])," lobos")
    return FinalString
print(simular_populacoes (Months,Eco))

#Aqui começa a Etapa 5
#Aqui começa a Etapa 6
#Aqui começa a Etapa 7
#Aqui começa a Etapa 8
#Aqui começa a Etapa 9
