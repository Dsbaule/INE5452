""" 
Autor: Daniel de Souza Baulé (16200639)

Disciplina: INE5452 - Topicos Especiais em Algoritmos II
Atividade:  Terceiro simulado - Questoes extra-URI

Algorítmo de Karatsuba

De wikipedia:
    procedure karatsuba(num1, num2)
        if (num1 < 10) or (num2 < 10)
            return num1 × num2
        
        /* Calculates the size of the numbers. */
        m = min(size_base10(num1), size_base10(num2))
        m2 = floor(m / 2) 
        /* m2 = ceil(m / 2) will also work */
        
        /* Split the digit sequences in the middle. */
        high1, low1 = split_at(num1, m2)
        high2, low2 = split_at(num2, m2)
        
        /* 3 calls made to numbers approximately half the size. */
        z0 = karatsuba(low1, low2)
        z1 = karatsuba((low1 + high1), (low2 + high2))
        z2 = karatsuba(high1, high2)
        
        return (z2 × 10 ^ (m2 × 2)) + ((z1 - z2 - z0) × 10 ^ m2) + z0
"""

# Divide o número por bits transformando em uma string
def split_by_string(n, m):
    num_string = bin(n)
    return int(num_string[2:m + 2],2), int(num_string[m + 2:],2)

# Divide o número por bits utilizando uma mascara
def split_by_mask(n, m):
    mask = sum(2**i for i in range(m))
    return n >> m, n & mask

# Algorítmo de Karatsuba recursivo
def karatsuba_rec(n1, n2):
    if n1 < 10 or n2 < 10:
        result = n1 * n2
        #print('K {} {} - {}'.format(n1, n2, result))
        return result
    
    # Obtem a metade do menor numero
    m = min(n1.bit_length(), n2.bit_length())
    m2 = m // 2

    # Divide os dois numeros
    high1, low1 = split_by_mask(n1, m2)
    high2, low2 = split_by_mask(n2, m2)

    # Calcula os valores parciais com o Algoritmo de Karatsuba
    z0 = karatsuba_rec(low1, low2)
    z1 = karatsuba_rec((low1 + high1), (low2 + high2))
    z2 = karatsuba_rec(high1, high2)

    # Calcula o valor total
    result = (z2 * (2 ** (m2 * 2))) + ((z1 - z2 - z0) * (2 ** m2)) + z0

    # Retorna o resultado
    return result

# Algorítmo de Karatsuba com ED (vetor)
def karatsuba(n1, n2, rec=False):
    # Verifica se a chamada é pelo algoritmo recursivo simples, para debug
    if rec:
        return karatsuba_rec(n1, n2)

    # Gera listas de bits a partir dos inteiros, do menos ao mais significativo
    n1 = [int(digito) for digito in bin(n1)[2:]][::-1]
    n2 = [int(digito) for digito in bin(n2)[2:]][::-1]

    # Retorna o resultado do algorítmo
    return karatsuba_ed(n1, n2, 0, len(n1), 0, len(n2))


# Algoritmo de Karatsuba com ED
def karatsuba_ed(n1, n2, l1, len1, l2, len2):
    # Caso o numero tenha menos de 5 bits, apenas multiplique
    if len1 < 5 or len2 < 5:
        return multiplica(n1, n2, l1, len1, l2, len2)

    # Obtem a metade do menor numero
    m = min(len1, len2)
    m2 = m // 2

    # Calcula os valores parciais com o Algoritmo de Karatsuba
    # Multiplicacao dos bits menos significativos
    z0 = karatsuba_ed(n1, n2, l1, m2, l2, m2)

    # Calcula a soma dos menos significativos com os mais significativos
    sum1 = soma(n1, n1, l1, m2, l1 + m2, len1 - m2)
    sum2 = soma(n2, n2, l2, m2, l2 + m2, len2 - m2)

    # Multiplicacao das somas
    z1 = karatsuba(sum1, sum2)

    # Multiplicacao dos bits mmais significativos
    z2 = karatsuba_ed(n1, n2, l1 + m2, len1 - m2, l2 + m2, len2 - m2)

    # Calcula o  resultaddo
    result = (z2 * (2 ** (m2 * 2))) + ((z1 - z2 - z0) * (2 ** m2)) + z0

    # Retorna o resultado
    return result


def multiplica(n1: list(), n2: list(), l1, len1, l2, len2):
    num1 = 0; num2 = 0

    # Calcula o segundo inteiro    
    for i in range(len1):
        num1 += (2 ** i) * n1[l1 + i]

    # Calcula o segundo inteiro    
    for i in range(len2):
        num2 += (2 ** i) * n2[l2 + i]

    # Retorna a multiplicacao dos inteiros
    return num1 * num2

def soma(n1: list(), n2: list(), l1, len1, l2, len2):
    num1 = 0; num2 = 0

    # Calcula o segundo inteiro    
    for i in range(len1):
        num1 += (2 ** i) * n1[l1 + i]

    # Calcula o segundo inteiro    
    for i in range(len2):
        num2 += (2 ** i) * n2[l2 + i]

    # Retorna a multiplicacao dos inteiros
    return num1 + num2

def main():
    # Obtem o número a ser multiplicado
    n1 = int(input("n1 = "))
    n2 = int(input("n2 = "))
    # Imprime o resultado da multiplicação
    print('Resultado da Multiplicacao: {}'.format(karatsuba(n1, n2)))

main()