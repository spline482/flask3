# импортируем модуль os для работы с файловой системой
import os
# импортируем модуль json для работы с файлом данных
import json
# импортируем функцию для хеширования паролей
from werkzeug.security import generate_password_hash, check_password_hash
# импортируем модуль datetime для работы с датами
from datetime import datetime


# функция для загрузки данных из json-файла
def load_users(filepath='users.json'):
    # если файл не существует — создаём пустой словарь
    if not os.path.exists(filepath):
        return {}
    # открываем файл для чтения с кодировкой utf-8 (для поддержки кириллицы)
    with open(filepath, 'r', encoding='utf-8') as f:
        # читаем и возвращаем данные как словарь
        return json.load(f)


# функция для сохранения данных в json-файл
def save_users(data, filepath='users.json'):
    # открываем файл для записи с кодировкой utf-8
    with open(filepath, 'w', encoding='utf-8') as f:
        # записываем данные с отступами для читаемости (indent=4)
        # ensure_ascii=False позволяет сохранять кириллицу без экранирования
        json.dump(data, f, indent=4, ensure_ascii=False)


# функция для хеширования пароля (превращаем пароль в защищённую строку)
def hash_password(password):
    # generate_password_hash создаёт безопасный хеш из пароля
    return generate_password_hash(password)


# функция для проверки пароля (сравниваем введённый пароль с хешем)
def check_password(password_hash, password):
    # check_password_hash возвращает True, если пароль верный
    return check_password_hash(password_hash, password)


# функция для получения текущей даты и времени в строковом формате
def get_current_datetime():
    # возвращаем дату в формате "ГГГГ-ММ-ДД ЧЧ:ММ:СС"
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')