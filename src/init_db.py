'''
CS3250 - Software Development Methods and Tools
Instructor: Thyago Mota
Student(s):
Description: Project 1 - GPA Calculator
'''

from app import app, db
from app.models import Course

courses = [
    ("CS", "1050", "Computer Science 1", 4 ),
    ("ACC", "4520", "Mergers and Aquisitions", 3),
    ("ANT", "2640", "Archaeology", 3),
    ("JPS", "1010", "Elementary Japanese I", 5),
    ("ENG", "2505", "Rhetoric of War", 3),
]

with app.app_context():
    for prefix, number, name, credits in courses:
        if not db.session.get(Course, (prefix, number)):
            db.session.add(Course(prefix=prefix, number=number, name=name, credits=credits))
    db.session.commit()
    print(f'Loaded {len(courses)} courses.')
