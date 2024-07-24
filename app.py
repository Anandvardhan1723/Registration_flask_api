from flask import Flask,url_for,request,render_template
app=Flask(__name__)
@app.route("/task",methods=["GET","POST"])
def task():
    if request.method=="POST":
        name=request.form["user"]
        print(name)
        email=request.form["mail"]
        print(email)
        number=request.form["num"]
        print(number)
        date=request.form["date"]
        print(date)
        time=request.form["time"]
        print(time)
    return render_template("index.html")
app.run(debug=True)