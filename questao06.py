def is_valid_date(dd: int, mm: int, aa: int) -> bool | None:
    if mm < 1 or mm > 12:
        return False
    if aa < 0:
        return False
    
    max_dias = 31
    
    if mm in {4, 6, 9, 11}:
        max_dias = 30
    elif mm == 2:
        if (aa % 4 == 0 and aa % 100 != 0) or (aa % 400 == 0):
            max_dias = 29
        else:
            max_dias = 28

    if dd < 1 or dd > max_dias:
        return False
    
    return True

def main():
    try:
        dd = int(input("Entre com o dia: "))
        mm = int(input("Entre com o mês: "))
        aa = int(input("Entre com o ano: "))
        valido = is_valid_date(dd, mm, aa)
        
        if valido is None:
            print("Data inválida")
        elif valido:
            print('A data',dd,'/',mm,'/',aa,'é válida')
        else:
            print("Data inválida")
    except ValueError:
        print("Data inválida")

if __name__ == '__main__':
    main()
