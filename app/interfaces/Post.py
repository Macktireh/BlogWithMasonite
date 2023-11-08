from typing import TypedDict


class IUpdatedPost(TypedDict):
    title: str
    body: str


class IPost(IUpdatedPost):
    author_id: int
