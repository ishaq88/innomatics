from flask import Flask, render_template, request

app = Flask(__name__)

notes = []
#updating the methods to this route
@app.route('/', methods=["POST", 'GET'])
def index():
    if request.method == "POST": #fetching notes only when method is post
        note = request.form.get("note") #replaced args with forms
        notes.append(note)
        
    return render_template("home.html", notes=notes)


if __name__ == '__main__':
    app.run(debug=True)