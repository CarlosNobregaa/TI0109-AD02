def pmt(L: float, r: float, m: int, t: int) -> float | None:
    if L <= 0 or r < 0 or m <= 0 or t <= 0:
        return None
    
    i = r / m
    
    denominator = 1 - (1 + i) ** (-m * t)
    if denominator == 0:
        return None
    
    R = (L * i) / denominator
    return R

def balance(R: float, i: float, m: int, t: int, k: int) -> float | None:
    if R <= 0 or i < 0 or m <= 0 or t <= 0 or k < 0 or k > m * t:
        return None
    
    L_prime = R * ((1 - (1 + i) ** (-(m * t - k))) / i)
    return L_prime

def main():
    try:
        L = float(input("Entre com o valor do empréstimo (L): "))
        r = float(input("Entre com a taxa de juros anual (r): "))
        m = int(input("Entre com o número de parcelas por ano (m): "))
        t = int(input("Entre com o número de anos do empréstimo (t): "))
        k = int(input("Entre com o número de parcelas pagas (k): "))
        
        parcela = pmt(L, r, m, t)
        if parcela is None:
            print("Dados inválidos para o cálculo da parcela.")
        else:
            print(f"O valor da parcela é: {parcela:.2f}")
        
        balanco = balance(parcela, r / m, m, t, k)
        if balanco is None:
            print("Dados inválidos para o cálculo do balanço.")
        else:
            print(f"O balanço do empréstimo após {k} parcelas pagas é: {balanco:.2f}")
    
    except ValueError:
        print("Entrada inválida. Por favor, insira valores numéricos válidos.")

if __name__ == '__main__':
    main()
