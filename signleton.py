fichier_configuration = "configuration.ini"

class Singleton:
    _instance = None
    _initialized = False

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, database: dict):
        if not self._initialized:
            self.database = database
            Singleton._initialized = True  # Empêche la réinitialisation

try:
    database = {}

    with open(fichier_configuration, "r") as f:
        for ligne in f:
            ligne = ligne.strip()
            if ligne and "=" in ligne:
                cle, valeur = ligne.split("=", 1)
                database[cle.strip()] = valeur.strip()

    singleton = Singleton(database)
    print(singleton.database)

    singleton_2 = Singleton(database)
    print(singleton_2.database)
    singleton_2.database['db.password'] = '<PASSWORD>'

    print(singleton.database)

except FileNotFoundError:
    print(f"Le fichier {fichier_configuration} est introuvable.")
except Exception as e:
    print(f"Une erreur est survenue : {e}")