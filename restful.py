from bottle import run, get, post, request, delete

emojies = [{'emoji1': 'var1', 'emoji2': 'var2'}]


@get('/emoji/<emoji1>/<emoji2>')
def getAll(emoji1, emoji2):
    return {emoji1, emoji2}

run(reloader=True, debug=True)
