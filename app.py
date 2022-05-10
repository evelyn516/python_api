from flask import Flask, render_template, request, jsonify, flash


app = Flask(__name__)


froggies = [
    {
        "id": 0,
        "name": "Jeremiah",
        "type": "Bullfrog"
    },
    {
        "id": 1,
        "name": "Kermit",
        "type": "Green frog"
    },
    {
        "id": 2,
        "name": "Hypnotoad",
        "type": "Hypnotist"
    },
    {
        "id": 3,
        "name": "Pepe",
        "type": "Meme"
    }
]

@app.route("/")
def home():
    return render_template('home.html', frogs=froggies)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/contact")
def contact():
    return render_template('contact.html', title='Contact')


# experimental route
@app.route("/<dude>")
def user(dude):
    return render_template(f'frog_user.html', title={dude})

# @app.route('/frogs', methods=['GET', 'POST'])
# def frogs():
#     if request.method == 'GET':
#         return jsonify({"frogs" : froggies})
#     if request.method == 'POST':
#         flash('New froggo added!')
#         new_frog = {
#         "id": len(froggies),
#         "name": request.form["name"],
#         "type": request.form["type"]
#         }

#         froggies.append(new_frog)
        
#         return jsonify({'frog': new_frog})
#     else:
#         return render_template('home.html', frogs=froggies)
        

# @app.route('/anime', methods=['GET', 'POST'])
# def anime():
#     if request.method == 'GET':
#         return jsonify(animes)  
#     if request.method == 'POST':
#         data = request.json
#         data['id'] = len(animes) + 1
#         animes.append(data)
#         return f"{data['name']} has been added to the anime list!"


@app.route('/frogs', methods=['GET', 'POST'])
def frogs():
    if request.method == 'POST':
        flash('New froggo added!')
        
        new_name = request.form["nome"],
        new_type = request.form["tipo"]

        new_frog = {
        "id": len(froggies),
        "name": new_name,
        "type": new_type
        }

        froggies.append(new_frog)
        
        return render_template(f'frog_user.html', title={new_name})
    else:
        return render_template('home.html', frogs=froggies)

@app.errorhandler(400)
def bad_request():
    return make_response("Oopsie-Daisy that's a Bad Request (err 404)")

if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'

    app.debug = True
    app.run()






