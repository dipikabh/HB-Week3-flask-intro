"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']

INSULTS = [
  'stupid', 'dummy', 'dirtbag', 'dumbass'
]


@app.route('/')
def start_here():
    """Home page."""


    return """
    <!doctype html>
      <html>
        <body>
          <p>Hi! This is the home page.</p>
          <p><a href="/hello">Click here to go to the next page.</a></p>

        </body>
      </html>"""


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          <p>What's your name? <input type="text" name="person"></p>
          <p>Select a compliment for yourself: 
            <select name="compliment">
              <option value="awesome">Awesome</option>
              <option value="fantastic">Fantastic</option>
              <option value="fantabulous">Fantabulous</option>
              <option value="neato">Neato</option>
              <option value="wowza">Wowza</option>
              <option value="lovely">Lovely</option>
              <option value="smashing">Smashing</option>
            </select>
          </p>
          <div><input type="submit" value="Submit"></div>
        </form>
      </body>
    </html>
    """


@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    # compliment = choice(AWESOMENESS)
    compliment = request.args.get("compliment")

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {player}! I think you're {compliment}!
      </body>
    </html>
    """.format(player=player, compliment=compliment)


@app.route('/diss')
def insult_person():
    """Get user by name."""

    player = request.args.get("person")
    
    insult = choice(INSULTS)
    # compliment = request.args.get("compliment")

    return """
    <!doctype html>
    <html>
      <head>
        <title>An Insult</title>
      </head>
      <body>
        Hi, {}! I think you're {}!
      </body>
    </html>
    """.format(player, insult)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True)
