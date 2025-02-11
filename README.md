Проект: Автоматизация тестирования для веб-сервиса «Stellar Burgers»
Тесты написаны с использованием Selenium и Python и охватывают ключевые функциональности, такие как регистрация, вход в аккаунт, работа с личным кабинетом и конструктором бургеров.

Описание проекта
Проект включает в себя автоматизированные тесты для проверки функциональности веб-сервиса «Stellar Burgers». Основные тестируемые сценарии:

Регистрация нового пользователя:

Успешная регистрация.

Регистрация с некорректным паролем.

Вход в аккаунт:

Вход через кнопку «Войти в аккаунт».

Вход через ссылку «Личный кабинет».

Вход через формы регистрации и восстановления пароля.

Личный кабинет:

Переход в личный кабинет.

Выход из аккаунта.

Переход на главную страницу через ссылки «Конструктор» и логотип.

Конструктор бургеров:

Переключение между категориями («Булки», «Соусы», «Начинки»).

Технологии
Python — язык программирования.

Selenium — фреймворк для автоматизации веб-приложений.

Pytest — фреймворк для написания и запуска тестов.

WebDriver — управление браузерами (Chrome, Firefox и др.).

Git — система контроля версий.

 Установка и настройка
1. Клонирование репозитория
Склонируйте репозиторий на ваш компьютер:

git clone https://github.com/kaleidka/Sprint_5.git

2. Установка зависимостей

pip install -r requirements.txt

 Запуск тестов
Для запуска всех тестов выполните команду:

pytest -v