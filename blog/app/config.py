import os

basedir = os.path.abspath(os.path.dirname(__file__))

# SQLITE
# MYSQL, POSTGRES, SQL SERVER
class Config:
    POSTS_PER_PAGE = 25
    SECRET_KEY = os.environ.get("SECRET_KEY") or "voce-nunca-adivinhara"
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL"
    ) or "sqlite:///" + os.path.join(basedir, "app.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ADMINS = ["naorespoda.microblog@gmail.com"]
    SENDGRID_API_KEY = os.environ.get("SENDGRID_API_KEY")
