from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app= Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///app.db'
app.config['SECRET_KEY']='a9003e534d94472d88dd294b2f126bb3'
SQLAlCHEMY_TRACK_MODIFICATIONS= True
db= SQLAlchemy(app)
migrate= Migrate(app,db)

class ToDo(db.Model):
    id= db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(200))

@app.route("/")
@app.route("/home",methods=["GET","POST"])
def home():
    if request.method=="POST":
        title= request.form["title"]
        todo= ToDo(title=title)
        db.session.add(todo)
        db.session.commit()
        return redirect('/')
    dataAll= ToDo.query.all()
    return render_template("index.html",data=dataAll)


@app.route("/remove/<int:todoid>")
def removeTodo(todoid):
    todo= db.session.query(ToDo).filter_by(id=todoid).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect("/")


@app.route("/update/<int:todoid>")
def updateTodo(todoid):
    todos = db.session.query(ToDo).filter_by(id=todoid).first()
    return render_template('update.html', todo=todos)
@app.route("/updatetodo", methods=["POST"])
def update():
    title = request.form['title']
    id= request.form['id']
    todos = db.session.query(ToDo).filter_by(id=id).first()
    todos.title=title
    db.session.commit()
    return redirect("/")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__=="__main__":
    app.run(debug=True)
















# # This is a sample Python script.
#
# # Press Shift+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
