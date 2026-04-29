from flask import Flask, request, redirect
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS teams
                 (team, college, class_name, leader, phone,
                  m1, m2, m3, m4)''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return open('index.html', encoding='utf-8').read()

@app.route('/signup')
def signup():
    return open('signup.html', encoding='utf-8').read()

@app.route('/submit', methods=['POST'])
def submit():
    data = request.form
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute("INSERT INTO teams VALUES (?,?,?,?,?,?,?,?,?)",
              (data['team'], data['college'], data['class'],
               data['leader'], data['phone'],
               data['member1'], data['member2'],
               data['member3'], data['member4']))
    conn.commit()
    conn.close()
    return "报名成功！"

if __name__ == '__main__':
    init_db()
    app.run()