import json
import pandas as pd
import random
import plotly.graph_objects as go
import plotly.express as px
from flask import Flask, render_template, request, session
from flask_session.__init__ import Session

''' Loading Tree Data '''
f = open("tree.json", 'r')
tree = json.load(f)
f.close()

''' Tree Nodes Construction '''
class Node():
    def __init__(self, left = None, right = None, data = None):
        self.left = left
        self.right = right
        self.data = data

'''Questions Nodes'''
movie = Node(data = tree[0])
movie.left = Node(data = tree[1][0])
movie.left.left = Node(data = tree[1][1][0])
movie.left.right = Node(data = tree[1][1][0])
movie.left.left.left = Node(data = tree[1][1][1][0])
movie.left.right.right = Node(data = tree[1][1][1][0])
movie.left.left.right = Node(data = tree[1][1][1][0])
movie.left.right.left = Node(data = tree[1][1][1][0])
movie.right = Node(data = tree[1][0])
movie.right.left = Node(data = tree[1][1][0])
movie.right.right = Node(data = tree[1][1][0])
movie.right.left.left = Node(data = tree[1][1][1][0])
movie.right.right.right = Node(data = tree[1][1][1][0])
movie.right.left.right = Node(data = tree[1][1][1][0])
movie.right.right.left = Node(data = tree[1][1][1][0])

'''Data Nodes'''
movie.left.left.left.left = Node(data = tree[1][1][1][1][0])
movie.left.left.left.right = Node(data = tree[1][1][1][2][0])
movie.left.left.right.left = Node(data = tree[1][1][2][1][0])
movie.left.left.right.right = Node(data = tree[1][1][2][2][0])
movie.left.right.left.left = Node(data = tree[1][2][1][1][0])
movie.left.right.left.right = Node(data = tree[1][2][1][2][0])
movie.left.right.right.left = Node(data = tree[1][2][2][1][0])
movie.left.right.right.right = Node(data = tree[1][2][2][2][0])
movie.right.left.left.left = Node(data = tree[2][1][1][1][0])
movie.right.left.left.right = Node(data = tree[2][1][1][2][0])
movie.right.left.right.left = Node(data = tree[2][1][2][1][0])
movie.right.left.right.right = Node(data = tree[2][1][2][2][0])
movie.right.right.left.left = Node(data = tree[2][2][1][1][0])
movie.right.right.left.right = Node(data = tree[2][2][1][2][0])
movie.right.right.right.left = Node(data = tree[2][2][2][1][0])
movie.right.right.right.right = Node(data = tree[2][2][2][2][0])



def get_recommendations(q1,q2,q3,q4):
    '''
    get the corresponding data according to answers to questions
    '''
    current_node = movie
    for i in [q1,q2,q3,q4]:
        if i == 'y':
            current_node = current_node.left
        elif i == 'n':
            current_node = current_node.right

    rec_list = []
    for movies in current_node.data:
        rec_list.append(movies)
    return rec_list



''' Setting Up Flask '''
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommendation')
def form_recommendation():
    return render_template('questions.html')

@app.route('/results', methods=['POST'])
def results():
    ans1 = request.form['ans1']
    ans2 = request.form['ans2']
    ans3 = request.form['ans3']
    ans4 = request.form['ans4']
    results = get_recommendations(ans1,ans2,ans3,ans4)
    result_list = []
    for n in range(len(results)):
        result_list.append(f"[{n+1}] {results[n]['title']} - {results[n]['rating']}")
    session['my_var'] = results
    return render_template('results.html', result_list = result_list, results = results)

@app.route('/details', methods=['POST'])
def plot():
    selected_num = int(request.form['track'])
    results = session.get('my_var', None)
    title = results[selected_num]["title"]
    director = results[selected_num]["director"]
    genre = results[selected_num]["genres"]
    year = results[selected_num]["year"]
    cast = results[selected_num]["cast"]
    countries = results[selected_num]["countries"]
    imdb_id = results[selected_num]["imdb_id"]
    rating = results[selected_num]["rating"]
    
    
    return render_template('details.html', title = title, rating = rating, year = year, director = director, cast = cast, genre=genre, imdb_id = imdb_id, countries = countries)


if __name__=="__main__":
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run(debug=True)