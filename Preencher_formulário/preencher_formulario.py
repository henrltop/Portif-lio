import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def iniciar_execucao():
    url = entry_url.get()
    pasta = entry_pasta.get()

    if not url or not pasta:
        messagebox.showwarning("Aviso", "Por favor, preencha todos os campos.")
        return

    try:
        df = pd.read_csv(f'{pasta}/formulario.csv')

        driver = webdriver.Chrome()
        wait = WebDriverWait(driver, 10)

        driver.get(url)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[aria-labelledby="i1"]')))

        for index, row in df.iterrows():
            codigo_input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[aria-labelledby="i1"]')))
            nome_input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[aria-labelledby="i5"]')))
            sobrenome_input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[aria-labelledby="i9"]')))
            curso_input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[aria-labelledby="i13"]')))

            codigo_input.clear()
            codigo_input.send_keys(row['Código'])

            nome_input.clear()
            nome_input.send_keys(row['Nome'])

            sobrenome_input.clear()
            sobrenome_input.send_keys(row['Sobrenome'])

            curso_input.clear()
            curso_input.send_keys(row['Vai_fazer_o_Curso'])

            submit_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[role="button"]')))
            submit_button.click()

            enviar_outra_resposta = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[contains(text(), "Enviar outra resposta")]')))
            enviar_outra_resposta.click()

        driver.quit()
        messagebox.showinfo("Informação", "Acabou a Execução!")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao executar o script: {e}")

def selecionar_pasta():
    pasta = filedialog.askdirectory()
    entry_pasta.delete(0, tk.END)
    entry_pasta.insert(0, pasta)

# Configurar interface gráfica
root = tk.Tk()
root.title("Automação de Formulários")

tk.Label(root, text="Link do Formulário:").grid(row=0, column=0, padx=10, pady=10)
entry_url = tk.Entry(root, width=50)
entry_url.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Pasta dos Dados:").grid(row=1, column=0, padx=10, pady=10)
entry_pasta = tk.Entry(root, width=50)
entry_pasta.grid(row=1, column=1, padx=10, pady=10)

btn_selecionar_pasta = tk.Button(root, text="Selecionar Pasta", command=selecionar_pasta)
btn_selecionar_pasta.grid(row=1, column=2, padx=10, pady=10)

btn_iniciar = tk.Button(root, text="Iniciar", command=iniciar_execucao)
btn_iniciar.grid(row=2, column=0, columnspan=3, padx=10, pady=20)

root.mainloop()

#ASS: Henrique