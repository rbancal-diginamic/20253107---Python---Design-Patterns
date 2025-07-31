from factory import *


# Produit final
class Produit:
    def __init__(self):
        self.nom = None
        self.score_nutritionnel = None
        self.marque = None
        self.categorie = None
        self.ingredients = []
        self.additifs = []
        self.allergenes = []

    def __repr__(self):
        return (f"Produit(nom={self.nom}, marque={self.marque}, catégorie={self.categorie},\n"
                f"        ingrédients={self.ingredients},\n"
                f"        additifs={self.additifs},\n"
                f"        allergènes={self.allergenes},\n"
                f"        score_nutritionnel={self.score_nutritionnel})")


class ProductBuilder:
    def __init__(self):
        self._produit = Produit()

    def informations(self, nom: str, marque: str, categorie: str):
        self._produit.nom = nom
        self._produit.marque = marque
        self._produit.categorie = categorie
        return self

    def ingredient(self, nom: str, valeur: float, unite: Unite):
        self._produit.ingredients.append(Ingredient(nom, valeur, unite))
        return self

    def additif(self, nom: str, valeur: float, unite: Unite):
        self._produit.additifs.append(Additif(nom, valeur, unite))
        return self

    def allergene(self, nom: str, valeur: float, unite: Unite):
        self._produit.allergenes.append(Allergene(nom, valeur, unite))
        return self

    def score_nutrition(self, valeur: str):
        self._produit.score_nutritionnel = valeur
        return self

    def build(self):
        return self._produit


if __name__ == "__main__":
    builder = ProductBuilder()
    produit = (builder
        .informations("Plateau Maki et Sushi", "SushiKa", "Plat Japonais")
        .ingredient("Riz", 1200, Unite.GRAMME)
        .ingredient("Saumon", 500, Unite.GRAMME)
        .additif("E621", 5, Unite.MILLIGRAMME)
        .allergene("Iode", 10, Unite.MICROGRAMME)
        .score_nutrition("C")
        .build()
    )

    print(produit)