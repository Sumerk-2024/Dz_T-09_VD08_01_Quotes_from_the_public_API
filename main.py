from flask import Flask, render_template, jsonify  # Импортируем необходимые модули из Flask
import requests  # Импортируем модуль requests для выполнения HTTP-запросов

app = Flask(__name__)  # Инициализируем Flask приложение


def fetch_random_quote():
    response = requests.get('https://api.quotable.io/random')  # Выполняем GET-запрос к API для получения случайной цитаты
    if response.status_code == 200:  # Проверяем, успешно ли выполнен запрос
        return response.json()  # Возвращаем JSON-ответ как словарь
    else:
        return None  # Возвращаем None, если запрос не был успешным


@app.route('/')  # Определяем маршрут для главной страницы
def index():
    quote = fetch_random_quote()  # Получаем случайную цитату
    if quote:  # Если цитата получена успешно
        return render_template('index.html', quote=quote)  # Рендерим шаблон index.html с переданной цитатой
    else:
        return "Ошибка при получении цитаты", 500  # Возвращаем сообщение об ошибке с кодом 500


@app.route('/api/quote')  # Определяем маршрут для API, который возвращает цитату в формате JSON
def api_quote():
    quote = fetch_random_quote()  # Получаем случайную цитату
    if quote:  # Если цитата получена успешно
        return jsonify(quote)  # Возвращаем цитату в формате JSON
    else:
        return jsonify({"error": "Ошибка при получении цитаты"}), 500  # Возвращаем сообщение об ошибке в формате JSON с кодом 500


if __name__ == '__main__':  # Проверяем, запущен ли модуль как основной
    app.run(debug=True)  # Запускаем сервер Flask в режиме отладки
