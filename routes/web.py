from masonite.routes import Route
from masonite.authentication import Auth


ROUTES = [
    Route.get("/", "HomeController@show").name("home"),
    Route.group(
        [
            Route.get("/create", "BlogController@show").name("blog"),
            Route.post("/create", "BlogController@store").name("blog.store"),
            Route.get("/@id", "BlogController@single").name("blog.single"),
            Route.get("/update/form/@id", "BlogController@updateForm").name("blog.update.form"),
            Route.post("/update/@id", "BlogController@update").name("blog.update"),
            Route.get("/delete/@id", "BlogController@delete").name("blog.delete"),
        ],
        prefix="blog",
        middleware=["auth", "web"],
    ),
]

ROUTES += Auth.routes()
