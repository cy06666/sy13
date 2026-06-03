from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "DevOps CI/CD实验：服务部署成功"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)