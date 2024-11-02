# Blog
使用 Flask 框架製作部落格

## 2024/6/27 新增功能

### auth.py
- 使用者註冊
- 使用者登入
- 使用者登出

### blog.py
- 新增文章
- 刪除文章
- 修改文章

### db.py
- 資料庫連線
- `flask init-db` 建立資料表

## 資料庫：SQLite

### SQL 資料表

#### `user` 表
```sql
CREATE TABLE user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
);
