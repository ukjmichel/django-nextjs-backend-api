import os
from ninja import NinjaAPI, Schema
from ninja_extra import NinjaExtraAPI
from ninja_jwt.authentication import JWTAuth
from ninja_jwt.controller import NinjaJWTDefaultController

# Initialize the NinjaExtraAPI and register JWT controller
api = NinjaExtraAPI()
api.register_controllers(NinjaJWTDefaultController)
api.add_router("/waitlists/", "waitlists.api.router")


class UserSchema(Schema):
    username: str
    is_authenticated: bool
    email: str = None


@api.get("/hello")
def hello(request):
    print(request)
    return {"message": "Hello World"}


@api.get("/me", response=UserSchema, auth=JWTAuth())
def me(request):
    # Construct the response data manually
    user_data = {
        "username": request.user.username,
        "is_authenticated": request.user.is_authenticated,
        "email": getattr(request.user, "email", None),
    }
    print("User Data:", user_data)  # Add this line for debugging
    return user_data
