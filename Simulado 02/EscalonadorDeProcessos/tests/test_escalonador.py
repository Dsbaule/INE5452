""" 
Autor: Daniel de Souza Baulé (16200639)

Disciplina: INE5452 - Topicos Especiais em Algoritmos II
Atividade:  Segundo simulado - Questoes extra-URI

Testes para Escalonador de Processos
Os testes utilizam os mesmos atributos para os processos, variando
sua ordem de chegada para observar como isso afeta o resultado final
"""

import unittest
import tester

class TestEscalonadorDeProcessos(unittest.TestCase):
    def test_1(self):
        t = 4
        conjuntos_de_processos = [
            [1, 2, 3],
            [4],
            [5],
            [6, 7, 8, 9],
            [10, 11]
        ]
        n = 11
        atributos = [
            [1, 3, 5, 1],
            [2, 3, 3, 2],
            [3, 3, 5, 3],
            [4, 2, 1, 4],
            [5, 2, 1, 5],
            [6, 3, 5, 6],
            [7, 1, 5, 7],
            [8, 2, 1, 8],
            [9, 1, 3, 9],
            [10, 2, 2, 10],
            [11, 4, 5, 11]
        ]
        tester.test(t, conjuntos_de_processos, n, atributos, 1)

    def test_2(self):
        t = 10
        conjuntos_de_processos = [
            [1],
            [2],
            [3],
            [4],
            [5],
            [6],
            [7],
            [8],
            [9],
            [10],
            [11]
        ]
        n = 11
        atributos = [
            [1, 3, 5, 1],
            [2, 3, 3, 2],
            [3, 3, 5, 3],
            [4, 2, 1, 4],
            [5, 2, 1, 5],
            [6, 3, 5, 6],
            [7, 1, 5, 7],
            [8, 2, 1, 8],
            [9, 1, 3, 9],
            [10, 2, 2, 10],
            [11, 4, 5, 11]
        ]
        tester.test(t, conjuntos_de_processos, n, atributos, 2)

    def test_3(self):
        t = 0
        conjuntos_de_processos = [
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        ]
        n = 11
        atributos = [
            [1, 3, 5, 1],
            [2, 3, 3, 2],
            [3, 3, 5, 3],
            [4, 2, 1, 4],
            [5, 2, 1, 5],
            [6, 3, 5, 6],
            [7, 1, 5, 7],
            [8, 2, 1, 8],
            [9, 1, 3, 9],
            [10, 2, 2, 10],
            [11, 4, 5, 11]
        ]
        tester.test(t, conjuntos_de_processos, n, atributos, 3)

    def test_4(self):
        t = 10
        conjuntos_de_processos = [
            [11],
            [10],
            [9],
            [8],
            [7],
            [6],
            [5],
            [4],
            [3],
            [2],
            [1]
        ]
        n = 11
        atributos = [
            [1, 3, 5, 1],
            [2, 3, 3, 2],
            [3, 3, 5, 3],
            [4, 2, 1, 4],
            [5, 2, 1, 5],
            [6, 3, 5, 6],
            [7, 1, 5, 7],
            [8, 2, 1, 8],
            [9, 1, 3, 9],
            [10, 2, 2, 10],
            [11, 4, 5, 11]
        ]
        tester.test(t, conjuntos_de_processos, n, atributos, 4)

    def test_5(self):
        t = 10
        conjuntos_de_processos = [
            [1, 2],
            [],
            [3, 4],
            [],
            [5, 6],
            [],
            [7, 8],
            [],
            [9, 10],
            [],
            [11]
        ]
        n = 11
        atributos = [
            [1, 3, 5, 1],
            [2, 3, 3, 2],
            [3, 3, 5, 3],
            [4, 2, 1, 4],
            [5, 2, 1, 5],
            [6, 3, 5, 6],
            [7, 1, 5, 7],
            [8, 2, 1, 8],
            [9, 1, 3, 9],
            [10, 2, 2, 10],
            [11, 4, 5, 11]
        ]
        tester.test(t, conjuntos_de_processos, n, atributos, 5)