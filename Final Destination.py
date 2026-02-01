import tkinter as tk
import random
import winsound  # biblioteca para sons no Windows

# Emojis do dado (Game Over em maiúsculas)
faces = {1: "🍡", 2: "🍒", 3: "🍩", 4: "🥬", 5: "🦑", 6: "-GAME OVER-"}

# Placar dos jogadores
comidas_jogador1 = 0
comidas_jogador2 = 0
meta = 50

# Controle de turno
vez_jogador1 = True

# Sons
def som_gameover():
    winsound.Beep(400, 700)  # grave e longo

def som_vitoria():
    winsound.Beep(1000, 400)  # agudo
    winsound.Beep(1200, 400)  # sequência alegre

def som_dado():
    winsound.Beep(800, 200)  # clique rápido

def rolar_dado():
    global comidas_jogador1, comidas_jogador2, vez_jogador1

    # Limpa mensagem antiga (Game Over ou Vitória) ao iniciar nova jogada
    label_status.config(text="")

    numero = random.randint(1, 6)
    resultado = faces[numero]
    label_resultado.config(text=resultado, font=("Segoe UI Emoji", 60))

    som_dado()  # som ao rolar

    if vez_jogador1:
        if resultado == "-GAME OVER-":
            if comidas_jogador1 > 0:
                comidas_jogador1 -= 1
            piscar_gameover()
            som_gameover()
            label_status.config(text="☠️ O destino não estava ao seu lado…")
        else:
            comidas_jogador1 += 1
        label_placar1.config(text=f"Jogador 1 🍽️: {comidas_jogador1}/{meta}")
    else:
        if resultado == "-GAME OVER-":
            if comidas_jogador2 > 0:
                comidas_jogador2 -= 1
            piscar_gameover()
            som_gameover()
            label_status.config(text="☠️ O destino não estava ao seu lado…")
        else:
            comidas_jogador2 += 1
        label_placar2.config(text=f"Jogador 2 🍽️: {comidas_jogador2}/{meta}")

    # Verifica vitória
    if comidas_jogador1 >= meta:
        mostrar_vitoria("Jogador 1")
        som_vitoria()
    elif comidas_jogador2 >= meta:
        mostrar_vitoria("Jogador 2")
        som_vitoria()

    # Alterna turno
    vez_jogador1 = not vez_jogador1
    if vez_jogador1:
        label_turno.config(text="Vez do Jogador 1")
    else:
        label_turno.config(text="Vez do Jogador 2")

def mostrar_vitoria(jogador):
    label_status.config(text=f"🎉 A sorte sorriu para {jogador}! 🎉", font=("Arial", 18, "bold"))
    # Piscar branco e roxo do botão principal (1 segundo)
    cores = ["#ffffff", "#5900ff"]
    for i in range(4):  # 4 alternâncias = 2 piscadas
        janela.after(250 * i, lambda cor=cores[i % 2]: janela.config(bg=cor))
    janela.after(250 * 4, lambda: janela.config(bg="#fff9c4"))

def piscar_gameover():
    # Piscar vermelho, verde, azul e amarelo em ciclos psicodélicos (1 segundo)
    cores = ["#ff0000", "#00ff00", "#0000ff", "#ffff00"]
    for i in range(5):  # 5 alternâncias rápidas
        janela.after(200 * i, lambda cor=cores[i % 4]: janela.config(bg=cor))
    janela.after(200 * 5, lambda: janela.config(bg="#fff9c4"))

def resetar_jogo():
    global comidas_jogador1, comidas_jogador2, vez_jogador1
    comidas_jogador1 = 0
    comidas_jogador2 = 0
    vez_jogador1 = True
    label_placar1.config(text=f"Jogador 1 🍽️: {comidas_jogador1}/{meta}")
    label_placar2.config(text=f"Jogador 2 🍽️: {comidas_jogador2}/{meta}")
    label_turno.config(text="Vez do Jogador 1")
    label_status.config(text="")
    label_resultado.config(text="🎲")
    janela.config(bg="#fff9c4")

# Configuração da janela
janela = tk.Tk()
janela.title("Do You Believe in Fortunes 🎢?")
janela.geometry("600x500")
janela.config(bg="#fff9c4")

# Banner inicial estilo filme
label_banner = tk.Label(janela, text="Do You Believe in Fortunes 🎢?",
                        font=("Impact", 22), fg="#5900ff", bg="#fff9c4")
label_banner.pack(pady=15)

# Botão principal
botao_rolar = tk.Button(janela, text="✨ Teste sua Sorte ✨", command=rolar_dado,
                        font=("Impact", 16), bg="#5900ff", fg="white")
botao_rolar.pack(pady=20)

# Resultado do dado
label_resultado = tk.Label(janela, text="🎲", font=("Segoe UI Emoji", 40), bg="#00aeff")
label_resultado.pack(pady=20)

# Turno
label_turno = tk.Label(janela, text="Vez do Jogador 1", font=("Arial", 14), bg="#c8e6c9")
label_turno.pack(pady=10)

# Placar dos jogadores
label_placar1 = tk.Label(janela, text=f"Jogador 1 🍽️: {comidas_jogador1}/{meta}", font=("Arial", 14), bg="#fff176")
label_placar1.pack(pady=10)

label_placar2 = tk.Label(janela, text=f"Jogador 2 🍽️: {comidas_jogador2}/{meta}", font=("Arial", 14), bg="#fff176")
label_placar2.pack(pady=10)

# Status (mensagens de vitória ou game over)
label_status = tk.Label(janela, text="", font=("Arial", 14), bg="#fff9c4")
label_status.pack(pady=20)

# Botão de reset pequeno e vermelho
botao_reset = tk.Button(janela, text="Reiniciar o jogo", command=resetar_jogo,
                        font=("Arial", 10), bg="red", fg="white")
botao_reset.pack(pady=5)

janela.mainloop()
