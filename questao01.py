from math import sqrt, pi

def volume(r: float, h: float) -> float | None:
    if not isinstance(r, float) or not isinstance(h, float):
        return None
    elif h <= 0 or r <= 0:
        return None
    else:
        V = (1/3) * pi * (r**2) * h
        return V

def area(r: float, h: float) -> float | None:
    if not isinstance(r, float) or not isinstance(h, float):
        return None
    elif h <= 0 or r <= 0:
        return None
    else:
        A = pi * r * (r + sqrt(r**2 + h**2))
        return A

def main():
    try:
        h = float(input('Entre com a altura: '))
        r = float(input('Entre com o raio da base: '))
        vol = volume(r, h)
        are = area(r, h)
        if vol is not None:
            print('Valor do volume: ', vol)
        else:
            print('Os valores devem ser números positivos.')
        if are is not None:
            print('Valor da área: ', are)  
        else:
            print('Os valores devem ser números positivos.')  
    except ValueError:
        print('Insira um número válido.')
        
if __name__ == '__main__':
    main()
