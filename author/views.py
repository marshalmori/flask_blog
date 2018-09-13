from flask_blog import app

@app.rout('/login')
def login():
    return 'Author login'
