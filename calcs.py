def semestral(g1,g2):
    media = ( (g1*2)+(g2*3) ) / 5

    state = None
    if media >= 60:
        # APROVADO
        state = "Aprovado"
        
    elif 20 <= media < 60:
        # PROVA FINAL
        state = "Prova Final"
        naf0 = 120 - media
        naf1 = (300-(3*g2))/2
        naf2= (300-(2*g1))/3
        
        result = min(naf0, naf1, naf2)

    else:
        #REPROVADO
        state = "Reprovado"
        pass
    
    print(f"Situação: {state} | MÉDIA: {media:.2f}")
    if state == 'Aprovado':
        print("Você está aprovado! :)")
    elif state == 'Prova Final':
        print(f"Você precisa de {round(result)} na prova Final!")
        pass
    elif state == 'Reprovado':
        print("Você está Reprovado! :(")

    
def anual(g1,g2,g3,g4):
    media = ( (g1+g2)*2 + (g3+g4)*3 )/ 10

    state = None
    if media >= 60:
        # APROVADO
        state = "Aprovado"

    elif 20 <= media < 60:
        # RECUPERAÇÃO
        state = "Prova Final"

        naf0 = 120-media
        naf1 = (600-(3*(g3+g4)))/2 - g2
        naf2 = (600-(3*(g3+g4)))/2 - g1
        naf3 = (600-(2*(g1+g2)))/3 - g4
        naf4 = (600-(2*(g1+g2)))/3 - g3
        
        result = min(naf0, naf1, naf2, naf3, naf4)
    else:
        #REPROVADO
        state = "Reprovado"
    
    print(f"Situação: {state} | MÉDIA: {media:.2f}")
    if state == 'Aprovado':
        print("Você está aprovado! :)")
    elif state == 'Prova Final':
        print(f"Você precisa de {round(result)} na prova Final!")
        pass
    elif state == 'Reprovado':
        print("Você está Reprovado! :(")