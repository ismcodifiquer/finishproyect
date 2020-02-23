from crypto import app
from flask import render_template, request, redirect, url_for
from .forms import CryptoForm

import sqlite3
import requests
from crypto import app


Base_Datos = './data/movements.db'
consulta = 'SELECT * FROM movements'

def abrir_base_datos_index(consulta, *args):
    conn = sqlite3.connect(Base_Datos)
    cursor = conn.cursor()

    rows = cursor.execute(consulta, args).fetchall()
    conn.commit()
    conn.close()
    return rows
        
@app.route("/", methods=['GET', 'POST'])
    
def index():
    registros = abrir_base_datos_index('SELECT * FROM movements;')
    

    return render_template("index.html", registros = registros)
@app.route("/purchase", methods=['GET', 'POST'])
def purchase():
    form = CryptoForm(request.form)
    return render_template("purchase.html", form=form)

@app.route("/status", methods=['GET', 'POST'])
def status():
    registros = abrir_base_datos_index('SELECT * FROM movements;')

    return render_template("status.html", registros=registros)
    