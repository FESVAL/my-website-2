from flask import Flask, request, redirect, render_template

app = Flask(__name__)

@app.route("/base_page")
def base_page():
    return render_template("base_page.html")

@app.route("/base_page/me")
def me():
    return render_template("me.html")

@app.route("/base_page/contact")
def contact():
    films=[
        "127 hours",
        "Touching the void",
        "Money Heist"
        ]
    return render_template("contact.html", films=films)


if __name__=="__main__":
    app.run



