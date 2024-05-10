import pyautogui
import time

pyautogui.PAUSE = 0.8

# Abrir o sistema da empresa
 
# abrir navegador
pyautogui.press("win")
pyautogui.write("chrome")
time.sleep(2)
pyautogui.press("enter")

# entrar no site (https://dlp.hashtagtreinamentos.com/python/intensivao/login)
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

time.sleep(3)

# Fazer login
pyautogui.click(x=888, y=464)
pyautogui.write("SeuEmail")

# passar para o outro campo
pyautogui.press("tab")

pyautogui.write("DigiteSuaSenha")

pyautogui.press("tab")
pyautogui.press("enter")

time.sleep(3)

# Abrir/importar base de dados
import pandas as pd

tabela = pd.read_csv("produtos.csv")

# Cadastrar um produto
for linha in tabela.index:
    pyautogui.click(x=575, y=322)

    # preencher código
    pyautogui.write(str(tabela.loc[linha, "codigo"]))

    pyautogui.press("tab")

    # marca
    pyautogui.write(str(tabela.loc[linha, "marca"]))

    pyautogui.press("tab")

    # tipo
    pyautogui.write(str(tabela.loc[linha, "tipo"]))

    pyautogui.press("tab")

    # categoria
    pyautogui.write(str(tabela.loc[linha, "categoria"]))

    pyautogui.press("tab")

    # preço
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))

    pyautogui.press("tab")

    # custo
    pyautogui.write(str(tabela.loc[linha, "custo"]))

    pyautogui.press("tab")

    # obs
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)
    
    pyautogui.press("tab")

    # confirmar
    pyautogui.press("enter")
    pyautogui.scroll(700)