from model import db,Person
from datetime import datetime

man1 = Person(
    'Taro',
    '080-2222-2222',
    21,
    datetime.now(),
    datetime.now()
)
man2 = Person(
    'Jiro',
    '090-4444-4444',
    23,
    datetime.now(),
    datetime.now()
)
man3 = Person(
    'Saburo',
    '080-3333-3333',
    20,
    datetime.now(),
    datetime.now()
)

# db.session.add_all([man1,man2,man3])
# db.session.commit()

# print(Person.query.get(3))
# print(Person.query.first())

# for x in Person.query.filter_by(name='mike').all():
#     print(x.name)

# for x in Person.query.filter(Person.age>15).all():
#     print(x)

# for x in Person.query.filter(Person.name.endswith('o')).limit(2):
#     print(x)

# Person.query.filter_by(id=1).delete()
# db.session.commit()

Person.query.filter_by(name='nanashi').update(
    {
        'name':'John',
        'update_at': datetime.now()
    }
)
db.session.commit()