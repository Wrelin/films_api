from src.database.models import Film


class FilmService(object):
    @staticmethod
    def fetch_all(session):
        return session.query(Film)

    @classmethod
    def find_by_uuid(cls, session, uuid):
        return cls.fetch_all(session).filter_by(uuid=uuid).first()
