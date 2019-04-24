from recommendation.utils.enum import Enum


class MatchAlgorithmEnum(Enum):
    """ name key proportion
    顺序即是优先级，若某一算法视频缺失，使用高优先级算法填补
    """
    rule_base = ("RB", 1)
    suprise_cf = ("SP", 0)
    item_cf = ("IC", 0)
    user_cf = ("UC", 0)
    tag_base = ("TB", 0)
    content_base = ("CB", 0)
