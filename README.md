# RuningString
Проект RuningString:
Создание видео бегущей строки.

для запуска проекта клонируйте репозиторий https://github.com/al-ar/RuningString

Cоздать и активировать виртуальное окружение:

python3 -m venv env
source env/bin/activate
Установить зависимости из файла requirements.txt:

python3 -m pip install --upgrade pip
pip install -r requirements.txt

Установите ImageMagick:
обратите внимание :
IMAGEMAGICK_BINARY
    For linux users, 'convert' should be fine.
    For Windows users, you must specify the path to the ImageMagick
    'magick' binary. For instance:

    IMAGEMAGICK_BINARY = r"C:\Program Files\ImageMagick-6.8.8-Q16\magick.exe"

Выполнить миграции:

python3 manage.py migrate
Запустить проект:

python3 manage.py runserver

Примеп работы: http://aleksandrov81.pythonanywhere.com/
автор: Александров Артем
