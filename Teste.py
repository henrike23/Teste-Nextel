from selenium import webdriver
import json

array = '{"google-me": ["Nextel", "Telefonia do futuro", "Selenium python"]}'
Response = json.loads(array)
print(Response)

driver = webdriver.Chrome()

open('resultados.txt', 'w')

for key in Response['google-me']:
    driver.get("https://www.google.com/search?q=" + key + '&start')
    assert "Google" in driver.title
    assert "não encontrou nenhum documento correspondente" not in driver.page_source
    lista = driver.find_elements_by_xpath("//*[@id='rso']//div/*[@class='r']")[:3]
    result1 = lista[0].text
    result2 = lista[1].text
    result3 = lista[2].text

    results = [result1, result2, result3]

    with open('resultados.txt', 'a') as filehandle:
        for listitem in results:
            filehandle.write('%s\n' % listitem)

f=open('resultados.txt')
line=f.readlines()

data = {}
data["Nextel"] = []
data["Nextel"].append({
    line[0]: line[1],
    line[2]: line[3],
    line[4]: line[5]
})

data["Telefonia do futuro"] = []
data["Telefonia do futuro"].append({
    line[6]: line[7],
    line[9]: line[10],
    line[11]: line[12]
})

data["Selenium python"] = []
data["Selenium python"].append({
    line[13]: line[14],
    line[16]: line[17],
    line[19]: line[20]
})

with open('output.json', 'w') as outfile:
    json.dump(data, outfile)

print(data)

driver.close()