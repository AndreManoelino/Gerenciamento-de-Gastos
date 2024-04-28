from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

from tkcalendar import DateEntry, Calendar
# Definição das cores
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

def hex_to_rgb(hex_color):
    return tuple(int(hex_color[i:i+2], 16) / 255.0 for i in (1, 3, 5))

colors = [hex_to_rgb('#5588bb'), hex_to_rgb('#66bbb'), hex_to_rgb('#99bb55'), hex_to_rgb('#ee9944'), hex_to_rgb('#444466'), hex_to_rgb('#bb5555')]

# Criação da janela principal
janela = Tk()
janela.title("Gerenciamento")
janela.geometry('900x650')
janela.configure(background=co9)
janela.resizable(width=False, height=False)

# Criação dos frames
frameCima = Frame(janela, width=900, height=50, bg=co1, relief="flat")
frameCima.grid(row=0, column=0)

frameMeio = Frame(janela, width=900, height=300, bg=co1, pady=20, relief="raised")
frameMeio.grid(row=1, column=0, pady=1, padx=0)

frameBaixo = Frame(janela, width=900, height=300, bg=co1, relief="flat")
frameBaixo.grid(row=2, column=0, pady=0, padx=0)

frame_gra_pie = Frame(frameMeio, width=300, height=250, bg=co2)
frame_gra_pie.place(x=580, y=5)

# Inserção da logo
app_img = Image.open('logo.png')
app_img = app_img.resize((45, 45))
app_img = ImageTk.PhotoImage(app_img)
app_logo = Label(frameCima, image=app_img, text="Gerenciamento ", width=300, compound=LEFT, padx=5, relief=RAISED, anchor=NW, font=('Verdana 20 bold'), bg=co1, fg=co4)
app_logo.pack()

# Função para porcentagem
def porcentagem():
    l_nome = Label(frameMeio, text="Porcentagem da Receita gastos", height=1, anchor=NW, font=('Verdana 12'), bg=co1, fg=co4)
    l_nome.place(x=10, y=5)
    
    style = ttk.Style()
    style.theme_use('default')
    style.configure("black.Horizontal.TProgressbar", background=co3)
    style.configure("TProgressbar", thickness=25)

    bar = ttk.Progressbar(frameMeio, length=100)
    bar.place(x=10, y=35)
    bar['value'] = 50

    valor = 50
    l_porcentagm = Label(frameMeio, text="{:,.2f}%".format(valor), anchor=NW, font=('Verdana 12'), bg=co1, fg=co4)
    l_porcentagm.place(x=200, y=35)

# Função para gráfico de barras
def grafico_bar():
    lista_categorias = ['Renda', 'Despesas', 'Saldo']
    lista_valores = [2000, 2500, 6236]

    figura = plt.Figure(figsize=(4, 3.45), dpi=60)
    ax = figura.add_subplot(111)

    ax.bar(lista_categorias, lista_valores, color=colors, width=0.9)

    c = 0 

    for i in ax.patches:
        ax.text(i.get_x()-0.1, i.get_height()+5,
                str("{:,.0f}".format(lista_valores[c])), fontsize=17, fontstyle='italic', verticalalignment='bottom', color=co4)

        c += 1
    ax.set_xticklabels(lista_categorias, fontsize=10)
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

    canva = FigureCanvasTkAgg(figura, frameMeio)
    canva.get_tk_widget().place(x=10, y=70)

# Função para resumo total
def resumo():
    valor = [1800, 1650, 150]

    l_linha = Label(frameMeio, text="", width=215, height=1, anchor=NW, font=('Arial 1'), bg=co0)
    l_linha.place(x=309, y=52)
    l_sumario = Label(frameMeio, text="total Renda Mensal        ".upper(), anchor=NW, font=('Verdana 12'), bg=co1, fg=co5)
    l_sumario.place(x=309, y=35)
    l_sumario = Label(frameMeio, text="R${:,.2f}".format(valor[0]), anchor=NW, font=('arial 17'), bg=co1, fg=co7)
    l_sumario.place(x=309, y=70)

    l_linha = Label(frameMeio, text="", width=215, height=1, anchor=NW, font=('Arial 1'), bg=co0)
    l_linha.place(x=309, y=132)
    l_sumario = Label(frameMeio, text="total Despesas Mensais".upper(), anchor=NW, font=('Verdana 12'), bg=co1, fg=co5)
    l_sumario.place(x=309, y=115)
    l_sumario = Label(frameMeio, text="R${:,.2f}".format(valor[1]), anchor=NW, font=('arial 17'), bg=co1, fg=co7)
    l_sumario.place(x=309, y=150)

    l_linha = Label(frameMeio, text="", width=215, height=1, anchor=NW, font=('Arial 1'), bg=co0)
    l_linha.place(x=309, y=207)
    l_sumario = Label(frameMeio, text="total Saldo                      ".upper(), anchor=NW, font=('Verdana 12'), bg=co1, fg=co5)
    l_sumario.place(x=309, y=190)
    l_sumario = Label(frameMeio, text="R${:,.2f}".format(valor[2]), anchor=NW, font=('arial 17'), bg=co1, fg=co7)
    l_sumario.place(x=309, y=220)

# Função para gráfico de pizza
def grafico_pie():
    figura = plt.Figure(figsize=(5, 3), dpi=90)
    ax = figura.add_subplot(111)

    lista_valores = [345, 225, 534]
    lista_categorias = ['Renda', 'Despesa', 'Saldo']

    explode = []
    for i in lista_categorias:
        explode.append(0.05)

    ax.pie(lista_valores, explode=explode, wedgeprops=dict(width=0.2), autopct='%1.1f%%', colors=colors, shadow=True, startangle=90)
    ax.legend(lista_categorias, loc="center right", bbox_to_anchor=(1.55, 0.50))

    canva_categoria = FigureCanvasTkAgg(figura, frame_gra_pie)
    canva_categoria.get_tk_widget().grid(row=0, column=0)

# Chamada das funções
grafico_pie()
resumo()
porcentagem()
grafico_bar()

# Frames dentro do frameBaixo
frame_renda = Frame(frameBaixo, width=300, height=205, bg=co1)
frame_renda.grid(row=0, column=0)

frame_operacoes = Frame(frameBaixo, width=220, height=250, bg=co1)
frame_operacoes.grid(row=0, column=1, padx=5)

frame_configuracao = Frame(frameBaixo, width=220, height=250, bg=co1)
frame_configuracao.grid(row=0, column=2, padx=5)

# Tabela de Despesas
app_tabela = Label(frameMeio, text="Tabela de Despesa", anchor=NW, font=('Verdana 12'), bg=co1, fg=co4)
app_tabela.place(x=5, y=309)

def mostrar_renda():
    tabela_head = ['#id', 'Categoria', 'Data', 'Quantia']
    lista_items = [[0, 'A', '29/05/2024', '1.800,00'],
                   [1, 'B', '29/05/2024', '800,00'],
                   [2, ' C', '29/05/2024', '350,00'],
                   [3, ' D', '29/05/2024', '798.00']]

    tree = ttk.Treeview(frame_renda, selectmode="extended", columns=tabela_head, show="headings")

    vsb = ttk.Scrollbar(frame_renda, orient="vertical", command=tree.yview)
    hsb = ttk.Scrollbar(frame_renda, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree.grid(column=0, row=0, stick='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, stick='ew')

    hd=["center", "center", "center", "center"]
    h=[30, 150, 100, 60]
    n = 0

    for col in tabela_head:
        tree.heading(col, text=col.title(), anchor=CENTER)
        tree.column(col, width=h[n], anchor=hd[n])

        n += 1
    for item in lista_items:
        tree.insert('', 'end', values=item)

mostrar_renda()

# Configurações de despesas 
l_info = Label(frame_operacoes, text="Insira novas despesas", height=1, anchor=NW, font=('Verdana 10 bold'), bg=co1, fg=co4)
l_info.place(x=10, y=10)

l_categoria = Label(frame_operacoes, text="Categoria", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_categoria.place(x=10, y=38)

# Pegando categorias

categoria_funcao = ['Alguel', 'Comida']
categoria = []

for i in categoria_funcao:
    categoria.append(i[1]) # Passando esse valor para pegar valores depois do id somente os valores da categoria

combo_categoria_despesas = ttk.Combobox(frame_operacoes, width=10, font=('Ivy 10'))
combo_categoria_despesas['values'] = (categoria)
combo_categoria_despesas.place(x=110, y=41)

#Despesas-------------------------------------------------------------------
l_despesas = Label(frame_operacoes, text='Data', height=1,anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_despesas.place(x=10,y=70)
e_cal_despesas = DateEntry(frame_operacoes,wigth=12,background='darkblue', foreground='white',borderwigth=2, year=2024)
e_cal_despesas.place(x=110,y=71)

a_valor_despesas = Label(frame_operacoes, text='Quantia Total', height=1,anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
a_valor_despesas.place(x=8,y=100)
e_valor_despesas = Entry(frame_operacoes,width=14, justify='left', relief='solid')
e_valor_despesas.place(x=110,y=100)

# Botão de inserir

L_adicionar = Label(frame_operacoes, text="Adicionar ",height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
L_adicionar.place(x=7,y=130)

img_add_despesas = Image.open('add.png')
img_add_despesas = img_add_despesas.resize((5, 5))
img_add_despesas = ImageTk.PhotoImage(img_add_despesas)
botao_inserir_despesas = Button(frame_operacoes, image=img_add_despesas, text="Adicionar".upper(), width=80, compound=LEFT,anchor=NW, font=('Ivy 7 bold'), bg=co1, fg=co2,overrelief=RIDGE)
botao_inserir_despesas.place(x=110,y=131)


# Botão de excluir

L_excluir = Label(frame_operacoes, text="Excluir Ações",height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
L_excluir.place(x=10,y=191)

img_delete_despesas = Image.open('remover.png')
img_delete_despesas = img_delete_despesas.resize((5, 5))
img_delete_despesas = ImageTk.PhotoImage(img_delete_despesas)
botao_inserir_despesas = Button(frame_operacoes, image=img_delete_despesas, text="Remover".upper(), width=80, compound=LEFT,anchor=NW, font=('Ivy 7 bold'), bg=co1, fg=co2,overrelief=RIDGE)
botao_inserir_despesas.place(x=120,y=190)





janela.mainloop()