from flask import Flask
import socket
from datetime import datetime

import os

app = Flask(__name__)

@app.route('/')
def hello():
    hoy = datetime.now().strftime("%Y-%m-%d")
    hostname = socket.gethostname()
    # Cambia este texto por tus datos
    return f"Jorge Luis Arias Tandaypan - {hoy} - {hostname}"


if __name__ == "__main__":
    # MUY IMPORTANTE: escuchar en 0.0.0.0 para que el host pueda acceder
    app.run(host="0.0.0.0", port=5000)
