# recommendation

## 项目介绍：
推荐系统

## 总体设计
- recommendation目录下完成推荐系统功能  
- 只有根目录下config允许从local_config导入配置，其余必须从config而非local_config导入配置 


##  目录说明     
├── docs  //详细说明文档     
├── logs  //日志文件目录       
├── recommendation //推荐系统主体              
│   ├── algorithms  //推荐算法       
│   │   ├── common //公用小工具                  
│   │   ├── recall //召回函数             
│   │   │   ├── content_base.py //基于内容的召回           
│   │   │   └── rule_base.py //基于规则的召回      
│   │   ├── matching.py //召回阶段      
│   │   └── ranking.py //排序阶段        
│   ├── dao  //数据库相关                     
│   ├── main  //flask蓝图        
│   │   └── views.py  //http视图路由                           
│   ├── objects  //对象相关      
│   ├── utils   //通用工具包               
│   ├── exceptions.py  //异常          
│   ├── ext.py  //flask 扩展    
│   ├── preprocessor.py  //项目启动预处理     
│   └── recommender.py  //推荐系统入口   
├── tests  //单元测试  
├── config.py  //配置文件    
├── local_config.py  //本地配置文件  
├── manage.py  //入口文件    
├── README.md  //说明文档   
├── requirements.txt  //依赖包   
├── server.py  //服务启动     
├── recommendation_algorithms.py  //前两次作业        
│   ├── bpr  //贝叶斯个性化排序      
│   └──  wide_and_deep  //Wide&Deep模型      


## 部署
      pip install -r requirements.txt
      按照docs/服务器部署.md部署服务


## 运行
     python3 server.py
     or
    nohup gunicorn -w 2 --threads 4 -t 10 -k gevent -b 127.0.0.1:9001 server:app --log-level=debug --reload --max-requests 1000 &

## 测试
     python3 tests/test_recommend.py

