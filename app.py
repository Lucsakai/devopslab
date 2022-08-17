from flask import Flask
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)

csrf = CSRFProtect(app)                                                                                                                           

@app.route("/")
def pagina_inicial():
    return "<br><marquee>Mão na massa, Aula DevOps_Impacta! --Lucas Sakai--</marquee>"

if __name__ == '__main__':
    app.run()