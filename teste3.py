import os
import json
from flask import Flask, request, jsonify
from collections import Counter
import matplotlib
matplotlib.use('Agg')  # Usar o backend 'Agg' para evitar problemas de GUI
import matplotlib.pyplot as plt

app = Flask(__name__)

def count_posts_by_day(json_data, target_day):
    counts = Counter()
    for result in json_data['results']:
        date = result['publishedAt'][0] 
        if date == target_day:
            counts[date] += 1
    return counts

@app.route('/fetch', methods=['GET'])
def fetch_news():
    day = request.args.get('day')
    if not day:
        return jsonify({"error": "Day parameter is required"}), 400

    themes = ['brasil', 'corruption', 'semiconductors']
    all_counts = {theme: 0 for theme in themes}

    # Percorrer todos os temas e arquivos de páginas
    for theme in themes:
        page_number = 1
        while True:
            file_path = f'api_files/{theme}_{page_number}.json'
            if not os.path.exists(file_path):
                break
            with open(file_path, encoding='utf-8') as file:
                try:
                    data = json.load(file)
                    daily_counts = count_posts_by_day(data, day)
                    all_counts[theme] += daily_counts.get(day, 0)
                except json.JSONDecodeError:
                    print(f"Erro ao decodificar o arquivo: {file_path}")
            page_number += 1

    # Salvar os resultados em um arquivo JSON
    if not os.path.exists('output'):
        os.makedirs('output')

    with open('output/news_data.json', 'w') as json_file:
        json.dump(all_counts, json_file, indent=4)

    # Gerar o histograma
    themes = list(all_counts.keys())
    counts = list(all_counts.values())

    plt.figure(figsize=(10, 5))
    plt.bar(themes, counts)
    plt.xlabel('Theme')
    plt.ylabel('Number of Posts')
    plt.title(f'Number of Posts on {day} API DO CARALHO')
    plt.tight_layout()
    plt.savefig('output/histogram.png')

    return jsonify(all_counts)

if __name__ == '__main__':
    app.run(port=3000)