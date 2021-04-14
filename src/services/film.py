from src.database.models import Film


class FilmService(object):
    @staticmethod
    def fetch_all(session):
        return session.query(Film)

    @classmethod
    def find_by_uuid(cls, session, uuid):
        return cls.fetch_all(session).filter_by(uuid=uuid).first()

    @staticmethod
    def bulk_create_films(session, films):
        films_to_create = [
            Film(**film)
            for film in films
        ]
        session.bulk_save_objects(films_to_create)
        session.commit()
        return len(films_to_create)
