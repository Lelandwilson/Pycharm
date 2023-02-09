from flask import Flask, render_template, jsonify
from random import sample

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/data')
# def data():
#     return jsonify({'readings' : sample(range(1,10),5)})


if __name__ == "__main__":
    app.run(debug=True)
