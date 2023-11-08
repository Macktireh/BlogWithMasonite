from typing import List

from app.interfaces.Post import IPost, IUpdatedPost
from app.models.Post import Post


class PostRepository:
    def getPosts(self) -> List[Post]:
        return Post.all()

    def getPostById(self, id: int) -> Post:
        return Post.find(id)

    def createPost(self, post: IPost) -> Post:
        return Post.create(**post)

    def updatePost(self, id: int, payload: IUpdatedPost) -> Post:
        post = Post.find(id)
        for key, value in payload.items():
            setattr(post, key, value)
        post.save()
        return post        

    def deletePost(self, id: int) -> None:
        return Post.find(id).delete()
