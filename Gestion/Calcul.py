def calcul(elo_principal:float, elo_adverse:float):
    
    if elo_principal < elo_adverse:
        diference = elo_adverse - elo_principal
        return float(10 + diference / 20)
    
    if elo_principal > elo_adverse:
        diference = elo_principal - elo_adverse
        point = float(10 - diference/50)

        if point <= 0:
            return 1.0

        else:
            return float(point)

    if elo_principale == elo_adverse:
        return 10.0