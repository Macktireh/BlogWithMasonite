from masonite.controllers import Controller
from masonite.views import View

from app.repositories.PostRepository import PostRepository


class HomeController(Controller):
    def show(self, view: View, postRepository: PostRepository) -> View:
        posts = postRepository.getPosts()
        return view.render("index", {"posts": posts})
