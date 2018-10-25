from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = '''
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color:#eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16 px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <h1>WEB CAESAR</h1>
        <p>Enter A Number To Rotate By And A Message To Encrypt</p>
        <form action="/" method="POST">
            <label>Rotate by:
                <input type="text" name="rot" value="0">
            </label>
            <label>And Message To Be Encrypted:
                <textarea name="text">{0}</textarea>
            </label>
            <input type="submit" value="ENCRYPT!">
        </form>
    </body>
</html>'''

@app.route("/")
def index():
    new_string = ""
    return form.format(new_string)

@app.route("/", methods=["POST"])
def encrypt():
    meat = str(request.form["text"])
    heat = int(request.form["rot"])
    steak = rotate_string(meat,heat)
    meal = "<h1>" + steak + "</h1>"
    return form.format(steak)

if __name__=="__main__":
    app.run()