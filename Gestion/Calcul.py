def calcul(elo_principale:float, elo_adverse:float):
    
    if elo_principal < elo_adverse:
        diference = elo_adverse - elo_principal
        return 10 + diference / 20
    
    if elo_principal > elo_adverse:
        diference = elo_principal - elo_adverse
        point = 10 - diference/50

        if point <= 0:
            return 1

        else:
            return point

    if elo_principale == elo_adverse:
        return 10