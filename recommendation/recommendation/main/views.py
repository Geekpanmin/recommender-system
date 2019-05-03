import datetime

from flask import jsonify, abort, request, current_app

from recommendation.apis.gaode import GaodeApi
from recommendation.main.tags import Tag
from recommendation.recommender import Recommender
from . import main

recommender = Recommender()

gaode_api = GaodeApi()


@main.after_app_request
def after_request(response):
    # for query in get_debug_queries():
    #     if query.duration >= current_app.config['FLASKY_SLOW_DB_QUERY_TIME']:
    #         current_app.logger.warning(
    #             'Slow query: {}\nParameters: {}\nDuration: {}\nContext: {}\n'.format(
    #                 query.statement, query.parameters, query.duration, query.context))
    return response


@main.route('/shutdown')
def server_shutdown():
    if not current_app.testing:
        abort(404)
    shutdown = request.environ.get('werkzeug.server.shutdown')
    if not shutdown:
        abort(500)
    shutdown()
    return 'Shutting down...'


@main.route('/', methods=['GET', 'POST'])
def test():
    return jsonify({"status": "success"})


@main.route('/recommend/', methods=['GET', 'POST'])
def recommend():
    user_id = request.form.get("user_id", "")
    num = int(request.form.get("num", 20))
    tags = request.form.get("tags", [])
    date_time = request.form.get("date_time", "")
    ip_expand = request.form.get("ip_expand", False)
    if ip_expand:
        ip = request.remote_addr
        addr = gaode_api.get_ip_addr(ip)
        now_weather = gaode_api.get_weather(addr["adcode"])
        if not date_time:
            now = datetime.datetime.now()
            date_time = {"month": now.month, "day": now.day, "hour": now.hour}
        default_tags = Tag(addr=addr, now_weather=now_weather, date_time=date_time).get_tags()
        tags = set(tags).update(set(default_tags))
    poems = recommender.recommend(user_id, num, tags)
    return jsonify([poem.to_dict() for poem in poems])
