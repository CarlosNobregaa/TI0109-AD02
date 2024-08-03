# Function to approve loan
def approve_loan(salary: float, installment: float) -> bool | None:
    if salary <= 0 or installment <= 0:
        return None
    
    max_installment = 0.3 * salary

    if installment <= max_installment:
        return True
    else:
        return False

def main():
    try:
        salary = float(input("Entre com o salário bruto: "))
        installment = float(input("Entre com o valor da prestação: "))
        
        result = approve_loan(salary, installment)
        
        if result is None:
            print("Dados inválidos.")
        elif result:
            print("O empréstimo pode ser concedido.")
        else:
            print("O empréstimo não pode ser concedido.")
    
    except ValueError:
        print("Insira valores numéricos válidos.")

if __name__=='__main__':
  # If your module is being executed directly, run the main function.
  main()
