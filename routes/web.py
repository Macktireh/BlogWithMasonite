from masonite.routes import Route
from masonite.authentication import Auth


ROUTES = [
    Route.get("/", "HomeController@show").name("home"),
    Route.group(
        [
            Route.get("/create", "BlogController@show").name("blog"),
            Route.post("/create", "BlogController@store").name("blog.store"),
        ],
        prefix="blog",
        middleware=["auth", "web"],
    ),
]

ROUTES += Auth.routes()
