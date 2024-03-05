from tkinter import *

# cores
cor1 = "#0a0a0a"  # preta
cor6 = "#3080f0"  # azul

# Configurando a janela -----------
janela = Tk()
janela.title("")
janela.geometry('300x180')
janela.configure(bg=cor1)
janela.resizable(width=FALSE, height=FALSE)

# Definindo variáveis globais
tempo = "00:00:00"
rodar = False
contador = 0
limitador = 59

# Função
def iniciar():
    global tempo
    global contador
    global limitador
    if rodar:
        # Antes do cronômetro começar
        if contador < 5:  # Ajuste o valor conforme necessário
            inicio = 'Começando em ' + str(5 - contador) + ' segundos'
            label_tempo['text'] = inicio
            label_tempo['font'] = 'Arial 10'
        else:
            label_tempo['font'] = 'times 50 bold'

            h, m, s = map(int, tempo.split(":"))

            if s >= limitador:
                contador = 0
                m += 1

            s = str(s + 1).zfill(2)
            m = str(m).zfill(2)
            h = str(h).zfill(2)

            # Atualizando os valores atuais
            tempo = h + ":" + m + ":" + s
            label_tempo['text'] = tempo

        label_tempo.after(1000, iniciar)
        contador += 1

# Função para dar início
def start():
    global rodar
    rodar = True
    iniciar()

# Função para pausar
def pausar():
    global rodar
    rodar = False

# Função para reiniciar
def reiniciar():
    global rodar
    global contador
    rodar = True
    contador = 0
    iniciar()

# Criando labels
label_app = Label(janela, text="Cronômetro", font="Arial 10", bg=cor1, fg=cor6)
label_app.place(x=20, y=5)

label_tempo = Label(janela, text=tempo, font=('times 50 bold'), bg=cor1, fg=cor6)
label_tempo.place(x=20, y=25)

# Criando botões
botao_iniciar = Button(janela, text="Iniciar", width=10, height=2, bg=cor1, fg=cor6, font=('Ivy 8 bold'), relief='raised', overrelief='ridge', command=start)
botao_iniciar.place(x=20, y=130)

botao_Pausa = Button(janela, text="Pausar", width=10, height=2, bg=cor1, fg=cor6, font=('Ivy 8 bold'), relief='raised', overrelief='ridge', command=pausar)
botao_Pausa.place(x=105, y=130)

botao_reiniciar = Button(janela, text="Reiniciar", width=10, height=2, bg=cor1, fg=cor6, font=('Ivy 8 bold'), relief='raised', overrelief='ridge', command=reiniciar)
botao_reiniciar.place(x=190, y=130)

janela.mainloop()
