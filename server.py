from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    users = [
        {'first_name' : 'Emir', 'last_name' : 'Kasen'},
        {'first_name' : 'Era', 'last_name' : 'Malikov'},
        {'first_name' : 'Ara', 'last_name' : 'Airikulov'},
        {'first_name' : 'Zaven', 'last_name' : 'Grigoryan'}
    ]
    return render_template("html_table.html",users=users)



if __name__=="__main__":
    app.run(debug=True)
