from pprint import pprint

from sqlalchemy import and_

from src import db
from src.database.models import Film

films = db.session.query(Film).order_by(Film.rating.desc()).all()
pprint(films)

hpcs = db.session.query(Film).filter(Film.title == 'Harry Potter and Chamber of Secrets').first()
pprint(hpcs)

hppa = db.session.query(Film).filter_by(title='Harry Potter and the Prizoner of Azkaban').first()
pprint(hppa)

and_state = db.session.query(Film).filter(and_(
    Film.title != 'Harry Potter and Chamber of Secrets',
    Film.rating >= 7.5
)).all()
pprint(and_state)

dhs = db.session.query(Film).filter(Film.title.ilike('%deathly Hallows%')).all()
pprint(dhs)

not_in_state = db.session.query(Film).filter(~Film.length.in_([146, 161]))[:3]
pprint(not_in_state)

films_with_actors = db.session.query(Film).join(Film.actors).all()
pprint(films_with_actors)