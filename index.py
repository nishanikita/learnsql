from flask import Flask,render_template,url_for,redirect,request
from flask_mysqldb import MySQL

app=Flask(__name__)
app.secret_key="nikita"

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Nisha@12345'
app.config['MYSQL_DB'] = 'employee'

mysql=MySQL(app)

@app.route("/")
def home():
    cur=mysql.connection.cursor()
    cur.execute("select *from emplo_info")
    data=cur.fetchall()
    cur.close()
    return render_template("index.html",value=data)

if __name__ == "__main__":
    app.run(debug=True)