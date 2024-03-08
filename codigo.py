# Passo a passo do projeto

# Passo 1: Entrar no sistema da empresa
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login
import pyautogui
import time

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



# Passo 4: Cadastrar um produto

# Passo 5: Repetir o processo até acabar
