from viev import UserInterface
from ramка import Ramка, add_ramka
from model import Rebro_Model


class Controller:
    def __init__(self):
        self.user_interface = UserInterface()
        self.rebro_model = Rebro_Model()

    def run(self):
        answer = None
        while answer != "q":
            self.user_interface = UserInterface()
            answer = self.user_interface.user_answer()
            print(answer)
            self.chek_answer(answer)

    def chek_answer(self, answer):

        if answer == "0":
            self.user_interface.coment()

        if answer == "1":
            a,b=self.user_interface.find_rebro()
            self.rebro_model.model_find_rebro(a,b)

        if answer == "2":
            new_rebro = self.user_interface.view_add_rebro()
            self.rebro_model.model_add_rebro(new_rebro)
            print(self.rebro_model)
            Ramка(50, "", "Новая деталь добавлена в базу", "","Предполагается, что сдесь должно быть", "обращение к КОМПАССу","для постоения 3D-модели и чертежа"," ")

        if answer == "3":
            print(self.rebro_model)

        if answer == "4":
            num=self.user_interface.viev_del_rebro_insert()

            for i in self.rebro_model.rebros:
                if i["Обозначение чертежа"]==num:
                    self.rebro_model.del_rebro(num)
                    break
            else:
                print ("деталь с номером "+num+"не найдена")


        if answer == "q":
            self.rebro_model.save_data()
