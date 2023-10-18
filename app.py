import os
from flask import Flask, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'debian-sys-maint'
app.config['MYSQL_PASSWORD'] = 'JyzkXoKPeruI9oGe'
app.config['MYSQL_DB'] = 'mydb'

app.config['ENV'] = 'development'
app.config['DEBUG'] = True

# Initialize MySQL
mysql = MySQL(app)

# Define routes
@app.route('/')
def index():
    # Execute SQL query
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM users")
    # Fetch all rows
    rows = cur.fetchall()
    # Close cursor
    cur.close()
    # Render template with data
    return render_template('index.html', rows=rows)
# Run app
if __name__ == '__main__':
    app.run(debug=True)