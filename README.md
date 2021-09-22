<h1 align="center">
    <img alt="Click Bot" title="Click Bot" src=".github/click-bot.png" width="120px" />
</h1>

<h2 align="center">
  	🤖 Click Bot
</h2>

<p align="center">
	<a href="#-tecnologias">Tecnologias</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
	<a href="#-projeto">Projeto</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
	<a href="#-instalação">Instalação</a>
</p>

## 🤖 Tecnologias

Esse projeto foi desenvolvido com as seguintes tecnologias:

- [Python](https://www.python.org/)
- [PyAutoGUI](https://pyautogui.readthedocs.io)


## 💻 Projeto
**Um simples robô para automatizar cliques em sequência**

## 🔧 Instalação

### Pré requisitos
Ter instalado:
- [Python](https://www.python.org/downloads/)


### No terminal, rodar
```sh
# Clonar repositório
git clone https://github.com/andre23arruda/click-bot.git

# Entrar na pasta
cd click-bot

# Criar um ambiente virtual
python -m venv venv

# Ativar o ambiente virtual
. activate.sh
# ou . venv/bin/activate
# ou source venv/Scripts/activate

# Instalar os pacotes necessários
pip install -r requirements.txt



# ==========  EXEMPLO ===========
# ABRA NO NAVEGADOR O ARQUIVO index.html

# Salvar coordenadas
python get_coordinates.py

# Executar cliques das coordenadas salvas
python main.py
```


<div align="center">
    <img alt="Coordinates" title="Coordinates" src=".github/video-1.gif?raw=true" width="600px" />
</div>
<p align="center">Gravando coordenadas</p>

<br>

<div align="center">
    <img alt="Clicks" title="Clicks" src=".github/video-2.gif?raw=true" width="600px" />
</div>
<p align="center">Executando cliques</p>
