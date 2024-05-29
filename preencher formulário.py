import pyautogui
import time
import pandas as pd


def esperar(tempo):
    time.sleep(tempo)



df = pd.read_csv('formulario.csv')
num_linhas = df.shape[0]

url = "https://forms.gle/8V1vVp84ibNcBaNF9"

pyautogui.press('win')
pyautogui.write('edge')
esperar(0.5)
pyautogui.press('enter')
esperar(0.5)
pyautogui.write(url, interval=0.1)
pyautogui.press('enter')
esperar(5)


for index, row in df.iterrows():

    pyautogui.moveTo(681, 309)
    pyautogui.click()

    pyautogui.write(row['Código'], interval=0.1)
    pyautogui.press('tab')  

    pyautogui.write(row['Nome'], interval=0.1)
    pyautogui.press('tab')

    pyautogui.write(row['Sobrenome'], interval=0.1)
    pyautogui.press('tab')

    pyautogui.write(row['Vai_fazer_o_Curso'], interval=0.1)
    pyautogui.press('tab')
    pyautogui.press('enter')
    esperar(3)
    pyautogui.moveTo(688, 228)
    pyautogui.click()
    esperar(3)
    
pyautogui.alert('Acabou a Execuçao!')