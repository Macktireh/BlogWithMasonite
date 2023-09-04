from masonite.providers import Provider
from masonite.facades import View

from app.repositories.PostRepository import PostRepository


class AppProvider(Provider):
    def __init__(self, application) -> None:
        self.application = application

    def register(self) -> None:
        self.application.singleton('PostRepository', PostRepository)
        View.filter('truncatechars', self.truncatechars)

    @staticmethod
    def truncatechars(value: str) -> str:
        return value[:70] + '...' if value and len(value) > 70 else value

    def boot(self) -> None:
        pass
