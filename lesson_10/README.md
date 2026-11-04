# Lesson 10: PageObject + Allure

Доработка домашней работы №7 «PageObject»: два UI-теста Selenium,
аннотации типов и docstring у всех методов Page Object, Allure-шаги,
описания тестов и проверка стиля PEP 8.

## Установка

Требуются Python, Google Chrome и Mozilla Firefox. Драйверы для
современного Selenium обычно предоставляет Selenium Manager.

Из корня репозитория:

```bash
python -m venv .venv
```

Активация в PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Установка зависимостей:

```bash
python -m pip install -r requirements.txt
```

## Запуск тестов и сбор результатов Allure

Из корня репозитория:

```bash
python -m pytest lesson_10 --alluredir=allure-results
```

Запуск калькулятора занимает не менее 45 секунд из-за задержки.
Тест магазина использует Firefox, а калькулятор Chrome.
Тесты требуют подключения к интернету.

## Просмотр отчёта Allure

Для просмотра нужен **Allure Commandline**, устанавливаемый отдельно
от Python-пакета `allure-pytest`. После установки команды `allure`:

```bash
allure serve allure-results
```

Команда создаёт временный отчёт и открывает его в браузере.
Чтобы отдельно сформировать статический отчёт:

```bash
allure generate allure-results -o allure-report --clean
allure open allure-report
```

## Проверка стиля

```bash
flake8 lesson_10
```

Папки `allure-results/` и `allure-report/` не нужно добавлять
в Git: в `.gitignore` проекта они исключены.

## Сдача

Создать Pull Request из ветки `lesson10` в `main`,
не объединять ветки до принятия наставником.
