from model import db,Person
from datetime import datetime

man1 = Person(
    'mike',
    '080-1111-1111',
    12,
    datetime.now(),
    datetime.now()
)
db.session.add(man1)
db.session.commit()