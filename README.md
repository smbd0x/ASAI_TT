## Видео-презентация
[Смотреть](https://streamable.com/jxih2r)

## .env и odoo.conf
Для тестового запуска можно скопировать следующее содержимое:

.env:
```
POSTGRES_DB=odoo
POSTGRES_USER=odoo
POSTGRES_PASSWORD=odoo
```

odoo.conf:
```
[options]
addons_path = /usr/lib/python3/dist-packages/odoo/addons,/mnt/extra-addons
db_host = db
db_port = 5432
db_user = odoo
db_password = odoo
admin_passwd = admin123
xmlrpc_port = 8069
```

## Доступ
Логин/пароль для веб интерфейса: 

**admin/admin**

## Функционал
Остановился на уровне medium. 
Основная логика из ТЗ реализована, есть юнит тесты, docker-compose, security файл для ограничения доступа к моделям.
