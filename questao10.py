# Function to compute credit based on mean balance
def credit(balance: float) -> float | None:
    if balance < 0:
        return None
    
    if balance >= 0 and balance <=500:
        saldo = 0
        return saldo
    
    elif balance > 500 and balance <= 1000:
        saldo = balance * 0.3
        return saldo
    
    if balance > 1000 and balance <= 3000:
        saldo = balance * 0.4
        return saldo
    
    if balance > 3000:
        saldo = balance * 0.5
        return saldo

def main():
    try:
        saldo_medio = float(input("Entre com o saldo médio: "))
        
        saldo_credito = credit(saldo_medio)
        
        if saldo_credito is None:
            print("Dados inválidos.")
        else:
            print("Saldo médio:", saldo_medio, "Valor de crédito:", saldo_credito)
    
    except ValueError:
        print("Insira valores numéricos válidos.")
if __name__=='__main__':
  # If your module is being executed directly, run the main function.
  main()
