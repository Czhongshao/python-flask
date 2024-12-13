from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

# 仅在开发环境中使用
if __name__ == '__main__':
    app.run(debug=True)  # 仅用于开发环境