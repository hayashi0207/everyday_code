from model import db,Employee,Project,Company

for e in Employee.query.all():
    print(e.projects[0].name)

e= Employee.query.first()
print(e)
print(e.company.name)
print(e.projects[1].name)
for p in e.projects:
    print(p.name)

print('*'*100)
p = Project.query.get(1)
print(p.employees.name)

c= Company.query.get(1)
print(c.employees.name)

e=Employee.query.first()
print(type(e.projects))
print(e.projects[0].name)