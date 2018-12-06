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
def evoluir_populacao_coelhos (Pco,Pce,Mce,Pcomax,Mco,Plo):
    Nco=(Pce/Mco*Plo)
    PcoAfter=Pco+(Nco*(1-(Pco/Pcomax)))-(Mco*Plo)
    return PcoAfter
