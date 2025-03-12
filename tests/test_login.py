from conftest import driver
from selenium.webdriver.common.by import By
from conftest import LOGIN_EMAIL_INPUT, LOGIN_PASSWORD_INPUT, LOGIN_BUTTON, PERSONAL_ACCOUNT_BUTTON, EMAIL_FIELD

user_email = 'filipp_aslapov_19_011@mail.ru'
user_pass_succes_reg = 'Pass123'

def test_login_from_button_log_in_to_your_account(driver):
    driver.get('https://stellarburgers.nomoreparties.site')

    driver.find_element(*LOGIN_BUTTON).click()

    driver.find_element(*LOGIN_EMAIL_INPUT).send_keys(user_email)
    driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys(user_pass_succes_reg)

    driver.find_element(*LOGIN_BUTTON).click()

    driver.find_element(*PERSONAL_ACCOUNT_BUTTON).click()

    email_field = driver.find_element(*EMAIL_FIELD)
    actual_email = email_field.get_attribute('value')

    assert actual_email == user_email

def test_login_from_personal_account_button(driver):
    driver.get('https://stellarburgers.nomoreparties.site')

    driver.find_element(*PERSONAL_ACCOUNT_BUTTON).click()

    driver.find_element(*LOGIN_EMAIL_INPUT).send_keys(user_email)
    driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys(user_pass_succes_reg)

    driver.find_element(*LOGIN_BUTTON).click()

    driver.find_element(*PERSONAL_ACCOUNT_BUTTON).click()

    email_field = driver.find_element(*EMAIL_FIELD)
    actual_email = email_field.get_attribute('value')

    assert actual_email == user_email


# 3. Вход через кнопку в форме регистрации
def test_login_from_registration_form(driver):
    driver.get('https://stellarburgers.nomoreparties.site/register')

    driver.find_element(By.CLASS_NAME, 'Auth_link__1fOlj').click()

    driver.find_element(*LOGIN_EMAIL_INPUT).send_keys(user_email)
    driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys(user_pass_succes_reg)

    driver.find_element(*LOGIN_BUTTON).click()

    driver.find_element(*PERSONAL_ACCOUNT_BUTTON).click()

    email_field = driver.find_element(*EMAIL_FIELD)
    actual_email = email_field.get_attribute('value')

    assert actual_email == user_email


# 4. Вход через кнопку в форме восстановления пароля
def test_login_from_password_recovery_form(driver):
    driver.get('https://stellarburgers.nomoreparties.site/forgot-password')

    driver.find_element(By.CLASS_NAME, 'Auth_link__1fOlj').click()

    driver.find_element(*LOGIN_EMAIL_INPUT).send_keys(user_email)
    driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys(user_pass_succes_reg)

    driver.find_element(*LOGIN_BUTTON).click()

    driver.find_element(*PERSONAL_ACCOUNT_BUTTON).click()

    email_field = driver.find_element(*EMAIL_FIELD)
    actual_email = email_field.get_attribute('value')

    assert actual_email == user_email