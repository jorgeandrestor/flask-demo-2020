# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template #allows us to send over an html document as one concrete unit 
from flask import request, redirect
from model import get_breakfast_rating
from datetime import datetime

# -- Initialization section --
app = Flask(__name__)


# -- Routes section --  if user requests / or /index, it will take them to the hello world site
@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", time=datetime.now())

@app.route('/results', methods=['GET','POST'])
def results():
    if request.method == 'POST':
        print(request.form)
        user_breakfast=request.form["breakfast"]
        user_name = request.form['nickname']
        breakfast_rating = get_breakfast_rating(user_breakfast)
        
        return render_template("breakfast.html",user_breakfast=user_breakfast, user_name=user_name, breakfast_rating=breakfast_rating)
    else:
        return redirect('/') #redirects are a way to handle user error by sending them to a specific page

@app.route('/secret')
def secret():
    return "You found the secret page."


#export FLASK_DEBUG=1 means turn debug mode on