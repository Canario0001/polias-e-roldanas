#!/usr/bin/env python3
from math import log2

def header(num):
        print('┅'*num)

def fpotente(fres, n):
	# fres → força de resistência
	# n → número de polias móveis
    
    return fres/(2**n)

def fresis(fpot, n):
    # fpot → força potente
    # n → número de polias móveis
    
    return fpot * (2**n)

def npolias(fres, fpot):
    # fres → força de resistência
    # fpot → força potente
    
    return log2(fres/fpot)

def lista():
    print('\n\nA lista estará da seguinte maneira:\nabreviação: o que significa\nDigite no formato abreviação:valor\n')
    print('fpot: Força Potente (usada para erguer o sistema)')
    print('fres: Força de Resistência (se opõe a força potente)\nn: Número de polias móveis')

def pato(fpot, fres, n):
    # fpot → força potente
    # fres → força de resistência
    # n → número de polias móveis
    
    err = 'Não foi possível encontrar.'
    
    if not fpot:
        try:
            fpot = fpotente(fres, n)
        except (ValueError, TypeError): # não tem fres ou n
            fpot = err

    if not fres:
        try:
            fres = fresis(fpot, n)
        except (ValueError, TypeError): # não tem fpot ou n
            fres = err

    if not n:
        try:
            n = npolias(fres, fpot)
        except (ValueError, TypeError): # não tem fres ou fpot
            n = err

    result = {
            'fpot': fpot,
            'fres': fres,
            'n': n
    }

    return result

def anotar(nome, resultado):
    texto = f'Resultados\n\nForça Potente: {resultado["fpot"]} N\nForça de Resistência: {resultado["fres"]} N\nNúmero de polias móveis: {resultado["n"]}\n'
    with open(f'{nome}.txt', 'w') as f: f.write(texto)

def main():
    header(40)
    print('  Calculadora de Polias e Roldanas!')
    header(40)
    print('\nDeseja ver a lista de abreviações ou quer começar agora?\n')
    print('[0] - Ver a lista de abreviações\n[1] - Começar sem ver a lista\n')
    choice = int(input('>>> '))
    if choice == 0: lista()
    elif choice == 1: pass
    else:
        print('Insira um valor válido. Tente novamente.')
        exit()

    fpot = None
    fres = None
    n = None
    print('\n\nDigite as informações que você possui de acordo com a lista de abreviações. Digite "q" se tiver terminado.\n')
    while True:
        # comp → composto
        comp = input('>>> ').strip().lower()
        if comp == 'q': break

        if comp.startswith('fpot'):
            _, fpot = comp.split(':')
            fpot = float(fpot)

        elif comp.startswith('fres'):
            _, fres = comp.split(':')
            fres = float(fres)

        elif comp.startswith('n'):
            _, n = comp.split(':')
            n = int(n)

        else: print('Digite uma informação válida!')

    resultado = pato(fpot, fres, n)
    print('\n')
    header(35)
    print('  Resultados')
    header(35)
    print('')
    print(f'  Força Potente: {resultado["fpot"]} N')
    print(f'  Força de Resistência: {resultado["fres"]} N')
    print(f'  Número de polias móveis: {resultado["n"]}')
    print('\n\nVocê quer escrever os resultados num arquivo de texto?\n\n[0] - Sim\n[1] - Não\n')
    choice = int(input('>>> ').strip())
    if choice == 0:
        print('\nQual será o nome do arquivo?\n')
        nome = input('>>> ').strip()
        anotar(nome, resultado)
        print(f'\nResultados salvos no arquivo {nome}.txt!')
    elif choice == 1: pass
    else: print('Opção inválida. Operação cancelada.')

    print('\nObrigado por usar!\nFeito por: Cristian (aka Canário)')

if __name__ == '__main__':
    main()
