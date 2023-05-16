from flask import Flask, render_template, request, redirect, session, flash

class Game:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

#VARIAVEIS GLOBAIS = FATOR GLOBAL
game1 = Game('Super Mario', 'Aventura', 'Nitendo')
game2 = Game('Fzero', 'Corrida', 'Nitendo 64')
game3 = Game('Mortal Kombat', 'Luta', 'Super Nitendo')
lista_games = [game1, game2, game3]


app = Flask(__name__)
app.secret_key = 'cdd' #adicionando chave p/ login

@app.route('/')

def index():

    return render_template('lista.html', titulo='Gameteca - Nerdzinhos safados', games=lista_games)

@app.route('/new')
def new():
    return render_template('new.html', titulo='New Game')

@app.route('/criar', methods=['POST',])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    games = Game(nome, categoria, console)
    lista_games.append(games)
    return redirect('/') #REDIRECT > REDIRECIONA PARA A ROTA BARRA '/'


@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/autenticar', methods=['POST',])
def autenticar():
    if 'vader' == request.form['senha']:
        #TODO: session guarda informações nos cookies do navegador
        session['usuario_logado'] = request.form['usuario']
        flash(session['usuario_logado'] + ' logado com sucesso!')
        return redirect('/')
    else:
        flash('Usuário não logado!')
        return redirect('/login')
@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso!')
    return redirect('/')
# trecho da app

app.run(debug=True)