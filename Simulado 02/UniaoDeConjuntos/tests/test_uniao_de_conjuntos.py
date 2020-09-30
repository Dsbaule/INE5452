""" 
Autor: Daniel de Souza Baulé (16200639)

Disciplina: INE5452 - Topicos Especiais em Algoritmos II
Atividade:  Segundo simulado - Questoes extra-URI

Testes para União de Conjuntos
Os testes realizam diversas operações de união em diversos grupos de conjuntos
"""

import unittest
import tester

class TestEscalonadorDeProcessos(unittest.TestCase):
    def test_1(self):
        n = 5
        conjuntos = [
            [11, 13, 2],
            [4],
            [7, 6, 3, 10],
            [9, 8],
            [1, 5, 12]
        ]
        m = 3
        operacoes = [
            (13, 4),
            (9, 8),
            (1, 2)
        ]
        tester.test(n, conjuntos, m, operacoes, 1)

    def test_2(self):
        n = 5
        conjuntos = [
            [1, 2],
            [3, 4],
            [5, 6],
            [7, 8],
            [9, 10]
        ]
        m = 4
        operacoes = [
            (2, 3),
            (4, 5),
            (6, 7),
            (8, 9)
        ]
        tester.test(n, conjuntos, m, operacoes, 2)

    def test_3(self):
        n = 5
        conjuntos = [
            [1, 2],
            [3, 4],
            [5, 6],
            [7, 8],
            [9, 10]
        ]
        m = 4
        operacoes = [
            (2, 3),
            (8, 9),
            (4, 5),
            (6, 7)
        ]
        tester.test(n, conjuntos, m, operacoes, 3)

    def test_4(self):
        n = 5
        conjuntos = [
            [1],
            [2],
            [3],
            [4],
            [5],
        ]
        m = 4
        operacoes = [
            (1, 2),
            (3, 4),
            (1, 5),
            (3, 5)
        ]
        tester.test(n, conjuntos, m, operacoes, 4)

    def test_5(self):
        n = 1
        conjuntos = [
            [1, 2, 3, 4, 5],
        ]
        m = 4
        operacoes = [
            (1, 2),
            (3, 4),
            (1, 5),
            (3, 5)
        ]
        tester.test(n, conjuntos, m, operacoes, 5)