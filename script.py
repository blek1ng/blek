from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Bem-vindo ao meu site!</h1><p>Este é um site simples feito com Flask.</p>"

if __name__ == '__main__':
    app.run(debug=True)


