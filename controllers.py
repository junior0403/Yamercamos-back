from flask.views import MethodView
from flask import jsonify, request
import pymysql
import time
import json
import bcrypt

class Login:
    def log(self, login):
        self.login = bool
class DataBase:
    connection = pymysql.connect(
        host="localhost",
        user="root",
        password="",
        db="suuper"
    )
    def insertar(name,lastname,email,password,phone):
            cursor = DataBase.connection.cursor()
            sql ='''
            INSERT INTO registro (name, lastname, email, password, phone) VALUES ('{}', '{}', '{}', '{}', '{}')
            '''.format(name,lastname,email,password,phone)
            cursor.execute(sql)
            DataBase.connection.commit()
    
    def iniciar_sesion(password,email):
        cursor = DataBase.connection.cursor()
        sql='''SELECT password FROM registro WHERE password='{}' and email='{}'
        '''.format(password,email)
        cursor.execute(sql)
        DataBase.connection.commit()
        if cursor.fetchall():
            print("Correo y contra Correctos")
            Login.log=True
        else:
            print("DATOS INCORRECTOS")
            Login.log=False
    def insertar_producto(nombre, precio, url):
        cursor = DataBase.connection.cursor()
        sql ='''
        INSERT INTO productos (nombre, precio, img) VALUES ('{}', '{}', '{}')
        '''.format(nombre,precio,url)
        cursor.execute(sql)
        DataBase.connection.commit()
class LoginUserControllers(MethodView):

    def post(self):
        datos = ""
        time.sleep(3)
        content = request.get_json()
        email = content.get("email")
        password = content.get("password")
        DataBase.iniciar_sesion(password,email)
        print(Login.log)
        if (Login.log==True):
            return jsonify({"login":True})
        else:
            print("Error")
class LoginUserControllers2(MethodView):

    def post(method=["POST"]):
        time.sleep(3)
        content = request.get_json()
        name = content.get("name")
        lastname = content.get("lastname")
        email = content.get("email")
        password = content.get("password")
        phone = content.get("phone")
        DataBase.insertar(name,lastname,email,password,phone)
        return jsonify({"login ok": True, "name":name ,"lastname": lastname , "email":email ,"password": password, "phone":phone}), 200

class LoginUserControllers3(MethodView):
    def post(method=["POST"]):
            productos = ["id","nombre","precio","url"]
            time.sleep(3)
            content = request.get_json()
            nombre = content.get("nombre")
            precio = content.get("precio")
            url = content.get("url")
            print(nombre,precio,url)
            DataBase.insertar_producto(nombre,precio,url)
            return jsonify({"añadido": True})


class LoginUserControllers4(MethodView):
    def get(methods=['POST']):
        cursor = DataBase.connection.cursor()
        sql='''SELECT * FROM productos
        '''
        cursor.execute(sql)
        rv = cursor.fetchall()
        productos = []
        for result in rv:
            content= {'id': result[0], 'nombre': result[1], 'precio': result[2],'url': result[3]}
            productos.append(content)
        print(productos)
        return jsonify(productos)




















'''
        cursor = DataBase.connection.cursor()
        cursor.execute=("""
        SELECT name,lastname,email,password,phone from usuarios where email=%s""",([email]))
        datos = cursor.fetchall()
        datos = datos[0]
        print(datos[2])
        email= datos[2]
        password = datos[3]
        print(datos[3])
        user={}
        user[email] = {"contraseña": password}
        if user.get(correo):
            contraseñaUser = user[correo]["contraseña"]
            if bcrypt.checkpw(bytes(str(password), encoding='utf-8'),contraseñaUser.encode('utf-8')):
                return jsonify({"login" : True}),200
            else:
                print("NO SIRVE")
        else:
            return jsonify({"login": True},200)
        '''