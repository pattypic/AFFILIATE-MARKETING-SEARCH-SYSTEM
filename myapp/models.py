from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# defines a Link model for a database table using the SQLAlchemy ORM (Object-Relational Mapping) library.
# defined as a subclass of db.Model, indicating that it is a SQLAlchemy model that will be mapped to a database table
# id, name, url attributes are defined as columns of the table, with id being the primary key column
# __repr__ defined for the Link class, which returns a string representation of a Link instance that includes its name. This method is used to provide a more human-readable output when Link instances are printed or logged.
class Link(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    url = db.Column(db.String(1000), nullable=False)

    def __repr__(self):
        return f'<Link {self.name}>'