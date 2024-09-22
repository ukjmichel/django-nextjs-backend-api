from ninja import Schema
from datetime import date

class MovieEntryDetailSchema(Schema):
    id: int
    title: str
    author: str
    casting: str
    director: str
    release_date: date
    genre: str
    description: str
    trailer: str
    image: str  # URL or path to the image
    average_rating: float = 0.0  # To display the average rating of the movie


class MoviesListEntrySchema(Schema):
    id: int
    title: str
    release_date: date
    genre: str
    average_rating: float = (
        0.0  # Display only essential information like the average rating
    )


class MovieUpdateSchema(Schema):
    title: str = None
    author: str = None
    casting: str = None
    director: str = None
    release_date: date = None
    genre: str = None
    description: str = None
    trailer: str = None
    image: str = None  # Optional in case the image is not being updated


class MovieRatingSchema(Schema):
    username: str  # The name of the user submitting the rating
    comment: str  # The user's comment on the movie
    score: float  # The rating score (e.g., from 1 to 10)
