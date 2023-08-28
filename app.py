from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime 

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///bbd.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class bbd(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, default= datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"
with app.app_context():
    db.create_all()

@app.route("/", methods=["GET", "POST"])
def hello_world():
    if request.method == "POST":
        print("post")
    object = bbd(title = "FIrst Person", desc ="Start donating blood")
    db.session.add(object)
    db.session.commit()
    allobject= bbd.query.all()
    print(allobject)
    return render_template("index.html", allobject = allobject)
    # return "<p>Hello, World!</p>"

@app.route("/blood")
def blood():
    allobject= bbd.query.all()
    print(allobject)
    return "<p>This is blood grougps page</p>"

if __name__ == "__main__":
    app.run(debug=True, port = 8000)