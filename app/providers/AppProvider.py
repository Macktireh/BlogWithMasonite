import re

from masonite.providers import Provider
from masonite.facades import View

from app.repositories.PostRepository import PostRepository


class AppProvider(Provider):
    def __init__(self, application) -> None:
        self.application = application

    def register(self) -> None:
        self.application.singleton('PostRepository', PostRepository)
        View.filter('truncatechars', self.truncatechars)
        View.filter('linebreaks', self.linebreaks)

    @staticmethod
    def truncatechars(value: str) -> str:
        return value[:70] + '...' if value and len(value) > 70 else value

    @staticmethod
    def linebreaks(value: str) -> str:
        paras = re.split("\n{2,}", str(value))
        paras = ["<p>%s</p>" % p.replace("\n", "<br>") for p in paras]
        return "\n\n".join(paras)

    def boot(self) -> None:
        pass
