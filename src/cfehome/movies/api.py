from typing import List, Optional
from django.shortcuts import get_object_or_404
from ninja import Router, Schema  # Ensure Schema is imported
from ninja_jwt.authentication import JWTAuth
from .models import MovieEntry
from .schemas import (
    MoviesListEntrySchema,
    MovieEntryDetailSchema,
    MovieUpdateSchema,
    DeleteResponseSchema,
)

router = Router()


# List all movies
@router.get("/", response=List[MoviesListEntrySchema], auth=JWTAuth())
def list_movies(request):
    movies = MovieEntry.objects.all()
    return [
        MoviesListEntrySchema(
            id=movie.id,
            title=movie.title,
            release_date=movie.release_date.isoformat(),  # Format date
            genre=movie.genre,
            average_rating=movie.average_rating(),  # Assuming this method exists
            movie_id=movie.id,
        )
        for movie in movies
    ]


# Get movie detail by ID
@router.get("/{movie_id}", response=MovieEntryDetailSchema, auth=JWTAuth())
def get_movie(request, movie_id: int):
    movie = get_object_or_404(MovieEntry, id=movie_id)
    return MovieEntryDetailSchema.from_orm(movie)


# Create a new movie
@router.post("/", response=MovieEntryDetailSchema, auth=JWTAuth())
def create_movie(request, data: MovieUpdateSchema):
    movie = MovieEntry(**data.dict())
    movie.save()
    return movie


# Update an existing movie by ID
@router.put("/{movie_id}", response=MovieEntryDetailSchema, auth=JWTAuth())
def update_movie(request, movie_id: int, data: MovieUpdateSchema):
    movie = get_object_or_404(MovieEntry, id=movie_id)
    for attr, value in data.dict(exclude_unset=True).items():
        setattr(movie, attr, value)
    movie.save()
    return movie


# Delete a movie by ID
@router.delete("/{movie_id}", response=DeleteResponseSchema, auth=JWTAuth())
def delete_movie(request, movie_id: int):
    movie = get_object_or_404(MovieEntry, id=movie_id)
    movie.delete()
    return {
        "status": "success",
        "message": "Movie deleted successfully.",
    }  # Return a dict for DeleteResponseSchema


# Movie Rating Schema
class MovieRatingSchema(Schema):
    username: str
    comment: Optional[str] = None
    score: float
