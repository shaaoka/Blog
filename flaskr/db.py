import sqlite3

import click
from flask import current_app,g


def get_db():
    if 'db' not in g :
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row
    return g.db


# 關閉連接資料庫
def close_db(e=None):
    # 從 g 取出 db 屬性，如果不存在回傳None
    db = g.pop('db',None)

    if db is not None:
        db.close()
        
# 數據庫初始化
def init_db():
    db = get_db()
    # 打開文件夾裡的schema.sql檔案 
    with current_app.open_resource('schema.sql') as f:
        #讀取並編碼成 utf-8格式 db.executescript() 並執行SQL腳本 
        db.executescript(f.read().decode('utf-8'))

#定義 flask init 的命令操作
@click.command('init-db')
def init_db_command():
    init_db()
    #印出訊息
    click.echo('初始化資料庫完成')

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)