from flask import Blueprint, request, jsonify, current_app
from .api import fetch_movies
from datetime import datetime, timezone
from . import get_db
import logging

main = Blueprint('main', __name__)

@main.route('/movies', methods=['POST', 'OPTIONS'])
def get_movies():
    if request.method == 'OPTIONS':
        return '', 204

    data = request.get_json()
    if not data:
        current_app.logger.error("Nenhum dado JSON recebido")
        return jsonify({"error": "Nenhum dado JSON recebido"}), 400

    user = data.get('user')
    movie_name = data.get('movie')
    if not user or not movie_name:
        current_app.logger.error("User e movie name são obrigatórios")
        return jsonify({"error": "User e movie name são obrigatórios"}), 400

    try:
        api_key = current_app.config.get("API_KEY")
        result = fetch_movies(movie_name, api_key)
        current_app.logger.info(f"Filmes buscados para {movie_name}")
        current_app.logger.info(f"{result}")

        # Verifica se pymongo está disponível
        #if 'pymongo' not in current_app.extensions:
        #    raise Exception("pymongo não está configurado corretamente")

        get_db().search_log.insert_one({
            "user": user,
            "movie_name": movie_name,
            "result": result,
            "timestamp": datetime.now(timezone.utc)
        })
        current_app.logger.info("Busca registrada no log de pesquisa")
        return jsonify(result), 200
    except Exception as e:
        current_app.logger.error(f"Erro ao buscar filmes: {e}")
        return jsonify({"error": str(e)}), 500

@main.route('/history', methods=['GET'])
def get_history():
    try:
        logs = get_db().search_log.find()
        history = []
        for log in logs:
            log['_id'] = str(log['_id'])
            history.append(log)
        return jsonify(history), 200
    except Exception as e:
        current_app.logger.error(f"Erro ao obter histórico: {e}")
        return jsonify({"error": str(e)}), 500

