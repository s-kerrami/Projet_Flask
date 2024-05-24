SECRET_KEY = '(1^q4p)khgaklh^#l6*&yb_l=a=q^x$xr!w&9fr^5t'
SCHEME = "postgresql+psycopg2"
USERNAME = "postgres"
PASSWORD = "postgres"
HOSTNAME = "localhost"
PORT = "5432"
DATABASE_NAME = "demo_db"

URL_DB = f"{SCHEME}://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE_NAME}"
SQLALCHEMY_DATABASE_URI = URL_DB