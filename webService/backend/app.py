from flask import Flask, Response, request, abort
from flask_cors import CORS
from runModel import run_model_main

# Flask 객체 인스턴스 생성
app = Flask(__name__)
CORS(app)


@app.route('/')  # 접속하는 url
def index():
    my_res = Response()
    my_res.headers["Access-Control-Allow-Origin"] = "*"

    return f'Hello, "World"!'


@app.route('/model/run', methods=['POST'])
def run_model():
    if "img_file" not in request.files:
        abort(400)

    result = run_model_main(request.files['img_file'])

    if result:
        result['ok'] = True
    else:
        result['ok'] = False

    return result


if __name__ == "__main__":
    # app.run(debug=True)
    app.run(host="127.0.0.1", port=5000, debug=True)
