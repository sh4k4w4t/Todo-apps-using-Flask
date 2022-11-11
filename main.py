from flask import Flask,render_template,request,redirect

app= Flask(__name__)

allTodosData=[{"id":1,"title": "Test todos 1"},
         {"id":2,"title": "Test todos 2"},
         {"id":3,"title": "Test todos 3"},
         {"id":4,"title": "Test todos 4"}]

@app.route("/")
@app.route("/home",methods=["GET","POST"])
def home():
    if request.method=="POST":
        title=request.form["title"]
        new_todo={"id":len(allTodosData)+1,"title": title+f" {len(allTodosData) + 1}"}
        allTodosData.append(new_todo)

    return render_template("index.html",data=allTodosData)

@app.route("/remove/<int:todoid>")
def removeTodo(todoid):
    for todo in allTodosData:
        if todo["id"]==todoid:
            allTodosData.remove(todo)
    return redirect("/")

@app.route("/update/<int:todoid>")
def updateTodo(todoid):
    for todo in allTodosData:
        if todo["id"]==todoid:
            return render_template('update.html',todo=todo)
    return redirect('/')

@app.route("/updatetodo", methods=["POST"])
def update():
    title = request.form['title']
    id= request.form['id']
    for todo in allTodosData:
        if todo['id']==int(id):
            todo['title']=title
            return redirect('/')
    return "ERROR"

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
