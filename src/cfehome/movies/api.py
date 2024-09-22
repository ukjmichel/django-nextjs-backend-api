from ninja import Router
from django.shortcuts import get_object_or_404
from .models import MovieEntry, Rating
from .schemas import (
    MovieEntryDetailSchema,
    MoviesListEntrySchema,
    MovieUpdateSchema,
    MovieRatingSchema,
)
from ninja_jwt.authentication import JWTAuth

router = Router()


@router.get("/", response=list[MoviesListEntrySchema], auth=JWTAuth())
def list_movies(request):
    movies = MovieEntry.objects.all()
    return [
        MoviesListEntrySchema(
            id=movie.id,
            title=movie.title,
            release_date=movie.release_date,
            genre=movie.genre,
            average_rating=movie.average_rating(),  # Assuming you have a method to calculate average rating
        )
        for movie in movies
    ]


@router.post("/", response=MovieEntryDetailSchema, auth=JWTAuth())
def add_movie(request, payload: MovieEntryDetailSchema):
    movie = MovieEntry.objects.create(**payload.dict())
    return movie


@router.get("/{movie_id}", response=MovieEntryDetailSchema)
def get_movie(request, movie_id: int):
    movie = get_object_or_404(MovieEntry, id=movie_id)
    return movie


@router.put("/{movie_id}", response=MovieEntryDetailSchema, auth=JWTAuth())
def update_movie(request, movie_id: int, payload: MovieUpdateSchema):
    movie = get_object_or_404(MovieEntry, id=movie_id)
    for attr, value in payload.dict().items():
        if value is not None:
            setattr(movie, attr, value)
    movie.save()
    return movie


@router.delete("/{movie_id}", response={204: None}, auth=JWTAuth())
def delete_movie(request, movie_id: int):
    movie = get_object_or_404(MovieEntry, id=movie_id)
    movie.delete()
    return 204  # No content


@router.post("/{movie_id}/rate", response=MovieRatingSchema, auth=JWTAuth())
def add_rating(request, movie_id: int, payload: MovieRatingSchema):
    movie = get_object_or_404(MovieEntry, id=movie_id)

    # Create a new rating entry in the database
    rating = Rating.objects.create(
        movie=movie,
        user=request.user,  # Assuming the user is authenticated
        comment=payload.comment,
        score=payload.score,
    )

    return {
        "username": request.user.username,
        "comment": rating.comment,
        "score": rating.score,
    }


@router.get("/movies/{movie_id}/ratings", response=list[MovieRatingSchema])
def get_ratings(request, movie_id: int):
    movie = get_object_or_404(MovieEntry, id=movie_id)
    ratings = (
        movie.ratings.all()
    )  # Assuming you have a related name set up in your Rating model
    return [
        MovieRatingSchema(
            username=rating.user.username, comment=rating.comment, score=rating.score
        )
        for rating in ratings
    ]
