from flask import Flask, render_template, redirect, url_for, request, jsonify, flash


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


@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/contact")
def contact():
    return render_template('contact.html', title='Contact')


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        flash('New froggo added!')
        
        new_name = request.form["nome"],
        new_type = request.form["tipo"]

        new_frog = {
        "id": len(froggies),
        "name": new_name,
        "type": new_type
        }

        print(new_frog)
        froggies.append(new_frog)
        
        return redirect(url_for("user", dude=new_name))
    else:
        return render_template('home.html', frogs=froggies)
        

@app.route("/<dude>")
def user(dude):
    return render_template(f'frog_user.html', title={dude}, name={dude})


@app.errorhandler(400)
def bad_request():
    return "Oopsie-Daisy that's a Bad Request (err 404)"

if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'

    app.run(debug = True)







