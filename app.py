from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

@app.route("/")
def home():
    try:
        conn = mysql.connector.connect(
            host="mysql",
            user="root",
            password="root123",
            database="cosmeticsdb"
        )

        cursor = conn.cursor()
        cursor.execute("SELECT name, price FROM products")
        products = cursor.fetchall()

        cursor.close()
        conn.close()

    except Exception as e:
        print(e)
        products = []

    return render_template("index.html", products=products)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
