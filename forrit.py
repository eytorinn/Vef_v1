from bottle import route, run

@route('/')
def hello():
    return "Hello World!"


@route('/about')
def about():
    return



run(host='vefforritun123', debug=True)

