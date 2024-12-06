import tkinter as tk
from PIL import Image, ImageTk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import customtkinter as ctk
import matplotlib.pyplot as plt
import os
import random
import requests
import threading
import time
import subprocess
import psutil


# Variáveis globais para armazenar os caminhos, estados e dados
frontend_path = None
backend_path = None
enviando = False
tempos = []  # Para o gráfico
temperaturas = []  # Valores de temperatura
umidades_ar = []  # Valores de umidade do ar
umidades_solo = []  # Valores de umidade do solo

# Função para buscar os diretórios Frontend e Backend
def find_project_dirs(base_dir, target):
    for root, dirs, files in os.walk(base_dir):
        if target in dirs:
            return os.path.join(root, target)
    return None

# Função para alternar a cor da luz (vermelha ou verde)
def toggle_light(canvas, state):
    if state == "on":
        canvas.itemconfig("light", fill="green")
    elif state == "off":
        canvas.itemconfig("light", fill="red")

# Função para executar o Frontend
def start_front():
    global frontend_path
    toggle_light(front_canvas, "on")
    try:
        if frontend_path:
            subprocess.Popen(
                f'start /MIN cmd /K "cd {frontend_path} && npm start"',
                shell=True
            )
    except Exception as e:
        print(f"Erro ao iniciar o Frontend: {e}")

# Função para encerrar o Frontend
def stop_front():
    toggle_light(front_canvas, "off")
    try:
        for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
            cmdline = proc.info.get('cmdline', [])
            if cmdline and any("npm" in arg for arg in cmdline) or proc.info['name'] == 'node.exe':
                proc.kill()
                print(f"Frontend finalizado (PID: {proc.info['pid']}).")
    except Exception as e:
        print(f"Erro ao finalizar o Frontend: {e}")
 

# Função para executar o Backend
def start_back():
    global backend_path
    toggle_light(back_canvas, "on")
    try:
        if backend_path:
            subprocess.Popen(
                f'start /MIN cmd /K "cd {backend_path} && dotnet run"',
                shell=True
            )
    except Exception as e:
        print(f"Erro ao iniciar o Backend: {e}")

# Função para encerrar o Backend
def stop_back():
    toggle_light(back_canvas, "off")
    try:
        for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
            cmdline = proc.info.get('cmdline', [])
            if cmdline and any("dotnet" in arg for arg in cmdline):
                proc.kill()
                print(f"Backend finalizado (PID: {proc.info['pid']}).")
    except Exception as e:
        print(f"Erro ao finalizar o Backend: {e}")

# Funções para gerar dados fictícios
def gerar_temperatura():
    return {
        "temperaturaAtual": round(random.uniform(20.0, 30.0), 2),
        "temperaturaIdeal": 25.0
    }

def gerar_umidade_ar():
    return {
        "umidadeAtual": round(random.uniform(40.0, 60.0), 2),
        "umidadeIdeal": 50.0
    }

def gerar_umidade_solo():
    return {
        "umidadeTerraAtual": round(random.uniform(30.0, 50.0), 2),
        "umidadeIdeal": 40.0
    }

# Função que envia os dados para a API
def enviar_dados():
    global enviando, tempos, temperaturas, umidades_ar, umidades_solo
    while enviando:
        try:
            temperatura = gerar_temperatura()
            umidade_ar = gerar_umidade_ar()
            umidade_solo = gerar_umidade_solo()

            response_temp = requests.post('http://localhost:5271/api/Temperatura', json=temperatura)
            response_umidade_ar = requests.post('http://localhost:5271/api/Umidade', json=umidade_ar)
            response_umidade_solo = requests.post('http://localhost:5271/api/UmidadeTerra', json=umidade_solo)

            text_respostas.insert(tk.END, f"Temp: {response_temp.text}\n")
            text_respostas.insert(tk.END, f"Ar: {response_umidade_ar.text}\n")
            text_respostas.insert(tk.END, f"Solo: {response_umidade_solo.text}\n")
            text_respostas.see(tk.END)

            tempos.append(len(tempos) * 5)
            temperaturas.append(temperatura["temperaturaAtual"])
            umidades_ar.append(umidade_ar["umidadeAtual"])
            umidades_solo.append(umidade_solo["umidadeTerraAtual"])
            atualizar_grafico()

        except Exception as e:
            text_respostas.insert(tk.END, f"Erro: {e}\n")
            text_respostas.see(tk.END)

        time.sleep(5)

# Função para atualizar o gráfico
def atualizar_grafico():
    ax.clear()
    ax.plot(tempos, temperaturas, label="Temperatura (°C)", color="red")
    ax.plot(tempos, umidades_ar, label="Umidade do Ar (%)", color="blue")
    ax.plot(tempos, umidades_solo, label="Umidade do Solo (%)", color="green")
    ax.set_xlabel("Tempo (s)")
    ax.set_ylabel("Valores")
    ax.set_title("Evolução dos Dados")
    ax.legend()
    canvas.draw()

# Função para ligar o servidor
def ligar_servidor():
    global enviando
    toggle_light(server_canvas, "on")
    enviando = True
    threading.Thread(target=enviar_dados, daemon=True).start()

# Função para desligar o servidor
def desligar_servidor():
    global enviando
    toggle_light(server_canvas, "off")
    enviando = False

# Configuração da janela principal (root)
root = ctk.CTk()
root.geometry("800x600")  # Tamanho da janela
root.configure(bg="black")  # Cor de fundo da janela principal
root.title("Gerador de Dados Mocados")  # Título da janela

# Adicionar ícone à janela
icon_path = os.path.join(os.path.dirname(__file__), "esp32.ico")  # Caminho dinâmico para o .ico
root.iconbitmap(icon_path)  # Define o ícone da janela

# Localizar os diretórios
base_dir = os.getcwd()
frontend_path = find_project_dirs(base_dir, "Frontend")
backend_path = find_project_dirs(base_dir, "Backend")

# Função para limpar o conteúdo do quadro de respostas JSON
def limpar_respostas():
    text_respostas.delete('1.0', tk.END)

    # Limpa os dados do gráfico
    global tempos, temperaturas, umidades_ar, umidades_solo
    tempos.clear()
    temperaturas.clear()
    umidades_ar.clear()
    umidades_solo.clear()
    
    # Atualiza o gráfico vazio
    ax.clear()
    ax.set_xlabel("Tempo (s)")
    ax.set_ylabel("Valores")
    ax.set_title("Evolução dos Dados")
    ax.legend()  # Adiciona a legenda vazia
    canvas.draw()

# Frame para controles (luzes e botões) com design moderno
frame_lights = tk.Frame(
    root, 
    borderwidth=0,  # Remove a borda padrão
    bg="#2e3b4e",   # Cor de fundo (amarelo claro)
    highlightthickness=4,  # Borda externa mais espessa
    highlightbackground="#00796b"  # Laranja vibrante para destacar
)
frame_lights.place(x=10, y=10, width=220, height=200)


# Configuração das luzes e botões com design criativo e detalhado
front_canvas = tk.Canvas(frame_lights, width=20, height=20, highlightthickness=0)
front_canvas.grid(row=0, column=0, padx=5, pady=5)
front_canvas.create_oval(5, 5, 15, 15, fill="red", tags="light")

tk.Label(
    frame_lights, 
    text="FRONT", 
    font=("Helvetica", 10, "italic bold"), 
    fg="#fff",  # Cor do texto (cinza suave)
    bg="#2e3b4e"   # Cor de fundo (amarelo claro)
).grid(row=0, column=1, padx=5)

ctk.CTkButton(
    frame_lights, 
    text="ON", 
    command=start_front, 
    corner_radius=8,  # Bordas mais arredondadas
    fg_color="#4CAF50",  # Verde mais claro para botões ligados
    hover_color="#3D8F41",  # Hover mais escuro para contraste
    text_color="white", 
    font=("Helvetica", 10, "bold"),
    width=1,  # Mantendo tamanhos confortáveis
    height=10,
    border_width=2,  # Adiciona uma borda para destaque
    border_color="#2E7D32"  # Cor da borda para combinar com o botão
).grid(row=0, column=2, padx=1)

ctk.CTkButton(
    frame_lights, 
    text="OFF", 
    command=stop_front, 
    corner_radius=8, 
    fg_color="#F44336",  # Vermelho vibrante para botões desligados
    hover_color="#D32F2F", 
    text_color="white", 
    font=("Helvetica", 10, "bold"),
    width=1, 
    height=10,
    border_width=2, 
    border_color="#B71C1C"
).grid(row=0, column=3, padx=1)

back_canvas = tk.Canvas(frame_lights, width=20, height=20, highlightthickness=0)
back_canvas.grid(row=1, column=0, padx=5, pady=5)
back_canvas.create_oval(5, 5, 15, 15, fill="red", tags="light")

tk.Label(
    frame_lights, 
    text="BACK", 
    font=("Helvetica", 10, "italic bold"),  # Estilo diferenciado para se destacar
    fg="#fff",
    bg="#2e3b4e"
).grid(row=1, column=1, padx=5)

ctk.CTkButton(
    frame_lights, 
    text="ON", 
    command=start_back, 
    corner_radius=8, 
    fg_color="#4CAF50", 
    hover_color="#3D8F41", 
    text_color="white", 
    font=("Helvetica", 10, "bold"),
    width=1, 
    height=10,
    border_width=2, 
    border_color="#2E7D32"
).grid(row=1, column=2, padx=1)

ctk.CTkButton(
    frame_lights, 
    text="OFF", 
    command=stop_back, 
    corner_radius=8, 
    fg_color="#F44336", 
    hover_color="#D32F2F", 
    text_color="white", 
    font=("Helvetica", 10, "bold"),
    width=1, 
    height=10,
    border_width=2, 
    border_color="#B71C1C"
).grid(row=1, column=3, padx=1)

server_canvas = tk.Canvas(frame_lights, width=20, height=20, highlightthickness=0)
server_canvas.grid(row=2, column=0, padx=5, pady=5)
server_canvas.create_oval(5, 5, 15, 15, fill="red", tags="light")

tk.Label(
    frame_lights, 
    text="SERVER", 
    font=("Helvetica", 10, "italic bold"),   # Estilo sublinhado para destaque adicional
    fg="#fff", 
    bg="#2e3b4e"
).grid(row=2, column=1, padx=5)

ctk.CTkButton(
    frame_lights, 
    text="ON", 
    command=ligar_servidor, 
    corner_radius=8, 
    fg_color="#4CAF50", 
    hover_color="#3D8F41", 
    text_color="white", 
    font=("Helvetica", 10, "bold"),
    width=1, 
    height=10,
    border_width=2, 
    border_color="#2E7D32"
).grid(row=2, column=2, padx=1)

ctk.CTkButton(
    frame_lights, 
    text="OFF", 
    command=desligar_servidor, 
    corner_radius=8, 
    fg_color="#F44336", 
    hover_color="#D32F2F", 
    text_color="white", 
    font=("Helvetica", 10, "bold"),
    width=1, 
    height=10,
    border_width=2, 
    border_color="#B71C1C"
).grid(row=2, column=3, padx=1)

# Configuração inicial do customtkinter
ctk.set_appearance_mode("System")  # Modo: "Light", "Dark", ou "System"
ctk.set_default_color_theme("blue")  # Tema: "blue", "green", ou "dark-blue"

# Substituir o botão "LIMPAR" com um botão arredondado
btn_limpar = ctk.CTkButton(
    master=frame_lights,
    text="LIMPAR",
    command=limpar_respostas,
    corner_radius=7,  # Define bordas arredondadas
    fg_color="#FF6347",  # Cor de fundo
    text_color="white",  # Cor do texto
    hover_color="#FF4500",  # Cor ao passar o mouse
    font=("Helvetica", 14, "bold"),  # Fonte personalizada
)
btn_limpar.grid(row=4, column=0, columnspan=4, pady=15)


# Frame para respostas JSON com design moderno e criativo
frame_respostas = tk.Frame(
    root, 
    borderwidth=0,  # Remove bordas antigas
    bg="#2e3b4e",  # Fundo cinza escuro para um estilo moderno
    highlightthickness=4,  # Espessura da borda
    highlightbackground="#00796b"  # Azul neon para borda externa  
)
frame_respostas.place(x=220, y=10, width=570, height=360)

# Título estilizado com ícone e sombra
tk.Label(
    frame_respostas, 
    text="🔷 RESPOSTAS DO JSON",  # Adiciona um ícone criativo
    font=("Helvetica", 14, "bold"), 
    fg="#ffffff",  # Texto branco para contraste
    bg="#2e3b4e",  # Mesmo fundo do frame
).pack(anchor="nw", padx=15, pady=15)

# Caixa de texto com design futurista
text_respostas = tk.Text(
    frame_respostas, 
    wrap="word", 
    font=("Courier New", 11),  # Fonte monoespaçada para estilo técnico
    bg="#1c2531",  # Fundo escuro para o texto
    fg="#00bcd4",  # Texto verde-água para estilo moderno 
    relief="flat",  # Remove as bordas padrão
    insertbackground="#00bcd4",  # Cursor com cor neon
    highlightthickness=3,  # Borda interna
    highlightbackground="#00796b",  # Verde escuro nas bordas internas
    highlightcolor="#00ffcc",  # Verde-água ao focar
)
text_respostas.pack(expand=True, fill="both", padx=15, pady=15)


# Frame para o GIF com design moderno
frame_gif = tk.Frame(
    root, 
    borderwidth=0,  # Remove bordas padrão
    bg="#2e3b4e",  # Fundo cinza escuro para consistência
    highlightthickness=4,  # Espessura da borda externa
    highlightbackground="#00796b"  # Borda laranja vibrante
)
frame_gif.place(x=10, y=170, width=213, height=200)

# Label estilizada para o GIF
gif_label = tk.Label(
    frame_gif, 
    bg="#2e3b4e",  # Fundo escuro para o GIF
    relief="flat",  # Sem bordas padrão
)
gif_label.pack(expand=True, padx=10, pady=10)

# Carregar o GIF
gif_path = os.path.join(os.path.dirname(__file__), "esp32.gif")
gif_frames = []

gif_image = Image.open(gif_path)
try:
    while True:
        gif_frames.append(ImageTk.PhotoImage(gif_image.copy()))
        gif_image.seek(len(gif_frames))
except EOFError:
    pass

# Função para animar o GIF
def animate_gif(index):
    gif_label.configure(image=gif_frames[index])
    root.after(100, animate_gif, (index + 1) % len(gif_frames))

animate_gif(0)


# Frame para o gráfico com design moderno
frame_grafico = tk.Frame(
    root, 
    borderwidth=0,  # Remove borda padrão
    bg="#2e3b4e",  # Fundo cinza escuro para consistência
    highlightthickness=4,  # Espessura da borda externa
    highlightbackground="#00796b"  # Borda verde vibrante
)
frame_grafico.place(x=10, y=380, width=780, height=200)

# Estilizando e posicionando o gráfico
fig, ax = plt.subplots(figsize=(10, 3))
fig.patch.set_facecolor("#1c2531")  # Fundo do gráfico no mesmo tom do frame
ax.set_facecolor("#2e3b4e")  # Fundo interno do gráfico em cinza escuro
ax.tick_params(colors="white")  # Cor branca para os ticks
for spine in ax.spines.values():
    spine.set_color("#4caf50")  # Verde para as bordas do gráfico

canvas = FigureCanvasTkAgg(fig, master=frame_grafico)
canvas.get_tk_widget().pack(fill="both", expand=True, padx=10, pady=10)


# Iniciar a interface
root.mainloop()