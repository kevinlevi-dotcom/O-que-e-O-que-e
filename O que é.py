import pygame
import time
import random
lista=['Banana','Casa','Anel']
textob=['o que é o que é,Tem casca, mas não se usa para fazer sopa','É amarela por fora e branca por dentro','Dizem que sou rica em potássio']
textoc=['O que é, o que é? Sou um livro de memórias','O que é, o que é? Começa em uma fundação','lar com vida e sentimento']
dicab=['É uma fruta,Amarela','Começão com B,Termina com A']
dicac=['Começão com C,Termina com A','É um imóver']
dicacontagen=0
ganho=7
pontos=0
i=0
pygame.init()
v=input("Dejesa jogar:")
if v == 'sim':
    while True:
        Ale=random.choice(lista)
        if Ale == 'Banana':
            Aleb=random.choice(textob)
            if Aleb == 'o que é o que é,Tem casca, mas não se usa para fazer sopa':
                print("O que é O que é,Tem casca, mas não se usa para fazer sopa")
                Letra_A=pygame.mixer.Sound("soba.wav")
                Letra_A.play()
                time.sleep(5)
                print("Se você quiser usar A 'dica'digite 1,porém você vai ganhar menos pontos")
                Letra_A=pygame.mixer.Sound("dica.wav")
                Letra_A.play()
                time.sleep(5)
                while True:
                    dica1=random.choice(dicab)
                    V=input("")
                    if V == '1':
                        print(dica1)
                        dicacontagen+=1
                        dica1=random.choice(dicab)
                        continue
                    if V == 'Banana' or V == 'banana':
                            if dicacontagen > 0:
                                ganho-=1
                                pontos=ganho
                                print(f"Você ganhor {pontos} pontos")
                                ganho=7
                                dicacontagen=0
                                aleb=''
                                break
                            else:
                                Letra_A=pygame.mixer.Sound("smw_1-up.wav")
                                Letra_A.play()
                                time.sleep(2)
                                pontos+=7
                                print("Correto,A respota é (Banana)")
                                Letra_A=pygame.mixer.Sound("Correto.wav")
                                Letra_A.play()
                                time.sleep(5)
                                v=''
                                i=0
                                aleb=''
                                break
                    else:
                        print("Você errou,mas vai ganhar 1,5 pontos,A respota certa é (Banana)")
                        pontos+=1.5
                        Letra_A=pygame.mixer.Sound("Errou.wav")
                        Letra_A.play()
                        time.sleep(5)
                        v=''
                        i=0
                        aleb=''
                        dicacontagen=0
                        break
            elif Aleb == 'É amarela por fora e branca por dentro':
                print("O que é O que é,É amarela por fora e branca por dentro")
                Letra_A=pygame.mixer.Sound("Amarela.wav")
                Letra_A.play()
                time.sleep(5)
                print("Se você quiser usar A 'dica'digite 1,porém você vai ganhar menos pontos")
                Letra_A=pygame.mixer.Sound("dica.wav")
                Letra_A.play()
                time.sleep(5)
                while True:
                    dica1=random.choice(dicab)
                    V=input("")
                    if V == '1':
                        print(dica1)
                        dicacontagen+=1
                        dica1=random.choice(dicab)
                        continue
                    if V == 'Banana' or V == 'banana':
                            if dicacontagen > 0:
                                ganho-=1
                                pontos=ganho
                                print(f"Você ganhor {pontos} pontos")
                                ganho=7
                                dicacontagen=0
                                aleb=''
                                break
                            else:
                                Letra_A=pygame.mixer.Sound("smw_1-up.wav")
                                Letra_A.play()
                                time.sleep(2)
                                pontos+=7
                                print("Correto,A respota é (Banana)")
                                Letra_A=pygame.mixer.Sound("Correto.wav")
                                Letra_A.play()
                                time.sleep(5)
                                v=''
                                i=0
                                aleb=''
                                break
                    else:
                        print("Você errou,mas vai ganhar 1,5 pontos,A respota certa é (Banana)")
                        pontos+=1.5
                        Letra_A=pygame.mixer.Sound("Errou.wav")
                        Letra_A.play()
                        time.sleep(5)
                        v=''
                        i=0
                        aleb=''
                        dicacontagen=0
                        break
            elif Aleb == 'Dizem que sou rica em potássio':
                print("Dizem que sou rica em potássio")
                Letra_A=pygame.mixer.Sound("potássio.wav")
                Letra_A.play()
                time.sleep(5)
                print("Se você quiser usar A 'dica'digite 1,porém você vai ganhar menos pontos")
                Letra_A=pygame.mixer.Sound("dica.wav")
                Letra_A.play()
                time.sleep(5)
                while True:
                    dica1=random.choice(dicab)
                    V=input("")
                    if V == '1':
                        print(dica1)
                        dicacontagen+=1
                        dica1=random.choice(dicab)
                        continue
                    if V == 'Banana' or V == 'banana':
                            if dicacontagen > 0:
                                ganho-=1
                                pontos=ganho
                                print(f"Você ganhor {pontos} pontos")
                                ganho=7
                                dicacontagen=0
                                aleb=''
                                break
                            else:
                                Letra_A=pygame.mixer.Sound("smw_1-up.wav")
                                Letra_A.play()
                                time.sleep(2)
                                pontos+=7
                                print("Correto,A respota é (Banana)")
                                Letra_A=pygame.mixer.Sound("Correto.wav")
                                Letra_A.play()
                                time.sleep(5)
                                v=''
                                i=0
                                aleb=''
                                break
                    else:
                        print("Você errou,mas vai ganhar 1,5 pontos,A respota certa é (Casa)")
                        pontos+=1.5
                        Letra_A=pygame.mixer.Sound("Errou.wav")
                        Letra_A.play()
                        time.sleep(5)
                        v=''
                        i=0
                        aleb=''
                        dicacontagen=0
                        break
        if Ale == 'Casa':
            Alec=random.choice(textoc)
            if Alec == 'O que é, o que é? Sou um livro de memórias':
                print("O que é, o que é? Sou um livro de memórias com paredes em vez de páginas, e cada quarto conta uma história diferente, guardando o passado enquanto se prepara para o futuro.")
                Letra_A=pygame.mixer.Sound("livro de memórias.wav")
                Letra_A.play()
                time.sleep(7)
                print("Se você quiser usar A 'dica'digite 1,porém você vai ganhar menos pontos")
                Letra_A=pygame.mixer.Sound("dica.wav")
                Letra_A.play()
                time.sleep(5)
                while True:
                    dica2=random.choice(dicac)
                    V=input("")
                    if V == '1':
                        print(dica2)
                        dicacontagen+=1
                        dica2=random.choice(dicac)
                        continue
                    if V == 'Casa' or V == 'casa':
                            if dicacontagen > 0:
                                ganho-=1
                                pontos=ganho
                                print(f"Você ganhor {pontos} pontos")
                                ganho=7
                                dicacontagen=0
                                alec=''
                                break
                            else:
                                Letra_A=pygame.mixer.Sound("smw_1-up.wav")
                                Letra_A.play()
                                time.sleep(2)
                                pontos+=7
                                print("Correto,A respota é (Casa)")
                                Letra_A=pygame.mixer.Sound("Correto(Casa).wav")
                                Letra_A.play()
                                time.sleep(5)
                                v=''
                                i=0
                                alec=''
                                break
                    else:
                        print("Você errou,mas vai ganhar 1,5 pontos,A respota certa é (Casa)")
                        pontos+=1.5
                        Letra_A=pygame.mixer.Sound("Errou(Casa).wav")
                        Letra_A.play()
                        time.sleep(5)
                        v=''
                        i=0
                        alec=''
                        dicacontagen=0
                        break
            elif Alec == 'O que é, o que é? Começa em uma fundação':
                print("O que é, o que é? Começa em uma fundação, mas não é uma escola. Ganha janelas para o mundo, mas não tem olhos. Serve de abrigo para o corpo e para a alma")
                Letra_A=pygame.mixer.Sound("Começa em uma fundação.wav")
                Letra_A.play()
                time.sleep(5)
                print("Se você quiser usar A 'dica'digite 1,porém você vai ganhar menos pontos")
                Letra_A=pygame.mixer.Sound("dica.wav")
                Letra_A.play()
                time.sleep(5)
                while True:
                    dica2=random.choice(dicac)
                    V=input("")
                    if V == '1':
                        print(dica2)
                        dicacontagen+=1
                        dica2=random.choice(dicac)
                        continue
                    if V == 'Casa' or V == 'casa':
                            if dicacontagen > 0:
                                ganho-=1
                                pontos=ganho
                                print(f"Você ganhor {pontos} pontos")
                                ganho=7
                                dicacontagen=0
                                alec=''
                                break
                            else:
                                Letra_A=pygame.mixer.Sound("smw_1-up.wav")
                                Letra_A.play()
                                time.sleep(2)
                                pontos+=7
                                print("Correto,A respota é (Casa)")
                                Letra_A=pygame.mixer.Sound("Correto(Casa).wav")
                                Letra_A.play()
                                time.sleep(5)
                                v=''
                                i=0
                                alec=''
                                break
                    else:
                        print("Você errou,mas vai ganhar 1,5 pontos,A respota certa é (Casa)")
                        pontos+=1.5
                        Letra_A=pygame.mixer.Sound("Errou(Casa).wav")
                        Letra_A.play()
                        time.sleep(5)
                        v=''
                        i=0
                        alec=''
                        dicacontagen=0
                        break
            elif Alec == 'lar com vida e sentimento':
                print("O que é, o que é? Nasço com tijolos e cimento, mas me torno um lar com vida e sentimento. O que é?")
                Letra_A=pygame.mixer.Sound("lar com vida e sentimento.wav")
                Letra_A.play()
                time.sleep(5)
                print("Se você quiser usar A 'dica'digite 1,porém você vai ganhar menos pontos")
                Letra_A=pygame.mixer.Sound("dica.wav")
                Letra_A.play()
                time.sleep(5)
                while True:
                    dica2=random.choice(dicac)
                    V=input("")
                    if V == '1':
                        print(dica2)
                        dicacontagen+=1
                        dica2=random.choice(dicac)
                        continue
                    if V == 'Casa' or V == 'casa':
                            if dicacontagen > 0:
                                ganho-=1
                                pontos=ganho
                                print(f"Você ganhor {pontos} pontos")
                                ganho=7
                                dicacontagen=0
                                alec=''
                                break
                            else:
                                Letra_A=pygame.mixer.Sound("smw_1-up.wav")
                                Letra_A.play()
                                time.sleep(2)
                                pontos+=7
                                print("Correto,A respota é (Casa)")
                                Letra_A=pygame.mixer.Sound("Correto(Casa).wav")
                                Letra_A.play()
                                time.sleep(5)
                                v=''
                                i=0
                                alec=''
                                break
                    else:
                        print("Você errou,mas vai ganhar 1,5 pontos,A respota certa é (Casa)")
                        pontos+=1.5
                        Letra_A=pygame.mixer.Sound("Errou(Casa).wav")
                        Letra_A.play()
                        time.sleep(5)
                        v=''
                        i=0
                        alec=''
                        dicacontagen=0
                        break
        if v == '':
            v=input("Dejesa continuar jogador ?:")
            if v == 'sim':
                continue
            elif v == 'não' or v == 'nao':
                break
            else:
                print(Ale)
print(f"Você concelho esse tanto de pontos[{pontos}] meus parabéns")