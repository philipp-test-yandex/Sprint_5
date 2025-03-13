import random

# Функция для генерации email, login используется только в test_regisration.py
def generate_email_and_login():
    number = random.randint(21, 999)
    login = f"filipp_aslapov_19_{number}"
    email = f"{login}@mail.ru"
    return login, email