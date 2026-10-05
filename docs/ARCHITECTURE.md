# Architecture

Flask handles pages and student actions. Forms collect input, and SQLAlchemy
saves or retrieves records in SQLite. The course-list page sends the student's
entries to the GPA library before displaying them.

|Location||
|---|---|
|`src/app/__init__.py`|Starts the app, creates database tables, and connects sign-in support.|
|`src/app/routes.py`|Handles account actions, course entry, listing, and deletion.|
|`src/app/forms.py`|Defines form fields and basic input checks.|
|`src/app/models.py`|Defines saved records and their relationships.|
|`src/gpa_calculator/`|Contains the GPA calculation and grade scale.|
|`src/init_db.py`|Loads the starting course catalog.|
|`src/pyproject.toml`|Describes the GPA package; placeholder values need completing.|
|`templates/` and `static/`|Provide page layouts and styles.|
|`uml/`|Contains diagrams of student actions and record relationships.|

## Saved records

- **User:** the student's ID, name, description, and password hash. The hash lets
  the app check a password without storing the original password.
- **Course:** its prefix, number, name, and credits.
- **Enrollment:** links one student to one course and stores their grade.

Students share a course catalog but keep separate graded entries. Each student
can record a course once. Course entry offers courses they have not recorded;
deletion looks up the entry using both the student and course identifiers.

## GPA calculation

The intended calculation multiplies each grade's points by the course credits,
adds the results, and divides by the total graded credits. An A in a four-credit
course and a B in a three-credit course give `(4 × 4 + 3 × 3) / 7 ≈ 3.57`.

The scale runs from A+ at 4.3 to F at 0. Empty input returns 0. The code expects
enrollment objects, although its description mentions dictionaries.

## Starting courses

|Course|Name|Credits|
|---|---|---|
|CS 1050|Computer Science 1|4|
|ACC 4520|Mergers and Acquisitions|3|
|ANT 2640|Archaeology|3|
|JPS 1010|Elementary Japanese I|5|
|ENG 2505|Rhetoric of War|3|

The loader adds missing courses and preserves existing records. Its “Loaded 5
courses” message counts configured courses, including those already saved.

The app uses a fixed development secret that must be replaced before deployment.
The [use case diagram](../uml/use_case.wsd) also has an invalid closing tag:
`@endum1` should be `@enduml`.
