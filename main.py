# import "packages" from flask
from flask import Flask, render_template, request
from algorithm.image import image_data
from pathlib import Path

# https://medium.com/@ageitgey/python-3-quick-tip-the-easy-way-to-deal-with-file-paths-on-windows-mac-and-linux-11a072b58d5f
# create a Flask instance
app = Flask(__name__)


# connects default URL to render index.html
@app.route('/')
def index():
    return render_template("index.html")


# connects /kangaroos path to render kangaroos.html
@app.route('/kangaroos/')
def kangaroos():
    return render_template("kangaroos.html")


@app.route('/walruses/')
def walruses():
    return render_template("walruses.html")


@app.route('/hawkers/')
def hawkers():
    return render_template("hawkers.html")


@app.route('/stub/')
def stub():
    return render_template("stub.html")


@app.route('/soma', methods=['GET', 'POST'])
def soma():
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:
            return render_template("Soma.html", nickname=name)
    return render_template("Soma.html", nickname="World")


@app.route('/nic', methods=['GET', 'POST'])
def nic():
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:
            return render_template("Nicolas.html", nickname=name)
    return render_template("Nicolas.html", nickname="World")


@app.route('/Paul', methods=['GET', 'POST'])
def paul():
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:
            return render_template("Paul.html", nickname=name)
    return render_template("Paul.html", nickname="World")


@app.route('/Jason', methods=['GET', 'POST'])
def jason():
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:
            return render_template("Jason.html", nickname=name)
    return render_template("Jason.html", nickname="World")

@app.route('/greet', methods=['GET', 'POST'])
def greet():
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:
            return render_template("greet.html", nickname=name)
    return render_template("greet.html", nickname="World")

@app.route('/designs/')
def designs():
    return render_template("designs.html")


@app.route('/binary/', methods=['GET', 'POST'])
def binary():
    if request.form:
        bits = request.form.get("bits")
        if int(bits) > 0:
            return render_template("Binary.html", BITS=int(bits))

    return render_template("Binary.html", BITS=8)

@app.route('/login/')
def login():
    return render_template("login.html")

@app.route('/rgb/', methods=["GET", "POST"])
def rgb():
    path = Path(app.root_path) / "static" / "assets"
    rawList = image_data(path)
    colorList = []
    grayList = []
    for img in rawList:
        colorList.append(img['base64'])
        grayList.append(img['base64_GRAY'])

    return render_template('rgb.html', images=rawList, colored=colorList, grayed=grayList)


# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)