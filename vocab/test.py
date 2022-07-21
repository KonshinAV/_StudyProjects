# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time

"""
class AppDynamicsJob(unittest.TestCase):
    def setUp(self):
        # AppDynamics will automatically override this web driver
        # as documented in https://docs.appdynamics.com/display/PRO44/Write+Your+First+Script
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_app_dynamics_job(self):
        driver = self.driver
        # ERROR: Caught exception [ERROR: Unsupported command [loadVars | KonshinAV_data.json | ]]
        driver.get("http://creditcalculator.pointschool.ru/")
        driver.find_element_by_xpath("//*[@data-btn-action='do-result']").click()
        driver.find_element_by_link_text(u"заполните анкету").click()
        driver.find_element_by_name("field-desired-loan").clear()
        driver.find_element_by_name("field-desired-loan").send_keys("${field-desired-loan}")
        driver.find_element_by_name("field-initial-payment").clear()
        driver.find_element_by_name("field-initial-payment").send_keys("${field-initial-payment}")
        driver.find_element_by_name("field-credit-term").clear()
        driver.find_element_by_name("field-credit-term").send_keys("${field-credit-term}")
        driver.find_element_by_name("second-name").clear()
        driver.find_element_by_name("second-name").send_keys("${second-name}")
        driver.find_element_by_name("first-name").clear()
        driver.find_element_by_name("first-name").send_keys("${first-name}")
        driver.find_element_by_name("middle-name").clear()
        driver.find_element_by_name("middle-name").send_keys("${middle-name}")
        driver.find_element_by_name("passport").clear()
        driver.find_element_by_name("passport").send_keys("${passport}")
        driver.find_element_by_name("issued-by").clear()
        driver.find_element_by_name("issued-by").send_keys("${issued-by}")
        driver.find_element_by_name("issued-date").clear()
        driver.find_element_by_name("issued-date").send_keys("${issued-date}")
        driver.find_element_by_name("education").click()
        Select(driver.find_element_by_name("education")).select_by_visible_text("${education}")
        driver.find_element_by_name("seniority").click()
        Select(driver.find_element_by_name("seniority")).select_by_visible_text("${seniority}")
        driver.find_element_by_name("term-work-last-place").click()
        Select(driver.find_element_by_name("term-work-last-place")).select_by_visible_text("${term-work-last-place}")
        driver.find_element_by_name("confirmation-income-ndfl").click()
        Select(driver.find_element_by_name("confirmation-income-ndfl")).select_by_visible_text(
            "${confirmation-income-ndfl}")
        driver.find_element_by_name("work-place-bank-area").click()
        Select(driver.find_element_by_name("work-place-bank-area")).select_by_visible_text("${work-place-bank-area}")
        driver.find_element_by_name("net-income").click()
        driver.find_element_by_name("net-income").clear()
        driver.find_element_by_name("net-income").send_keys("${net-income}")
        driver.find_element_by_name("registration-place-bank-area").click()
        Select(driver.find_element_by_name("registration-place-bank-area")).select_by_visible_text(
            "${registration-place-bank-area}")
        Select(driver.find_element_by_name("previous-conviction")).select_by_visible_text("${previous-conviction}")
        driver.find_element_by_name("car").click()
        Select(driver.find_element_by_name("car")).select_by_visible_text("${car}")
        driver.find_element_by_name("real-estate").click()
        Select(driver.find_element_by_name("real-estate")).select_by_visible_text("${real-estate}")
        # Запускаем расчет
        driver.find_element_by_xpath("//*[@data-btn-action='do-result']").click()
        # Ждем пока проподет окно loadingModalLabel "Обработка запроса"
        for i in range(60):
            try:
                if not driver.find_element_by_xpath("//*[@id='loadingModalLabel']").is_displayed(): break
            except:
                pass
            time.sleep(1)
        else:
            self.fail("time out")
        # Проверяем результаты
        # Решение об одобрении (Текст)
        self.assertEqual("${credit-message}", driver.find_element_by_xpath("//*[@id='credit-message']").text)
        # Процентная ставка
        self.assertEqual("${credit-rate}", driver.find_element_by_xpath("//*[@id='credit-rate']").text)
        # Ежемесячный платеж
        self.assertEqual("${credit-monthly-payment-full}",
                         driver.find_element_by_xpath("//*[@id='credit-monthly-payment-full']").text)
        # переплата по кредиту
        self.assertEqual("${credit-credit-overpayment}",
                         driver.find_element_by_xpath("//*[@id='credit-credit-overpayment']").text)
        # Срок выплаты кредита
        self.assertEqual("${payments-loan-period}",
                         driver.find_element_by_xpath("//*[@id='payments-loan-period']").text)
        # ERROR: Caught exception [ERROR: Unsupported command [endLoadVars |  | ]]

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        # To know more about the difference between verify and assert,
        # visit https://www.seleniumhq.org/docs/06_test_design_considerations.jsp#validating-results
        self.assertEqual([], self.verificationErrors)
"""

browser = webdriver.Firefox()
browser.get("http://creditcalculator.pointschool.ru/")
browser.find_element(by='name',value='field-desired-loan').clear()
browser.find_element(by='name',value='field-desired-loan').send_keys(300000)
browser.find_element(by='xpath',value='//*[@name="field-initial-payment"]').clear()
browser.find_element(by='xpath',value='//*[@name="field-initial-payment"]').send_keys(100000)
browser.find_element(by='xpath',value='//*[@name="field-credit-term"]').clear()
browser.find_element(by='xpath',value='//*[@name="field-credit-term"]').send_keys(12)
browser.find_element(by='xpath', value='//*[@data-btn-action="do-result"]').click()

print(browser.find_element(by='xpath',value='//*[@class="col monthly-payment-short"]').text)





