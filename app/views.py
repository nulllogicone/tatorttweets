# -*- coding: utf-8 -*-
#!/usr/local/bin/python2.7

from flask import request, render_template, current_app, _app_ctx_stack, redirect, url_for


from app import app
from sqlite3 import dbapi2 as sqlite3
# from flask import Flask, request, session, g, redirect, url_for, abort, \
#      render_template, flash, _app_ctx_stack

# create our little application :)
app.config.from_object(__name__)


global entries


def init_db():
    """Creates the database tables."""
    with app.app_context():
        db = get_db()


def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    top = _app_ctx_stack.top
    if not hasattr(top, 'sqlite_db'):
        sqlite_db = sqlite3.connect(app.config['DATABASE'])
        sqlite_db.row_factory = sqlite3.Row
        top.sqlite_db = sqlite_db

    return top.sqlite_db


@app.route('/')
def index():
    
    global entries

    db = get_db()
    cur = db.execute('select * from metadata order by lfd desc')
    entries = cur.fetchall()
    return render_template('base.html', entries=entries)


@app.route('/<selected>', methods=['GET', 'POST'])

@app.route('/', methods=['POST'])
def work(selected=None):

    current_app.logger.debug(request.method); 
    global entries

    if request.method == 'GET':
        try:
            entries
        except NameError:
            entries = None
        
        if entries is None:
            db = get_db()
            cur = db.execute('select * from metadata order by lfd desc')
            entries = cur.fetchall()
    
        if selected is not None: 
            db = get_db()
            cur = db.execute("SELECT lfd FROM tatorttweets WHERE lfd='" + selected + "' LIMIT 1")
            if not cur.fetchone(): 
                return render_template('base.html', entries=entries)
            
        return render_template('base.html', entries=entries, selected=selected)


    
    if request.method == 'POST':
        
        dataset = request.form.items()
        current_app.logger.debug(dataset[0][1])
        
        return redirect(url_for('work', selected=dataset[0][1]))
    
#         return render_template('base.html', entries=entries, selected=dataset[0][1])
     

if __name__ == '__main__':
    app.run()
