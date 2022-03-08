from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

# Os testes estão organizados em classes que herdam de unitest.TestCase
class NewVisitorTest(unittest.TestCase):
    # Os dois métodos a seguir serão executados, mesmo que haja falha no teste
    #
    # Método executado ao iniciar cada teste
    def setUp(self):
        self.browser = webdriver.Firefox()
    # Método iniciado ao finalizar cada teste
    def tearDown(self):
        self.browser.quit()

    # O corpo principal do teste está aqui, qualquer método que comece com test
    # será executado como teste pelo Test Runner.
    def test_can_start_a_list_and_retrieve_it_later(self):
        # Testando conexão com a home
        self.browser.get('http://localhost:8000')
        
        # Testando título da janela e cabeçalho
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # Testando inserção de dados
        inputbox = self.browser.find_element_by_tag_name('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # Digitação dos dados
        input.send_keys('Buy peacock feathers!')

        # Recarregar a página e inserir o item digitado em uma lista
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows)
        )

        # AInda existe uma caixa sendo possivel adicionar outro item, ao inserir

        # A pagina é carregada novamente e mostra os dois itens inseridos

        # O site lembrará de sua lista?

        # URL unica com pequeno texto explicativo

        # Ao acessar a URL os itens continuam lá 

        self.fail('Finish the test!')

if __name__ == '__main__':
    unittest.main()
