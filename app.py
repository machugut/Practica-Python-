from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    
    if username == "sergio" and password == "1234": 
        return "Login Successful"
    else:
        return "Invalid Username or Password"

if __name__ == '__main__':
    app.run(debug=True)