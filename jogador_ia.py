# -*- coding: utf-8 -*-
from random import randint

from jogador import Jogador
from tabuleiro import Tabuleiro

class JogadorIA(Jogador):
    def __init__(self, tabuleiro : Tabuleiro, tipo : int):
        super().__init__(tabuleiro, tipo)
            

    def getJogada(self) -> (int, int):
        lista = []

        #requisito 1
        for l in range (0,3): 
            somal = 0
            for c in range (0,3):
                somal += self.matriz[l][c]

                if somal == 2:
                    for x in range (0,3):
                        if self.matriz[l][x] == Tabuleiro.DESCONHECIDO:
                            return (l, x)
        
        for c in range (0,3):
            somac = 0
            for l in range (0,3):
                somac += self.matriz[l][c]

                if somac == 2:
                    for x in range (0,3):
                        if self.matriz[x][c] == Tabuleiro.DESCONHECIDO:
                            return (x, c)

        somad = 0
        for i in range (0,3):
            somad += self.matriz[i][i]
            if somad == 2:
                for i in range (0,3):
                    if self.matriz[i][i] == Tabuleiro.DESCONHECIDO:
                        return (i, i) 


        somad = 0
        for i in range (0,3):
            somad += self.matriz[i][2-i]
            if somad == 2:
                for i in range (0,3):
                    if self.matriz[i][2-i] == Tabuleiro.DESCONHECIDO:
                        return (i, 2-i)  
        
        for l in range (0,3):
            somal = 0
            for c in range (0,3):
                somal += self.matriz[l][c]

                if somal == 8:
                    for x in range (0,3):
                        if self.matriz[l][x] == Tabuleiro.DESCONHECIDO:
                            return (l, x)
        
        for c in range (0,3):
            somac = 0
            for l in range (0,3):
                somac += self.matriz[l][c]

                if somac == 8:
                    for x in range (0,3):
                        if self.matriz[x][c] == Tabuleiro.DESCONHECIDO:
                            return (x, c)


        somad = 0
        for i in range (0,3):
            somad += self.matriz[i][i]
            if somad == 8:
                for i in range (0,3):
                    if self.matriz[i][i] == Tabuleiro.DESCONHECIDO:
                        return (i, i)


        somad = 0
        for i in range (0,3):
            somad += self.matriz[i][2-i]
            if somad == 8:
                for i in range (0,3):
                    if self.matriz[i][2-i] == Tabuleiro.DESCONHECIDO:
                        return (i, 2-i)
        #fim do requisito 1


        #requisito 2
        # for l in range (0,3):
        #     somal = 0
            
        #     for c in range(0,3):
        #         somal += self.matriz[l][c]
        #         if somal == 1:
        #             linha = l        
        #             for c in range (0,3):
        #                 somac = 0

                        
        #                 for l in range(0,3):
        #                     somac += self.matriz[l][c]
        #                     if somac == 1:
        #                         coluna = c
        #                         if self.matriz[linha][coluna] == Tabuleiro.DESCONHECIDO:
        #                             return (linha, coluna)


        # for l in range(0,3):
        #     somal = 0
        #     for c in range(0,3):
        #         somal += self.matriz[l][c]
        #         if somal == 1:
        #             somal = 0
        #             for c in range(0,3):
        #                 somal += self.matriz[l][c]
        #                 if somal != 1:
        #                     return (l, c)
                        


        # for c in range(0,3):
        #     somac = 0
        #     for l in range(0,3):
        #         somac += self.matriz[l][c]
        #         if somac == 1:
        #             somac = 0
        #             for l in range(0,3):
        #                 somac += self.matriz[l][c]
        #                 if somac != 1:
        #                     return (l, c)



        #fim do requisito 2                        

        #requisito 3
        if self.matriz[1][1] == Tabuleiro.DESCONHECIDO:
            return (1, 1)
        #fim do requisito 3

        #requisito 4
        if self.matriz[0][0] == Tabuleiro.JOGADOR_X and self.matriz[2][2] == Tabuleiro.DESCONHECIDO:
            return (2, 2)

        if self.matriz[0][2] == Tabuleiro.JOGADOR_X and self.matriz[2][0] == Tabuleiro.DESCONHECIDO:
            return (2, 0)

        if self.matriz[2][0] == Tabuleiro.JOGADOR_X and self.matriz[0][2] == Tabuleiro.DESCONHECIDO:
            return (0, 2)

        if self.matriz[2][2] == Tabuleiro.JOGADOR_X and self.matriz[0][0] == Tabuleiro.DESCONHECIDO:
            return (0, 0)

        #fim do requisito 4


        #requisito 5
        cantos = [(0,0),(0,2),(2,0),(2,2)]
        for l, c in cantos:
            if self.matriz[l][c] == Tabuleiro.DESCONHECIDO:
                return (l, c)
        #fim do requisito 5

        #requisito 6
        for l in range(0,3):
            for c in range(0,3):
                if self.matriz[l][c] == Tabuleiro.DESCONHECIDO:
                    lista.append((l, c))


        if(len(lista) > 0):
            p = randint(0, len(lista)-1)
            return lista[p]
        else:
           return None
        #fim do requisito 6