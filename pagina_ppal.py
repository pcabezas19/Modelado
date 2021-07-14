class Pagina1:

    def __init__(self, my_driver):
        self.barra_busqueda = 'search_query_top'
        self.lupa = 'submit_search'
        self.my_driver = my_driver

    def buscar(self, item):
        self.my_driver.find_element_by_id(self.barra_busqueda).send_keys(item)
        self.my_driver.find_element_by_name(self.lupa).click()

    def buscar2(self, item):
        self.my_driver.find_element_by_id(self.barra_busqueda).send_keys(item)
        self.my_driver.find_element_by_name(self.lupa).click()

    def buscar3(self, item):
        self.my_driver.find_element_by_id(self.barra_busqueda).send_keys(item)
        self.my_driver.find_element_by_name(self.lupa).click()
