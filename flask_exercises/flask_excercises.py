from flask import Flask, request


class FlaskExercise:
    """
    Вы должны создать API для обработки CRUD запросов.
    В данной задаче все пользователи хранятся в одном словаре, где ключ - это имя пользователя,
    а значение - его параметры. {"user1": {"age": 33}, "user2": {"age": 20}}
    Словарь (dict) хранить в памяти, он должен быть пустым при старте flask.

    POST /user - создание пользователя.
    В теле запроса приходит JSON в формате {"name": <имя пользователя>}.
    Ответ должен вернуться так же в JSON в формате {"data": "User <имя пользователя> is created!"}
    со статусом 201.
    Если в теле запроса не было ключа "name", то в ответ возвращается JSON
    {"errors": {"name": "This field is required"}} со статусом 422

    GET /user/<name> - чтение пользователя
    В ответе должен вернуться JSON {"data": "My name is <name>"}. Статус 200

    PATCH /user/<name> - обновление пользователя
    В теле запроса приходит JSON в формате {"name": <new_name>}.
    В ответе должен вернуться JSON {"data": "My name is <new_name>"}. Статус 200

    DELETE /user/<name> - удаление пользователя
    В ответ должен вернуться статус 204
    """

    db = {}

    @staticmethod
    def configure_routes(app: Flask) -> None:
        pass

        @app.post("/user")
        def create_user():
            try:
                name = request.get_json()["name"]
            except KeyError:
                response = {"errors": {"name": "This field is required"}}
                return response, 422
            else:
                FlaskExercise.db[name] = "created"
                response = {"data": f"User {name} is created!"}
                return response, 201

        @app.get("/user/<username>")
        def get_user(username):
            if FlaskExercise.db[username] == "deleted":
                return "", 404
            response = {"data": f"My name is {username}"}
            return response, 200

        @app.patch("/user/<username>")
        def update_user(username):
            name = request.get_json()["name"]
            FlaskExercise.db[username] = "deleted"
            FlaskExercise.db[name] = "created"
            response = {"data": f"My name is {name}"}
            return response, 200

        @app.delete("/user/<username>")
        def delete_user(username):
            FlaskExercise.db[username] = "deleted"
            response = {"data": f"{username} deleted"}
            return "", 204
