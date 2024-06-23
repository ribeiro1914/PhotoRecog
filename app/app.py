from flask import Flask, jsonify, render_template

app = Flask(__name__, template_folder='../templates', static_folder='../static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result')
def result_page():
    return render_template('result.html')

@app.route('/calculate')
def calculate():
    result = 1 + 1
    return jsonify(result=result)
