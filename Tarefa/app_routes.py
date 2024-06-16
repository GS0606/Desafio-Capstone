from flask import Flask, request, jsonify
from service_news_service import service_news_service

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_news():
    theme = request.args.get('theme')
    start_time = request.args.get('start_time')
    end_time = request.args.get('end_time')
    page = request.args.get('page', default=1)  

    data = service_news_service.get_news_service(theme, start_time, end_time, page)

    return jsonify(data)

