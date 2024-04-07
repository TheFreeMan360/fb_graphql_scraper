# -*- coding: utf-8 -*-
from dataclasses import dataclass, field


@dataclass
class FacebookAccount(object):
    name: str = field(default=None)
    password: str = field(default=None)
