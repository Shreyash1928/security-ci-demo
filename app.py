from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    password = "admin123"   # hardcoded password (security issue)
    return "Hello Security Testing!"

if __name__ == "__main__":
    app.run(debug=True)
