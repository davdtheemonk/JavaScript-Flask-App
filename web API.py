#API - Application programming interface
"""This is a part of a computer program designed to be used or manipulated by another program
Reasons for creating an API:
    1.Your data set is larger
    2.Users require acces to your data in real time
    3.Your data changes rapidly/oftenly
    4.Your users will need access to a part of the data at any one time
    5.Your users will need to perform actions other than rertrieve data ,such as contributing ,updating,or deleting data"""

import flask

from flask import request,jsonify,render_template

app = flask.Flask(__name__)
app.config["DEBUG"] = True

#Test data
data = [
    {'id':0,
    'name':'programmer X',
    'language':'Python,JS,Java',
    'product':'Web API'},
    {'id':1,
    'name':'Bill Gates',
    'language':'C#',
    'product':'Windows'},
    {'id':2,
    'name':'Steve Jobs',
    'language':'Assembly',
    'product':'Apple'
    }
]

@app.route('/',methods=['GET'])
def home():#This will show when localhost is loaded in the browser
     return render_template('index.html')

@app.route('/api/docs/hackers/all',methods=['GET'])
def api_all():
    return jsonify(data)

@app.route('/api/docs/hackers',methods=['GET'])
def api_id():
    if 'name' in request.args:
        name = request.args['name']
    else:
        return "Error : the hacker isn't famous brudda (:."

    results=[]
    for info in data:
        if info['name'] == name:
            results.append(info)
    
    return jsonify(results)
    
app.run()
