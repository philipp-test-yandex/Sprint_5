from conftest import driver
from conftest import LOGIN_EMAIL_INPUT, LOGIN_PASSWORD_INPUT, LOGIN_BUTTON, PERSONAL_ACCOUNT_BUTTON, CONSTRUCTOR_BUTTON, HEADER_TEXT_BURGER

user_email = 'filipp_aslapov_19_015@mail.ru'
user_pass_succes_reg = 'Pass123'
def test_switching_from_personal_account_to_constructor(driver):
    driver.get('https://stellarburgers.nomoreparties.site/login')

    driver.find_element(*LOGIN_EMAIL_INPUT).send_keys(user_email)
    driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys(user_pass_succes_reg)

    driver.find_element(*LOGIN_BUTTON).click()

    driver.find_element(*PERSONAL_ACCOUNT_BUTTON).click()

    driver.find_element(*CONSTRUCTOR_BUTTON).click()

    header_text = driver.find_element(*HEADER_TEXT_BURGER).text
    assert header_text == "Соберите бургер"

