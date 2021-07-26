# Программа для экспорта json в sql базу данных

## Подготовка к работе

Создать виртуальное окружение,
например:

```
python3 -m venv env
```

установить все необходимые для работы зависимости:

```
pip install -r requirements.txt
```

## Проверки

```
tox
```

## Работа с программой

Файл main.py содержит функцию json_to_db, параметром для которой необходимо указать путь к файлу .json, данные из которого необходимо внести в базу данных. Программа записывает все данные в файл warehouse.db. Если файл не существует он будет создан автоматически при запуске программы.