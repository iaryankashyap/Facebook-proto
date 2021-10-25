from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/details_check", methods=["POST"])
def detailchk():
    if request.method=="POST":
        name=request.form.get("nm")
        password=request.form.get("password")
    if name=="superuser" and password=="root":
        return render_template("home.html")
    else:
        return render_template("wrong.html")


if __name__=="__main__":
    app.run(debug=True)
