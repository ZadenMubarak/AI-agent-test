from flask import Flask

app = Flask(__name__)

@app.route("/")
def hi():

    return "<h1>Hello Gang!</h1>"

#CRUD

@app.route("/create")
def create():
    pass

@app.route('/read')
def read():
    pass

@app.route("/update")
def update():
    pass

@app.route("delete")
def delete():
    pass


app.run(host='localhost', port=8080)