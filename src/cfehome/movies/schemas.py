from typing import List, Optional
from ninja import Schema
from datetime import date


class MoviesListEntrySchema(Schema):
    id: int
    title: str
    release_date: str  # Use str to format date
    genre: str
    average_rating: float
    movie_id: int


class MovieEntryDetailSchema(Schema):
    id: int
    title: str
    author: str
    casting: str
    director: str
    release_date: str  # Adjust as needed (e.g., use ISO format)
    genre: str
    description: str
    trailer: str
    image: Optional[str] = None  # Image field is optional
    average_rating: float = 0.0  # Default average rating


class MovieUpdateSchema(Schema):
    title: Optional[str] = None
    author: Optional[str] = None
    casting: Optional[str] = None
    director: Optional[str] = None
    release_date: Optional[str] = None  # Adjust as needed
    genre: Optional[str] = None
    description: Optional[str] = None
    trailer: Optional[str] = None
    image: Optional[str] = None


class DeleteResponseSchema(Schema):
    status: str
    message: str


class MovieRatingSchema(Schema):
    username: str  # The name of the user submitting the rating
    comment: Optional[str] = None  # The user's comment on the movie (optional)
    score: float  # The rating score (e.g., from 1 to 10)
