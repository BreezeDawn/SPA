# SPA
> 本题解答使用框架: 前端 Vue + TS , 后端 Flask

使用须知:

    > 后端数据库配置文件路径: SPA/SPA_back/src/py/config/sql.ini
    > 根据步骤启动后,将在后端根目录下生成日志文件夹存储日志文件 
    > 前端 api-url 配置文件路径: SPA/SPA_front/spa_front/config/config.ts
    
    1. 数据表迁移, 进入 SPA/SPA_back/
    
        a. python app.py mc init
        
        b. python app.py mc migrtate
        
        c. python app.py mc upgrade
        
    2. 相同目录下启动后端, python app.py runserver --host 0.0.0.0 --port 7777 
    
    3. 前端安装依赖包, 进入 SPA/SPA_front/spa_front, 执行 yarn install
    
    4. 相同目录下启动前端, yarn serve
     

##### 要求
1. 使用 Flask

2. 使用 Vue

3. 使用 TS

4. 使用 Mysql

5. freestyle

6. beautiful

7. github

   
##### 需求分析 - 不明了的地方
    1.前端获取随机数组后,以什么图表展示,数组是几维
    2.后端存储当前数据,存储的是单个数组还是拆开数组存储里面的数
    3.Subpage2 展示至多 100 条数据, "数据"指的是"数组"还是"数字"

    > 这里我把理解为数字 

##### DB

​	2 个表

##### 后端

​	api 随机数组存储至 表1 并返回
​	api 存储数据至 表2
​	api 100 个 表2 数据

##### 前端

​	页面
​		10 秒刷新的图表
​		button 存储数据
​	页面
​		100图表数据

