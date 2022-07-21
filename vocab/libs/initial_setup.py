import os
from db import SQLiteDB
import json


def check_initial_data(main_path="D:\\study\\_StudyProjects\\vocab", auto_create=True):
    create_initial_data(main_path) if not os.path.exists(f"{main_path}\\data\\") and auto_create is True else None

def create_initial_data(main_path="D:\\study\\_StudyProjects\\vocab"):
    data_path = f"{main_path}\\data\\"
    os.mkdir(data_path)
    sqlite_db = SQLiteDB (db_file=f"{data_path}\\database.db")

if __name__ == '__main__':
    check_initial_data()