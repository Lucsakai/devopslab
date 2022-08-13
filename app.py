from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "Mão na massa, Aula DevOps_Impacta! --Lucas Sakai--"

if __name__ == '__main__':
    app.run()