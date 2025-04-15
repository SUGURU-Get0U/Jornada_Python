import pyautogui
import time


# Escrever o Passo a passo de como fazer manualmente o cadastro de algo no site da empresa
# // inserir o delay do comando para evitar bugs:
pyautogui.PAUSE = 0.4
# 1- abrir o chrome
pyautogui.press("win")     # ]
pyautogui.write("chrome")  # } -> aperta o botao windows, digita chrome e aperta a tecla enter
pyautogui.press("enter")   # ]
pyautogui.click(x=831, y=493)
# 2- digitar a url do site da empresa
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login") # } -> espera 0.5 segundos, digita a URL e aperta a tecla ENTER
pyautogui.press("enter")                                                       # 
# 3- fazer login no site da empresa
pyautogui.click(x=845, y=406) # clica na aba de digitar user
# 3.1) digitar user
pyautogui.write("GojoSatoruTheHonoredOne")
pyautogui.press("tab") # pula para a aba da senha
pyautogui.press("enter")
# 3.2) digitar senha
pyautogui.write("banana123")
pyautogui.press("enter")
# 4- cadastar os items

time.sleep(1) # esperar o site carregar

import pandas 

Tabela = pandas.read_csv("produtos.csv") # usa a biblioteca pandas para ler a planilha  

for linhas in Tabela.index: 

    # Selecionar a primeira aba
    pyautogui.click(x=798, y=291)

    # Digita a parte do codigo da tabela:
    codigo = Tabela.loc[linhas, "codigo"]
    pyautogui.write(str(codigo))

    # passa para proximo
    pyautogui.press("tab")

    # Digita a parte da marca da tabela:
    marca = Tabela.loc[linhas, 'marca']
    pyautogui.write(str(marca))

    # passa para proximo
    pyautogui.press("tab")

    # Digita a parte do tipo da tabela:
    tipo = Tabela.loc[linhas, "tipo"]
    pyautogui.write(str(tipo))

    # passa para proximo
    pyautogui.press("tab")
    
    # Digita a parte do tipo da tabela:
    categoria = Tabela.loc[linhas, "categoria"]
    pyautogui.write(str(categoria))

    # passa para proximo
    pyautogui.press("tab")

    # Digita a parte do preco da tabela:
    preco_unitario = Tabela.loc[linhas, "preco_unitario"]
    pyautogui.write(str(preco_unitario))

    # passa para proximo
    pyautogui.press("tab")

    # Digita a parte do custo da tabela:
    custo = Tabela.loc[linhas, "custo"]
    pyautogui.write(str(custo))

    # passa para proximo
    pyautogui.press("tab")

    # Digita a parte das observacoes da tabela:
     # condicional para evitar o print de NAN -> not a number
    obs = Tabela.loc[linhas, "obs"]
    if pandas.isna(obs) != True:
        pyautogui.write(str(obs))

    # recomeca o processo
    pyautogui.press("tab") 
    pyautogui.press("Enter")   

    pyautogui.scroll(10000)              