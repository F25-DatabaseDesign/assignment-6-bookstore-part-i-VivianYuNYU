from flask import Flask, render_template, request, redirect, url_for, make_response


# instantiate the app
app = Flask(__name__)
categories = [
    [1, "Fantasy"],
    [2, "Mystery"],
    [3, "Science Fiction"],
    [4, "Romance"],
]

books = [
    #Harry Potter and the Sorcerer's Stone
    [1, 1, "Harry Potter and the Sorcerer's Stone", "J.K. Rowling", "13-9780590353427", 9.50, "Harry Potter and the Sorcerer's Stone.png", 1],
    #The Lord of the Rings: The Fellowship of the Ring
    [2, 1, "The Lord of the Rings: The Fellowship of the Ring", "J.R.R. Tolkien", "13-9780547928210", 10.41, "The Lord of the The Fellowship of the Ring.png", 0],
    #A Game of Thrones
    [3, 1, "A Game of Thrones", "George R. R. Martin", "13-9780553593716", 18.00, "A Game of Thrones.png", 0],
    #The Chronicles of Narnia: The Lion, the Witch and the Wardrobe
    [4, 1, "The Chronicles of Narnia: The Lion, the Witch and the Wardrobe", "C.S. Lewis", "13-9780064471046", 8.99, "The Chronicles of Narnia.png", 0],
    #The Da Vinci Code
    [5, 2, "The Da Vinci Code", "Dan Brown", "13-9780307474278", 9.99, "The Da Vinci Code.png", 0],
    #And Then There Were None
    [6, 2, "And Then There Were None", "Agatha Christie", "13-9780062073488", 10.99, "And Then There Were None.png", 1],
    #Gone Girl
    [7, 2, "Gone Girl", "Gillian Flynn", "13-9780307588371", 9.99, "Gone Girl.png", 0],
    #Sherlock Holmes: The Hound of the Baskervilles
    [8, 2, "Sherlock Holmes: The Hound of the Baskervilles", "Arthur Conan Doyle", "13-9780141034324", 10.99, "Sherlock Holmes.png", 0],
    #Dune
    [9, 3, "Dune", "Frank Herbert", "13-9780593099322", 10.99, "Dune.png", 1],
    #1984
    [10, 3, "1984", "George Orwell", "13-9780451524935", 9.99, "1984.png", 0],
    #The Hitchhiker's Guide to the Galaxy
    [11, 3, "The Hitchhiker's Guide to the Galaxy", "Douglas Adams", "13-9780345391803", 8.99, "The Hitchhiker's Guide to the Galaxy.png", 0],
    #Ender's Game
    [12, 3, "Ender's Game", "Orson Scott Card", "13-9780812550702", 10.99, "Ender's Game.png", 0],
    #Pride and Prejudice
    [13, 4, "Pride and Prejudice", "Jane Austen", "13-9780141439518", 9.99, "Pride and Prejudice.png", 1],
    #The Notebook
    [14, 4, "The Notebook", "Nicholas Sparks", "13-9781455582877", 9.99, "The Notebook.png", 0],
    #Me Before You
    [15, 4, "Me Before You", "Jojo Moyes", "13-9780143130154", 10.99, "Me Before You.png", 1],
    #Gone with the Wind
    [16, 4, "Gone with the Wind", "Margaret Mitchell", "13-9781451635621", 22.00, "Gone with the Wind.png", 0]
]
# set up routes
@app.route('/')
def home():
    return render_template("index.html", categories=categories)


@app.route('/category')
def category():
    category_id = request.args.get("categoryId", type=int)

    if category_id is None:
        return render_template("error.html", error="No categoryId was provided.")

    selected_books = [b for b in books if b[1] == category_id]

    return render_template(
        "category.html",
        selectedCategory=category_id,
        categories=categories,
        books=selected_books
    )


@app.route('/search', methods=["POST"])
def search():
    keyword = request.form.get("search", "").lower()

    results = [b for b in books if keyword in b[2].lower()]

    return render_template(
        "category.html",
        selectedCategory=None,
        categories=categories,
        books=results
    )

@app.errorhandler(Exception)
def handle_error(e):
    return render_template("error.html", error=e)

if __name__ == "__main__":
    app.run(debug=True)
