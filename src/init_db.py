'''
CS3250 - Software Development Methods and Tools
Instructor: Thyago Mota
Student(s):
Description: Project 1 - GPA Calculator
'''

from app import app, db
from app.models import Course

# TODO
courses = [
    
]

with app.app_context():
    for prefix, number, name, credits in courses:
        if not db.session.get(Course, (prefix, number)):
            db.session.add(Course(prefix=prefix, number=number, name=name, credits=credits))
    db.session.commit()
    print(db.engine.url)
    print(db.session.scalars(db.select(Course)).all())
    print(f'Loaded {len(courses)} courses.')
