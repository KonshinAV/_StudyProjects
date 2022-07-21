import os
import json



MAIN_PATH = os.getcwd()
CONFIG_PATH = f"{MAIN_PATH}\\data\\"
CONFIG_FILE_PATH = f"{CONFIG_PATH}conf.json"
DB_FILE_PATH = f"{CONFIG_PATH}vocab.db"
BASE_CONFIG = {"main_path": MAIN_PATH,
               "config_path": CONFIG_PATH,
               "config_file": CONFIG_FILE_PATH,
               "db_file": DB_FILE_PATH}

with open(CONFIG_FILE_PATH, 'w') as file: json.dump(BASE_CONFIG, file)

print(DB_FILE_PATH)
# sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS projects (
#                                             id integer PRIMARY KEY,
#                                             name text NOT NULL,
#                                             begin_date text,
#                                             end_date text
#                                         ); """
# sql_create_tasks_table = """CREATE TABLE IF NOT EXISTS tasks (
#                                         id integer PRIMARY KEY,
#                                         name text NOT NULL,
#                                         priority integer,
#                                         status_id integer NOT NULL,
#                                         project_id integer NOT NULL,
#                                         begin_date text NOT NULL,
#                                         end_date text NOT NULL,
#                                         FOREIGN KEY (project_id) REFERENCES projects (id)
#                                     );"""
# initial_setup.check_initial_data(main_path=os.getcwd())
# db = db.SqliteDb(db_file="D:\\study\\_StudyProjects\\vocab\data\\pythonsqlite.db")
# db.create_connection()
# if db.conn is not None:
#     # create projects table
#     db.create_table(sql_create_projects_table)
#     # create tasks table
#     db.create_table(sql_create_tasks_table)
# else:
#     print("Error! cannot create the database connection.")
#
#
# print(db.create_connection())
