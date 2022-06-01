from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pprint import pprint

class WebElement ():
    def __init__(self,browser, xpath_string):
        self.xpath_string = xpath_string
        self.browser = browser

    def click (self):
        self.browser.find_element(by=By.XPATH, value=self.xpath_string).click()

    def get_attr(self, attr):
        return self.browser.find_element(by=By.XPATH,value=self.xpath_string).get_attribute(attr)

class Button (WebElement):
    pass

class TextFieldInput (WebElement):
    def clear(self):
        self.browser.find_element(by=By.XPATH, value=self.xpath_string).clear()

    def input_value(self, value):
        self.click()
        self.clear()
        self.browser.find_element(by=By.XPATH, value=self.xpath_string).send_keys(value)

class TextField (WebElement):
    pass

class FormControl (WebElement):
    def get_all_options(self):
        pass

class Creditcalc ():
    def __init__(self, browser = 'chrome', base_url = 'http://creditcalculator.pointschool.ru/'):
        self.base_url = base_url
        self.browser = webdriver.Chrome()
        self.browser.get(base_url)

        # Кнопка рассчитать
        self.button_calculate = Button(browser=self.browser,
                                       xpath_string='/html/body/div[1]/div/div[1]/div[3]/div/form/div/div[4]/button')
        # Кнопка/ссыка для отображения формы заполнения заявки
        self.button_fill_full_form = Button(browser=self.browser,
                                       xpath_string='/html/body/div[1]/div/div[1]/div[4]/div[2]/div[2]/a')
        # Поле для ввода - Желаемая сумма кредита
        self.input_credit_sum = TextFieldInput(browser=self.browser,
                                         xpath_string='/html/body/div[1]/div/div[1]/div[3]/div/form/div/div[1]/input')
        # Поле для ввода - Первоначальный взнос
        self.input_first_deposit = TextFieldInput(browser=self.browser,
                                            xpath_string='/html/body/div[1]/div/div[1]/div[3]/div/form/div/div[2]/input')
        # Поле для ввода - срок кредита
        self.input_credit_period = TextFieldInput(browser=self.browser,
                                            xpath_string= '/html/body/div[1]/div/div[1]/div[3]/div/form/div/div[3]/input')
        # Поле с отображением результатов простого расчета
        self.field_simple_monthly_payment = TextField (browser=self.browser,
                                                 xpath_string='html/body/div[1]/div/div[1]/div[4]/div[2]/div[1]/div[1]/div/div[2]')
        # Фамилия
        self.input_second_name = TextFieldInput(browser=self.browser,
                                              xpath_string='/html/body/div[1]/div/div[1]/div[5]/div[2]/form/div[1]/div[1]/input')
        # Имя
        self.input_first_name = TextFieldInput(browser=self.browser,
                                              xpath_string='/html/body/div[1]/div/div[1]/div[5]/div[2]/form/div[1]/div[2]/input')
        # Отчетство
        self.input_middle_name = TextFieldInput(browser=self.browser,
                                              xpath_string='/html/body/div[1]/div/div[1]/div[5]/div[2]/form/div[1]/div[3]/input')
        # Паспорт
        self.input_passport = TextFieldInput(browser=self.browser,
                                              xpath_string='/html/body/div[1]/div/div[1]/div[5]/div[2]/form/div[2]/div[1]/input')
        # Кем выдан
        self.input_issued_by = TextFieldInput(browser=self.browser,
                                              xpath_string='/html/body/div[1]/div/div[1]/div[5]/div[2]/form/div[2]/div[2]/input')
        # Когда выдан
        self.input_issued_date = TextFieldInput(browser=self.browser,
                                              xpath_string='/html/body/div[1]/div/div[1]/div[5]/div[2]/form/div[2]/div[3]/input')
        # Образование
        self.form_control_education = FormControl(browser=self.browser,
                                              xpath_string='/html/body/div[1]/div/div[1]/div[5]/div[2]/form/div[3]/div[2]/select')
        # Общий трудовой стаж
        self.form_control_seniority = FormControl(browser=self.browser,
                                              xpath_string='/html/body/div[1]/div/div[1]/div[5]/div[2]/form/div[4]/div[2]/select')
        # Срок работы на последнем месте
        self.form_term_work_last_place = FormControl(browser=self.browser,
                                              xpath_string='/html/body/div[1]/div/div[1]/div[5]/div[2]/form/div[5]/div[2]/select')
        # Подтверждение 2НДФЛ
        self.form_confirmation_income_ndfl = FormControl(browser=self.browser,
                                              xpath_string='/html/body/div[1]/div/div[1]/div[5]/div[2]/form/div[6]/div[2]/select')
        # Место работы в районе регистрации банка
        self.form_work_place_in_bank_location = FormControl(browser=self.browser,
                                              xpath_string='/html/body/div[1]/div/div[1]/div[5]/div[2]/form/div[7]/div[2]/select')
        # Место работы в районе регистрации банка
        self.form_work_place_bank_area = FormControl(browser=self.browser,
                                              xpath_string='/html/body/div[1]/div/div[1]/div[5]/div[2]/form/div[7]/div[2]/select')
        # Читый доход
        self.input_net_income = FormControl(browser=self.browser,
                                              xpath_string='/html/body/div[1]/div/div[1]/div[5]/div[2]/form/div[8]/div[2]/input')
        # Место прописки в районе регистрации банка
        self.form_registration_place_bank_area = FormControl(browser=self.browser,
                                              xpath_string='/html/body/div[1]/div/div[1]/div[5]/div[2]/form/div[9]/div[2]/select')
        # Есть ли судимость
        self.form_previous_conviction = FormControl(browser=self.browser,
                                              xpath_string='/html/body/div[1]/div/div[1]/div[5]/div[2]/form/div[10]/div[2]/select')
        # Есть ли собственный автомобиль
        self.form_car = FormControl(browser=self.browser,
                                              xpath_string='/html/body/div[1]/div/div[1]/div[5]/div[2]/form/div[11]/div[2]/select')
        # Есть ли у вас в собственности недвижимость
        self.form_real_estate = FormControl(browser=self.browser,
                                              xpath_string='/html/body/div[1]/div/div[1]/div[5]/div[2]/form/div[12]/div[2]/select')
        # Вернуться к краткому расчету
        self.button_return_short_form = FormControl(browser=self.browser,
                                              xpath_string='/html/body/div[1]/div/div[1]/button')

    def basic_calculation (self):
        self.button_calculate.click()
        while self.field_simple_monthly_payment.get_attr('textContent') == '':
            continue
        result = self.field_simple_monthly_payment.get_attr('textContent')
        print(f"result = {result}")
        return result

    def close_browser (self):
        self.browser.quit()

if __name__ == '__main__':
    credcalc = Creditcalc ()
    credcalc.basic_calculation()
    credcalc.button_fill_full_form.click()
    credcalc.input_second_name.input_value('Иванов')
    credcalc.input_first_name.input_value('Иван')
    credcalc.input_middle_name.input_value('Иванович')
    credcalc.input_passport.input_value('1111 223344')
    credcalc.input_issued_by.input_value('Отделением')
    credcalc.input_issued_date.input_value ('11.11.1933')
    credcalc.button_calculate.click()

