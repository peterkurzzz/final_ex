import src.datas.locators as lc
import src.datas.datas as datas


def test_reg_page(browser):
    browser.find_element(*lc.AutoPageLoc.LOCATOR_REG_TAB).click()
    assert browser.find_element(*lc.RegPageLoc.LOCATOR_REG_FIELD).text == 'Регистрация'
    print("\nПереход на страницу регистрации прошел успешно ")
    print("\nТест № TC_FAR-018 Пройден")


def test_reg_page_registration(browser_reg_page):
    input_field = browser_reg_page.find_elements(*lc.RegPageLoc.LOCATOR_INPUT_FIELD)
    input_field[0].send_keys(datas.fake_firstname)
    input_field[1].send_keys(datas.fake_lastname)
    input_field[3].send_keys(datas.fake_email)
    input_field[4].send_keys(datas.fake_password)
    input_field[5].send_keys(datas.fake_password)
    browser_reg_page.find_element(*lc.RegPageLoc.LOCATOR_BUTTON_REGISTRATION).click()
    assert browser_reg_page.find_element(*lc.RegPageLoc.LOCATOR_REGISTRATION_CODE_FIELD).text == \
           'Подтверждение email'
    print("\nПереход на страницу получения кода подтверждения прошел успешно ")
    print("\nТест № TC_FAR-020 Пройден")


def test_reg_page_no_data(browser_reg_page):
    input_field = browser_reg_page.find_elements(*lc.RegPageLoc.LOCATOR_INPUT_FIELD)
    input_field[0].send_keys()
    input_field[1].send_keys()
    input_field[3].send_keys()
    input_field[4].send_keys()
    input_field[5].send_keys()
    browser_reg_page.find_element(*lc.RegPageLoc.LOCATOR_BUTTON_REGISTRATION).click()
    error_message = browser_reg_page.find_elements(*lc.RegPageLoc.LOCATOR_ERROR_MESS)
    name_error_message = error_message[0]
    last_name_error_message = error_message[1]
    mail_error_message = error_message[2]
    password_error_message = error_message[3]
    password_confirm_error_message = error_message[4]
    assert name_error_message.text == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'\
           and last_name_error_message.text == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'\
           and mail_error_message.text == 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в '\
                                          'формате example@email.ru'\
           and password_error_message.text == 'Длина пароля должна быть не менее 8 символов'\
           and password_confirm_error_message.text == 'Длина пароля должна быть не менее 8 символов'
    print("\n Появились сообщения об ошибке регистрации ")
    print("\nТест № TC_FAR-021 Пройден")


def test_reg_page_all_ready_reg(browser_reg_page):
    input_field = browser_reg_page.find_elements(*lc.RegPageLoc.LOCATOR_INPUT_FIELD)
    input_field[0].send_keys(datas.valid_firstname)
    input_field[1].send_keys(datas.valid_lastname)
    input_field[3].send_keys(datas.valid_email)
    input_field[4].send_keys(datas.valid_password)
    input_field[5].send_keys(datas.valid_password)
    browser_reg_page.find_element(*lc.RegPageLoc.LOCATOR_BUTTON_REGISTRATION).click()
    assert browser_reg_page.find_element(*lc.RegPageLoc.LOCATOR_REGISTRATION_CODE_FIELD).text == 'Регистрация'
    print("\nПоявилась форма, сообщающая о том, что пользователь уже зарегистрирован ")
    print("\nТест № TC_FAR-022 Пройден")


def test_reg_page_invalid_name(browser_reg_page):
    input_field = browser_reg_page.find_elements(*lc.RegPageLoc.LOCATOR_INPUT_FIELD)
    input_field[0].send_keys('23rgfd!')
    input_field[1].send_keys(datas.fake_lastname)
    input_field[3].send_keys(datas.fake_email)
    input_field[4].send_keys(datas.fake_password)
    input_field[5].send_keys(datas.fake_password)
    browser_reg_page.find_element(*lc.RegPageLoc.LOCATOR_BUTTON_REGISTRATION).click()
    error_message = browser_reg_page.find_elements(*lc.RegPageLoc.LOCATOR_ERROR_MESS)
    name_error_message = error_message[0]
    assert name_error_message.text == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'
    print("\n Появилось сообщение об ошибке ввода имени ")


def test_reg_page_invalid_name_short(browser_reg_page):
    input_field = browser_reg_page.find_elements(*lc.RegPageLoc.LOCATOR_INPUT_FIELD)
    input_field[0].send_keys('ж')
    input_field[1].send_keys(datas.fake_lastname)
    input_field[3].send_keys(datas.fake_email)
    input_field[4].send_keys(datas.fake_password)
    input_field[5].send_keys(datas.fake_password)
    browser_reg_page.find_element(*lc.RegPageLoc.LOCATOR_BUTTON_REGISTRATION).click()
    error_message = browser_reg_page.find_elements(*lc.RegPageLoc.LOCATOR_ERROR_MESS)
    name_error_message = error_message[0]
    assert name_error_message.text == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'
    print("\n Появилось сообщение об ошибке ввода имени ")


def test_reg_page_name_long(browser_reg_page):
    input_field = browser_reg_page.find_elements(*lc.RegPageLoc.LOCATOR_INPUT_FIELD)
    input_field[0].send_keys('оченьдлинныйоеимякотороенеподойдет')
    input_field[1].send_keys(datas.fake_lastname)
    input_field[3].send_keys(datas.fake_email)
    input_field[4].send_keys(datas.fake_password)
    input_field[5].send_keys(datas.fake_password)
    browser_reg_page.find_element(*lc.RegPageLoc.LOCATOR_BUTTON_REGISTRATION).click()
    error_message = browser_reg_page.find_elements(*lc.RegPageLoc.LOCATOR_ERROR_MESS)
    name_error_message = error_message[0]
    assert name_error_message.text == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'
    print("\n Появилось сообщение об ошибке ввода имени ")
    print("\nТест № TC_FAR-023 Пройден")


def test_reg_page_invalid_lastname(browser_reg_page):
    input_field = browser_reg_page.find_elements(*lc.RegPageLoc.LOCATOR_INPUT_FIELD)
    input_field[0].send_keys(datas.fake_firstname)
    input_field[1].send_keys('123gfhfj!&')
    input_field[3].send_keys(datas.fake_email)
    input_field[4].send_keys(datas.fake_password)
    input_field[5].send_keys(datas.fake_password)
    browser_reg_page.find_element(*lc.RegPageLoc.LOCATOR_BUTTON_REGISTRATION).click()
    error_message = browser_reg_page.find_elements(*lc.RegPageLoc.LOCATOR_ERROR_MESS)
    last_name_error_message = error_message[0]
    assert last_name_error_message.text == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'
    print("\n Появилось сообщение об ошибке ввода фамилии ")


def test_reg_page_invalid_lastname_short(browser_reg_page):
    input_field = browser_reg_page.find_elements(*lc.RegPageLoc.LOCATOR_INPUT_FIELD)
    input_field[0].send_keys(datas.fake_firstname)
    input_field[1].send_keys('ж')
    input_field[3].send_keys(datas.fake_email)
    input_field[4].send_keys(datas.fake_password)
    input_field[5].send_keys(datas.fake_password)
    browser_reg_page.find_element(*lc.RegPageLoc.LOCATOR_BUTTON_REGISTRATION).click()
    error_message = browser_reg_page.find_elements(*lc.RegPageLoc.LOCATOR_ERROR_MESS)
    last_name_error_message = error_message[0]
    assert last_name_error_message.text == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'
    print("\n Появилось сообщение об ошибке ввода фамилии ")


def test_reg_page_invalid_lastname_long(browser_reg_page):
    input_field = browser_reg_page.find_elements(*lc.RegPageLoc.LOCATOR_INPUT_FIELD)
    input_field[0].send_keys(datas.fake_firstname)
    input_field[1].send_keys('нуоченьдлиннаяфамилиянеподойдет')
    input_field[3].send_keys(datas.fake_email)
    input_field[4].send_keys(datas.fake_password)
    input_field[5].send_keys(datas.fake_password)
    browser_reg_page.find_element(*lc.RegPageLoc.LOCATOR_BUTTON_REGISTRATION).click()
    error_message = browser_reg_page.find_elements(*lc.RegPageLoc.LOCATOR_ERROR_MESS)
    lastname_error_message = error_message[0]
    assert lastname_error_message.text == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'
    print("\n Появилось сообщение об ошибке ввода фамилии ")
    print("\nТест № TC_FAR-024 Пройден")


def test_reg_page_invalid_mail(browser_reg_page):
    input_field = browser_reg_page.find_elements(*lc.RegPageLoc.LOCATOR_INPUT_FIELD)
    input_field[0].send_keys(datas.fake_firstname)
    input_field[1].send_keys(datas.fake_lastname)
    input_field[3].send_keys('qwertyui')
    input_field[4].send_keys(datas.fake_password)
    input_field[5].send_keys(datas.fake_password)
    browser_reg_page.find_element(*lc.RegPageLoc.LOCATOR_BUTTON_REGISTRATION).click()
    error_message = browser_reg_page.find_elements(*lc.RegPageLoc.LOCATOR_ERROR_MESS)
    mail_error_message = error_message[0]
    assert mail_error_message.text == 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в ' \
                                      'формате example@email.ru'
    print("\n Появилось сообщение об ошибке ввода адреса электронной почты или номера мобильного телефона ")
    print("\nТест № TC_FAR-025 Пройден")


def test_reg_page_invalid_password_short(browser_reg_page):
    input_field = browser_reg_page.find_elements(*lc.RegPageLoc.LOCATOR_INPUT_FIELD)
    input_field[0].send_keys(datas.fake_firstname)
    input_field[1].send_keys(datas.fake_lastname)
    input_field[3].send_keys(datas.fake_email)
    input_field[4].send_keys('12345')
    input_field[5].send_keys(datas.fake_password)
    browser_reg_page.find_element(*lc.RegPageLoc.LOCATOR_BUTTON_REGISTRATION).click()
    error_message = browser_reg_page.find_elements(*lc.RegPageLoc.LOCATOR_ERROR_MESS)
    password_error_message = error_message[0]
    assert password_error_message.text == 'Длина пароля должна быть не менее 8 символов'
    print("\n Появилось сообщение об ошибке в выборе пароля ")


def test_reg_page_invalid_password_without_up_letter(browser_reg_page):
    input_field = browser_reg_page.find_elements(*lc.RegPageLoc.LOCATOR_INPUT_FIELD)
    input_field[0].send_keys(datas.fake_firstname)
    input_field[1].send_keys(datas.fake_lastname)
    input_field[3].send_keys(datas.fake_email)
    input_field[4].send_keys('12345678')
    input_field[5].send_keys(datas.fake_password)
    browser_reg_page.find_element(*lc.RegPageLoc.LOCATOR_BUTTON_REGISTRATION).click()
    error_message = browser_reg_page.find_elements(*lc.RegPageLoc.LOCATOR_ERROR_MESS)
    password_error_message = error_message[0]
    assert password_error_message.text == 'Пароль должен содержать хотя бы одну заглавную букву'
    print("\n Появилось сообщение об ошибке в выборе пароля ")


def test_reg_page_invalid_password_without_onle_en_letter(browser_reg_page):
    input_field = browser_reg_page.find_elements(*lc.RegPageLoc.LOCATOR_INPUT_FIELD)
    input_field[0].send_keys(datas.fake_firstname)
    input_field[1].send_keys(datas.fake_lastname)
    input_field[3].send_keys(datas.fake_email)
    input_field[4].send_keys('12345678Ж')
    input_field[5].send_keys(datas.fake_password)
    browser_reg_page.find_element(*lc.RegPageLoc.LOCATOR_BUTTON_REGISTRATION).click()
    error_message = browser_reg_page.find_elements(*lc.RegPageLoc.LOCATOR_ERROR_MESS)
    password_error_message = error_message[0]
    assert password_error_message.text == 'Пароль должен содержать только латинские буквы'
    print("\n Появилось сообщение об ошибке в выборе пароля ")


def test_reg_page_invalid_password_without_low_letter(browser_reg_page):
    input_field = browser_reg_page.find_elements(*lc.RegPageLoc.LOCATOR_INPUT_FIELD)
    input_field[0].send_keys(datas.fake_firstname)
    input_field[1].send_keys(datas.fake_lastname)
    input_field[3].send_keys(datas.fake_email)
    input_field[4].send_keys('12345678S')
    input_field[5].send_keys(datas.fake_password)
    browser_reg_page.find_element(*lc.RegPageLoc.LOCATOR_BUTTON_REGISTRATION).click()
    error_message = browser_reg_page.find_elements(*lc.RegPageLoc.LOCATOR_ERROR_MESS)
    password_error_message = error_message[0]
    assert password_error_message.text == 'Пароль должен содержать хотя бы одну строчную букву'
    print("\n Появилось сообщение об ошибке в выборе пароля ")
    print("\nТест № TC_FAR-026 Пройден")


def test_reg_page_invalid_password_confirm(browser_reg_page):
    input_field = browser_reg_page.find_elements(*lc.RegPageLoc.LOCATOR_INPUT_FIELD)
    input_field[0].send_keys(datas.fake_firstname)
    input_field[1].send_keys(datas.fake_lastname)
    input_field[3].send_keys(datas.fake_email)
    input_field[4].send_keys(datas.fake_password)
    input_field[5].send_keys('12345678Ss')
    browser_reg_page.find_element(*lc.RegPageLoc.LOCATOR_BUTTON_REGISTRATION).click()
    error_message = browser_reg_page.find_elements(*lc.RegPageLoc.LOCATOR_ERROR_MESS)
    password_error_message = error_message[0]
    assert password_error_message.text == 'Пароли не совпадают'
    print("\n Появилось сообщение об ошибке подтверждения пароля ")
    print("\nТест № TC_FAR-027 Пройден")
