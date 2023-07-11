from src.datas.locators import *


def test_pass_recovery_page(browser):
    browser.find_element(*AutoPageLoc.LOCATOR_FORGOT_PASSWORD).click()
    assert browser.find_element(*PassRecLoc.LOCATOR_PassRec_FIELD).text == 'Восстановление пароля'
    print("\nПереход на страницу восстановления прошел успешно ")
    print("\nТест № TC_FAR-016 Пройден")
    