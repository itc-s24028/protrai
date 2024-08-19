# s24028
# Flaskの練習

from flask import Flask,send_file,request
import datetime

app = Flask(__name__)

@app.route('/')
def main_index():
    return send_file('index.html')

@app.route('/himitsu')
def main_himitsu():
    return "秘密のページ"

@app.route('/msg')
def main_msg():
    return send_file('msg.html')

@app.route('/submit',methods=['POST'])
def main_submit():
    content = request.form['content']
    with open('data.txt','a') as file:
        file.write(f'\n{datetime.datetime.now()}\n{content}\n')
        return f'書き込みました'

app.run(host='127.0.0.1',debug=True)