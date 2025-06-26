from selenium import webdriver

driver = webdriver.Chrome()

driver.get("")

element = driver.find_element_by_class_name("")
data = element.text

# Pegar vários elementos de uma vez
cards = navegador.find_elements_by_class_name('coderCard')
for card in cards:
    nameHolder = card.find_element_by_class_name('nameHolder')
    firstP = nameholder.find_element_by_tag_name('p')
    tagB = firstP.find_element_by_tag_name('b')
    nome = tagB.get_attribute('innerHTML')
    print(nome)

print(data)
