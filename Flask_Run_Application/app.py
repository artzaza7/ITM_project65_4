from flask import Flask, render_template, request, redirect, url_for
import pymysql

app = Flask(__name__)

# connection Database
def openConnection():
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='',
                                 database='', # Name of database
                                 charset='utf8',
                                 cursorclass=pymysql.cursors.DictCursor)
    return connection
# localhost, username, password, database
@app.route("/")
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)