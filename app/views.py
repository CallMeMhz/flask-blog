from datetime import datetime
from markdown import markdown
from . import app, db, lm
from .models import Article, Category
from .forms import EditArticleFrom
from config import BLOG_SETTING
from flask import render_template, redirect, url_for, flash, g, request
from flask_login import logout_user, logout_user, current_user, login_required


@app.before_request
def before_request():
    g.admin = current_user
    g.setting = BLOG_SETTING


@app.template_filter('md')
def markdown_to_html(text):
    return markdown(text)


@app.route('/')
def show_articles():
    page = request.args.get('page', 1, type=int)
    print Article.query.join(Category, (Category.id == Article.category)).first()
    pagination = Article.query.join(Category, (Category.id == Article.category))\
        .order_by(Article.id.desc())\
        .paginate(page, per_page=app.config['PER_PAGE'], error_out=False)
    return render_template('show_articles.html', pagination=pagination)


@app.route('/add', methods=['GET', 'POST'])
def add_article():
    form = EditArticleFrom()
    if form.validate_on_submit():
        article = Article(title=form.title.data,
                          category_id=int(form.category.data),
                          content=form.content.data,
                          created_at=datetime.utcnow())
        db.session.add(article)
        flash('New article was successfully posted')
        return redirect(url_for('show_articles'))
    return render_template('edit_article.html', form=form, edit_mode=False)


@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_article(id):
    form = EditArticleFrom()
    article = Article.query.get_or_404(id)
    if form.validate_on_submit():
        article.title = form.title.data
        article.category_id = form.category.data
        article.content = form.content.data
        article.modified_at = datetime.utcnow()
        db.session.add(article)
        flash('Successfully edit th article')
        return redirect(url_for('article', id=id))
    form.title.data = article.title
    form.category.data = article.id
    form.content.data = article.content
    return render_template('edit_article.html', form=form, edit_mode=True, article_id=id)


@app.route('/remove/<int:id>')
def remove_article(id):
    article = Article.query.get_or_404(id)
    db.session.delete(article)
    flash('The post has been deleted')
    return redirect(url_for('show_articles'))


@app.route('/article/<int:id>')
def article(id):
    article = Article.query.get_or_404(id)
    return render_template('article.html', article=article)