import mysql.connector
from flask import Flask,jsonify

app = Flask(__name__)

@app.route("/")
def index():
    connection = mysql.connector.connect(
        user='root', password='root', host='mysql', port="3306", database='db')
    print("DB connected")

    cursor = connection.cursor()
    cursor.execute('Select * FROM students')
    students = cursor.fetchall()
    connection.close()

    print(students)
    return jsonify(students)

if __name__ == "__main__":
    app.run(host='0.0.0.0')