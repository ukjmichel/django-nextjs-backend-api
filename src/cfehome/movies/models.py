from django.db import models
from django.contrib.auth.models import (
    User,
)  # Assuming you're using Django's built-in User model


class MovieEntry(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    casting = models.TextField()
    director = models.CharField(max_length=255)
    release_date = models.DateField()
    genre = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="movie_images/")
    trailer = models.URLField()
    movie_id = models.CharField(max_length=255, unique=True)

    class Meta:
        db_table = "movie_entry"
        managed = True
        indexes = [
            models.Index(
                fields=[
                    "title",
                    "author",
                    "casting",
                    "director",
                    "release_date",
                    "genre",
                    "description",
                    "image",
                    "trailer",
                    "movie_id",
                ]
            ),
        ]

    def __str__(self):
        return self.title

    def average_rating(self):
        ratings = self.ratings.all()  # Get all ratings related to this movie
        if ratings.exists():
            total_score = sum(rating.score for rating in ratings)
            return total_score / ratings.count()  # Calculate the average score
        return 0  # Return 0 if no ratings are available


class Rating(models.Model):
    movie = models.ForeignKey(
        "MovieEntry", related_name="ratings", on_delete=models.CASCADE
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    score = models.FloatField()
    created_at = models.DateTimeField(
        auto_now_add=True
    )  # This will automatically set the timestamp on creation

    def __str__(self):
        return f"{self.user.username} rated {self.movie.title}: {self.score}"
