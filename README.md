Дипломный проект: Реальный кейс от компании «Ростелеком Информационные Технологии»

Объект тестирования: новый интерфейс авторизации в личном кабинете от заказчика Ростелеком (https://b2c.passport.rt.ru/auth/)

Требования по проекту: Требования_SSO_для_тестирования_last.pdf

При разработке тестов использованы:
1) IDE - PyCharm 2023.1.3 (Community Edition);
2) ЯП - Python v3.9, в том числе:
		pytest v7.4.0,
		selenium v4.10.0,
		Faker v18.11.2,

Для тестирования использованы:
1) Веб браузер Google Chrom v114.0.5735
2) Веб драйвер chromedriver v114.0.5735

Использованные техники тест-дизайна:
- граничные значения
- эквивалентные разделения
- таблица принятия решений

Из-за появления Captcha прохождение некоторых тестов невозможно.

Дефекты во время тестирования не обнаружены, все автотесты завершены успешно

В корне проекта находятся следующие файлы:
- requirements.txt - список используемых библиотек
- README.md 

В папке tests находятся файлы:
- conftest.py - файл с фикстурами
- test_base_page.py - тестирует функционал страницы авторизации
- test_auto_page.py - тестирует разные способы авторизации на сайте
- test_pass_recovery_page.py - тестирует функционал страницы смены пароля
- test_reg_page.py - тестирует разные способы регистрации на сайте

В папке src/datas находятся файлы:
- locators.py - список локаторов проекта
- datas.py - список используемых переменных

В папке src/driver находится файл веб драйвера.
