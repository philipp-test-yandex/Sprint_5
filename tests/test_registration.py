from conftest import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import generate_email_and_login
from conftest import LOGIN_BUTTON,REGISTER_LINK,NAME_INPUT,LOGIN_EMAIL_INPUT,LOGIN_PASSWORD_INPUT, ERROR_MESSAGE

def test_successful_registration(driver):
    user_name, user_email = generate_email_and_login()
    user_pass_succes_reg = 'Pass123'

    driver.get('https://stellarburgers.nomoreparties.site/')

    driver.find_element(*LOGIN_BUTTON).click()
    driver.find_element(*REGISTER_LINK).click()

    driver.find_element(*NAME_INPUT).send_keys(user_name)
    driver.find_element(*LOGIN_EMAIL_INPUT).send_keys(user_email)
    driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys(user_pass_succes_reg)

    button_reg = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "button_button__33qZ0")))
    driver.execute_script("arguments[0].click();", button_reg)

    WebDriverWait(driver, 10).until(
        EC.url_contains("login")
    )

    assert "login" in driver.current_url

def test_password_contains_less_than_6_characters(driver):
    user_name, user_email = generate_email_and_login()
    user_pass_less_6_char = 'pas'

    driver.get('https://stellarburgers.nomoreparties.site/')

    driver.find_element(*LOGIN_BUTTON).click()
    driver.find_element(*REGISTER_LINK).click()

    driver.find_element(*NAME_INPUT).send_keys(user_name)
    driver.find_element(*LOGIN_EMAIL_INPUT).send_keys(user_email)
    driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys(user_pass_less_6_char)

    driver.find_element(By.CLASS_NAME, "button_button__33qZ0").click()

    error_message = driver.find_element(*ERROR_MESSAGE).text
    assert "Некорректный пароль" in error_message