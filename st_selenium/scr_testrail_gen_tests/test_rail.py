from selenium import webdriver
from selenium.webdriver.common.by import By
from st_credit_calc import WebElement,TextField,TextFieldInput, Site
import pickle
import time
import datetime

def save_cookie (browser):
    site = webdriver.Chrome()
    site.get('https://konshinav88.testrail.io/index.php?/auth/login/')
    time.sleep(100)
    pickle.dump(site.get_cookies(), open('session', 'wb'))
    print('Куки сохранены')

def add_case (in_title, in_preconditions, in_steps, exp_result):
    # add_test_case = '/html/body/div[4]/div/div[1]/div[2]/div[18]/div/div/div/div[5]/div[1]/div[3]/a[1]'
    add_test_case = '/html/body/div[4]/div/div[5]/div[2]/a/span'
    site.find_element(by=By.XPATH, value=add_test_case).click()
    title = '/html/body/div[4]/div/div[1]/div[2]/form/div[1]/div[1]/input'
    time.sleep(1)
    site.find_element(by=By.XPATH, value=title).send_keys(in_title)

    section = '/html/body/div[4]/div/div[1]/div[2]/form/div[1]/div[2]/div[1]/div/a/span'
    site.find_element(by=By.XPATH, value=section).click()
    first_calc_field = '/html/body/div[4]/div/div[1]/div[2]/form/div[1]/div[2]/div[1]/div/div/ul/li[2]'
    site.find_element(by=By.XPATH, value=first_calc_field).click()

    #
    m_type = '/html/body/div[4]/div/div[1]/div[2]/form/div[1]/div[2]/div[3]/div/a/span'
    site.find_element(by=By.XPATH, value=m_type).click()
    functionional = '/html/body/div[4]/div/div[1]/div[2]/form/div[1]/div[2]/div[3]/div/div/ul/li[6]'
    site.find_element(by=By.XPATH, value=functionional).click()
    #

    preconditions = '/html/body/div[4]/div/div[1]/div[2]/form/div[1]/div[3]/div[1]/div'
    site.find_element(by=By.XPATH, value=preconditions).send_keys(in_preconditions)
    steps = '/html/body/div[4]/div/div[1]/div[2]/form/div[1]/div[4]/div[1]/div'
    site.find_element(by=By.XPATH, value=steps).send_keys(in_steps)
    expected_result = '/html/body/div[4]/div/div[1]/div[2]/form/div[1]/div[5]/div[1]/div'
    site.find_element(by=By.XPATH, value=expected_result).send_keys(exp_result)
    add_case_button = '/html/body/div[4]/div/div[1]/div[2]/form/div[2]/button[1]'
    site.find_element(by=By.XPATH, value=add_case_button).click()

    site.find_element(by=By.XPATH, value=test_cases).click()
    pass

def add_case_test (in_title, in_preconditions, in_steps, exp_result):
    print(
    f"""
    Title = {in_title},
    Preconditions = {in_preconditions},
    Steps = {in_steps}
    Result = {exp_result}
    """)

if __name__ == '__main__':
    site = webdriver.Chrome()
    site.get ('https://konshinav88.testrail.io/index.php?/auth/login/')
    for cookie in pickle.load(open('session', 'rb')):
        site.add_cookie(cookie)
    print('Куки загружены')
    site.refresh()
    point_project_button = '/html/body/div[4]/div/div[1]/div[2]/div[3]/div/div/div[2]/div/div[2]/div[2]/div[1]/a'
    site.find_element(by=By.XPATH, value=point_project_button).click()
    test_cases = '/html/body/div[2]/ul/li[6]/a'
    site.find_element(by=By.XPATH, value=test_cases).click()

    with open("../in_test_data.txt", 'r') as file:
        data_file = file.readlines()
    # print (data_file)
    lst = []
    for st in data_file:
        lst.append(st.replace('\n', '').split('\t'))
    for record in lst:
        print(record)
        if record[3] == 'passed':
            add_case(in_title= f'Формирование предварительного расчета ({record[0]}/{record[1]}/{record[2]})',
                          in_preconditions= 'Открыта страница сайта http://creditcalculator.pointschool.ru/',
                          in_steps= f"1.Заполнить поля следующими значениями\n"
                                    f"Желаемая сумма кредита = {record[0]}\n"
                                    f"Первоначальный взнос = {record[1]}\n"
                                    f"Срок кредита = {record[2]}\n"
                                    "\n"
                                    f"2. Нажать кнопку Рассчитать\n",
                          exp_result="Кнопка 'Рассчитать' нажимается (ее можно нажать).\n"
                                     "Рассчет выполнен.Появилось поле 'Результат расчета', содержащее поле 'ежемесячный платеж'.\n"
                                     "В поле 'Ежемесячный платеж' отображен приблизительный рассчет ежемесячного платежа")
        elif record[3] == 'failed':
            add_case(in_title= f'Формирование предварительного расчета ({record[0]}/{record[1]}/{record[2]})',
                          in_preconditions= 'Открыта страница сайта http://creditcalculator.pointschool.ru/',
                          in_steps= f"1.Заполнить поля следующими значениями\n"
                                    f"Желаемая сумма кредита = {record[0]}\n"
                                    f"Первоначальный взнос = {record[1]}\n"
                                    f"Срок кредита = {record[2]}\n"
                                    "\n"
                                    f"2. Нажать кнопку Рассчитать\n",
                          exp_result=f"Кнопка Рассчитать нажимается (ее можно нажать).\n"
                                     f"Рассчет не выполнен - сообщение об ошибке 'Первоначальный взнос больше суммы кредита'")



    # add_case(in_title= f'Case{datetime.datetime.now()}', in_preconditions = 'in_preconditions', in_steps= "Steps", exp_result= 'exp_result')
    # add_case(in_title= f'Case{datetime.datetime.now()}', in_preconditions = 'in_preconditions', in_steps= "Steps", exp_result= 'exp_result')



