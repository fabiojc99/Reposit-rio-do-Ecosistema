def simular_populacoes (num_meses,param):
    param={"Pce0":50000,"Pco0":50,"Plo0":5}
    Iteration=0
    while Iteration<=num_meses: #Isto está tudo errado, volta sempre ao valor inicial Xxx0
        CenourasIntermidiate=evoluir_populacao_cenouras (param[Pce0],Rce,Pcemax,Mce,param[Pco0])
        CoelhosIntermidiate=evoluir_populacao_coelhos (param[Pco0], param[Pce0],Mce,Pcomax,Mco, param[Plo])
        LobosIntermidiate=evoluir_populacao_lobos (param[Plo],param[Pco],Mco,Plomax,Mlo)
        Iteration+=1
    param[Pce0]=CenourasIntermidiate
    param[Pco0]=CoelhosIntermidiate
    param[Plo0]=LobosIntermidiate
    FinalString=("Mês "+num_mes+" : "+param[Pce0]+" cenouras, "+param[Pco0]+" coelhos,"+param[Plo0]+" lobos")
    return FinalString
print(simular_populacoes (Months,Eco))
