import os
import cloudinary

DEBUG = os.environ.get('DEBUG', True)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SQLALCHEMY_DATABASE_URI=os.environ.get('SQLALCHEMY_DATABASE_URI',"sqlite:///"+ BASE_DIR + "/app.db")
SQLALCHEMY_TRACK_MODIFICATIONS=os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS',True)
CLOUDINARY_CLOUD_NAME=os.environ.get('CLOUDINARY_CLOUD_NAME',"djm")
CLOUDINARY_API_KEY=os.environ.get('CLOUDINARY_API_KEY',"181761581922274")
CLOUDINARY_API_SECRET=os.environ.get('CLOUDINARY_API_SECRET',"phjxEW7_P8DAzx1paVrDuSNQwqM")

SECURITY_REGISTERABLE = True
SECURITY_SEND_REGISTER_EMAIL = False
SECURITY_EMAIL_SENDER = "jabstarter"
SECURITY_PASSWORD_HASH = "pbkdf2_sha512"
SECURITY_PASSWORD_SALT = "D92oPsDk2mZs.Asd@"

SECRET_KEY = "_\xe3a[:\x81J\xda(\x11\x9e\xca~\xd0\x03\x10$x\xbf\x01\n\xe82\n"


cloudinary.config(
  cloud_name = CLOUDINARY_CLOUD_NAME,
  api_key = CLOUDINARY_API_KEY,
  api_secret = CLOUDINARY_API_SECRET
)