
### Wiki Encyclopedia
### Автор: Константин Коробейников

Вики-энциклопедия, позволяющая создавать, редактировать и просматривать статьи в формате Markdown. Реализован поиск и отображение случайных страниц.

**Ключевые технологии:** Django, Markdown, Функциональное программирование.





1.  **Клонируйте репозиторий:**
    ```bash
    git clone https://github.com/Korobox3221/Wiki.git
    cd wiki
    ```
2.  **Установите зависимости:**
    ```bashcd
    pip install -r requirements.txt
    ```
3.  **Примените миграцию базы данных:**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```
4.  **Создайте суперпользователя (необязательно):**
    ```bash
    python manage.py createsuperuser
    ```
5.  **Запустите сервер для разработки:**
    ```bash
    python manage.py runserver
    ```

Приложение будет запущено на `http://127.0.0.1:8000/`.


