import pickle

from flask import Flask, jsonify, request
from flask_basicauth import BasicAuth
from textblob import TextBlob
import os

modelo = pickle.load(open('models/modelo.sav', 'rb'))
colunas = ['tamanho', 'ano', 'garagem']


app = Flask(__name__)

app.config['BASIC_AUTH_USERNAME'] = os.environ.get('BASIC_AUTH_USERNAME')
app.config['BASIC_AUTH_PASSWORD'] = os.environ.get('BASIC_AUTH_PASSWORD')

basic_auth = BasicAuth(app)


@app.route('/')
def home():
    return ('api está no ar!')


@app.route('/sentimento/<frase>')
@basic_auth.required
def sentimento(frase):
    tb = TextBlob(frase)
    tb_en = tb.translate(from_lang='pt', to='en')
    polarity = tb_en.sentiment.polarity
    return 'polaridade: {}'.format(polarity)


@app.route('/cotacao/', methods=['POST'])
def cotacao():
    dados = request.get_json()
    dados_inputs = [dados[col] for col in colunas]
    preco = modelo.predict([dados_inputs])

    return jsonify(preco=preco[0])

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
