from flask import Flask
from controllers import character_controller as cc

app = Flask(__name__)

# Rota principal: criar personagem
app.add_url_rule("/", "criar_personagem", cc.criar_personagem, methods=["GET", "POST"])

# Rota para escolher atributo sequencialmente
app.add_url_rule("/escolher", "escolher_atributo", cc.escolher_atributo, methods=["POST"])

# Rota opcional: listar personagens
app.add_url_rule("/listar", "listar_personagens", cc.listar_personagens)

if __name__ == "__main__":
    app.run(debug=True)
