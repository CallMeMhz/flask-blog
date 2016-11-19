# coding=utf-8
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField
from wtforms.validators import DataRequired
from .models import Category


class EditArticleFrom(FlaskForm):
    title = StringField(u'文章标题', validators=[DataRequired()])
    # db.create_all()的时候先将 choices 留空，否则将会出现找不到 Category 的错误
    category = SelectField(u'类别', choices=Category.to_select_tag(), coerce=int, validators=[DataRequired()])
    content = TextAreaField(u'内容', validators=[DataRequired()])