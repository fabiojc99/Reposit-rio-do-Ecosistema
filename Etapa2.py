
def evoluir_populacao_coelhos (Pco,Pce,Mce,Pcomax,Mco,Plo):
    Nco=(Pce/(Mce*Pco))
    PcoAfter=Pco+Nco*(1-(Pco/Pcomax))-(Mco*Plo)
    return round(PcoAfter)


