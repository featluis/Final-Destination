import tkinter as tk
import random

faces = {1:"🍡", 2:"🍒", 3:"🍩", 4:"🍕", 5:"🦑", 6:"game over"}

# Novas variáveis para placar e histórico
vitorias = 0
derrotas = 0
historico = []

def rolar_dado():
    global vitorias, derrotas, historico
    numero = random.randint(1, 6)
    resultado = faces[numero]

    # Mostra emoji grande no centro
    label_resultado.config(text=resultado, font=("Segoe UI Emoji", 60))

    # Atualiza placar
    if resultado == "game over":
        derrotas += 1
    else:
        vitorias += 1

    # Atualiza histórico
    historico.append(resultado)
    label_placar.config(text=f"Vitórias: {vitorias} | Derrotas: {derrotas}")
    label_historico.config(text="Histórico: " + " ".join(historico[-5:]))

def resetar():
    global vitorias, derrotas, historico
    vitorias = 0
    derrotas = 0
    historico = []
    label_placar.config(text="Vitórias: 0 | Derrotas: 0")
    label_historico.config(text="Histórico: ")
    label_resultado.config(text="🎲", font=("Segoe UI Emoji", 40))

janela = tk.Tk()
janela.title("Jogo do Mussatto")
janela.geometry("500x400")
janela.config(bg="#fff9c4")

# Botão principal
botao_rolar = tk.Button(janela, text="🎲 Rolar Dado", command=rolar_dado,
                        font=("Impact", 16), bg="#5900ff", fg="white")
botao_rolar.pack(pady=20)

# Botão de reset
botao_reset = tk.Button(janela, text="🔄 Resetar", command=resetar,
                        font=("Arial", 12), bg="#ff4444", fg="white")
botao_reset.pack(pady=10)

# Resultado (emoji grande)
label_resultado = tk.Label(janela, text="🎲", font=("Segoe UI Emoji", 40), bg="#00aeff")
label_resultado.pack(pady=20)

# Placar
label_placar = tk.Label(janela, text="Vitórias: 0 | Derrotas: 0", font=("Arial", 14), bg="#fff176")
label_placar.pack(pady=10)

# Histórico
label_historico = tk.Label(janela, text="Histórico: ", font=("Arial", 12), bg="#c8e6c9")
label_historico.pack(pady=10)

janela.mainloop()
