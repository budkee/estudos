# Função para calcular o Fibonacci e contar as chamadas recursivas
def fibonacci(n, calls):
    calls[0] += 1 # Incrementa o contador de chamadas

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1, calls) + fibonacci(n - 2, calls)

# Função principal
def main():
    N = int(input())

    for _ in range(N):
        X = int(input())

        calls = [0] # Inicializa o contador de chamadas
        result = fibonacci(X, calls)

        print(f'fib({X}) = {calls[0] - 1} calls = {result}')

if __name__ == "__main__":
    main()
