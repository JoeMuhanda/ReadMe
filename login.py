//Flask

from flask import Flask, render_template, request

app = Flask(__name__)

# Set up database connection and initialize user list
# (This is just for the example, you would typically store the users in a database)
users = []

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
  # Retrieve form data
  username = request.form['username']
  password = request.form['password']

  # Connect to database and retrieve user with given username
  user = retrieve_user(username)
  if user is None:
    # Return error message if user is not found
    return "Error: User not found"
  if user.password != password:
    # Return error message if password is incorrect
    return "Error: Incorrect password"
  # Return success message if login is successful
  return "Login successful"

@app.route('/register', methods=['POST'])
def register():
  # Retrieve form data
  username = request.form['username']
  password = request.form['password']

  # Check if username is already taken
  for user in users:
    if user.username == username:
      return "Error: Username is already taken"
  
  # Add new user to the database
  add_user(username, password)
  # Return success message
  return "Registration successful"
