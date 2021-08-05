from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

announcement_put_args = reqparse.RequestParser()
announcement_put_args.add_argument('heading', type=str, help='Заголовок Статьи', required=True)
announcement_put_args.add_argument('description', type=str, help='Описание', required=True)
announcement_put_args.add_argument('date of creation', type=str, help='Дата создания', required=True)
announcement_put_args.add_argument('owner', type=str, help='Владелец', required=True)

announcements = {}

def abort_if_announcement_doesnt_exist(anno_id):
    if anno_id not in announcements:
        abort(404, message='Не удалось найти')

def abort_if_announcement_exists(anno_id):
    if anno_id in announcements:
        abort(409, message='уже существует')

class Announcement(Resource):
    def get(self, anno_id):
        abort_if_announcement_doesnt_exist(anno_id)
        return announcements[anno_id]

    def put(self, anno_id):
        abort_if_announcement_exists(anno_id)
        args = announcement_put_args.parse_args()
        announcements[anno_id] = args
        return announcements[anno_id], 201

    def delite(self,anno_id):
        abort_if_announcement_doesnt_exist(anno_id)
        del announcements[anno_id]
        return '', 204

api.add_resource(Announcement, "/announcements/<int:anno_id>")

if __name__ == "__main__":
    app.run(debug=True)
