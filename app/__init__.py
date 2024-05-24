from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from app.models.db.db_model import Base, User
from config import SECRET_KEY, URL_DB
from flask_wtf.csrf import CSRFProtect
from sqlalchemy.exc import SQLAlchemyError

# Inititalisation de l'application Flask
app = Flask(__name__)

# mise en place du jeton d'accès (formulaire)
app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = URL_DB
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Configuration de flask-login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

# Inititialisation de CSRFProtect pour la protection contre les attaques CSRF
csrf = CSRFProtect(app)

# Définir la variable pour vérifier la connexion a la base de donnée
db_connected = False

# Esssayer de se connecter à la base de donnée
try:
    # Inititialisation de SQLAlchemy avec l'application Flask
    db = SQLAlchemy(app)
    
    # Céation d'un moteur de de basse de donnée SQLAlchemy à partir de L'url de la base de donnée
    engine = create_engine(URL_DB)
    
    # Récupération des métadonnée de la base de données à partir du modèle de donnée Base
    metadata = Base.metadata
    
    db_connected = True
except SQLAlchemyError as error:
    # En cas d'erreur SQLAlchemy, affichage du message d'erreur 
    print(f"Erreur de connexion à la base de données : \n {error}")


if db_connected:
    # Suppresion de la db
    # metadata.drop_all(bind=engine)
    # metadata.create_all(bind=engine)
    
    # Ajouter l'import des routes
    from app.routes import other, task, user, auth
    
    print("----------------------")
    print("Connexion db établie !")
    print("----------------------")