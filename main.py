# import "packages" from flask
from flask import Flask, render_template, request
from algorithm.image import image_data
from pathlib import Path
import math

# https://medium.com/@ageitgey/python-3-quick-tip-the-easy-way-to-deal-with-file-paths-on-windows-mac-and-linux-11a072b58d5f
# create a Flask instance
app = Flask(__name__)


# connects default URL to render index.html
@app.route('/')
def index():
    return render_template("Other/index.html")


# connects /kangaroos path to render kangaroos.html
@app.route('/kangaroos/')
def kangaroos():
    return render_template("Other/kangaroos.html")


@app.route('/walruses/')
def walruses():
    return render_template("Other/walruses.html")


@app.route('/stub/')
def stub():
    return render_template("Other/stub.html")


@app.route('/soma', methods=['GET', 'POST'])
def soma():
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:
            return render_template("AboutUs/Soma.html", nickname=name)
    return render_template("AboutUs/Soma.html", nickname="World")


@app.route('/nic', methods=['GET', 'POST'])
def nic():
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:
            return render_template("AboutUs/Nicolas.html", nickname=name)
    return render_template("AboutUs/Nicolas.html", nickname="World")


@app.route('/Paul', methods=['GET', 'POST'])
def paul():
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:
            return render_template("AboutUs/Paul.html", nickname=name)
    return render_template("AboutUs/Paul.html", nickname="World")


@app.route('/Jason', methods=['GET', 'POST'])
def jason():
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:
            return render_template("AboutUs/Jason.html", nickname=name)
    return render_template("AboutUs/Jason.html", nickname="World")


@app.route('/greet', methods=['GET', 'POST'])
def greet():
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:
            return render_template("MiniLabs/greet.html", nickname=name)
    return render_template("MiniLabs/greet.html", nickname="World")


@app.route('/designs/')
def designs():
    return render_template("layouts/designs.html")


@app.route('/dbd/')
def dbd():
    return render_template("ForWebPage/dbd.html")

@app.route('/horror/')
def horror():
    return render_template("ForWebPage/horror.html")

@app.route('/gamefinder/')
def gamefinder():
    return render_template("ForWebPage/gamefinder.html")

@app.route('/platforms/')
def platforms():
    return render_template("ForWebPage/platforms.html")

@app.route('/binary/', methods=['GET', 'POST'])
def binary():
    if request.form:
        bits = request.form.get("bits")
        if int(bits) > 0:
            return render_template("MiniLabs/binary.html", BITS=int(bits))

    return render_template("MiniLabs/binary.html", BITS=8)


@app.route('/login/')
def login():
    return render_template("layouts/login.html")


@app.route('/rgb/', methods=["GET", "POST"])
def rgb():
    path = Path(app.root_path) / "static" / "assets"
    color = []
    gray = []
    for img in image_data(path):
        color.append(img['base64'])
        gray.append(img['base64_GRAY'])

    return render_template('MiniLabs/rgb.html', images=image_data(path), colored=color, grayed=gray)


@app.route('/addbinary/', methods=['GET', 'POST'])
def addbinary():
    if request.form:
        bits = request.form.get("bits")
        if int(bits) > 0:
            return render_template("MiniLabs/addbinary.html", BITS=int(bits))

    return render_template("MiniLabs/addbinary.html", BITS=8)

@app.route('/journals/')
def journals():
    return render_template("MiniLabs/journals.html")

# @app.route('/colorcode/')
# def colorcode():
#     return render_template("MiniLabs/colorcode.html")


# runs the application on the development server
@app.route('/hawkers/', methods=['GET', 'POST'])
def hawkers():
    if request.form:
        value1 = request.form.get("value1")
        value2 = request.form.get("value2")
        if int(value1) == 1:
            return render_template("Other/hawkers.html", output=int(value1))
        if int(value2) == 1:
            return render_template("Other/hawkers.html", output=int(value2))
        return render_template("Other/hawkers.html", output=0)
    return render_template("Other/hawkers.html")

@app.route('/logicgate/')
def logicgate():
    return render_template("MiniLabs/logicgate.html")

@app.route('/colorcode')
def colorcode():
    return render_template("layouts/colorcode.html")

@app.route('/overwatch')
def overwatch():
    return render_template("ForWebPage/overwatch.html")

#@app_starter.route('/joke', methods=['GET', 'POST'])
#def joke():
#    """
 #   # use this url to test on and make modification on you own machine
  #  url = "http://127.0.0.1:5222/api/joke"
   # """
    #url = "https://csp.nighthawkcodingsociety.com/api/joke"
    #response = requests.request("GET", url)
    #return render_template("other/joke.html", joke=response.json())


#@app_starter.route('/jokes', methods=['GET', 'POST'])
#def jokes():
 #   """
  #  # use this url to test on and make modification on you own machine
   # url = "http://127.0.0.1:5222/api/jokes"
    #"""
    #url = "https://csp.nighthawkcodingsociety.com/api/jokes"

    #response = requests.request("GET", url)
    #return render_template("Other/jokes.html", jokes=response.json())

if __name__ == "__main__":
    app.run(debug=True)
