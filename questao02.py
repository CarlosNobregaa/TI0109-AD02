from math import sqrt, pi

def volume(a: float) -> float | None:
    if not isinstance(a, float):
        return None
    elif a <= 0:
        return None
    else:
        V = (1/3) * (((a**2 * sqrt(3)) / 4) * ((a * sqrt(6)) / 3))
        return V

# Function to compute the surface area of a tetrahedron
def area(a: float) -> float | None:
    if not isinstance(a, float):
        return None
    elif a <= 0:
        return None
    else:
        A = (a**2) * sqrt(3)
        return A

def main():
    try:
        a = float(input('Entre com o comprimento da aresta: '))
        vol = volume(a)
        are = area(a)
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

if __name__=='__main__':
  # If your module is being executed directly, run the main function.
  main()
