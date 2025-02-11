from selenium.webdriver.common.by import By

REGISTER_BUTTON = "//a[contains(@class, 'Auth_link__1fOlj') and @href='/register' and text()='Зарегистрироваться']"

PASSWORD_BUTTON_REGISTRATION = "//input[@type='password' and @name='Пароль']"
EMAIL_BUTTON_REGISTRATION = "//input[@type='text' and @name='name' and @value='']"
NAME_BUTTON_REGISTRATION = "//input[@type='text' and @name='name']"

LOGIN_EMAIL_BUTTON = "//div[contains(@class, 'input_type_text') and contains(@class, 'input_size_default')]//input[@type='text' and @name='name']"
LOGIN_PASSWORD_BUTTON = "//div[contains(@class, 'input_type_password') and contains(@class, 'input_size_default')]//input[@type='password' and @name='Пароль']"
LOGIN_SUBMIT_BUTTON = "//button[contains(@class, 'button_button__33qZ0') and contains(@class, 'button_button_type_primary__1O7Bx') and text()='Войти']"

PERSONAL_ACCOUNT_BUTTON = "a.AppHeader_header__link__3D_hX[href='/account']"

WRONG_PASSWORD_BUTTON = "//p[@class='input__error text_type_main-default' and text()='Некорректный пароль']"

ENTER_TO_ACCOUNT_BUTTON = "//button[contains(@class, 'button_button__33qZ0') and contains(@class, 'button_button_size_large__G21Vg') and text()='Войти в аккаунт']"

CREATE_ORDER_BUTTON = ".//button[text() = 'Оформить заказ']"
ENTER_BUTTON_ON_REGISTRATION = "//a[@class='Auth_link__1fOlj' and @href='/login' and text()='Войти']"
PASSWORD_RECOVER_BUTTON = "//a[@class='Auth_link__1fOlj' and @href='/forgot-password' and text()='Восстановить пароль']"

RECOVER_TEXT_PLACE = "//div[contains(@class, 'Auth_login')]//h2"
CONSTRUCTOR_BUTTON = (By.XPATH, "//p[@class='AppHeader_header__linkText__3q_va ml-2' and text()='Конструктор']")
BURGER_TEXT = "//h1[contains(@class, 'text') and text()='Соберите бургер']"
LOGO_BURGERS_BUTTON = (By.CSS_SELECTOR, "div.AppHeader_header__logo__2D0X2 a[href='/']")

PROFILE_BUTTON = "//a[contains(@class, 'Account_link') and text() = 'Профиль']"
EXIT_BUTTON = "//li[@class='Account_listItem__35dAP']//button[contains(@class, 'Account_button__14Yp3') and text()='Выход']"

SAUCE_TAB = "//div[contains(@class, 'tab_tab__1SPyG') and contains(., 'Соусы')]"
TOPPINGS_TAB = "//div[contains(@class, 'tab_tab__1SPyG') and contains(., 'Начинки')]"
CONSTRUCTOR_SECTION = "section.BurgerIngredients_ingredients__1N8v2"

SPICY_X_SAUCE = "//p[contains(., 'Соус Spicy-X')]"
SHELLFISH_MEAT = "//p[contains(., 'Мясо бессмертных моллюсков Protostomia')]"

REGISTER_BUTTON_ON_REGISTER_PAGE = "//button[contains(@class, 'button_button__33qZ0') and text()='Зарегистрироваться']"
RECOVER_PASSWORD_BUTTON = "//button[contains(@class, 'button')]"
