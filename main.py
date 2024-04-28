# uso os asteriscos para importar todas funcionalidades do tkinter
from tkinter import * 
from tkinter import Tk, ttk

# importando barra de progresso tkinter
from PIL import Image, ImageTk

# importando matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from matplotlib.figure import Figure

# cores a serem utilizadas futuramente
co0 = "#2e2d2b" # Preto
co1 = "#feffff" # Branca
co2 = "#4fa882" # Verde
co3 = "#38576b" # Valor
co4 = "#403d3d" # Letra
co5 = "#e06636" 
co6 = "#038cfc" 
co7 = "#3fbfb9" 
co8 = "#263238"
co9 = "#e9edf5"

# Convertendo cores hexadecimais para RGB
def hex_to_rgb(hex_color):
    return tuple(int(hex_color[i:i+2], 16) / 255.0 for i in (1, 3, 5))

# Definindo as cores em formato RGB
colors = [hex_to_rgb('#5588bb'), hex_to_rgb('#66bbb'), hex_to_rgb('#99bb55'), hex_to_rgb('#ee9944'), hex_to_rgb('#444466'), hex_to_rgb('#bb5555')]

# Criando uma janela 
janela = Tk() # interface 
janela.title() # definindo titulo depois
janela.geometry('900x650') #  definindo largura e comprimento da tela  
janela.configure(background=co9) # Definindo uma cor de fundo 
janela.resizable(width=False, height=False)

style= ttk.Style(janela)
style.theme_use("clam")    # usando temas

# Criando frames para divisão da tela
frameCima = Frame(janela, width=1403, height=50, bg=co1, relief="flat")
frameCima.grid(row=0, column=0)

frameMeio = Frame(janela, width=1403, height=361, bg=co1, pady=20, relief="raised" )
frameMeio.grid(row=1, column=0, pady=1, padx=0, stick=NSEW)

frameBaixo = Frame(janela, width=1043, height=300, bg=co1, relief="flat")
frameBaixo.grid(row=2, column=0, pady=0, padx=10, stick=NSEW)

frame_gra_pie = Frame(frameMeio, width=580, height=250, bg=co2)
frame_gra_pie.place(x=415, y=5)

# Inserindo uma logo para o meu app no frameCima.
# acessando  a imagem
app_img = Image.open('logo.png')
app_img = app_img.resize((45,45))
app_img = ImageTk.PhotoImage(app_img)  # preparando a imagem para ser usada no tkinter

app_logo = Label(frameCima, image= app_img, text="Gerenciamento ", width=300, compound=LEFT, padx=5, relief=RAISED, anchor=NW,font=('Verdana 20 bold'), bg=co1, fg=co4 )# passando a imagem para dentro desse Label
app_logo.place(x=0, y=0)

# porcentagem
def porcentagem():
    l_nome = Label(frameMeio, text="Porcentagem da Receita gastos", height=1, anchor=NW, font=('Verdana 12'), bg=co1,fg=co4)
    l_nome.place(x=7, y=5)
    
    style = ttk.Style()
    style.theme_use('default')
    style.configure("black.Horizontal.TProgressbar", background=co3)
    style.configure("TProgressbar", thickness=25)

    bar = ttk.Progressbar(frameMeio, length=100)
    bar.place(x=10, y=35)
    bar['value'] = 50

    valor = 50
    l_porcentagm = Label(frameMeio, text="{:,.2f}%".format(valor), anchor=NW, font=('Verdana 12'), bg=co1,fg=co4)
    l_porcentagm.place(x=200, y=35)

# função para grafico
def grafico_bar():
    lista_categorias = ['Renda', 'Despesas', 'Saldo']
    lista_valores = [2000, 2500, 6236]

    # Fazendo figura e atribuindo objetos eixo
    figura = plt.figure(figsize=(4,3.45), dpi=60)
    ax = figura.add_subplot(111)
    #ax.autoscale(enable=True, axis='both', tight=None)

    ax.bar(lista_categorias, lista_valores, color=colors, width=0.9)

    c = 0 

    for i in ax.patches:
        ax.text(i.get_x()-0.1, i.get_height()+5,
                str("{:,.0f}".format(lista_valores[c])), fontsize=17, fontstyle='italic', verticalalignment='bottom', color=co4)

        c += 1
    ax.set_xticklabels(lista_categorias,fontsize=10)
    ax.patch.set_facecolor('#ffffff')
    ax.spines['bottom'].set_color('#CCCCCC')
    ax.spines['bottom'].set_linewidth(1)
    ax.spines['right'].set_linewidth(0)
    ax.spines['top'].set_linewidth(0)
    ax.spines['left'].set_color('#CCCCCC')
    ax.spines['left'].set_linewidth(1)

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.tick_params(bottom=False, left=False)
    ax.set_axisbelow(True)
    ax.yaxis.grid(False, color=co8)
    ax.xaxis.grid(False)

    canva = FigureCanvasTkAgg(figura,frameMeio)
    canva.get_tk_widget().place(x=10,y=70)


# criando uma função de resumo total

def resumo():
    valor = [1800,1650,150]

    l_linha = Label(frameMeio, text="", width=215,height=1, anchor=NW, font=('Arial 1'), bg=co0)
    l_linha.place(x=309, y=52)
    l_sumario = Label(frameMeio, text="total Renda Mensal      ".upper(), anchor=NW, font=('Verdana 12'), bg=co1, fg=co5)
    l_sumario.place(x=309, y=35)
    l_sumario = Label(frameMeio, text="R${:,.2f}".format(valor[0]), anchor=NW, font=('arial 17') ,bg=co1, fg=co7)
    l_sumario.place(x=309, y=70)

    l_linha = Label(frameMeio, text="", width=215,height=1, anchor=NW, font=('Arial 1'), bg=co0)
    l_linha.place(x=309, y=132)
    l_sumario = Label(frameMeio, text="total Despesas Mensais      ".upper(), anchor=NW, font=('Verdana 12'), bg=co1, fg=co5)
    l_sumario.place(x=309, y=115)
    l_sumario = Label(frameMeio, text="R${:,.2f}".format(valor[1]), anchor=NW, font=('arial 17') ,bg=co1, fg=co7)
    l_sumario.place(x=309, y=150)

    l_linha = Label(frameMeio, text="", width=215,height=1, anchor=NW, font=('Arial 1'), bg=co0)
    l_linha.place(x=309, y=207)
    l_sumario = Label(frameMeio, text="total Saldo                      ".upper(), anchor=NW, font=('Verdana 12'), bg=co1, fg=co5) # sando essa quantidade de backspace para cobrimento da barra 
    l_sumario.place(x=309, y=190)
    l_sumario = Label(frameMeio, text="R${:,.2f}".format(valor[2]), anchor=NW, font=('arial 17') ,bg=co1, fg=co7)
    l_sumario.place(x=309, y=220)

# funçãp gráfico pie
def grafico_pie():
    # Criando  figura e atribuindo  objetos de eixo
    figura = plt.Figure(figsize=(5, 3), dpi=90)
    ax = figura.add_subplot(111)

    lista_valores = [345,225,534]
    lista_categorias = ['Renda', 'Despesa', 'Saldo']

    #only "explode" the 2nd slice (i.e. 'Hogs')

    explode = []
    for i in lista_categorias:
        explode.append(0.05)

    ax.pie(lista_valores, explode=explode, wedgeprops=dict(width=0.2), autopct='%1.1f%%', colors=colors,shadow=True, startangle=90)
    ax.legend(lista_categorias, loc="center right", bbox_to_anchor=(1.55, 0.50))

    canva_categoria = FigureCanvasTkAgg(figura, frame_gra_pie)
    canva_categoria.get_tk_widget().grid(row=0, column=0)


grafico_pie()
resumo()
porcentagem()
grafico_bar()

#Criando frames dentro do frame Baixo
frame_renda = Frame(frameBaixo, width=300, height=205, bg=co1)
frame_renda.grid(row=0, column=0)

frame_operacoes = Frame(frameBaixo, width=220, height=250, bg=co1)
frame_operacoes.grid(row=0, column=0, padx=5)

frame_configuracao = Frame(frameBaixo, width=220, height=250, bg=co1)
frame_configuracao.grid(row=0, column=2, padx=5)

#Tabela Renda Mensal

app_tabela = Label(frameMeio, text="Tabela de Despesa", anchor=NW,font=('Verdana 12'), bg=co1, fg=co4 )
app_tabela.place(x=5, y=309)

#função mostrar renda
def mostrar_renda():
    tabela_head = ['#id', 'Categoria', 'Data', 'Quantia']
    lista_items = [[0, 'Categoria A', '2024-04-27', 1000],
                   [1, 'Categoria B', '2024-04-27', 1500],
                   [2, 'Categoria C', '2024-04-27', 2000],
                   [3, 'Categoria D', '2024-04-27', 2500]]

    global UnicodeTranslateError
    tree = ttk.Treeview(frame_renda, selectmode="extended", columns=tabela_head, show="headings")

    vsb = ttk.Scrollbar(frame_renda, orient="vertical", command=tree.yview)
    hsb = ttk.Scrollbar(frame_renda, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree.grid(column=0, row=0, stick='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, stick='ew')

    hd=["center", "center", "center", "center"]
    h=[30,150,100,60]
    n =0

    for col in tabela_head:
        tree.heading(col, text=col.title(), anchor=CENTER)
        tree.column(col, width=h[n], anchor=hd[n])

        n+=1
    for item in lista_items:
        tree.insert(' ', 'end', values=item)

mostrar_renda()

janela.mainloop()
