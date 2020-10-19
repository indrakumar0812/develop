from selenium import webdriver
tableData = list()
driver = webdriver.Chrome(executable_path="C:\\Users\\indrasen\\Documents\\chromedriver_win32\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
#rowData = driver.find_elements_by_xpath("//table[@id='product']/tbody/tr[2]/td")
#for i in rowData:
#    print(i.text)
#rowData = driver.find_element_by_xpath("//table[@id='product']/tbody/tr[2]/td[2]")
#print(rowData.text)

rowData = driver.find_elements_by_xpath("//table[@id='product']/tbody/tr")

for i in rowData:
    tableData.append(i.text)

print(tableData)








'''

'''