from flask import Flask, render_template, request, redirect, url_for
from bs4 import BeautifulSoup
from functions import *

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():  
    if request.method == 'POST':        
        print('***************************')
        link = request.form['book_url']
        books = get_books(link)
        return render_template('index.html', books = books)
        
    else:
        return render_template('index.html')
        

@app.route('/graphs')
def graphs():
    return render_template('graphs.html')

@app.errorhandler(Exception)
def all_exception_handler(error):
   return render_template('error.html'), 500

