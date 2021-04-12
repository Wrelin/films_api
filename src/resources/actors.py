from flask_restful import Resource
from sqlalchemy.orm import selectinload

from src import db
from src.database.models import Actor
from src.resources.auth import token_required
from src.schemas.actor import ActorSchema


class ActorListApi(Resource):
    actor_schema = ActorSchema()

    @token_required
    def get(self):
        actors = db.session.query(Actor).options(selectinload(Actor.films)).all()
        return self.actor_schema.dump(actors, many=True), 200

    def post(self):
        pass

    def put(self):
        pass

    def patch(self):
        pass

    def delete(self):
        pass
