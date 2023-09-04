"""CreatePostsTable Migration."""

from masoniteorm.migrations import Migration


class CreatePostsTable(Migration):
    def up(self) -> None:
        """
        Run the migrations.
        """
        with self.schema.create("posts") as table:
            table.increments("id")
            table.string("title")
            table.text("body")
            table.integer("author_id")
            table.foreign("author_id").references("id").on("users")

            table.timestamps()

    def down(self) -> None:
        """
        Revert the migrations.
        """
        self.schema.drop("posts")
