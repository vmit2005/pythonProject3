import pickle
import os

class Rebro:
    def __init__(self, number, a, b, c, s, marka, not_s):
        self.number = number
        self.a = a
        self.b = b
        self.c = c
        self.s = s
        self.marka = marka
        self.not_s = not_s

    def __str__(self):
        return f"Обозначение {self.number}\nРазмеры A, B, C {self.a}x{self.b}-{self.c} \n Толщина {self.s} \n Марка стали {self.marka}\nИмеются неуказанные параметры {self.not_s}"



class Rebro_Model:
    def __init__(self):
        self.rebro_db = "rebro.re"
        self.rebros = self.load_data()

    def model_add_rebro(self, rebro):
        print("model_Add_rebro",rebro)
        detal = Rebro(*rebro.values())
        self.rebros[rebro.number]=detal

    def load_data(self):
        if os.path.exists(self.rebro_db):
            with open(self.rebro_db,"rb") as f:
                return pickle.load(f)
        else:
            return dict()

    def save_data(self):
        with open(self.rebro_db, "wb") as f:
            pickle.dump(self.articles, f)

