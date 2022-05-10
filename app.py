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
def welcome():
    return "Welcome to the world of frogs"

@app.route("/home")
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

@app.route('/frogs', methods=['GET', 'POST'])
def frogs():
    if request.method == 'GET':
        return jsonify({"frogs" : froggies})
    if request.method == 'POST':
        flash('New froggo added!')
        new_frog = {
        "id": len(froggies),
        "name": request.form["name"],
        "type": request.form["type"]
        }

        froggies.append(new_frog)
        
        return jsonify({'frog': new_frog})
    else:
        return render_template('home.html', frogs=froggies)
        

# @app.route('/anime', methods=['GET', 'POST'])
# def anime():
#     if request.method == 'GET':
#         return jsonify(animes)  
#     if request.method == 'POST':
#         data = request.json
#         data['id'] = len(animes) + 1
#         animes.append(data)
#         return f"{data['name']} has been added to the anime list!"


if __name__ == '__main__':
    app.run(debug=True)







