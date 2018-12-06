Pce0=50000
Rce=1
Pcemax=100000
Mce = 5
Pco0 = 50
Pcomax = 1000
Mco = 2
Plo0 = 5
Plomax = 100
Mlo = 0.0005

Ecosistema={"Pce0":50000,"Pco0":50,"Plo0":5}
def evoluir_populacao_cenouras (Pce,Rce,Pcemax,Mce,Pco):
    PceAfter=Pce+(Rce*Pce)*(1-(Pce/Pcemax))-(Mce*Pco)
    return PceAfter
print(evoluir_populacao_cenouras(5000,1,100000,5,50))   
    
