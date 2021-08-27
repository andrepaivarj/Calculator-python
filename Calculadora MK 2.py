def numero():
    def menu_numero():
        print('\n  CALCULADORA NÙMEROS  \n\n')
        print('  Digite: ')
        print('1 - SOMA ')
        print('2 - SUBTRAÇÃO ')
        print('3 - MULTIPLICAÇÃO ')
        print('4 - DIVISÃO ')
        print('5 - EXPONENCIAÇÃO ')
        print('6 - RADICIAÇÃO ')
        print('7 - CONSULTA PRIMO ')
        print('V - VOLTAR ')
        opcao_numero = input('\nQUAL A OPCÃO DESEJADA ? ')
        return (opcao_numero)
    
    def primo():
        n = int(input('Insira um numero: '))
        contdiv = 0
        div = []
        for i in range (1,n,1):
            if n % i == 0:
                contdiv = contdiv + 1
                div.append(i)
        if contdiv < 2:
            print('O Número é Primo!!!\n')
        else:
            print ('O Número não é primo e é divisível por ', contdiv,' numeros que sao:', div,'\n')        

    def soma():
        a = float(input('Insira um número: '))
        b = float(input('Insira outro número: '))
        c = a + b
        print('A Soma dos números ', a,' e ',b,' é: ',c,'\n')

    def subtracao():
        a = float(input('Insira um número: '))
        b = float(input('Insira outro número: '))
        c = a - b
        print('A Subtração dos números ', a,' e ',b,' é: ',c,'\n')
        
    def multiplicacao():
        a = float(input('Insira um número: '))
        b = float(input('Insira outro número: '))
        c = a * b
        print('A Multiplicação dos números ', a,' e ',b,' é: ',c,'\n')

    def divisao():
        a = float(input('Insira um número: '))
        b = float(input('Insira outro número: '))
        c = a / b
        print('A Divisão dos números ', a,' e ',b,' é: ',c,'\n')

    def exponenciacao():
        a = float(input('Insira um número: '))
        b = float(input('Insira outro número: '))
        c = a ** b
        print('A Exponenciação dos números ', a,' e ',b,' é: ',c,'\n')

    def radiciacao():
        a = float(input('Insira um número: '))
        b = float(input('Insira outro número: '))
        c = a ** (1/b)
        print('A Radiciação dos números ', a,' e ',b,' é: ',c,'\n')

    opcao_numero = menu_numero()
    while opcao_numero != 'V':
        if opcao_numero == '1' :
            soma()
        elif opcao_numero == '2' :
            subtracao()
        elif opcao_numero == '3' :
            multiplicacao()
        elif opcao_numero == '4' :
            divisao()
        elif opcao_numero == '5' :
            exponenciacao()
        elif opcao_numero == '6' :
            radiciacao()
        elif opcao_numero == '7' :
            primo()
        else:
            print('Opcão Inválida\n')
        opcao_numero = menu_numero()

        
def vetor():
    def menu_vetor():
        print('\nCALCULADORA VETORIAL \n\n')
        print('DIGITE:\n\n1 - SOMA VETORIAL\n2 - SUBTRACAO VETORIAL\n3- MULTIPLICACÃO ESCALAR\n4 - MULTIPLICACÃO VETORIAL\nV -VOLTAR AO MENU PRINCIPAL')
        opcao_vetor = input('QUAL A OPCÃO DESEJADA? ')
        return(opcao_vetor)
    
    def soma():
        vetor1 = []
        dim1  = int(input('\nInsira a dimensao do vetor: '))
        for i in range (0, dim1):
            aij = int(input('Insira um elemnto do vetor: '))
            vetor1.append(aij)

        vetor2 = []
        dim2  = int(input('Insira a dimensao do vetor: '))
        for j in range (0, dim2):
            bij = int(input('Insira um elemnto do vetor: '))
            vetor2.append(bij)

        vetorsoma = []
        if (dim1 == dim2):
            for k in range (0,dim1):
                s = vetor1[k] + vetor2[k]
                vetorsoma.append(s)
            print('A soma dos vetores ', vetor1,' e ', vetor2,' é: ', vetorsoma,'\n')
        else:
            print('Não foi possível somar os vetores...\n')

    def subtracao():
        vetor1 = []
        dim1  = int(input('\nInsira a dimensao do vetor: '))
        for i in range (0, dim1):
            aij = int(input('Insira um elemnto do vetor: '))
            vetor1.append(aij)

        vetor2 = []
        dim2  = int(input('Insira a dimensao do vetor: '))
        for j in range (0, dim2):
            bij = int(input('Insira um elemnto do vetor: '))
            vetor2.append(bij)

        vetorsubt = []
        if (dim1 == dim2):
            for k in range (0,dim1):
                s = vetor1[k] - vetor2[k]
                vetorsubt.append(s)
            print('A subtracão dos vetores ', vetor1,' e ', vetor2,' é: ', vetorsubt,'\n')
        else:
            print('Não foi possível subtrair os vetores...\n')


    def multiplicacao_escalar():
        n = int(input('Insira o escalar a ser multiplicado: '))
        
        vetor1 = []
        dim1  = int(input('\nInsira a dimensao do vetor: '))
        for i in range (0, dim1):
            aij = int(input('Insira um elemnto do vetor: '))
            vetor1.append(aij)

        vetormultesc = []
        for j in range(len(vetor1)):
            vesc = vetor1[j] * n
            vetormultesc.append(vesc)
        print('A multiplicacão do vetor ',vetor1,' com o número ',n,' é: ', vetormultesc)
        
    def multiplicacao_vetorial():
        vetor1 = []
        dim1  = int(input('\nInsira a dimensao do vetor: '))
        for i in range (0, dim1):
            aij = int(input('Insira um elemnto do vetor: '))
            vetor1.append(aij)

        vetor2 = []
        dim2  = int(input('Insira a dimensao do vetor: '))
        for j in range (0, dim2):
            bij = int(input('Insira um elemnto do vetor: '))
            vetor2.append(bij)

        vetormult = []
        if (dim1 == dim2):
            for k in range (0,dim1):
                s = vetor1[k] * vetor2[k]
                vetormult.append(s)
            print('A multiplicacão dos vetores ', vetor1,' e ', vetor2,' é: ', vetormult,'\n')
        else:
            print('Não foi possível multiplicar os vetores...\n')

        
    opcao_vetor = menu_vetor()
    while opcao_vetor != 'V':
        if opcao_vetor == '1' :
            soma()
        elif opcao_vetor == '2' :
            subtracao()
        elif opcao_vetor == '3' :
            multiplicacao_escalar()
        elif opcao_vetor == '4' :
            multiplicacao_vetorial()
        else: 
            print('Opcão Inválida\n')
        opcao_vetor = menu_vetor()

def matriz():
    def soma():
        matriz1 = []
        linha = int(input('Informe a quantidade de linhas da matriz: '))
        coluna = int(input('Informe a quantidade de colunas da matriz: '))
        for i in range (0,linha):
            matriz1.append([])
            for j in range (0,coluna):
                aij = float(input('Insira um termo da matriz: '))
                matriz1[i].append(aij)
        
        matriz2 = []
        linha2 = int(input('Informe a quantidade de linhas da matriz: '))
        coluna2 = int(input('Informe a quantidade de colunas da matriz: '))
        for k in range (0,linha):
            matriz2.append([])
            for l in range (0,coluna):
                bij = float(input('Insira um termo da matriz: '))
                matriz2[k].append(bij)
        
        matrizsoma = []
        if (linha == linha2) and (coluna == coluna2):
            for m in range (0,linha):
                matrizsoma.append([])
                for n in range (0,coluna):
                    s = matriz1[m][n] + matriz2[m][n]
                    matrizsoma[m].append(s)
            print('A soma das matrizes ', matriz1,' e ', matriz2,' é: ', matrizsoma,'\n')
        else:
            print('Não foi possível somar as matrizes...\n')

    
    def subtracao():
        matriz1 = []
        linha = int(input('Informe a quantidade de linhas da matriz: '))
        coluna = int(input('Informe a quantidade de colunas da matriz: '))
        for i in range (0,linha):
            matriz1.append([])
            for j in range (0,coluna):
                aij = float(input('Insira um termo da matriz: '))
                matriz1[i].append(aij)
        
        matriz2 = []
        linha2 = int(input('Informe a quantidade de linhas da matriz: '))
        coluna2 = int(input('Informe a quantidade de colunas da matriz: '))
        for k in range (0,linha):
            matriz2.append([])
            for l in range (0,coluna):
                bij = float(input('Insira um termo da matriz: '))
                matriz2[k].append(bij)
        
        msub = []
        if (linha == linha2) and (coluna == coluna2):
            for m in range (0,linha):
                msub.append([])
                for n in range (0,coluna):
                    s = matriz1[m][n] - matriz2[m][n]
                    msub[m].append(s)
            print('A subtracão das matrizes ', matriz1,' e ', matriz2,' é: ', msub,'\n')
        else:
            print('Não foi possível somar as matrizes...\n')

    def mat_transposta():
        matriz1 = []
        linhas = len(matriz1)
        colunas = len(matriz1[0])
        At = [[0 for i in range(linhas)]for j in range (colunas)]
        for i in range (linhas):
            for j in range (colunas):
                At[j][i] = matriz1[i][j]
        return print ('A matriz transposta de',matriz1,' e: ', At)

    def new_func():
        matriz1 = []
        linha = int(input('Informe a quantidade de linhas da matriz: '))
        coluna = int(input('Informe a quantidade de colunas da matriz: '))
        for i in range (0,linha):
            matriz1.append([])
            for j in range (0,coluna):
                aij = float(input('Insira um termo da matriz: '))
                matriz1[i].append(aij)
        return matriz1
    
        
    def menu_matriz():
        print('   CALCULADORA DE MATRIZES\n\n')
        print('DIGITE: \n1 - SOMA \n2 - SUBTRACÃO \n3 - MATRIZ TRANSPOSTA \n4 - MULTIPLICACÃO ESCALAR \nV - VOLTAR AO MENU PRINCIPAL')
        opcao_matriz = input('\nQUAL A OPCÃO DESEJADA? ')
        return (opcao_matriz)

    opcao_matriz = menu_matriz()
    while opcao_matriz != 'V':
        if opcao_matriz == '1' :
            soma()
        elif opcao_matriz == '2' :
            subtracao()
        elif opcao_matriz == '3' :
            mat_transposta()    
        else:
            print('Opcão Inválida\n')
        opcao_matriz = menu_matriz()
        
def main():
    def menu():
        print('\n\nCALCULADORA MK-II \n\n')
        print('DIGITE:\n\n1 - NÚMEROS \n2- VETORES \n3 - MATRIZES')
        opcao = input('QUAL A OPCÃO DESEJADA? ')
        return(opcao)
        
    opcao = menu()
    while opcao != 'F':
        if opcao == '1' :
            numero()
        elif opcao == '2' :
            vetor()
        elif opcao == '3' :
            matriz()
        else:
            print('Opcão Inválida\n')
        opcao = menu()
    
    print('O Programa foi finalizado.')
main()