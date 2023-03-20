<<<<<<< Updated upstream:gpttest.py
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 14:43:56 2023

@author: kevinchen
"""

from flask import request,redirect,url_for,Flask
from gpt import GPT
import os

app = Flask(__name__,  static_url_path='/static')
gptAPI = GPT(os.environ.get('APIKEY'))
f = open("secret_apikey.txt" , "r")
# Set the secret key to some random bytes. Keep this really secret!


app.secret_key = f.read

@app.route('/')
def index():
    ''' display a link to the general query page '''
    print('processing / route')
    return '''
    <h1>Mid-Sized Sedan</h1>
    <ul>
      <li><a href="/gpt">Try Chat-GPT</a></li>

      <li><a href="/about">About Page</a></li>
      <li><a href="/team">Team Members</a></li>
      
      <li><a href="/index">Index</a></li>

      
      
      <img src="/static/altima.jpg" alt = "This should be a Honda Accord" style="width:888px;height:500px"/>
       

    </ul>

    '''
@app.route('/gpt', methods= ['GET', 'POST'])
def gpt():
    return '''

    <h1>GPT Prompts</h1>
    
    <li><a href="/gpt/kevin">Travel destinations</a></li>
    
    <li><a href="/gpt/ken">Convert code from Python to Java with GPT</a></li>
    
    <li><a href="/gpt/jack">name for jacks prompt</a></li>




    '''

@app.route('/about', methods=['GET', 'POST'])
def about():
    return '''
    <h1>GPT Demo About</h1>
    
    This program is a creative assignment by Kevin Chen, Ken Kirio, and ______ , created in COSI 103, Spring 2023 <br>
    This is a web server app that takes in queries from the user, sends them to OpenAI's GPT, then return 
    that response.
    '''
    
@app.route('/team', methods=['GET', 'POST'])
def team():
    return '''
    <h1>Team Mid-Sized Sedan</h1>
    
    <ul>
      <li>Kevin created gpt.py and gptwebapp.py, made the index and about webpages, and wrote his gpt demo</li> 
      <li>Ken made the team webpage, altered the structure so each team member could write their own GPT query, and wrote his gpt demo</li> 
      <li>Jack [list your contributions here]</li> 
    </ul>
    
    
    '''
    
@app.route('/team/kevin', methods=['GET', 'POST'])
def teamkevin():
    return '''

    <h1>Kevin Chen</h1>
    
    I worked on this project <br>
    
     <img src="/static/clown.jpg" />

    
    '''

@app.route('/team/ken', methods=['GET', 'POST'])
def teamken():
    return '''

    <h1>Ken Kirio</h1>

    put your bio here ken, or something


    
    '''

@app.route('/index', methods=['GET', 'POST'])
def index2():
    return '''
    <h1>Team Members Index</h1>
    
    <ul>
      <li><a href="/team/kevin">Kevin Chen</a></li>
      <li><a href="/team/ken">Ken Kirio</a></li>
      <li><a href="/team/member_3">Member 3</a></li>       

    </ul>
    
    
    '''

@app.route('/gpt/kevin', methods=['GET', 'POST'])
def kevin_gptdemo():
    ''' handle a get request by sending a form 
        and a post request by returning the GPT response
    
    '''
    if request.method == 'POST':
        prompt = request.form['prompt']
        answer = gptAPI.kevin_response(prompt)
        return f'''
        <h1>Travel Destinations</h1>
        <pre style="bgcolor:yellow">{prompt}</pre>
        <hr>
        Some places to consider visiting:
        <div style="border:thin solid black">{answer}</div>
        Some places to consider visiting:
        <pre style="border:thin solid black">{answer}</pre>
        <li><a href={url_for('kevin_gptdemo')}> make another query</a></li>
        <li><a href={url_for('index')}> back to home</a></li>

        
        '''
    else:
        return '''
        <h1>Travel Destinations</h1>
        Enter a place you want to visit
        <form method="post">
            <textarea name="prompt"></textarea>
            <p><input type=submit value="get response">
        </form>
        '''

@app.route('/gpt/ken', methods=['GET', 'POST'])
def ken_gptdemo():
    ''' handle a get request by sending a form 
        and a post request by returning the GPT response
    
    '''
    if request.method == 'POST':
        prompt = request.form['prompt']
        answer = gptAPI.ken_response(prompt)
        return f'''
        <h1>Ken's GPT Demo</h1>
        <pre style="bgcolor:yellow">{prompt}</pre>
        <hr>
        Here is the answer in text mode:
        <div style="border:thin solid black">{answer}</div>
        Here is the answer in text mode:
        <pre style="border:thin solid black">{answer}</pre>
        <li><a href={url_for('ken_gptdemo')}>Make another query</a></li>
        <li><a href={url_for('index')}> back to home</a></li>

        '''
    else:
        return '''
        <h1>Convert your code from Python to Java</h1>
         Input the Python code:
        <form method="post">
            <textarea name="prompt"></textarea>
            <p><input type=submit value="get response">
        </form>
        '''


if __name__=='__main__':
    # run the code on port 5001, MacOS uses port 5000 for its own service :(
    app.run(debug=True,port=5001)
=======
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 14:43:56 2023

@author: kevinchen
"""

from flask import request, redirect, url_for, Flask, render_template
from gpt import GPT
import os

app = Flask(__name__,  static_url_path='/static')
gptAPI = GPT(os.environ.get('APIKEY'))


@app.route('/')
def index():
    ''' display a link to the general query page '''
    print('processing / route')
    return '''
    <h1>Mid-Sized Sedan</h1>
    <ul>
      <li><a href="/gpt">Try Chat-GPT</a></li>
      <li><a href="/about">About Page</a></li>
      <li><a href="/team">Team Members</a></li>
      <li><a href="/index">Index</a></li>
      <img src="/static/altima.jpg" alt = "This should be a Honda Accord" style="width:888px;height:500px"/>
    </ul>
    '''


@app.route('/gpt', methods=['GET', 'POST'])
def gpt():
    return '''

    <h1>GPT Prompts</h1>
    
    <li><a href="/gpt/kevin">Travel destinations</a></li>
    <li><a href="/gpt/ken">Convert code from Python to Java with GPT</a></li>
    <li><a href="/gpt/jack">Runtime analysis of a python function with GPT</a></li>

    '''


@app.route('/about', methods=['GET', 'POST'])
def about():
    return '''
    <h1>GPT Demo About</h1>
    
    This program is a creative assignment by Kevin Chen, Ken Kirio, and Jack Napoleone, created in COSI 103, Spring 2023 <br>
    This is a web server app that takes in queries from the user, sends them to OpenAI's GPT, then returns its response.
    '''


@app.route('/team', methods=['GET', 'POST'])
def team():
    return '''
    <h1>Team Mid-Sized Sedan</h1>
    
    <ul>
      <li>Kevin created gpt.py and gptwebapp.py, made the index and about webpages, and wrote his gpt demo</li> 
      <li>Ken made the team webpage, altered the structure so each team member could write their own GPT query, and wrote his gpt demo</li> 
      <li>Jack fixed image links andwrote his gpt demo</li> 
    </ul>
    '''


@app.route('/team/kevin', methods=['GET', 'POST'])
def teamkevin():
    return '''

    <h1>Kevin Chen</h1>
    
    I worked on this project <br>
     <img src="/static/clown.jpg" alt = "This should be a clown licence">
    '''


@app.route('/team/ken', methods=['GET', 'POST'])
def teamken():
    return '''

    <h1>Ken Kirio</h1>

    I worked on this project. <br />
    Here's my GPT app: 
    <a href="/gpt/ken">Convert code from Python to Java with GPT</a></li>
    '''


@app.route('/team/jack', methods=['GET', 'POST'])
def teamjack():
    return '''
    <h1>Jack Napoleone</h1>
    Here's my GPT app:
    <a href="/gpt/jack">Get the runtime of a Python function</a>
    '''


@app.route('/index', methods=['GET', 'POST'])
def index2():
    return '''
    <h1>Team Members Index</h1>
    
    <ul>
      <li><a href="/team/kevin">Kevin Chen</a></li>
      <li><a href="/team/ken">Ken Kirio</a></li>
      <li><a href="/team/jack">Jack Napoleone</a></li>       
    </ul>
    '''


@app.route('/gpt/kevin', methods=['GET', 'POST'])
def kevin_gptdemo():
    ''' handle a get request by sending a form 
        and a post request by returning the GPT response
    '''
    if request.method == 'POST':
        prompt = request.form['prompt']
        answer = gptAPI.kevin_response(prompt)
        return f'''
        <h1>Travel Destinations</h1>
        <pre style="bgcolor:yellow">{prompt}</pre>
        <hr>
        Some places to consider visiting:
        <div style="border:thin solid black">{answer}</div>
        Some places to consider visiting:
        <pre style="border:thin solid black">{answer}</pre>
        <li><a href={url_for('kevin_gptdemo')}> make another query</a></li>
        <li><a href={url_for('index')}> back to home</a></li>

        
        '''
    else:
        return '''
        <h1>Travel Destinations</h1>
        Enter a place you want to visit
        <form method="post">
            <textarea name="prompt"></textarea>
            <p><input type=submit value="get response">
        </form>
        '''


@app.route('/gpt/ken', methods=['GET', 'POST'])
def ken_gptdemo():
    ''' handle a get request by sending a form 
        and a post request by returning the GPT response

    '''
    if request.method == 'POST':
        prompt = request.form['prompt']
        answer = gptAPI.ken_response(prompt)
        return f'''
        <h1>Ken's GPT Demo</h1>
        The Python code:
        <pre style="bgcolor:yellow">{prompt}</pre>
        <hr>
        The Java code:
        <pre style="border:thin solid black">{answer}</pre>
        <li><a href={url_for('ken_gptdemo')}>Make another query</a></li>
        <li><a href={url_for('index')}> back to home</a></li>
        '''
    else:
        return '''
        <h1>Convert your code from Python to Java</h1>
         Input the Python code:
        <form method="post">
            <textarea name="prompt"></textarea>
            <p><input type=submit value="get response">
        </form>
        '''


@app.route('/gpt/jack', methods=['GET', 'POST'])
def jack_gptdemo():
    ''' handle a get request by sending a form 
    and a post request by returning the GPT response
    '''
    if request.method == 'POST':
        prompt = request.form['prompt']
        answer = gptAPI.jack_response(prompt)
        return f'''
        <h1>GPT Demo</h1>
        <pre style="bgcolor:yellow">{prompt}</pre>
        <hr>
        Here is the answer in text mode:
        <div style="border:thin solid black">{answer}</div>
        Here is the answer in "pre" mode:
        <pre style="border:thin solid black">{answer}</pre>
        <a href={url_for('jack_gptdemo')}> make another query</a>
        '''
    else:
        return '''
        <h1>Python Runtime Analysis with GPT</h1>
        Enter your query below
        <form method="post">
            <textarea name="prompt"></textarea>
            <p><input type=submit value="get response">
        </form>
        '''


if __name__ == '__main__':
    # run the code on port 5001, MacOS uses port 5000 for its own service :(
    app.run(debug=True, port=5001)
>>>>>>> Stashed changes:ca01/gptwebapp.py
