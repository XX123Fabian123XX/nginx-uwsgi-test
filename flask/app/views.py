from app.start import app

@app.route("/")
def index():
    return "hello"