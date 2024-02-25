from abc import ABC
from dataclasses import dataclass
from datetime import datetime


@dataclass
class Post:
    message: str
    timestamp: int


class SocialChannel(ABC):
    def __init__(self, network: str, follower: int) -> None:
        self.network = network
        self.follower = follower
        self.current_time = datetime.now()
        self.currrent_hour = int(self.current_time.strftime("%H"))


class YouTube(SocialChannel):
    def make_a_post(self, message, timestamp):
        if timestamp <= self.currrent_hour:
            print(
                f"You see post for {self.network}, message is ({message}), we have {self.follower} followers"  # noqa
            )


class Facebook(SocialChannel):
    def make_a_post(self, message, timestamp):
        if timestamp <= self.currrent_hour:
            print(
                f"You see post for {self.network}, message is ({message}), we have {self.follower} followers"  # noqa
            )


class Twitter(SocialChannel):
    def make_a_post(self, message, timestamp):
        if timestamp <= self.currrent_hour:
            print(
                f"You see post for {self.network}, message is ({message}), we have {self.follower} followers"  # noqa
            )


def post_a_message(
    channel: SocialChannel, message: str, timestamp: int
) -> None:
    channel.make_a_post(message, timestamp)


def process_schedule(posts: list[Post], channels: list[SocialChannel]) -> None:
    for post in posts:
        message, timestamp = post.message, post.timestamp
        for channel in channels:
            post_a_message(channel, message, timestamp)


post_1 = Post(message="Test post #1", timestamp=19)
post_2 = Post(message="Test post #2", timestamp=20)
post_3 = Post(message="Test post #3", timestamp=21)

process_schedule(
    posts=[post_1, post_2, post_3],
    channels=[
        YouTube(network="youtube", follower=31800),
        Facebook(network="facebook", follower=55000),
        Twitter(network="twitter", follower=87800),
    ],
)
