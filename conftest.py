import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import random

# Фикстура
@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

# Функция для генерации email, login используется только в test_regisration.py
def generate_email_and_login():
    number = random.randint(21, 999)
    login = f"filipp_aslapov_19_{number}"
    email = f"{login}@mail.ru"
    return login, email

# Локаторы используются во всех тестах
LOGIN_EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")
LOGIN_PASSWORD_INPUT = (By.NAME, 'Пароль')
LOGIN_BUTTON = (By.XPATH, "//button[contains(text(),'Войти')]")
PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[contains(text(),'Личный Кабинет')]")

# Локаторы для test_constructor.py
CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")
HEADER_TEXT_BURGER = (By.XPATH, "//h1[text()='Соберите бургер']")

# Локаторы для test_log_out.py
LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")
HEADER_TEXT_LOGIN = (By.XPATH, "//h2[text()='Вход']")

# Локаторы для test_login.py
EMAIL_FIELD = (By.XPATH, "//input[@name='name']")

# Локаторы для test_personal_account.py
REGISTER_LINK = (By.CLASS_NAME, 'Auth_link__1fOlj')
NAME_INPUT = (By.NAME, 'name')
REGISTER_BUTTON = (By.CLASS_NAME, "button_button__33qZ0")
ERROR_MESSAGE = (By.CLASS_NAME, 'input__error')

# Локаторы для test_sections_of_constructor.py
BREAD_SECTION = (By.XPATH, "//div[contains(@class, 'tab_tab__') and contains(., 'Булки')]//span[text()='Булки']")
SAUCES_SECTION = (By.XPATH, "//span[text()='Соусы']")
FILLINGS_SECTION = (By.XPATH, "//span[text()='Начинки']")
# Локаторы для проверки состояния вкладок для test_sections_of_constructor.py
ACTIVE_TAB_CLASS = "tab_tab_type_current__"