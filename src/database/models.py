import uuid

from werkzeug.security import generate_password_hash

from src import db

films_actors = db.Table(
    'films_actors',
    db.Column('actor_id', db.Integer, db.ForeignKey('actors.id'), primary_key=True),
    db.Column('film_id', db.Integer, db.ForeignKey('films.id'), primary_key=True)
)


class Film(db.Model):
    __tablename__ = 'films'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    release_date = db.Column(db.Date, nullable=False, index=True)
    uuid = db.Column(db.String(36), unique=True)
    description = db.Column(db.Text)
    distributed_by = db.Column(db.String(120), nullable=False)
    length = db.Column(db.Float)
    rating = db.Column(db.Float)
    age_rating = db.Column(db.Integer)
    actors = db.relationship('Actor', secondary=films_actors, lazy='subquery',
                             backref=db.backref('films', lazy='subquery'))

    def __init__(self, title, release_date, description, distributed_by, length, rating, actors=None):
        self.title = title
        self.release_date = release_date
        self.description = description
        self.distributed_by = distributed_by
        self.length = length
        self.rating = rating
        self.uuid = str(uuid.uuid4())
        self.actors = actors if actors else []

    def __repr__(self):
        return f'Film({self.title}, {self.release_date}, {self.uuid}, {self.distributed_by}, {self.rating}, {self.length}, {self.actors if self.actors else []})'


class Actor(db.Model):
    __tablename__ = 'actors'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    birthday = db.Column(db.Date)
    is_active = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'Actor({self.name}, {self.birthday})'


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(254), nullable=False)
    is_admin = db.Column(db.Boolean(), default=False)
    uuid = db.Column(db.String(36), unique=True)

    def __init__(self, name, email, password, is_admin=False):
        self.name = name
        self.email = email
        self.password = generate_password_hash(password)
        self.is_admin = is_admin
        self.uuid = str(uuid.uuid4())

    def __repr__(self):
        return f'User({self.username}, {self.email}, {self.uuid})'

    @classmethod
    def find_by_name(cls, name):
        return cls.query().filter_by(name=name).first()

    @classmethod
    def find_by_uuid(cls, uuid):
        return cls.query().filter_by(uuid=uuid).first()
