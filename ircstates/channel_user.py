from typing import List
from .user import User
from .channel import Channel

class ChannelUser(object):
    def __init__(self,
            channel: Channel,
            user:    User):
        self.channel          = channel
        self.user             = user
        self.modes: List[str] = []

    def __repr__(self) -> str:
        return (f"ChannelUser(user={self.user.nickname!r},"
            f" channel={self.channel.name!r},"
            f" modes={''.join(self.modes)!r})")
