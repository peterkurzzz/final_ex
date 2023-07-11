from faker import Faker

valid_firstname = 'Петр'
valid_lastname = 'Петров'
valid_email = 'petrpetrov@yandex.ru'
valid_password = 'pg5-hqW-C4Q-Ysj'
valid_phone = '+79118355819'
valid_login = 'Petr-Petrov'
valid_ls = '111111111111'

fake_ru = Faker('ru_RU')
fake_firstname = fake_ru.first_name()
fake_lastname = fake_ru.last_name()
fake_phone = '89999999999'

fake = Faker()
fake_firstname_en = fake.first_name()
fake_lastname_en = fake.last_name()

fake_password = fake.password()
fake_email = fake.email()
fake_login = fake.user_name()
invalid_ls = '222222222222'
