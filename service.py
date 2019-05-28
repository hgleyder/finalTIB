from flask import Flask
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from flask import jsonify, request
import json
from flask_cors import CORS

from joblib import dump, load

app = Flask(__name__)

CORS(app)


@app.route('/')
def hello_world():
    vect = load('parseador.p')
    model = load('model.p')
    instances = ['TPDCVTGKVEYTKYNDDDTFTVKVGDKELFTNRWNLQSLLLSAQITGMTVTIKTNACHNGGGFSEVIFR', 'TPDCVTGKVEYTKYNDDDTFTVKVGDKELFTNRWNLQSLLLSAQITGMTVTIKTNACHNGGGFSEVIFR']


    X_test_df = vect.transform(instances)

    predictions = model.predict(X_test_df)
    print(predictions)

    return jsonify(predictions.tolist())

@app.route('/clasifica', methods = ['POST',])
def image():
    if request.method == 'POST':
        data = json.loads(request.data)
        sequence = data['data']['sequence']

        vect = load('parseador.p')
        model = load('model.p')
        clases = load('clases.p')

        instances = [sequence]

        X_test_df = vect.transform(instances)

        predictions = model.predict(X_test_df)
        probabilidades = model.predict_proba(X_test_df)

        response = jsonify({'main': predictions.tolist()[0], 'probabilidades': probabilidades.tolist(), 'clases': clases})
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

#uwsgi --socket 127.0.0.1:5000 --protocol=http -w


if __name__ == '__main__':
    app.run(host='0.0.0.0')