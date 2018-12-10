# clinicalinvestv2
中医临床流调数据中心-API接口

### 表格的模板对应的文件是"模板表格.xlsx"

### MYSQL数据库
```shell
# 1. 注意: clinicalinvestv2/settings文件中LN94、LN95修改自己本地的账号和密码

# 2. 本地创建数据库命令
create database clinical charset=utf8;

# 3. 导入数据库
mysql -uroot -p clinical < clinical.sql
```

## 数据管理后台与应用的创建
1. 后台管理员操作
    - url: http://localhost:8000/admin/
    - admin账号: 1@163.com
       admin密码: admin111

2. application的创建和修改
    - 创建
    访问 http://localhost:8000/o/applications/ 进行创建(注意设置项)






