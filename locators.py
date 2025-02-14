from selenium.webdriver.common.by import By

class Locators:
    # Общий локатор для кнопок
    BUTTON = '//button[text()="{btn}"]'  # XPath для любой кнопки с текстом

    # Локатор формы для "Регистрации" или "Входа"
    FORM = './/h2[text()="{form}"]/parent::div/form'  # XPath для заголовков форм

    # Поля ввода для форм "Регистрация" или "Вход"
    FORM_FIELDS = FORM + '//label[text()="{field}"]/parent::div/input'  # XPath для полей формы

    # Поля профиля: "Имя", "Логин" или "Пароль"
    PROFILE_FIELDS = (
        './/li[contains(@class, "profile")]//label[text()="{field}"]'
        '/parent::div/input'
    )  # XPath для полей ввода профиля

    # Категории в конструкторе бургеров: "Булки", "Соусы" или "Начинки"
    CATEGORIES = './/span[text()="{name}"]/parent::div'  # XPath для разделов категорий

    # СОЗДАНИЕ АККАУНТА:
    ACCOUNT_LINK = By.XPATH, './/p[text()="Личный Кабинет"]'  # Ссылка на личный кабинет
    SIGN_UP_LINK = By.XPATH, './/a[text()="Зарегистрироваться"]'  # Ссылка для регистрации
    SIGN_UP_NAME_INPUT = (
        By.XPATH, FORM_FIELDS.format(form='Регистрация', field='Имя')
    )  # Поле ввода "Имя" в форме регистрации
    SIGN_UP_EMAIL_INPUT = (
        By.XPATH, FORM_FIELDS.format(form='Регистрация', field='Email')
    )  # Поле ввода "Email" в форме регистрации
    SIGN_UP_PASSWORD_INPUT = (
        By.XPATH, FORM_FIELDS.format(form='Регистрация', field='Пароль')
    )  # Поле ввода "Пароль" в форме регистрации
    SIGN_UP_BUTTON = (
        By.XPATH, (FORM + BUTTON).format(
            form='Регистрация', btn='Зарегистрироваться'
        )
    )  # Кнопка "Зарегистрироваться" в форме регистрации

    # ВХОД В АККАУНТ:
    SIGN_IN_FORM = By.XPATH, './/div[contains(@class, "Auth_login")]/h2'  # Заголовок формы входа
    SIGN_IN_EMAIL_INPUT = (
        By.XPATH, FORM_FIELDS.format(form='Вход', field='Email')
    )  # Поле ввода "Email" в форме входа
    SIGN_IN_PASSWORD_INPUT = (
        By.XPATH, FORM_FIELDS.format(form='Вход', field='Пароль')
    )  # Поле ввода "Пароль" в форме входа
    SIGN_IN_BUTTON = By.XPATH, (FORM + BUTTON).format(form='Вход', btn='Войти')  # Кнопка "Войти" в форме входа
    SIGN_IN_LINK = (
        By.XPATH, './/p[text()="Уже зарегистрированы?"]/a[text()="Войти"]'
    )  # Ссылка "Войти" под формой регистрации

    # ПРОВЕРКА ПРОФИЛЯ:
    PROFILE_LINK = By.XPATH, './/a[text()="Профиль"]'  # Ссылка на профиль
    PROFILE_NAME = By.XPATH, PROFILE_FIELDS.format(field='Имя')  # Поле "Имя" в профиле
    PROFILE_LOGIN = By.XPATH, PROFILE_FIELDS.format(field='Логин')  # Поле "Логин" в профиле
    PERSONAL_ACCOUNT = By.XPATH, './/p[contains(@class, "Account_text")]'  # Текст на странице личного кабинета
    EXIT_BUTTON = By.XPATH, BUTTON.format(btn='Выход')  # Кнопка "Выход" в личном кабинете

    # ЭЛЕМЕНТЫ НА ГЛАВНОЙ СТРАНИЦЕ:
    ENTER_ACCOUNT_BUTTON = By.XPATH, BUTTON.format(btn='Войти в аккаунт')  # Кнопка "Войти в аккаунт"
    CONSTRUCTOR_LINK = By.XPATH, './/p[text()="Конструктор"]'  # Ссылка на конструктор
    LOGO_LINK = By.XPATH, './/div[contains(@class, "log")]/a[@href="/"]'  # Ссылка-логотип "Stellar Burgers"
    CONSTRUCT_BURGER = (
        By.XPATH, './/section[contains(@class, "ingredients")]/h1'
    )  # Заголовок "Соберите бургер"
    BUNS = By.XPATH, CATEGORIES.format(name='Булки')  # Раздел "Булки" в конструкторе
    SAUCES = By.XPATH, CATEGORIES.format(name='Соусы')  # Раздел "Соусы" в конструкторе
    TOPPINGS = By.XPATH, CATEGORIES.format(name='Начинки')  # Раздел "Начинки" в конструкторе

    # ДРУГИЕ ЭЛЕМЕНТЫ:
    INVALID_PASSWORD_WARNING = (
        By.XPATH,
        FORM.format(form='Регистрация') + '//p[contains(@class, "error")]'
    )  # Предупреждение о некорректном пароле
    RESTORE_PASSWORD_LINK = (
        By.XPATH,
        './/p[text()="Забыли пароль?"]/a[text()="Восстановить пароль"]'
    )  # Ссылка "Восстановить пароль" под формой входа
    REMEMBER_PASSWORD_SIGN_IN_LINK = (
        By.XPATH, './/p[text()="Вспомнили пароль?"]/a[text()="Войти"]'
    )  # Ссылка "Войти" под формой восстановления пароля
    BASKET_BUTTON = By.XPATH, BUTTON.format(btn="Оформить заказ")  # Кнопка "Оформить заказ" в корзине
