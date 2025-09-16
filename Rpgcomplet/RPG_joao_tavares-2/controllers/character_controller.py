from flask import render_template, request, redirect, url_for
from models.character import Character
from models.dice import gerar_atributos

# Lista global de personagens
personagens = []

def criar_personagem():
    """
    Rota para criar personagem: exibe formulário ou inicia escolha sequencial.
    """
    if request.method == "POST":
        nome = request.form.get("nome")
        classe = request.form.get("classe")
        raca = request.form.get("raca")
        modo_dados = request.form.get("modo_dados")

        resultado = gerar_atributos(modo_dados)
        atributos_nome = ["Força", "Destreza", "Constituição", "Inteligência", "Sabedoria", "Carisma"]

        if modo_dados == "3d6":
            # Modo automático: atribui na ordem e finaliza
            atributos_dict = dict(zip(atributos_nome, resultado))
            personagem = Character(nome, raca, classe, attributes=atributos_dict, modo_dados=modo_dados)
            personagens.append(personagem)
            return render_template("criar_personagem.html", criado=True, personagem=personagem)

        else:
            # Modos sequenciais: iniciar escolha do zero
            return render_template(
                "escolher_ordem_sequencial.html",
                nome=nome,
                classe=classe,
                raca=raca,
                modo_dados=modo_dados,
                atributo=atributos_nome[0],
                valores=resultado,
                escolhidos="",
                valores_gerados=",".join(map(str, resultado)),
                erro=None
            )

    # GET: exibe formulário
    return render_template("criar_personagem.html", criado=False, personagem=None)


def escolher_atributo():
    """
    Rota sequencial: escolhe um atributo por vez nos modos choose_values ou 4d6_drop_lowest.
    """
    if request.method == "POST":
        nome = request.form.get("nome")
        classe = request.form.get("classe")
        raca = request.form.get("raca")
        modo_dados = request.form.get("modo_dados")
        valor_escolhido = request.form.get("valor")

        # Recupera valores já escolhidos
        escolhidos = request.form.get("escolhidos")
        escolhidos = list(map(int, escolhidos.split(","))) if escolhidos else []

        # Recupera valores gerados
        valores = request.form.get("valores_gerados")
        valores = list(map(int, valores.split(","))) if valores else gerar_atributos(modo_dados)

        atributos_nome = ["Força","Destreza","Constituição","Inteligência","Sabedoria","Carisma"]
        proximo_indice = len(escolhidos)

        if valor_escolhido is None:
            atributo = atributos_nome[proximo_indice] if proximo_indice < 6 else None
            return render_template(
                "escolher_ordem_sequencial.html",
                nome=nome,
                classe=classe,
                raca=raca,
                modo_dados=modo_dados,
                atributo=atributo,
                valores=valores,
                escolhidos=",".join(map(str, escolhidos)),
                valores_gerados=",".join(map(str, valores)),
                erro="Você precisa escolher um valor!"
            )

        valor_escolhido = int(valor_escolhido)

        # Remove valores já escolhidos da lista de disponíveis
        disponiveis = valores.copy()
        for v in escolhidos:
            if v in disponiveis:
                disponiveis.remove(v)

        if valor_escolhido not in disponiveis:
            atributo = atributos_nome[proximo_indice] if proximo_indice < 6 else None
            return render_template(
                "escolher_ordem_sequencial.html",
                nome=nome,
                classe=classe,
                raca=raca,
                modo_dados=modo_dados,
                atributo=atributo,
                valores=disponiveis,
                escolhidos=",".join(map(str, escolhidos)),
                valores_gerados=",".join(map(str, valores)),
                erro=f"O valor {valor_escolhido} não está disponível!"
            )

        # Adiciona valor escolhido
        escolhidos.append(valor_escolhido)
        proximo_indice += 1

        # Se todos atributos escolhidos, cria personagem
        if proximo_indice >= len(atributos_nome):
            atributos_dict = dict(zip(atributos_nome, escolhidos))
            personagem = Character(nome, raca, classe, attributes=atributos_dict, modo_dados=modo_dados)
            personagens.append(personagem)
            return render_template("criar_personagem.html", criado=True, personagem=personagem)

        # Próximo atributo
        proximo_atributo = atributos_nome[proximo_indice]
        disponiveis = valores.copy()
        for v in escolhidos:
            if v in disponiveis:
                disponiveis.remove(v)

        return render_template(
            "escolher_ordem_sequencial.html",
            nome=nome,
            classe=classe,
            raca=raca,
            modo_dados=modo_dados,
            atributo=proximo_atributo,
            valores=disponiveis,
            escolhidos=",".join(map(str, escolhidos)),
            valores_gerados=",".join(map(str, valores)),
            erro=None
        )

    return redirect(url_for("criar_personagem"))


def listar_personagens():
    """
    Lista todos os personagens criados.
    """
    return render_template("listar_personagens.html", personagens=personagens)
