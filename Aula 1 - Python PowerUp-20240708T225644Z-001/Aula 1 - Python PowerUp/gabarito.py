# Passo a passo do projeto
# Passo 1: Entrar no sistema da empresa 
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login

import pyautogui 
import time

# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar 1 tecla
# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.hotkey -> combinação de teclas
pyautogui.PAUSE = 1

# abrir o navegador (chrome)
pyautogui.press("win")
time.sleep(1)
pyautogui.write("chrome")
time.sleep(1)
pyautogui.press("enter")
time.sleep(2)

# entrar no link 
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
time.sleep(1)
pyautogui.press("enter")
time.sleep(3)


# Passo 2: Fazer login
# selecionar o campo de email
# selecionar o campo de e-mail e deletar
pyautogui.click(x=624, y=428)
pyautogui.hotkey("ctrl", "a")
pyautogui.press("delete")

# escrever o seu email
pyautogui.write("vinyvirtus18@gmail.com")
pyautogui.press("tab")  # passando para o próximo campo
pyautogui.write("sua senha")
pyautogui.click(x=683, y=596) # clique no botao de login
time.sleep(2)
pyautogui.click(x=444, y=296)

# Passo 3: Importar a base de produtos pra cadastrar
import pandas as pd

tabela = pd.read_csv("Aula 1 - Python PowerUp/produtos.csv")

print(tabela)
# Passo 4: Cadastrar um produto
for linha in tabela.index:
    # clicar no campo de código
    time.sleep(1)
    pyautogui.click(x=444, y=296)
    # pegar da tabela o valor do campo que a gente quer preencher
    codigo = tabela.loc[linha, "codigo"]
    # preencher o campo
    pyautogui.write(str(codigo))
    # passar para o proximo campo
    pyautogui.press("tab")
    # preencher o campo
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter") # cadastra o produto (botao enviar)
    # dar scroll de tudo pra cima
    pyautogui.scroll(5000)
    # Passo 5: Repetir o processo de cadastro até o fim
