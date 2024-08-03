# Function to compute equivalent weight
def equiv_weight(weight: float, planet_id: int) -> float | None:
    if not isinstance(weight, float) or not isinstance(planet_id, int):
        return None
    elif weight <= 0 or planet_id <= 0:
        return None
    else:
        if planet_id == 1:
          x = 0.37
          return weight * x
        elif planet_id == 2:
          x = 0.88
          return weight * x
        elif planet_id == 3:
          x = 0.38
          return weight * x
        elif planet_id == 4:
          x = 2.64
          return weight * x
        elif planet_id == 5:
          x = 1.15
          return weight * x
        elif planet_id == 6:
          x = 1.17
          return weight * x                                
def main():
    try:
        weight = float(input('Entre com o peso: '))
        planet_id = int(input('Entre com o número do planeta, sendo: \n 1 = Mercúrio \n 2 = Vênus \n 3 = Marte \n 4 = Júpiter \n 5 = Saturno \n 6 = Urano \n '))
        peso = round(equiv_weight(weight,planet_id))

        if peso is not None:
            print('Valor do peso:', peso )
        else:
            print('Os valores devem ser um inteiro positivo.') 
    except ValueError:
        print('Insira um número válido.')

if __name__=='__main__':
  # If your module is being executed directly, run the main function.
  main()
