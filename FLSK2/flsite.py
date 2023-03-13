from flask import Flask, render_template, url_for


app=Flask(__name__)
menu = [{"name":"Главная", "url":"index"},
        {"name":"Онас", "url":"About"},
        {"name":"Обратная связь", "url":"contact"}]


@app.route("/")
@app.route("/index")
def index():
    print(url_for('index'))
    return render_template("index.html",title="Главная", menu=menu)



@app.route("/about")
def about():
    print(url_for('about'))
    return render_template("about.html", title="О нас", menu=menu)


@app.route("/contact", methods=["POST","GET"])
def contact():
    return render_template("contact.html", title="обратная связь", menu=menu)



@app.route("/profile/<path:username>")
def profile(username):
    return f"Пользователь: {username}"



if __name__=="__main__":
    app.run(debug=True)