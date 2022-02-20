from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://app.bluealert.pl/ba/form/formularz-testowy")
driver.find_element_by_id("id_first_name").send_keys("Anna")
driver.find_element_by_id("id_last_name").send_keys("Kowalska")
driver.find_element_by_id("id_email").send_keys("anna.kowalska@gmail.com")
driver.find_element_by_id("id_phone").send_keys("788285806")
driver.find_element_by_id("id_pesel").send_keys("94013054129")
driver.find_element_by_id("id_id_numer").send_keys("ANH886567")
driver.find_element_by_name("date").send_keys("2022-02-10")
driver.find_element_by_name("date").send_keys(Keys.ENTER)


#driver.find_element_by_xpath("//button[text()='Dalej']").click()
