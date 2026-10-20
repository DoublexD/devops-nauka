from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "moja pierwsza aplikacja"

@app.route("/health")
def health():
    return {"status":"OK"}

@app.route("/version")
def version():
    return {"version": "2.0"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)