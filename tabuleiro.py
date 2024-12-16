# -*- coding: utf-8 -*-

class Tabuleiro:
    DESCONHECIDO = 0
    JOGADOR_0 = 1
    JOGADOR_X = 4

    def __init__(self):
        self.matriz = [ [Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO], 
                        [Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO],
                        [Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO]]
       
        
    def tem_campeao(self):


        for l in range(0,3):
         somal = 0

         for c in range(0,3):
            somal = somal + self.matriz[l][c]

            if somal == 3:
                return Tabuleiro.JOGADOR_0
            
            elif somal == 12:
                return Tabuleiro.JOGADOR_X        
         

        for c in range(0,3):
            somac = 0

            for l in range(0,3):
                somac = somac + self.matriz[l][c]

                if somac == 3:
                    return Tabuleiro.JOGADOR_0
                
                elif somac == 12:
                    return Tabuleiro.JOGADOR_X  

        somadp = 0
        somads = 0
        for i in range(0,3):           
            somadp += self.matriz[i][i]
            if somadp == 3:
                return Tabuleiro.JOGADOR_0
            if somadp == 12:
                return Tabuleiro.JOGADOR_X
            
            somads += self.matriz[i][2-i]
            if somads == 3:
                return Tabuleiro.JOGADOR_0
            if somads == 12:
                return Tabuleiro.JOGADOR_X
        
        
        return Tabuleiro.DESCONHECIDO