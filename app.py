from flask import Flask, render_template,g,request
import sqlite3
app = Flask(__name__)
app.secret_key = 'abcdef12345!@#$%'

# Set the database file name
DATABASE = 'Store.db'

# Define a function to get the database connection
def get_db():
    # Get the database connection from the app context
    db = getattr(g, '_database', None)
    if db is None:
        # Create a new database connection if one does not exist
        db = g._database = sqlite3.connect(DATABASE)
        # Set the row factory to sqlite3.Row to return rows as dictionaries
        db.row_factory = sqlite3.Row
    return db
def get2db():
     # Get the database connection from the app context
    db = getattr(g, '_database', None)
    db = g._database = sqlite3.connect(DATABASE)
        # Set the row factory to sqlite3.Row to return rows as dictionaries
    db.row_factory = sqlite3.Row
    return db
# Define a function to close the database connection when the app context is torn down
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()
@app.errorhandler(sqlite3.Error)
def handle_database_error(error):
    return 'A database error occurred: ' + str(error), 500



@app.route('/')
def home():
    try:
        db = get_db()
        
        # Create a cursor to execute SQL statements
        cursor = db.cursor()
        # Create a users table if it does not exist
        cursor.execute('CREATE TABLE IF NOT EXISTS users ( name TEXT,password INTEGER PRIMARY KEY, email TEXT)')
        # Commit the changes to the database
        db.commit()
        # Close the cursor
        cursor.close()
        # Return the index.html template
        return render_template('index.html')
    except sqlite3.Error as e:
        # Return an error message if a database error occurs
        return 'A database error occurred: ' + str(e), 500

@app.route('/home',methods = ['GET', 'POST'])
def about():
    return render_template('login.html')
@app.route('/signup',methods = ['GET', 'POST'])
def signup():
    return render_template('signup.html')
@app.route('/createac',methods=['GET','POST'])
def create():
    db = get_db()
    # Get the form data from the request
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    cursor=db.cursor()

    cursor.execute('INSERT INTO users (name , email, password) VALUES (?, ?, ?)',
                (name, email, password))
    # Commit the changes to the database
    db.commit()
    # Close the cursor
    cursor.close()  
    return render_template("index.html")
@app.route("/login",methods=['GET','POST'])
def login():
    db=get2db()
    email = request.form['email']
    password = request.form['password']
    cursor=db.cursor()
    new_value= cursor.execute("SELECT (email,password) FROM db where email=%s and password=%s",('email','password'))
    if new_value> 0:
            return render_template('index.html')
    else:
            return render_template("signup.html")
if __name__ == '__main__':
    app.run(debug=True)