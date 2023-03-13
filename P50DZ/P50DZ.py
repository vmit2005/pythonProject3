from flask import Flask, render_template, url_for


app=Flask(__name__)
menu = [{"name":"Кому нужен водонагреватель", "url":"index"},
        {"name":"Накопительный или проточный", "url":"cumulative"},
        {"name":"Кому не нужен ", "url":"not_needed"},
        {"name":"Cколько стоит", "url":"price"},
        {"name":"Обратная связь", "url":"contact"}]


@app.route("/")
@app.route("/index")
def index():
    # print(url_for('index'))
    return render_template("index.html",title="Главная", menu=menu)

@app.route("/cumulative")
def cumulative():
    # print(url_for('about'))
    return render_template("cumulative.html", title="Накопительный или проточный", menu=menu)



@app.route("/not_needed")
def not_needed():
    # print(url_for('about'))
    return render_template("not_needed.html", title="Кому не нужен Водонагреватель", menu=menu)

@app.route("/price")
def price():
    return render_template("price.html", title="Цена", menu=menu)


@app.route("/contact", methods=["POST","GET"])
def contact():
    return render_template("contact.html", title="обратная связь", menu=menu)



@app.route("/profile/<path:username>")
def profile(username):
    return f"Пользователь: {username}"



if __name__=="__main__":
    app.run(debug=True)