class Pagina2:

    def __init__(self, my_driver):
        self.sustitut = '//*[@id="center_column"]/ul/li[1]/div/div[2]/h5/a'
        self.sustitut2 = '//*[@id="center_column"]/p'
        self.my_driver = my_driver

    def verifi(self):
        return self.my_driver.find_element_by_xpath(self.sustitut).text

    def verifi2(self):

        return self.my_driver.find_element_by_xpath(self.sustitut).text

    def verifi3(self):
        return self.my_driver.find_element_by_xpath(self.sustitut2).text
