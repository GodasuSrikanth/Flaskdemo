""" from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hi Srikanth</p>"

if __name__=='__main__':
    app.run(debug=True) """

""" from flask import Flask
from markupsafe import escape

app = Flask(__name__)
@app.route("/<name>")
def hello(name):
    return f"Hello, {escape(name)}!" """


""" from flask import url_for,Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'index'

@app.route('/login')
def login():
    return 'login'

@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))
 
 """


""" from flask import Flask
app=Flask(__name__)
@app.route('/home/')
def home(age):
    return"Age=%d" %age

if __name__=='__main__':
    app.run(debug=True) """

""" from flask import Flask
app=Flask(__name__)
def about():
    return"Thisisaboutpage"
app.add_url_rule("/about","about",about)
if __name__=='__main__':
    app.run(debug=True)  """


#url for
""" from flask import * 
app = Flask(__name__) 
@app.route('/') 
def customer():
 return render_template('customer1.html')  
@app.route('/success',methods = ['POST', 'GET']) 
def render_datafunction(): 
 if request.method == 'POST': 
    result = request.form 
 return render_template("result_data.html",result = result) 
if __name__ == '__main__': 
 app.run(debug = True)   """




 #Sessions
from flask import *  
app = Flask(__name__)  
app.secret_key = "ayush"  
@app.route('/')  
def home():   
  return render_template("homepage2.html")  
@app.route('/login')  
def login():  
  return render_template("loginpage3.html")  
@app.route('/success',methods = ["POST"])   
def success():  
  if request.method == "POST":  
   session['email']=request.form['email']  
   return render_template('success.html')  
@app.route('/logout')  
def logout(): 
  if 'email' in session:  
    session.pop('email',None)  
    return render_template('logoutpage2.html');  
  else:  
    return '<p>user already logged out</p>'   
@app.route('/profile')  
def profile():  
    if 'email' in session:  
        email = session['email']  
        return render_template('homepage2.html',name=email)   
    else:  
        return '<p>Please login first</p>'  

if __name__ == '__main__': 
 app.run(debug = True)