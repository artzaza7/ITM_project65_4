from flask import Flask, render_template, request, redirect, url_for
import pymysql

app = Flask(__name__)

# connection Database
def openConnection():
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='',
                                 database='itm_database', # Name of database
                                 charset='utf8',
                                 cursorclass=pymysql.cursors.DictCursor)
    return connection
# localhost, username, password, database

# =======================================================
# Without User Login
@app.route("/")
def indexWithoutUser():
    return render_template('index.html')

@app.route("/shopping")
def shoppingWithoutUser():
    return render_template('pageWithoutUser/shop.html')

@app.route("/search")
def searchWithoutUser():
    return render_template('pageWithoutUser/search.html')

@app.route("/sign_in")
def signInPage():
    return render_template('pageWithoutUser/signin.html')

@app.route("/sign_up")
def signUpPage():
    return render_template('pageWithoutUser/signup.html')

# =======================================================


if __name__ == "__main__":
    app.run(debug=True)