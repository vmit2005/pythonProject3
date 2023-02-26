from viev import UserInterface
from ramка import Ramка, add_ramka
from model import Rebro_Model

class Controller:
    def __init__(self):
        self.user_interface=UserInterface()
        self.rebro_model=Rebro_Model()

    def  run(self):
        answer=None
        while answer !="q":
            self.user_interface = UserInterface()
            answer=self.user_interface.user_answer()
            print(answer)
            self.chek_answer(answer)

    def chek_answer(self,answer):

        if answer=="0":
            self.user_interface.coment()


        if answer=="1":
            self.user_interface.find_rebro()

        if answer=="2":
            new_rebro=self.user_interface.view_add_rebro()
            print(new_rebro)
            self.rebro_model.model_add_rebro(new_rebro)


