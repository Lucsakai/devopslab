from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "<br><marquee>Mão na massa, Aula DevOps_Impacta! --Lucas Sakai--</marquee>"

if __name__ == '__main__':
    app.run()