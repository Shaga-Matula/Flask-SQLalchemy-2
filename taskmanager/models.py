from taskmanager import db


class Category(db.Model):
    # schema for Category model
    id = db.Column(db.integer, primary_key=True)
    category_name = db.column(db.String(25), unique=True, nullable=False)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.category_name


class Task(db.Model):
    # schema for Task Model
    id = db.Column(db.integer, primary_key=True)
    task_name = db.column(db.String(50), unique=True, nullable=False)
    task_description = db.column(db.Text, nullable=False)
    

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
