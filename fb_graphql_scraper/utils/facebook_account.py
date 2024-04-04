from dataclasses import dataclass, field


@dataclass
class FacebookAccount:
    name: str = field(default=None)
    password: str = field(default=None)
