import pathlib as pl

import numpy as np
import pandas as pd

from flask import Flask, jsonify, request
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

data = pl.Path(__file__).parent.absolute() / 'data'

# Charger les données CSV
associations_df = pd.read_csv(data / 'associations_etudiantes.csv')
evenements_df = pd.read_csv(data / 'evenements_associations.csv')

## Vous devez ajouter les routes ici : 

# Vérifie si le serveur est actif
@app.route("/api/alive", methods=["GET"])
def alive():
    return jsonify({"message": "Alive"}), 200

# Liste de toutes les associations
@app.route("/api/associations", methods=["GET"])
def list_associations():
    ids = associations_df["id"].tolist()
    return jsonify(ids), 200

if __name__ == '__main__':
    app.run(debug=False)
