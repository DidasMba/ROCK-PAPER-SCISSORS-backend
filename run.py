from app import app, db

# Importez vos modèles ici, si nécessaire
from app.models import User

if __name__ == '__main__':
    # Créez les tables de la base de données si elles n'existent pas encore
    with app.app_context():
        db.create_all()

    # Lancer l'application Flask
    app.run(debug=True)
