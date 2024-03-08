# Passo a passo do projeto

# Passo 1: Entrar no sistema da empresa
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login
import pyautogui
import time
import pandas

pyautogui.PAUSE = 0.5

    #abrir navegador
pyautogui.press("win")
pyautogui.write("firefox")
pyautogui.press("enter")

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

    #Delay
time.sleep(3)

# Passo 2: Fazer Login
    #login
pyautogui.click(x=681, y=376)
pyautogui.write("usuario@gmail.com")
    #senha
pyautogui.press("tab")
pyautogui.write("senha123")
pyautogui.press("enter")

# Passo 3: Importar a base de dados
    #delay
time.sleep(3)

    #importar tabela
tabela = pandas.read_csv("produtos.csv")

# Passo 4: Cadastrar um produto

    #Para cada linha
for linha  in tabela.index:

        #Clicar no 1º campo
    pyautogui.click(x=688, y=258)

        #Cadastro

            #Codigo
    pyautogui.write(tabela.loc[linha, "codigo"])
    pyautogui.press("tab")

            #Marca
    pyautogui.write(tabela.loc[linha, "marca"])
    pyautogui.press("tab")

            #Tipo
    pyautogui.write(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")

            #Categoria
    pyautogui.write(tabela.loc[linha, "categoria"])
    pyautogui.press("tab")

            #Preço
    pyautogui.write(tabela.loc[linha, "preco_unitario"])
    pyautogui.press("tab")

            #Custo
    pyautogui.write(tabela.loc[linha, "custo"])
    pyautogui.press("tab")

            #OBS
    pyautogui.write(tabela.loc[linha, "obs"])
    pyautogui.press("tab")

            #Enviar
    pyautogui.press("enter")

            #Voltar para o inicio da tela
    pyautogui.scroll(5000)

# Passo 5: Repetir o processo até acabar
