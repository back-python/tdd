from selenium import webdriver
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
        self.browser.get('http://localhost:8000')

        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

if __name__ == '__main__':
    unittest.main()

# Inserir um item de tarefa

# Digita um item na lista de tarefas

# QUando aperta enter a página é atualizada e lista o item

# AInda existe uma caixa sendo possivel adicionar outro item, ao inserir

# A pagina é carregada novamente e mostra os dois itens inseridos

# O site lembrará de sua lista?

# URL unica com pequeno texto explicativo

# Ao acessar a URL os itens continuam lá 
