# Define fields of input or output data
from .extensions import api
from flask_restx import fields


# user register data format
user_input_model = api.model("BookswapUser", {
    # "id": fields.Integer,
    "username": fields.String,
    "email": fields.String,
    "password": fields.String,
})

# all username / email data format
username_model = api.model("BookswapUserName", {
    "username": fields.String,
    "email": fields.String,
})

# login data format
user_login_model = api.model("BookswapUserLogin", {
    "email": fields.String,
    "password": fields.String,
})

# jwt token format
jwt_token_model = api.model("JWTToken", {
    "access_token": fields.String,
    "token_type": fields.String,
})
