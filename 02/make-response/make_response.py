from flask import Flask, make_response

app = Flask(__name__)

@app.route('/')
def index():
    response = make_response('<h1>This document carries a cookie!')
    response.set_cookie('answer', '42')
    return response
