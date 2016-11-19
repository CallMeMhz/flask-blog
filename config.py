import os
basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG=True
BLOG_SETTING = {
    'blog_title': "Hyuk's Blog",
    'footer': 'Blog built by Mega Hertz'
}

CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'
PER_PAGE = 5

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_COMMIT_ON_TEARDOWN = True