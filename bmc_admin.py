#!/usr/bin/env python
#importacoes
import os

#variaveis
rodando = True

while rodando == True:
    os.system('clear')
    comando = raw_input("Comando? (N)ovo, (M)odificar, (E)xcluir, (L)istar, (S)air: ")
    if comando not in "nNmMeElLsS":
        print "Opcao invalida, tente novamente"
    elif comando in "nN":
        print "Novo"
    elif comando in "sS":
        print "Sair"
        rodando = False
