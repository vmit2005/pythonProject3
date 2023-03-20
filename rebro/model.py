import pickle
import os


# class Rebro:
#     def __init__(self, number, a, b, c, s, marka, not_s):
#         self.number = number
#         self.a = a
#         self.b = b
#         self.c = c
#         self.s = s
#         self.marka = marka
#         self.not_s = not_s
#
#     def __str__(self):
#         return f"Обозначение {self.number}\nРазмеры A, B, C: {self.a}x{self.b}-{self.c} \nТолщина {self.s} \nМарка стали {self.marka}\nИмеются неуказанные параметры {self.not_s}"


class Rebro_Model():
    def __init__(self):
        self.rebro_db = "rebro.re"
        self.rebros = []
        self.rebros = self.load_data()

    def __str__(self):
        p = ""

        for i in self.rebros:
            print(
            "Обозначение чертежа"+i["Обозначение чертежа"]+"\n",
            "A", i["A"],"\n",
            "B", i["B"],"\n",
            "C",i["C"],"\n",
            "S",i["S"],"\n",
            "марка",i["марка"],"\n",
            "не указанные параметры",i["не указанные параметры"])


        return p

    def model_find_rebro(self,a,b):
        k=1.25
        amin=float(a)/k
        amax=float(a)*k
        bmin=float(b)/k
        bmax=float(b)*k
        print(amin,amax,bmin,bmax)
        for i in self.rebros:
            if amin<float(i["A"])<amax or bmin<float(i["B"])<bmax:
                print(i['Обозначение чертежа'],":",i['A'],"x",i['B'])


    def model_add_rebro(self, rebro):
        self.rebros.append(rebro)

    def load_data(self):
        if os.path.exists("rebro.re"):
            with open(self.rebro_db, "rb") as f:
                return load(f)
        else:
            return dict()

    def save_data(self):
        with open(self.rebro_db, "wb") as f:
            pickle.dump(self.rebros, f)

    def load_data(self):
        if os.path.exists(self.rebro_db):
            with open(self.rebro_db, "rb") as f:
                p=pickle.load(f)
                return p
        else:
            return dict()

    def del_rebro(self,number):
        for i in range(len(self.rebros)):
            if self.rebros[i]==number:
                self.rebros.pop[i]





def main():
    # a = Rebro("6696 677", 20, 30, 8, 6, "Ст3", "N")
    # print(a)

    new_rebro = {
        "Обозначение чертежа": "1234 567 8901 234",
        "A": 50,
        "B": 20,
        "C": 8,
        "S": 4,
        "марка": "Ст 3",
        "не указанные параметры": "N"
    }
    new_rebro2 = {
        "Обозначение чертежа": "4567 567 8901 234",
        "A": 150,
        "B": 120,
        "C": 10,
        "S": 8,
        "марка": "Ст 3",
        "не указанные параметры": "N"
    }
    rm = Rebro_Model()
    # rm.rebros=rm.load_data()
    print(rm)
    print("load data_rm", rm)
    rm.model_add_rebro(new_rebro)
    print("add rebro1")
    rm.model_add_rebro(new_rebro2)
    print(rm)
    rm.save_data()
    # rm.del_rebro("2")
    # print(rm)


if __name__ == '__main__':
    main()
