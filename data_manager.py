'''
Реализовать класс, который будет обрабатывать csv-файл. Добавлять данные
или из этого файла отправлять данные, если потребуется. 
'''
import pandas as pd

class DataManager:
    
    def __init__(self, filename):
        df = pd.read_csv(filename)
        return df
    
    def add_water(self):
        '''В этом методе реализовать добавление в файл даты и кол-во воды 
        в мл'''
        pass
    
    def get_datetime(self):
        datetime = ''
        '''Этот метод должен возвращать дату из файла'''
        pass

    def get_ml(self):
        ml = 0
        '''Должен возвращать кол-во миллилитров в определенную дату
        или за все время'''
        pass