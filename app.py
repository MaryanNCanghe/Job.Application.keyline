from flask import Flask, render_template,jsonify

app = Flask(__name__)

JOBS =[
  {
    'id': 1,
    'title':'Data Analyst',
    'localização':' portugal, lisboa',
    'salário':'1.000€'
  },
  {
     'id': 2,
    'title':'Data Analyst',
    'localização':'frança, lyon',
    'salário':'4.000€'
  },
  {
   'id': 3,
    'title':'web develoter',
    'localização':'Norway, oslo',
    'salário':'7.000€'
 },
   {
   'id': 4,
    'title':'web develoter',
    'localização':'remote',
    'salário':'10.000€'
 },
]


@app.route("/")
def hello_keyline():
  return render_template('home.html', 
                         jobs=JOBS, 
                         company_name='keyline')

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
