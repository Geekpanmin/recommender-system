from flask import jsonify, abort, request, current_app

from manage import recomender
from . import main


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
    user_id = request.form["user_id"]
    num = int(request.form["num"])
    poems = recomender.recommend(user_id, num)
    return jsonify([poem.to_dict() for poem in poems])
