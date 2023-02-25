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
                                #  cursorclass=pymysql.cursors.DictCursor
                                )
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

# action
@app.route("/sign_up/actions/login", methods=['POST'])
def signUpLogin():
    email = request.form['email']
    password = request.form['password']
    conn = openConnection()
    cur = conn.cursor()
    sql = "SELECT * FROM `user` NATURAL JOIN `user_type` WHERE user.user_email = %s AND user.user_password = %s"
    cur.execute(sql, (email, password))
    result = cur.fetchone()
    # print(result)
    userType = result[6]
    conn.close()
    if userType == "ADMIN":
        # print("Yes")
        # print(result[6])
        # print(result[1])
        return redirect(url_for('adminPageUser', userType_name = result[6], user_id = result[1]))
    elif (userType == "USER"):
        return redirect(url_for('signInPage'))
    else :
        return redirect(url_for('signInPage'))
    
# =======================================================
# With User Login
@app.route("/<string:userType_name>/<string:user_id>/users")
def adminPageUser(userType_name, user_id):

    conn = openConnection()
    cur = conn.cursor()
    sql = "SELECT * FROM `user` WHERE user_id != %s"
    cur.execute(sql, (user_id))
    result_user = cur.fetchall()
    conn.close()
    # print(result_user)
    return render_template('pageWithUser/Adminpage/user/user.html', data_user = result_user, data_id = user_id, data_userType = userType_name)

@app.route("/<string:userType_name>/<string:user_id>/products")
def adminPageProduct(userType_name, user_id):

    conn = openConnection()
    cur = conn.cursor()
    sql = "SELECT * FROM `product` NATURAL JOIN product_color NATURAL JOIN product_category"
    cur.execute(sql)
    result_product = cur.fetchall()
    conn.close()
    return render_template('pageWithUser/Adminpage/product/product.html', data_product = result_product, data_id = user_id, data_userType = userType_name)

@app.route("/<string:userType_name>/<string:user_id>/products/addProduct")
def adminPageAddProduct(userType_name, user_id):
    return render_template('pageWithUser/Adminpage/Addproduct/addproduct.html', data_id = user_id, data_userType = userType_name)
# =======================================================



if __name__ == "__main__":
    app.run(debug=True)