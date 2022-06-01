from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pprint import pprint


class Creditcalc ():
    def __init__(self, browser = 'chrome', base_url = 'http://creditcalculator.pointschool.ru/'):

        self.base_url = base_url
        self.browser = webdriver.Chrome()
        self.browser.get(base_url)
        # Кнопка рассчитать
        self.button_calculate = '/html/body/div[1]/div/div[1]/div[3]/div/form/div/div[4]/button'
        # Поле для ввода - Желаемая сумма кредита
        self.field_credit_sum = '/html/body/div[1]/div/div[1]/div[3]/div/form/div/div[1]/input'
        # Поле для ввода - Первоначальный взнос
        self.field_first_deposit = '/html/body/div[1]/div/div[1]/div[3]/div/form/div/div[2]/input'
        # Поле для ввода - срок кредита
        self.field_credit_period = '/html/body/div[1]/div/div[1]/div[3]/div/form/div/div[3]/input'
        # Поле с отображением результатов простого расчета
        self.field_simple_monthly_payment = '/html/body/div[1]/div/div[1]/div[4]/div[2]/div[1]/div[1]/div/div[2]'
        # Результат простого расчета
        self.field_simple_monthly_payment_value = ''


    def simple_calculation (self):
        """

        :return:
        """
        self.browser.find_element(by=By.XPATH, value=self.button_calculate).click()
        while self.browser.find_element(by=By.XPATH, value=self.field_simple_monthly_payment).get_attribute('textContent') == '':
            continue
        res_monthly_payment_short = self.browser.find_element(by=By.XPATH, value=self.field_simple_monthly_payment).get_attribute('textContent')
        return res_monthly_payment_short

    def close (self):
        self.browser.quit()

    def write_simple_params (self, credit_sum = '', first_deposit = '', credit_period = ''):

        if credit_sum != '':
            self.browser.find_element(by=By.XPATH, value=self.field_credit_sum).clear()
            self.browser.find_element(by=By.XPATH, value=self.field_credit_sum).send_keys(credit_sum)

        if first_deposit != '':
            self.browser.find_element(by=By.XPATH, value=self.field_first_deposit).clear()
            self.browser.find_element(by=By.XPATH, value=self.field_first_deposit).send_keys(first_deposit)

        if credit_period != '':
            self.browser.find_element(by=By.XPATH, value=self.field_credit_period).clear()
            self.browser.find_element(by=By.XPATH, value=self.field_credit_period).send_keys(credit_period)

if __name__ == '__main__':
    credcalc = Creditcalc ()
    credcalc.write_simple_params('10','11111','500')
    print (credcalc.simple_calculation())
