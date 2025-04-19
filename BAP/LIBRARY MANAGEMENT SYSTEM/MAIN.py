from flask import Flask, request, render_template
from lms import *

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def form_submit():
    if request.method == "GET":
        return render_template("index.html")

    id = request.form["idText"]
    title = request.form["titleText"]
    author = request.form["authorText"]
    year = request.form["yearText"]
    search = request.form["searchText"]

    dbobj = LMS()
    dbobj.ConnectDB()
    dbobj.CreateTable()

    if request.form["action_button"] == "Add a book":
        booksText = dbobj.AddBook(int(id), title, author, int(year))
    elif request.form["action_button"] == "Update a book":
        booksText = dbobj.UpdateBook(int(id), title, author, int(year))
    elif request.form["action_button"] == "Delete a book":
        booksText = dbobj.DeleteBook(int(id))
    else:
        ret = dbobj.SearchBook(search)
        if "There is no book" not in ret:
            booksText = ">>> Number of books retrieved is: " + str(len(ret)) + "\n"
            for book in ret:
                booksText += str(book) + "\n"
        else:
            booksText = ret
    return render_template("index.html", i=id, t=title, a=author, y=year, s=search, b=booksText)


if __name__ == "__main__":
    app.run(debug=True)