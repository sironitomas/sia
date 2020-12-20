from flask import Flask, session, redirect, url_for, request
from . import model

app = Flask(__name__)

@app.route('/api/analyze_mushroom', methods=['POST'])
def analyze_mushroom():
    if request.method == 'POST':
        content = request.json
        return model.analysis(content)