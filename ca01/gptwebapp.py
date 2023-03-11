# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 17:58:42 2023

@author: kevinchen
"""

from flask import request,redirect,url_for,Flask
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
      <li><a href="/about">About Page</a></li>
      <li><a href="/team">Team Members</a></li>
      
      <li><a href="/index">Index</a></li>

      
      
      <img src="/static/altima.jpg" alt = "This should be a Honda Accord" style="width:888px;height:500px"/>
       

    </ul>

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

    <a href="/kevin/gptdemo">Ask ChatGPT about [topic]</a>


    I worked on this project <br>
    
     <img src="/static/clown.jpg" />

    
    '''

@app.route('/team/ken', methods=['GET', 'POST'])
def teamken():
    return '''

    <h1>Ken Kirio</h1>

    <a href="/ken/gptdemo">Convert code from Python to Java with GPT</a>


    
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

@app.route('/kevin/gptdemo', methods=['GET', 'POST'])
def kevin_gptdemo():
    ''' handle a get request by sending a form 
        and a post request by returning the GPT response
    
    '''
    if request.method == 'POST':
        prompt = request.form['prompt']
        answer = gptAPI.getResponse(prompt)
        return f'''
        <h1>GPT Demo</h1>
        <pre style="bgcolor:yellow">{prompt}</pre>
        <hr>
        Here is the answer in text mode:
        <div style="border:thin solid black">{answer}</div>
        Here is the answer in "pre" mode:
        <pre style="border:thin solid black">{answer}</pre>
        <a href={url_for('kevin_gptdemo')}> make another query</a>
        '''
    else:
        return '''
        <h1>GPT Demo App</h1>
        Enter your query below
        <form method="post">
            <textarea name="prompt"></textarea>
            <p><input type=submit value="get response">
        </form>
        '''

@app.route('/ken/gptdemo', methods=['GET', 'POST'])
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
        Here is the answer in "pre" mode:
        <pre style="border:thin solid black">{answer}</pre>
        <a href={url_for('ken_gptdemo')}>Make another query</a>
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