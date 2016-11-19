# flask-blog
A single-user blog powered by Flask, SQLAlchemy, Foundation.

### 安装依赖包
    >>> pip install flask Flask-SQLAlchemy Flask-WTF markdown

### 初始化数据库
首先将 app/forms.py 中的 EditArticleForm 中下拉框 category 的 choices 留空
然后在 python 交互环境下执行：

    >>> from app import db
    >>> db.create_all()