from selenium import webdriver

browser = webdriver.Firefox()

# Edith ouviu falar de uma aplicação online interessante para
# lista de tarefas. Ela decide verificar sua homepage
browser.get('http://localhost:8000')

# Ela verifica o seguinte título na página
assert 'Congratulations!' in browser.title