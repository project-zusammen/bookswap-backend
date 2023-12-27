from flask_restx import Resource, Namespace
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

from .extensions import db
from .api_data_models import user_input_model, username_model, user_login_model, jwt_token_model
from .models import BookswapUser


ns = Namespace("api")


@ns.route("/")
class Index(Resource):
    def get(self):
        return {"Hello": "Bookswap"}

# return all registered username


@ns.route("/all-users")
class AllUsers(Resource):
    @ns.marshal_list_with(username_model, code=200)
    def get(self):
        return BookswapUser.query.all()


# user registration
@ns.route("/register")
class Register(Resource):
    @ns.expect(user_input_model)
    @ns.marshal_with(username_model, code=201)
    def post(self):
        # save user info in database
        try:
            # validating email
            user_email = ns.payload["email"]
            if "@" not in user_email or "." not in user_email:
                raise ValueError("Invalid email format")

            hashed_user_password = generate_password_hash(
                ns.payload["password"], method='pbkdf2')
            new_user = BookswapUser(
                username=ns.payload["username"],
                email=user_email,
                password=hashed_user_password)
            db.session.add(new_user)
            db.session.commit()

            return new_user, 201

        except Exception as e:
            # Handle specific exception for duplicate username, assuming you have one
            if "unique constraint" in str(e).lower():
                ns.abort(409, "Username already exists")
                # return {"Failed": "Username already exists"}, 409  # Conflict
            else:
                # Internal Server Error
                ns.abort(409, e)
                # return {"Failed": "Unknown error"}, 500


@ns.route("/login")
class Login(Resource):
    @ns.expect(user_login_model)
    @ns.marshal_with(jwt_token_model, code=200)
    def post(self):
        try:
            user_email = ns.payload["email"]
            user_password = ns.payload["password"]

            # get user data from database
            user = BookswapUser.query.filter_by(email=user_email).first()

            if user and check_password_hash(user.password, user_password):
                # password correct give access token
                access_token = create_access_token(identity=user.id)
                login_auth = {"access_token": access_token,
                              "token_type": "Bearer"}
                return login_auth, 200
            else:
                # Invalid credentials
                ns.abort(401, "Invalid email or password")

        except Exception as e:
            ns.abort(500, f"Unknown error {e}")

# dummy route to test access token


@ns.route("/protected")
class ProtectedResource(Resource):
    @jwt_required()
    @ns.marshal_with(username_model, code=200)
    def get(self):
        # Access the identity of the current user with get_jwt_identity
        current_user = get_jwt_identity()
        user = BookswapUser.query.get(current_user)

        return user, 200
