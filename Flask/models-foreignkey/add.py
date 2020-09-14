from model import db, Employee, Project, Company

john = Employee('John')
adam = Employee('Adam')

db.session.add_all([john,adam])
db.session.commit()

company1=Company('Microsoft',john.id)
company2=Company('Apple',adam.id)

db.session.add_all([company1,company2])
db.session.commit()

john_project1 = Project('Word Project', john.id)
john_project2 = Project('Excel Project', john.id)
adam_project1 = Project('Mac Project', adam.id)
adam_project2 = Project('Iphone Project', adam.id)


db.session.add_all([john_project1,john_project2,adam_project1,adam_project2])

db.session.commit()