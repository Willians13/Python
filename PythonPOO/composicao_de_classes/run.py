class Insert:
    def insert_many(self):
        print('Insert_many')
        
    def insert_one(self):
        print('Insert_one')

class Select:
    def select_many(self):
        print('Select_many')
        
    def select_one(self):
        print('Select_one')

class Repositorio:
    
    def __init__(self):
        self.__insert = Insert()
        self.__select = Select()
    
    def select_by_id(self):
        self.__select.select_one()

repo = Repositorio()

repo.select_by_id()