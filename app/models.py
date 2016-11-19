from . import db


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=True)
    articles = db.relationship('Article', backref='category', lazy='dynamic')

    @staticmethod
    def to_select_tag():
        return [(cg.id, cg.name) for cg in Category.query.all()]

    def __repr__(self):
        return '<Category %r>' % self.name


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime)
    modified_at = db.Column(db.DateTime)

    def __repr__(self):
        return '<Article %r>' % self.title