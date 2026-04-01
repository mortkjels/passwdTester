from flask import Flask, request, render_template, jsonify, redirect, url_for

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])

def hello_world():
    return "<p> Hello, World!</p>"

if __name__ == '__main__':
    app.run(port=8250)

    