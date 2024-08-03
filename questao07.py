def day_period(hh: int, mm: int, ss: int) -> int | None:
    if hh < 0 or hh > 23 or mm < 0 or mm > 59 or ss < 0 or ss > 59:
        return None

    if 0 <= hh < 6:
        return 0
    elif 6 <= hh < 12:
        return 1
    elif 12 <= hh < 18:
        return 2
    else:
        return 3

def main():
    try:
        hh = int(input("Entre com as horas (0-23): "))
        mm = int(input("Entre com os minutos (0-59): "))
        ss = int(input("Entre com os segundos (0-59): "))
        periodo = day_period(hh, mm, ss)
        
        if periodo is None:
            print("Horário inválido")
        else:
            if periodo == 0:
                print('O horário:',hh,':',mm,':',ss,'está no período da Madrugada.')
            elif periodo == 1:
                print('O horário:',hh,':',mm,':',ss,'está no período da Manhã.')
            elif periodo == 2:
                print('O horário:',hh,':',mm,':',ss,'está no período da Tarde.')
            elif periodo == 3:
                print('O horário:',hh,':',mm,':',ss,'está no período da Noite.')
    except ValueError:
        print("Entrada inválida. Por favor, insira números inteiros.")

if __name__ == '__main__':
    main()
