from flask import Flask, render_template, request, jsonify, flash


app = Flask(__name__)


froggies = [
    {
        "name": "Jeremiah",
        "type": "Bullfrog"
    },
    {
        "name": "Kermit",
        "type": "Green frog"
    },
    {
        "name": "Hypnotoad",
        "type": "Hypnotist"
    },
    {
        "name": "Pepe",
        "type": "Meme"
    }
]

@app.route("/")
def home():
    return render_template('home.html', froggies=froggies)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/contact")
def contact():
    return render_template('contact.html', title='Contact')


""" @app.route('/frogs', method=['GET', 'POST'])
def frog():
    if request.method == 'GET':
        return jsonify(froggies)
    if request.method == 'POST':
        return f"{frog['name']} has joined the party" """


if __name__ == '__main__':
    app.run(debug=True)







