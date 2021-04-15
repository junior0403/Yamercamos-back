from flask import Flask, jsonify
from routes import *
from flask_cors import CORS


app = Flask(__name__)

productos = [
            {
                    "id":1,
                    "nombre": "arroz",
                    "precio": "3000",
                    "url": "https://exitocol.vtexassets.com/arquivos/ids/290289/Arroz-Exito-180405_a.jpg?v=637003149029730000"
                },
            {
                    "id": 2 ,
                    "nombre": "cocaCola",
                    "precio": "3500",
                    "url": "https://exitocol.vtexassets.com/arquivos/ids/5670379-800-auto?width=800&height=auto&aspect=true"

                },
            {
                    "id":3,
                    "nombre": "panela",
                    "precio": "3000",
                    "url": "https://exitocol.vtexassets.com/arquivos/ids/5628512-800-auto?width=800&height=auto&aspect=true"

                },
            {
                    "id":4,
                    "nombre": "leche",
                    "precio": "12000",
                    "url": "https://exitocol.vtexassets.com/arquivos/ids/1976112-800-auto?width=800&height=auto&aspect=true"

                },
            {
                    "id":5,
                    "nombre": "cerveza",
                    "precio": "15000",
                    "url": "https://cdn.shopify.com/s/files/1/0247/8768/1379/products/cerveza_stella_artois_ilforno@2x.jpg?v=1561492084"

                },
                {
                    "id":6,
                    "nombre": "cereal",
                    "precio": "3000",
                    "url": "https://metrocolombiafood.vteximg.com.br/arquivos/ids/159590-1000-1000/7702103001085-1.jpg?v=636670251018830000"

                }
]


@app.route("/api/v1/productos/")
def get_all():
    return jsonify(productos)

CORS(app, resources={r"/*": {"origins": "*"}})

app.add_url_rule(user["login_user"], view_func=user["login_user_controllers"])
app.add_url_rule(user["login2_user"], view_func=user["login2_user_controllers"])
app.add_url_rule(user["login3_user"], view_func=user["login3_user_controllers"])
app.add_url_rule(user["login4_user"], view_func=user["login4_user_controllers"])
