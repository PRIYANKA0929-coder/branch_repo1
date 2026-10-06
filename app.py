from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""

    if request.method == "POST":
        a = int(request.form["a"])
        b = int(request.form["b"])
        result = a + b

    return render_template("index.html", result=result)

app.run(debug=True)