from bottle import route, run

@route('/')
def hello():
    return "Hello World!"


@route('/about')
def about():
    return



run(host='https://vefforritun123.herokuapp.com/', debug=True)

