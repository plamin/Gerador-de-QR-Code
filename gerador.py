import qrcode
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

def gerar_qrcode():
    link = entrada.get()
    if not link:
        messagebox.showwarning("Aviso", "Por favor, insira um link.")
        return
    
    # Gera QR Code
    qr_img = qrcode.make(link)
    qr_img.save("QRCode_gerado.png")

    # Exibe na interface
    qr_img = qr_img.resize((300, 300))
    qr_tk = ImageTk.PhotoImage(qr_img)
    imagem_label.config(image=qr_tk)
    imagem_label.image = qr_tk  # Referência para manter imagem na tela

# Interface
janela = tk.Tk()
janela.title("Gerador de QR Code")
janela.geometry("400x500")

titulo = tk.Label(janela, text="Digite o link para gerar o QR Code:", font=("Arial", 14))
titulo.pack(pady=10)

entrada = tk.Entry(janela, width=50)
entrada.pack(pady=10)

botao = tk.Button(janela, text="Gerar QR Code", command=gerar_qrcode)
botao.pack(pady=10)

imagem_label = tk.Label(janela)
imagem_label.pack(pady=20)

janela.mainloop()
