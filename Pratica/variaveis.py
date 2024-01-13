def variaveis():
    # Tipagem dinâmica
    valor1 = 3
    valor2 = "janeiro"
    valor3 = 3.0
    valor4 = [3, 6, 9, 12]

    # Sobreposição de valores em variáveis
    valor1 = "Três"

    # Regras na construção de nomes de variáveis
    variavelComNomeLongo = "Isso é uma variável com nome longo"

    # Exibindo tipos das variáveis
    print(f"{valor1} has a type {type(valor1)}")
    print(f"{valor2} has a type {type(valor2)}")
    print(f"{valor3} has a type {type(valor3)}")
    print(f"{valor4} has a type {type(valor4)}")

if __name__ == '__main__':
    variaveis()
