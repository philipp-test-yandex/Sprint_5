from conftest import driver
from selenium.webdriver.common.by import By
from conftest import LOGIN_EMAIL_INPUT,LOGIN_PASSWORD_INPUT,LOGIN_BUTTON,BREAD_SECTION,SAUCES_SECTION, FILLINGS_SECTION

user_email = 'filipp_aslapov_19_015@mail.ru'
user_pass_succes_reg = 'Pass123'

def test_go_to_the_section_bread(driver):
    driver.get('https://stellarburgers.nomoreparties.site/login')

    driver.find_element(*LOGIN_EMAIL_INPUT).send_keys(user_email)
    driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys(user_pass_succes_reg)
    driver.find_element(*LOGIN_BUTTON).click()

    bread_button = driver.find_element(*BREAD_SECTION)
    driver.execute_script("arguments[0].scrollIntoView();", bread_button)
    driver.execute_script("arguments[0].click();", bread_button)

    assert ("tab_tab_type_current__" in driver.find_element(By.XPATH, "//span[text()='Булки']/parent::div").get_attribute("class")
            and "tab_tab_type_current__" not in driver.find_element(By.XPATH, "//span[text()='Соусы']/parent::div").get_attribute("class")
            and "tab_tab_type_current__" not in driver.find_element(By.XPATH, "//span[text()='Начинки']/parent::div").get_attribute("class")
            )

def test_go_to_the_section_souce(driver):
    driver.get('https://stellarburgers.nomoreparties.site/login')

    driver.find_element(*LOGIN_EMAIL_INPUT).send_keys(user_email)
    driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys(user_pass_succes_reg)
    driver.find_element(*LOGIN_BUTTON).click()

    souce = driver.find_element(*SAUCES_SECTION)
    driver.execute_script("arguments[0].scrollIntoView();", souce)
    driver.execute_script("arguments[0].scrollIntoView(); arguments[0].click();", souce)

    assert (
            "tab_tab_type_current__" in driver.find_element(By.XPATH, "//span[text()='Соусы']/parent::div").get_attribute("class")
            and "tab_tab_type_current__" not in driver.find_element(By.XPATH, "//span[text()='Начинки']/parent::div").get_attribute("class")
            and "tab_tab_type_current__" not in driver.find_element(By.XPATH, "//span[text()='Булки']/parent::div").get_attribute("class")
            )

def test_go_to_the_section_fillings(driver):
    driver.get('https://stellarburgers.nomoreparties.site/login')

    driver.find_element(*LOGIN_EMAIL_INPUT).send_keys(user_email)
    driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys(user_pass_succes_reg)
    driver.find_element(*LOGIN_BUTTON).click()

    fillings = driver.find_element(*FILLINGS_SECTION)
    driver.execute_script("arguments[0].scrollIntoView();", fillings)
    driver.execute_script("arguments[0].scrollIntoView(); arguments[0].click();", fillings)

    assert (
            "tab_tab_type_current__" in driver.find_element(By.XPATH, "//span[text()='Начинки']/parent::div").get_attribute("class")
            and "tab_tab_type_current__" not in driver.find_element(By.XPATH, "//span[text()='Соусы']/parent::div").get_attribute("class")
            and "tab_tab_type_current__" not in driver.find_element(By.XPATH, "//span[text()='Булки']/parent::div").get_attribute("class")
            )