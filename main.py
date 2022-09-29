import logging
from flask import Flask, request
from flask import jsonify


def create_app():
    app = Flask(__name__)
    return app


app = create_app()


@app.route('/api/v1/users', methods=['GET'])
def get_users():
    f = open("db.txt", "r")
    users = []
    for line in f.readlines():
        users.append(line[:-1])
    f.close()
    response = {'users': users}
    return jsonify(response)


@app.route('/api/v1/users/', methods=['POST'])
def create_user():
    json = request.get_json(force=True)
    if (json.get("user") is None):
        return {"error": "Bad Request"}
    user = json['user']
    f = open("db.txt", "a")
    f.write(user + "\n")
    f.close()
    response = {'message': 'success'}
    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)
else:
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)
