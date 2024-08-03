def is_palindrome(num: int) -> bool | None:
    if num < 1 or num > 9999:
        return None
    
    original_num = num
    reverso = 0

    while num > 0:
        ultimo_digito = num % 10
        reverso = reverso * 10 + ultimo_digito
        num = num // 10
    
    return original_num == reverso

def main():
    try:
        N = int(input('Entre com um número inteiro entre 1 e 9999: '))
        result = is_palindrome(N)
        
        if result is None:
            print('Número fora do intervalo válido.')
        elif result:
            print('O número',N,'é um palíndromo.')
        else:
            print('O número',N,'não é um palíndromo.')
    except ValueError:
        print('Entrada inválida. Por favor, insira um número inteiro válido.')

if __name__ == '__main__':
    main()
