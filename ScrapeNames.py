from selenium import webdriver
option = webdriver.ChromeOptions()
option.add_argument('headless')
driver = webdriver.Chrome()
graves_dict = {}
driver.get("https://he.wikipedia.org/wiki/קטגוריה:קברי_צדיקים_בארץ_ישראל")
for i in range(1, 7):
    graves = driver.execute_script(f"return document.getElementsByClassName('navbox nowraplinks')[0].querySelectorAll('tbody')[0].rows[{i}].cells[1].innerText")
    graves_list = graves.split("•")
    districts = driver.execute_script(f"return document.getElementsByClassName('navbox nowraplinks')[0].querySelectorAll('tbody')[0].rows[{i}].cells[0].innerText")
    for j in range(len(graves_list)-1):
        graves_dict[graves_list[j]] = districts
print(graves_dict)
driver.close()