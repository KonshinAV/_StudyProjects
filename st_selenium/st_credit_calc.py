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

class Button (WebElement):
    pass

class TextFieldInput (WebElement):
    def clear(self):
        self.browser.find_element(by=By.XPATH, value=self.xpath_string).clear()

    def input_string(self, value):
        self.click()
        self.clear()
        self.browser.find_element(by=By.XPATH, value=self.xpath_string).send_keys(value)

class TextField (WebElement):
    def get_attr(self, attr):
        return self.browser.find_element(by=By.XPATH,value=self.xpath_string).get_attribute(attr)

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