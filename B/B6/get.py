from bottle import route
from bottle import run
from bottle import request
from bottle import HTTPError

@route("/add")
def add():
    try:
        x = int(request.query.x)
        y = int(request.query.y)
    except ValueError:
        result = HTTPError(400, "Некорректные параметры")
    else:
        s = x + y
        result = "Сумма {} и {} равна {}".format(x, y, s)
    return result

if __name__ == "__main__":
    run(host="localhost", port=8080, debug=True)