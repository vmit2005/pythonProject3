import pickle
import os

class Article:
    def __init__(self, title, author, page, description):
        self.title = title
        self.author = author
        self.page = page
        self.description = description

    def __str__(self):
        return f"{self.title} ({self.author})"


class ArticleModel:
    def __init__(self):
        self.db_name="db.txt"
        self.articles = self.load_data()

    def add_article(self, dict_article):
        article = Article(*dict_article.values())
        print("self.user_interface.add_user_article", article)
        self.articles[article.title] = article

    def get_all_article(self):
        return self.articles.values()

    def get_single_aticle(self, user_title):
        article = self.articles[user_title]
        dict_article = {
            "Название": article.title,
            "Автор": article.author,
            "Количество страниц": article.page,
            "Описание": article.description
        }
        return dict_article

    def remove_article(self,user_title):
        return self.articles.pop(user_title)

    def remove_single_article(user,article):
        print(f"Статья {article} - была удалена")

    def load_data(self):
        if os.path.exists(self.db_name):
            with open(self.db_name,"rb") as f:
                return pickle.load(f)
        else:
            return dict()

    def save_data(self):
        with open (self.db_name,"wb") as f:
            pickle.dump(self.articles,f)
