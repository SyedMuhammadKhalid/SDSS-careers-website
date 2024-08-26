from flask import Flask, render_template
app= Flask(__name__)
JOBS =[
    {
        'id':1,
        'title':'Team Lead',
        'Location':'Quetta, Pakistan',
        'Salary': 'Competetive',
        
    },
    { 
        'id':2,
        'title':'Research Associate',
        'Location':'Quetta, Pakistan',
        'Salary': 'Competetive',
    },
{
    'id':3,
    'title':'Research Assistant',
    'Location':'Quetta, Pakistan',
    'Salary': 'Competitive',
}
]
@app.route("/")
def hello():
    return render_template('home.html',jobs=JOBS)
if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)
    
