# -*- coding: utf-8 -*-
from dataclasses import dataclass, field


@dataclass
class PostRecord(object):
    # self.res = {
    #     "post_caption": [],
    #     "post_date": [],
    #     "post_likes": [],
    #     "comment_share_type": [],
    #     "comment_share_value": []
    # }

    post_id: str = field(default=None)
    password: str = field(default=None)
    reaction_count: int = field(default=0)
