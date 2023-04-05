import random

def jogo_da_forca():
    print('\n---- JOGO DA FORCA ----')

    # gera palavra
    def gerar_palavra():
        palavras = []
        with open("palavras.txt", "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                linha = linha.strip()
                palavras.append(linha)

        numero = random.randrange(0, len(palavras))
        palavra_secreta = palavras[numero].upper()
        return palavra_secreta

    # posição da letra na palavra
    def localizar(texto, palavra):
        posicoes = []
        for i in range(0,len(texto)):
            if texto[i] == palavra:
                posicoes.append(i)
        return posicoes

    palavra = gerar_palavra()
    
    chances = 0
    
    palavra_secreta = list('_' * len(palavra))

    while chances <= 10:
        chute = input('Tente chutar uma única letra: ').upper() 

        if chute in palavra:
            print(f'Você acertou a letra {chute}!')                 
            posicao = localizar(palavra, chute)

            for i in posicao:    
                palavra_secreta[i] = chute           
            print('\n', palavra_secreta)  

            opcao = input('\nVocê sabe qual é a palavra completa? (S ou N): ')        
            if opcao.upper() == 'S':
                resposta = input('Digite sua resposta: ')
                if resposta.upper() == palavra:
                    print(f'\nParabéns!!!!\nVocê acertou a palavra {palavra}! ')
                    print('---------------') 
                    break
                else:
                    print('\nVocê errou...')
                    print(f'A palavra era {palavra}.')
                    print('--------  Você morreu enforcado. --------') 
                    break
            else:
                print(f'\nVocê ainda tem mais {9-int(chances)} chances.')             
        else:
            print(f'Você errou! Não tem a letra {chute}.')
            print('\n',palavra_secreta) 
            opcao = input('\nVocê sabe qual é o nome da palavra? (S ou N): ')
            if opcao.upper() == 'S':
                resposta = input('Digite sua resposta: ')
                if resposta.upper() == palavra:
                    print(f'Parabéns!!!!\nVocê acertou a palavra {palavra}! ')
                    print('---------------') 
                    break
                else:
                    print('Você errou...')
                    print(f'A palavra era {palavra}.')
                    print('--------  Você morreu enforcado. --------') 
                    break
            else:
                print(f'\nVocê ainda tem mais {9-int(chances)} chances') 
                
        chances +=1
        if chances >= 10:
            print('-------- Você morreu enforcado. --------') 
            print(f'A palavra era {palavra}.')
            break


jogo_da_forca()