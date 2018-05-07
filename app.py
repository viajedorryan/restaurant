from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
import pyodbc
import os

app = Flask(__name__)

# Config SQL Server
conn = pyodbc.connect("DRIVER={ODBC Driver 11 for SQL Server};"
                      "SERVER=(local);"
                      "DATABASE=SampleDB;"
                      "UID=sa;"
                      "PWD=1tc0r3;"
                      "Trusted_Connection=yes;")


# cursor = conn.cursor()
# cursor.execute('SELECT * FROM ClientInfo')
# for row in cursor:
#     print('row = %r' % (row,))

@app.route("/")
def hello():
    cur = conn.cursor()
    cur.execute("{CALL sp_test2()}")

    clients = cur.fetchall()
    cur.close()
    return render_template('home.html', clients=clients)

if __name__ == '__main__':
    app.secret_key='itcsi'
    app.debug = True
    host = os.environ.get('IP', '127.0.0.1')
    port = int(os.environ.get('PORT', 7777))
    app.run(host=host, port=port)