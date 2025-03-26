dia = int(input("Digite um dia numerico"))

match dia:
    case 1 :
        print("dia útil")
    
    case 2: 
        print("Final de Semana ou Feriado")

    case 3:
        print("Bad day")
    case 4:
        print(f"Numero {dia} Invalido")
    case _ :
        print("failed")