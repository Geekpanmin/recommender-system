# 北京大学软件与微电子学院《推荐系统技术》课程作业

## 作业内容

![课堂作业](docs/homework.png)

----

## 任务安排

###  1.算法实现

>  说明：
>
>  a. 每组从下面的列表选一个算法，并在群里接龙以避免重复，例：“1. 张三 组 选算法3 WR-MF； 2. 李四组 选算法6 RSTE；...”；
>
>  b. **第5次课**前，提交两个版本的代码：（1）基于普通python3的版本（自己实线优化算法）；（2）基于TensorFlow的版本；
>
>  c. 做好算法设计，并给出设计文档，至少包含6个函数：（1）数据集的拆分（训练/验证/测试）；（2）数据加载；（3）模型训练（参数学习）；（4）模型（参数）保存；（5）模型（参数）加载；（6）模型测试或评估
>
>  d. 代码中应该有足够多的注释以便于阅读和理解。



贝叶斯个性化排序（BPR，Bayesian Personalized Ranking）

原始论文：[BPR: Bayesian Personalized Ranking from Implicit Feedback](https://arxiv.org/abs/1205.2618)

- BPR Python版  （3.16，第四周周六晚）：王胜广
- BPR tensorflow版 （3.16，第四周周六晚）：龚润宇、梅楚鹤
- BPR算法设计文档 （3.16，第四周周六晚）：龚润宇、梅楚鹤


### 2.论文阅读
原始论文：[Wide & Deep Learning for Recommender Systems](https://arxiv.org/abs/1606.07792)

- Wide&Deep论文翻译 （3.16，第四周周六晚）：柳俊志、尹国健
- 论文算法实现  （3.23，第五周周六晚）：王胜广
- 汇报PPT制作 （3.23，第五周周六晚）：王胜广
- 上台汇报（4.7，第六周周日课堂）：王胜广



### 3.课程项目

    11周提交，下周（9周）课前提交题目
    
    1.工程：找一个应用场景，新场景（非MovieLens等已有公开数据集），
    非热门领域（非商品视频新闻推荐，比如教育领域、新闻领域等），主要解决当前领域推荐需求，
    需要做出实用产品，最好使用自己小组汇报过的算法，训练数据集没有可以自己生成，主要是要能解决当前实际场景问题
    2.研究：改进现有算法问题，实现新算法
    3.综述：针对某一专题PPT的算法整理出一个章节，系统化梳理细化之
    

下次课前（4月21日前）各组选定课程项目题目，并在群里发布，以避免重复。
选题范围（三选一）：
1. 推荐系统应用：发掘某个行业（或应用)痛点，设计基于推荐的接近方案；
要求：完成后台的设计与实现；
2. 算法改进：针对选定的一个（或一类）最近的算法，提出改进方案，并进行测试验证；
3. 经典算法整理：选择某次课件，整理并补充完善，形成文字；
要求：可作为教材的一章
    

##  目录说明 
├── docs //文档         
├── logs  //日志文件目录       
├── recommendation //推荐系统主体        
│   ├── algorithms  //推荐算法   
│   │   ├── cf //协同过滤算法                  
│   │   ├── common //公用小工具          
│   │   │   ├── bases.py //基础工具函数         
│   │   │   └── constants.py //常量          
│   │   ├── recall //召回函数             
│   │   │   ├── content_base.py //基于内容的召回           
│   │   │   └── rule_base.py //基于规则的召回  
│   │   ├── wide_deep //召回函数             
│   │   │   ├── data_helper.py //数据准备             
│   │   │   └── train.py //模型训练         
│   │   ├── matching.py //召回阶段      
│   │   └── ranking.py //排序阶段        
│   ├── apis  //API   
│   │   └── gaode.py //高德地图api         
│   ├── dao  //数据库相关   
│   │   ├── models //数据库表对应model               
│   │   │   ├── ext_types.py //数据库列扩展类型             
│   │   │   ├── mongo_models.py //mongoDB数据库表模型           
│   │   │   └── mysql_models.py //mysql数据库表模型    
│   │   ├── db.py  //处理数据库连接               
│   │   ├── db_tools.py  //数据库相关小工具                  
│   │   ├── memory.py  //内存管理                  
│   │   ├── mongo_utils.py  //mongoDB查询语句               
│   │   └── mysql_utils.py  //mysql查询语句                 
│   ├── main  //flask蓝图        
│   │   └── views.py  //http视图路由                           
│   ├── objects  //对象相关    
│   │   ├── __init__.py  //objects模块对外可导入部分                   
│   │   ├── object_utils.py  //object通用工具               
│   │   ├── poems.py  //poem对象                 
│   │   └── users.py  //user对象     
│   ├── tasks   //离线任务       
│   │   ├── load_poem.py  //诗词数据存入mysql                        
│   │   ├── tags.py  //用户上下文转换为tags                          
│   │   ├── tasks.py  //给诗词打标签                 
│   │   └── word2vec.py  //词向量训练        
│   ├── utils   //通用工具包    
│   │   ├── async_tools.py  //异步执行函数                      
│   │   ├── enum.py  //不可变类型                       
│   │   ├── logger.py  //log配置工具               
│   │   ├── tools.py  //基础工具                   
│   │   └── view_helper.py  //打印输出ResultPoem信息    
│   ├── config.py  //配置文件                     
│   ├── local_config.py  //本地配置文件，密码等                      
│   ├── manage.py  //入口文件                       
│   └── server.py  //服务启动文件                       
└── recommendation_algorithms //前两次推荐作业          

