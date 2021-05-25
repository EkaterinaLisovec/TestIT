import time

class TestplanHelper:

    def __init__(self, app):
        self.app = app

    def selectTestplan(self):
        wd = self.app.wd
        wd.find_element_by_xpath("// *[text() = 'LKO CASES NEW']").click()
        wd.find_element_by_xpath("// *[text() = ' Тест-планы ']").click()
        # здесь через сцепку нужно объявить переменную проекта
        wd.find_element_by_xpath("// *[text() = 'Автотестовый']").click()
        wd.find_element_by_xpath("//button[@class = 'button create-section-button ng-star-inserted']").click()
        wd.find_element_by_xpath("// *[text() = ' Набор из секции библиотеки ']").click()

    def savePlan(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//button[contains(@class, 'floating-button')]").click()


    def selectCases(self):
        list = ['2607',
'2606',
'2603',
'2602',
'2573']
        wd = self.app.wd
        for i in list:
            wd.find_element_by_xpath("//input[@placeholder='Название, ID']").click()
            wd.find_element_by_xpath("//input[@placeholder='Название, ID']").clear()
            wd.find_element_by_xpath("//input[@placeholder='Название, ID']").send_keys(i)
            time.sleep(1.5)
            wd.find_element_by_xpath("//input[@type='checkbox'][1]").click()





