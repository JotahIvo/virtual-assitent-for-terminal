import os, sys
from ai_assistant import lu_translate, dev_lu


def main():
    os.system("clear")
    print('''Bem vindo a Assistente Virtual para Terminal LU!
Antes de começarmos... qual o seu nome?''')

    name = str(input())

    print("Qual linguagem de programação você está trabalhando nesse momento?")
    prog_lang = str(input())

    os.system("clear")
    print(f"Olá {name}, eu sou a LU, sua assistente virtual para terminal!")
    print("Vamos começar...")
    input()


    while True:
        os.system("clear")
        print('''[1] Para aprender a usar a LU
[2] Para usar a LU Translate
[3] Para usar a Dev LU
[4] Para sair        
        ''')
        option = int(input("Selecione a opção: "))

        match option:
            case 1:
                os.system("clear")
                print('''A LU tem 2 opções para ser usada:
1° é a LU Translate, que é o tradutor da LU, você escolhe a língua para que deseja traduzir e depois escrevea frase que deseja ser traduzida. Assim em um instante a LU traduz a frase e te manda de volta!

2° é a Dev LU, que te auxilia nos projetos que você está fazendo, a LU conhece todas as linguagens de programação! Sendo assim, você escolhe a linguagem que você está trabalhando e detalha o problema para a LU e em segundos ela resolve o problema para você!

Simples né? Para voltar ao menu principal e começar a usar, aperte ENTER...''')
                input()

            case 2:
                os.system("clear")
                print("Bem vindo ao LU Translate!!!")
                lang = str(input("Para língua você deseja traduzir sua mensagem? "))
                os.system("clear")
                print(f"Ótimo... eu sou fluente em {lang}!!!")
                text = str(input("Agora... escreva o que deseja traduzir: "))
                print("Traduzindo...")
                lu_translate(name, text, lang)
                input()

            case 3:
                os.system("clear")
                print("Bem vindo a Dev LU!")
                print(f"Descreva o seu problema {prog_lang} para que possamos resolver da melhor forma: ")
                problem = str(input())
                print("\nAguarde enquanto eu soluciono seu problema...\n")
                dev_lu(name, problem, prog_lang)
                input()

            case 4:
                print("Obrigado por usar a LU!!!")
                sys.exit()


if __name__ == "__main__":
    main()