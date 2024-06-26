import os
from flask import Flask


def create_app(test_config=None):
    # instance_relative_config=True 設定True會去尋找 instance 文件夾尋找配置文件(例:密碼、本地配置)
    app = Flask(__name__,instance_relative_config=True)
    # config.from_mapping() 設定想要的配置
    # SECRET_KEY 應用程式密碼
    # DATABASE= DATABASE 資料庫設定 
    # 要使用的sqlite檔案 os.path.join(app.instance_path,'flaskr.sqlite') 
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
        )
    if test_config is None:
        # silent=True #默認發生錯誤或警告，開發時可以使用。
        app.config.from_pyfile('config.py',silent=True)
    else:
        app.config.from_mapping(test_config)
    
    try:
    # 如果嘗試創建instance文件夾，忽略錯誤。
    # 可能的錯誤資料夾已存在、或是權限不足
        os.makedirs(app.instance_path)
    except OSError:
        pass
    # 測試app
    @app.route('/hello')
    def hello():
        return 'Hello, World!'
    # 初始化資料庫
    from . import db
    db.init_app(app)
    # 建立管理註冊、登入、登出藍圖，認證藍圖將包括註冊新用戶、登入、登出視圖
    from . import auth
    app.register_blueprint(auth.bp)
    # 建立blog藍圖。
    from . import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')

    return app



  

  