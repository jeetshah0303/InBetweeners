from flask import Flask, render_template, request, redirect, url_for, flash, session, make_response
import cv2
app = Flask(__name__)
@app.route('/', methods=["GET", "POST"])
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(host='127.0.0.9',port=4455,debug=True)
