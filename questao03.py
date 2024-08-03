# Function to compute health insurance price
def health_insurance_price(age: int) -> float | None:
    if not isinstance(age, int):
        return None
    elif age < 0:
        return None
    else:
        if age <= 10:
          x = 30
          return x
        elif age > 10 and age <= 29:
          x = 60
          return x
        elif age > 29 and age <= 45:
          x = 120
          return x 
        elif age > 45 and age <= 59:
          x = 150
          return x
        elif age > 59 and age <= 65:
          x = 250
          return x
        elif age > 65 and age <= 150:
          x = 400
          return x                               

def main():
    try:
        age = int(input('Entre com a idade: '))
        preco = health_insurance_price(age)
        if preco is not None:
            print('Valor do plano: R$', preco, ',00')
        else:
            print('Os valores devem ser um inteiro positivo.') 
    except ValueError:
        print('Insira um número válido.')

if __name__=='__main__':
  # If your module is being executed directly, run the main function.
  main()
