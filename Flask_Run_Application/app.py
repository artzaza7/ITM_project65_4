from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash
import pymysql

app = Flask(__name__)
app.secret_key = 'itm_group_4'
# connection Database


def openConnection():
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='',
                                 database='itm_database',  # Name of database
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

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('signInPage'))

@app.route("/sign_in/actions", methods=['POST'])
def signInLogin():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        conn = openConnection()
        cur = conn.cursor()
        # hashed_password = generate_password_hash(password, method='sha256')
        # print(hashed_password)
        # sql = "SELECT * FROM `user` NATURAL JOIN `user_type` WHERE user.user_email = %s AND user.user_password = %s"
        sql = "SELECT * FROM `user` NATURAL JOIN `user_type` WHERE user.user_email = %s"
        cur.execute(sql, (email))
        result = cur.fetchone()

        userType = result[6]
        conn.close()
        if result and check_password_hash(result[5], password):
        # if result :
            session['user'] = result[1]
            if userType == "ADMIN":
                return redirect(url_for('adminPageUser', userType_name=result[6], user_id=result[1]))
            elif (userType == "USER"):
                return "USER LOGIN"
        else:
            return redirect(url_for('signInPage'))
    else:
        return redirect(url_for('signInPage'))


@app.route("/sign_up/actions", methods=['POST'])
def signUpLogin():
    firstname = request.form['firstname']
    lastname = request.form['lastname']
    email = request.form['email']
    password = request.form['password']
    user = 2
    hashed_password = generate_password_hash(password, method='sha256')
    conn = openConnection()
    cur = conn.cursor()
    sql = "INSERT INTO `user`(`user_email`, `user_fname`, `user_lname`, `user_password`, `userType_id`) VALUES (%s, %s, %s, %s, %s)"
    cur.execute(sql, (email, firstname, lastname, hashed_password, user))
    conn.commit()
    conn.close()
    # INSERT INTO `user`(`user_id`, `user_email`, `user_fname`, `user_lname`, `user_password`, `userType_id`) VALUES ('[value-1]','[value-2]','[value-3]','[value-4]','[value-5]','[value-6]')
    return redirect(url_for('signInPage'))

# =======================================================
# With User Login


@app.route("/<string:userType_name>/<string:user_id>/users")
def adminPageUser(userType_name, user_id):
    if 'user' in session:
        conn = openConnection()
        cur = conn.cursor()
        sql = "SELECT * FROM `user` WHERE user_id != %s"
        cur.execute(sql, (user_id))
        result_user = cur.fetchall()
        conn.close()
        return render_template('pageWithUser/Adminpage/user/user.html', data_user=result_user, data_id=user_id, data_userType=userType_name)
    else:
        return redirect(url_for('signInPage'))


@app.route("/<string:userType_name>/<string:user_id>/products")
def adminPageProduct(userType_name, user_id):

    if 'user' in session:
        conn = openConnection()
        cur = conn.cursor()
        sql = "SELECT * FROM `product` NATURAL JOIN product_color NATURAL JOIN product_category"
        cur.execute(sql)
        result_product = cur.fetchall()
        conn.close()
        return render_template('pageWithUser/Adminpage/product/product.html', data_product=result_product, data_id=user_id, data_userType=userType_name)
    else:
        return redirect(url_for('signInPage'))


@app.route("/<string:userType_name>/<string:user_id>/products/addProduct")
def adminPageAddProduct(userType_name, user_id):
    if 'user' in session:
        return render_template('pageWithUser/Adminpage/Addproduct/addproduct.html', data_id=user_id, data_userType=userType_name)
    else:
        return redirect(url_for('signInPage'))
# =======================================================


if __name__ == "__main__":
    app.run(debug=True)
