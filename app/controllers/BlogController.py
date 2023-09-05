from masonite.controllers import Controller
from masonite.views import View
from masonite.request import Request
from masonite.response import Response

from app.interfaces.Post import IPost
from app.repositories.PostRepository import PostRepository


class BlogController(Controller):
    def show(self, view: View, postRepository: PostRepository) -> View:
        return view.render("blog/store")

    def store(self, request: Request, response: Response, postRepository: PostRepository) -> View:
        payload = IPost(
            title=request.input("title"), body=request.input("body"), author_id=request.user().id
        )
        postRepository.createPost(payload)

        return response.redirect(name="home")
    
    def single(self, view: View, request: Request, postRepository: PostRepository) -> View:
        post = postRepository.getPostById(request.param("id"))
        return view.render("blog/single", {"post": post})
