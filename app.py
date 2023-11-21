from flask import Flask, render_template, redirect, url_for, request
import requests

app = Flask(__name__)

# Index page
@app.route('/')
def index():
    return render_template('index.html')

# Play page
@app.route('/play/<string:stream_name>')
def play(stream_name):
    return render_template('play.html', stream_name=stream_name)

if __name__ == '__main__':
    app.run(debug=True)