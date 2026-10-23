# UI-автотесты на Selenium + Pytest (SauceDemo)

Учебный проект по автоматизации UI-тестирования демо-сайта [SauceDemo](https://www.saucedemo.com/).

## Структура проекта
- `tests/` — автотесты на Pytest
- `pages/` — Page Object Model (локаторы и методы страниц)
- `conftest.py` — фикстуры (драйвер, авторизация)
- `docs/checklist.md` — чек-лист для всех страниц SauceDemo
- `docs/test-cases.md` — тест-кейсы
- `docs/bug-reports/` — баг-репорты
- `data/products.py` — словарь с данными товаров  

## Покрытые сценарии
- Авторизация (успешная / с неверным паролем / заблокированный пользователь)
- Добавление товара в корзину
- Удаление товара из корзины
- Оформление заказа (checkout)
- Сортировка товаров

## Стек
- Python 3.14
- pytest — тестовый фреймворк
- Selenium WebDriver — управление браузером
- Page Object Model — архитектурный паттерн
- Git — контроль версий

## Установка и запуск

1. Клонировать репозиторий
```bash
git clone https://github.com/nyanfisa/ui-selenium-testing.git
cd ui-selenium-testing
```
2. Создать и активировать виртуальное окружение

# Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

# Linux/macOS:
```bash
python -m venv venv
source venv/bin/activate
```

3. Установить зависимости
```bash
pip install -r requirements.txt
```

4. Запустить тесты

```bash
pytest -sv
```