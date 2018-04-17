from splinter import Browser
import time
import json

# browser = Browser('firefox', headless=True)
browser = Browser('firefox')

browser.visit('https://cidades.ibge.gov.br/')

if browser.is_element_present_by_xpath('//button[@class="button__action"]', 10):
    browser.find_by_xpath('//button[@class="button__action"]').first.click()
else:
    browser.quit()

if browser.is_element_present_by_xpath('//li[@id="menu__municipio"]/i[@class="fa fa-chevron-right"]', 10):
    browser.find_by_xpath(
        '//li[@id="menu__municipio"]/i[@class="fa fa-chevron-right"]').first.click()
else:
    browser.quit()

states_number = {
    1: "Acre",
    2: "Alagoas",
    3: "Amapá",
    4: "Amazonas",
    5: "Bahia",
    6: "Ceará",
    7: "Distrito Federal",
    8: "Espitiro Santo",
    9: "Goiás",
    10: "Maranhão",
    11: "Mato Grosso",
    12: "Mato Grosso do Sul",
    13: "Minas Gerais",
    14: "Paraná",
    15: "Paraíba",
    16: "Pará",
    17: "Pernambuco",
    18: "Piauí",
    19: "Rio Grande do Norte",
    20: "Rio Grande do Sul",
    21: "Rio de Janeiro",
    22: "Rondônia",
    23: "Roraima",
    24: "Santa Catarina",
    25: "Sergipe",
    26: "São Paulo",
    27: "Tocantins",
}

state_count = 0
cities_count = 0

result = {}

states = browser.find_by_xpath('//div[@id="segunda-coluna"]/ul/li/div/i')

states.pop(0)

for state in states:
    state_count += 1

    state.click()

    cities = browser.find_by_xpath('//div[@class="conjunto"]//a')

    for city in cities:
        cities_count += 1
        result[cities_count] = {'name': city.text,
                                'state':  {state_count : states_number[state_count]}}
        
browser.quit()


with open('result.json', 'w', encoding='utf-8') as fp:
    json.dump(result, fp, ensure_ascii=False, sort_keys=True)

print(state_count)
print(cities_count)
