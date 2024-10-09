# Instalar e importar o pyautogui, time e pandas
import pyautogui
import time
import pandas

# Pause padrão para evitar erros
pyautogui.PAUSE = 0.5

# STEP 1 --> Abrir o navegador

pyautogui.press('win') # Pressionando a tecla Windows

pyautogui.write('edge') # Pesquisando pelo navegador

pyautogui.press('enter')

pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login') # Acessando o sistema

pyautogui.press('enter')

time.sleep(2) # Aguardar carregamento da página

# STEP 2 --> Fazer login
btn_email = {'x': 958, 'y': 452}    # Localização do botão de e-mail
btn_cod_produto = {'x': 953, 'y': 304} # Localização do campo de código do produto

pyautogui.click(btn_email['x'], btn_email['y']) # Clicando no botão de email

pyautogui.write('teste') # Inserindo login

pyautogui.press('tab') # Trocando para o campo de senha

pyautogui.write('teste') # Inserindo senha

pyautogui.press('tab') # Trocando para o botão de logar

pyautogui.press('enter') # Realizando o login

time.sleep(1) # Aguardar carregamento da página

# STEP 3 --> Importar base de dados
produtos = pandas.read_csv('produtos.csv')

# STEP 4 --> Cadastrar produto
linha = 0

for linha in produtos.index:    # Percorrer a lista de produtos

    # Selecionar primeiro campo
    pyautogui.click(btn_cod_produto['x'], btn_cod_produto['y'])

    # Código
    pyautogui.write(str(produtos.loc[linha, 'codigo']))
    pyautogui.press('tab')

    # Marca
    pyautogui.write(str(produtos.loc[linha, 'marca']))
    pyautogui.press('tab')

    # Tipo
    pyautogui.write(str(produtos.loc[linha, 'tipo']))

    pyautogui.press('tab')

    # Categoria
    pyautogui.write(str(produtos.loc[linha, 'categoria']))
    pyautogui.press('tab')

    # Preço
    pyautogui.write(str(produtos.loc[linha, 'preco_unitario']))
    pyautogui.press('tab')

    # Custo
    pyautogui.write(str(produtos.loc[linha, 'custo']))
    pyautogui.press('tab')

    # Observação
    if not pandas.isna(produtos.loc[linha, 'obs']): # Verificar se observação está vazia

        pyautogui.write(str(produtos.loc[linha, 'obs']))
    
    pyautogui.press('tab')

    # Enviar
    pyautogui.press('enter')

    # Voltar página ao topo
    pyautogui.scroll(5000)
