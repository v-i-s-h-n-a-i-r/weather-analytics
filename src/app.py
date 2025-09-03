from flask import Flask, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # For session management

@app.route('/')
def home():
    return "Hello, World! from Flask"


# Simple login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        # Dummy check
        if username == 'admin' and password == 'password':
            session['user'] = username
            return redirect(url_for('home'))
        return 'Invalid credentials', 401
    return '''
        <form method="post">
            Username: <input type="text" name="username"><br>
            Password: <input type="password" name="password"><br>
            <input type="submit" value="Login">
        </form>
    '''

# Simple logout route
@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)
