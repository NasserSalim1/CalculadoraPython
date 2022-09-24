# Fazer a janela do app
# Importando biblioteca tkinter
from tkinter import *
from tkinter import ttk

# Cores

cor1 = '#3b3b3b' # Preta
cor2 = '#feffff' # Branca
cor3 = '#38576b' # Azul
cor4 = '#ECEFF1' # Cinza
cor5 = '#FFAB40' # Laranja

janela = Tk()
janela.title('Calculadora')
janela.geometry('235x309')
janela.config(bg = cor1)

# criando frames

frame_tela = Frame(janela, width = 235, height = 50,  bg = cor3)
frame_tela.grid(row = 0, column = 0)

frame_corpo = Frame(janela, width = 235, height = 268)
frame_corpo.grid(row = 1, column = 0)

# varavel todos_valores
todos_valores = ''

# criando label
valor_texto = StringVar()

# criando função
def entrar_valor(i):

    global todos_valores
    todos_valores = todos_valores + str(i)

    # passando valor para tela
    valor_texto .set(todos_valores)

# função para calcular

def calcular():
    global todos_valores
    resultado = eval(todos_valores)
    valor_texto.set(str(resultado))
# função limpar tela

def limpar_tela():
    global todos_valores
    todos_valores = ''
    valor_texto.set('')
    resultado = ''
app_label = Label(frame_tela, textvariable = valor_texto, width = 16, height = 2, padx = 7, relief = FLAT, anchor = 'e', justify = RIGHT, font = ('Ivy 18 '), bg = cor3, fg = cor2)
app_label.place(x = 0, y = 0)

# criando botões

b_1 = Button(frame_corpo, command = limpar_tela, text = "C", width = 11, height = 2, bg = cor4, font = ('Ivy 13 bold'), relief = RAISED, overrelief = RIDGE)
b_1.place(x = 0, y = 0)
b_2 = Button(frame_corpo, command = lambda: entrar_valor('%'), text = "%", width = 5, height = 2, bg = cor4, font = ('Ivy 13 bold'), relief = RAISED, overrelief = RIDGE)
b_2.place(x = 118.5, y = 0)
b_3 = Button(frame_corpo, command = lambda: entrar_valor('/'),text = "/", width = 5, height = 2, bg = cor5, fg = cor2, font = ('Ivy 13 bold'), relief = RAISED, overrelief = RIDGE)
b_3.place(x = 177, y = 0)

b_4 = Button(frame_corpo, command = lambda: entrar_valor('7'), text = "7", width = 5, height = 2, bg = cor4, font = ('Ivy 13 bold'), relief = RAISED, overrelief = RIDGE)
b_4.place(x = 0, y = 52)
b_5 = Button(frame_corpo, command = lambda: entrar_valor('8'), text = "8", width = 5, height = 2, bg = cor4, font = ('Ivy 13 bold'), relief = RAISED, overrelief = RIDGE)
b_5.place(x = 59, y = 52)
b_6 = Button(frame_corpo, command = lambda: entrar_valor('9'), text = "9", width = 5, height = 2, bg = cor4, font = ('Ivy 13 bold'), relief = RAISED, overrelief = RIDGE)
b_6.place(x = 118, y = 52)
b_7 = Button(frame_corpo, command = lambda: entrar_valor('*'), text = "*", width = 5, height = 2, bg = cor5, fg = cor2, font = ('Ivy 13 bold'), relief = RAISED, overrelief = RIDGE)
b_7.place(x = 177, y = 52)

b_8 = Button(frame_corpo, command = lambda: entrar_valor('4'), text = "4", width = 5, height = 2, bg = cor4, font = ('Ivy 13 bold'), relief = RAISED, overrelief = RIDGE)
b_8.place(x = 0, y = 104)
b_9 = Button(frame_corpo, command = lambda: entrar_valor('5'), text = "5", width = 5, height = 2, bg = cor4, font = ('Ivy 13 bold'), relief = RAISED, overrelief = RIDGE)
b_9.place(x = 59, y = 104)
b_10 = Button(frame_corpo, command = lambda: entrar_valor('6'), text = "6", width = 5, height = 2, bg = cor4, font = ('Ivy 13 bold'), relief = RAISED, overrelief = RIDGE)
b_10.place(x = 118, y = 104)
b_11 = Button(frame_corpo, command = lambda: entrar_valor('-'), text = "-", width = 5, height = 2, bg = cor5, fg = cor2, font = ('Ivy 13 bold'), relief = RAISED, overrelief = RIDGE)
b_11.place(x = 177, y = 104)

b_12 = Button(frame_corpo, command = lambda: entrar_valor('1'), text = "1", width = 5, height = 2, bg = cor4, font = ('Ivy 13 bold'), relief = RAISED, overrelief = RIDGE)
b_12.place(x = 0, y = 155)
b_13 = Button(frame_corpo, command = lambda: entrar_valor('2'), text = "2", width = 5, height = 2, bg = cor4, font = ('Ivy 13 bold'), relief = RAISED, overrelief = RIDGE)
b_13.place(x = 59, y = 155)
b_14 = Button(frame_corpo, command = lambda: entrar_valor('3'), text = "3", width = 5, height = 2, bg = cor4, font = ('Ivy 13 bold'), relief = RAISED, overrelief = RIDGE)
b_14.place(x = 118, y = 155)
b_15 = Button(frame_corpo, command = lambda: entrar_valor('+'), text = "+", width = 5, height = 2, bg = cor5, fg = cor2, font = ('Ivy 13 bold'), relief = RAISED, overrelief = RIDGE)
b_15.place(x = 177, y = 155)

b_16 = Button(frame_corpo, command = lambda: entrar_valor('0'), text = "0", width = 11, height = 2, bg = cor4, font = ('Ivy 13 bold'), relief = RAISED, overrelief = RIDGE)
b_16.place(x = 0, y = 207)
b_17 = Button(frame_corpo, command = lambda: entrar_valor('.'), text = ".", width = 5, height = 2, bg = cor4, font = ('Ivy 13 bold'), relief = RAISED, overrelief = RIDGE)
b_17.place(x = 118, y = 207)
b_18 = Button(frame_corpo, command = calcular, text = "=", width = 5, height = 2, bg = cor5, fg = cor2, font = ('Ivy 13 bold'), relief = RAISED, overrelief = RIDGE)
b_18.place(x = 177, y = 207)

janela.mainloop()

"""
Operações matemáricas

-> Colocar 'int' antes de 'input' quando for usar números

# 1. Adição
# 2. Subtração
# 3. Multiplicação
# 4. Divisão


num1 = float(input('Digite o seu primeiro número: ')) # Variável do numero ja atribuindo seu valor
num2 = float(input('Digite o seu segundo número: '))

print('Escolha uma operação: ')
print('1. Para adição')
print('2. Para subtração')
print('3. Para multiplicação')
print('4. Para divisão')
print('5. Exit')

while(True):
    escolha = int(input('Escolha uma operação: '))
    if escolha in (1, 2, 3, 4, 5):
        if escolha == 1: # Adição
            print(f'A soma é: {num1 + num2}')
        elif escolha == 2: # Subtração
            print(f'A subtração é: {num1 - num2}')
        elif escolha == 3: # Multiplicação
            print(f'A multiplicação é: {num1 * num2}')
        elif escolha == 4: # Divisão
            print(f'A divisão é: {num1 / num2}')
        elif escolha == 5: # Exit
            print('Obrigado!')
            exit()
    else:
        print('Opção inválida, tente denovo!')
"""