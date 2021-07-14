import unittest
from selenium import webdriver
from pagina_ppal import Pagina1
from pagina_secundaria import Pagina2
# import time


class PruebasStandards(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'C:\Users\thepa\Desktop\curso\Soifer2\chromedriver.exe')
        self.driver.get('http://automationpractice.com/index.php')
        self.driver.maximize_window()

    def test_ejercicio(self):
        primer_test = Pagina1(self.driver)
        self.driver.implicitly_wait(3)
        primer_test.buscar('DRESS')
        ejercicio = Pagina2(self.driver)
        ejercicio.verifi()
        self.assertEqual('Printed Summer Dress', ejercicio.verifi())

    def test_ejercicio2(self):
        segundo_test = Pagina1(self.driver)
        segundo_test.buscar2('T-SHIRT')
        ejercicio2 = Pagina2(self.driver)
        ejercicio2.verifi2()
        self.assertTrue('Faded Short Sleeve T-shirts' in ejercicio2.verifi2())

    def test_ejercicio3(self):
        tercer_test = Pagina1(self.driver)
        tercer_test.buscar3('Pedro')
        ejercicio3 = Pagina2(self.driver)
        ejercicio3.verifi3()
        self.assertEqual('Pedro', ejercicio3.verifi3(), "******ES DIFERENTE******")

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
