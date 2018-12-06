#Aqui começa a Etapa 1
#####
#####


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

param={"Pce0":50000,"Pco0":50,"Plo0":5}
def evoluir_populacao_cenouras (Pce,Rce,Pcemax,Mce,Pco):
    PceAfter=Pce+(Rce*Pce)*(1-(Pce/Pcemax))-(Mce*Pco)
    return PceAfter
print(evoluir_populacao_cenouras(5000,1,100000,5,50))   

#Aqui começa a Etapa 2

Ecosistema={"Pce0":50000,"Pco0":50,"Plo0":5}
def evoluir_populacao_coelhos (Pco,Pce,Mce,Pcomax,Mco,Plo):
    Nco=(Pce/Mco*Plo)
    PcoAfter=Pco+(Nco*(1-(Pco/Pcomax)))-(Mco*Plo)
    return PcoAfter

#Aqui começa a Etapa 3
def evoluir_populacao_lobos (Plo,Pco,Mco,Plomax,Mlo):
    Nlo=(Pco/(Mco*Plo))
    PloAfter=Plo+Nlo*(1-(Plo/Plomax))-(Mlo*Plo)
    return PloAfter

#Aqui começa a Etapa 4
#Aqui começa a Etapa 5
#Aqui começa a Etapa 6
#Aqui começa a Etapa 7
#Aqui começa a Etapa 8
#Aqui começa a Etapa 9
