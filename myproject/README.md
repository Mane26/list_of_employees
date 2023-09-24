## Departments - CRUD для Myproject. 

CRUD (сокр. от англ. create, read, update, delete — «создать, прочесть, обновить, удалить») — акроним, обозначающий четыре базовые функции, используемые при работе с персистентными хранилищами данных:
* создание;
* чтение;
* редактирование;
* удаление.

Для создания веб-страницы, отображающей древовидную структуру отделов со списком сотрудников, информацией о каждом сотруднике и возможностью управления записями в административной части CRUD в Django, я проделала следующую работу:

Клонируем проект:

```bash
git clone https://github.com/Mane26/list_of_employees.git
```

или

```bash
git clone git@github.com:Mane26/list_of_employees.git
```

Переходим в папку с проектом:

```bash
cd list_of_employees
```

Устанавливаем виртуальное окружение:

```bash
python -m venv venv
```

Активируем виртуальное окружение:

```bash
source venv/Scripts/activate
```

> Для деактивации виртуального окружения выполним (после работы):
> ```bash
> deactivate
> ```

Устанавливаем зависимости:

```bash
python -m pip install --upgrade pip
```
```bash
pip install -r requirements.txt
```

Применяем миграции:

```bash
python myproject/manage.py makemigrations
```
```bash
python myproject/manage.py migrate
```

Создаем суперпользователя:

```bash
python myproject/manage.py createsuperuser
```

Не забываем добавить в .gitingore файлы:

```bash
.env
.venv
```