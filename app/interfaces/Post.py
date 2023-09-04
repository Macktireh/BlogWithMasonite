from typing import TypedDict


class IPost(TypedDict):
    author_id: int
    title: str
    body: str
