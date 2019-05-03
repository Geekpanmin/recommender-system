from recommendation.utils.tools import synchronized


class Memory(object):
    """ 内存管理"""
    _instance = None  # 单例模式

    @synchronized
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            _instance = super(Memory, cls).__new__(cls, *args, **kwargs)
            _instance.all_poems_dict = {}  # {"poem_id":Poem}
            _instance.all_poets_dict = {}  # {"poet_id":Poet}
            _instance.all_poem_ids = []
            _instance.popular_poem_ids = []
            # instance
            cls._instance = _instance
        return cls._instance

    __slots__ = ("all_poems_dict", "all_poets_dict", "all_poem_ids", "popular_poem_ids")  # 限制实例object能动态绑定的属性名称

    def __init__(self):
        """此处绑定属性会有问题，每次初始化时会覆盖原先的值，勿操作"""
        pass
