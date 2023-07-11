from selenium.webdriver.common.by import By


class AutoPageLoc:
    """Локаторы для страницы авторизации"""
    LOCATOR_PHONE_TAB = (By.ID, 't-btn-tab-phone')
    LOCATOR_PHONE_FIELD = (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/div/span[2]')
    LOCATOR_PHONE_FIELD_ACTIV = (By.ID, 'username')
    LOCATOR_MAIL_TAB = (By.ID,  't-btn-tab-mail')
    LOCATOR_MAIL_FIELD = (By.XPATH, '//span[contains(text(),"Электронная почта")]')
    LOCATOR_MAIL_FIELD_ACTIV = (By.ID, 'username')
    LOCATOR_LOGIN_TAB = (By.ID, 't-btn-tab-login')
    LOCATOR_LOGIN_FIELD = (By.XPATH, '//span[contains(text(),"Логин")]')
    LOCATOR_LOGIN_FIELD_ACTIV = (By.ID, 'username')
    LOCATOR_LS_TAB = (By.ID, 't-btn-tab-ls')
    LOCATOR_LS_FIELD = (By.XPATH, '//span[contains(text(),"Лицевой счёт")]')
    LOCATOR_LS_FIELD_ACTIV = (By.ID, 'username')
    LOCATOR_PASSWORD_TAB = (By.ID, 'password')
    LOCATOR_ENTER_TAB = (By.ID, 'kc-login')
    LOCATOR_ERROR = (By.ID, 'form-error-message')
    LOCATOR_FORGOT_PASSWORD = (By.ID, 'forgot_password')
    LOCATOR_ERROR_MESS = (By.XPATH, '//span[contains(@class, "rt-input-container__meta")]')
    LOCATOR_REG_TAB = (By.ID, 'kc-register')

    """Локатор личного кабинета"""
    LOCATOR_LK_TAB = (By.ID, 'lk-btn')


class PassRecLoc:
    """Локатор для страницы смены пароля"""
    LOCATOR_PassRec_FIELD = (By.CLASS_NAME, 'card-container__title')


class RegPageLoc:
    """Локаторы для страницы регистрации"""
    LOCATOR_REG_FIELD = (By.CLASS_NAME, 'card-container__title')
    LOCATOR_BUTTON_REGISTRATION = (By.NAME, 'register')
    LOCATOR_REGISTRATION_CODE_FIELD = (By.CLASS_NAME, 'card-container__title')
    LOCATOR_ERROR_MESS = (By.XPATH, '//span[contains(@class, "rt-input-container__meta")]')
    LOCATOR_INPUT_FIELD = (By.XPATH, '//input[contains(@class, "rt-input__input")]')

