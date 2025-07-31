from abc import ABC
from enum import Enum


class Unite(Enum):
    MICROGRAMME = "micro-grammes"
    MILLIGRAMME = "milligrammes"
    GRAMME = "grammes"


class ElementValidator:
    @staticmethod
    def validate(attribut, valeur, types):
        if not isinstance(valeur, types):
            raise TypeError(f"Le champ '{attribut}' doit être de type : {types}.")


class Element(ABC):
    def __init__(self, nom: str, valeur: float, unite: Unite):
        ElementValidator.validate("nom", nom, str)
        ElementValidator.validate("valeur", valeur, (int, float))
        ElementValidator.validate("unite", unite, Unite)
        self.nom = nom
        self.valeur = valeur
        self.unite = unite

    def __str__(self):
        return f"{self.__class__.__name__}(nom={self.nom}, valeur={self.valeur}, unite={self.unite.name})"


class Ingredient(Element):
    def __str__(self):
        return f"Ingrédient : " + super().__str__()


class Additif(Element):
    def __str__(self):
        return f"Allergène : " + super().__str__()


class Allergene(Element):
    def __str__(self):
        return f"Additif : " + super().__str__()


class TypeElement(Enum):
    INGREDIENT = 1
    ADDITIF = 2
    ALLERGENE = 3
    AUTRES = 0


class ElementFactory:
    @staticmethod
    def creation_element(type_element: TypeElement, nom: str, valeur: float, unite: Unite) -> Element:
        if type_element == TypeElement.INGREDIENT:
            return Ingredient(nom, valeur, unite)
        elif type_element == TypeElement.ADDITIF:
            return Additif(nom, valeur, unite)
        elif type_element == TypeElement.ALLERGENE:
            return Allergene(nom, valeur, unite)
        else:
            raise ValueError("Erreur de catégorisation d'élément")


# Exemple de test de la factory
if __name__ == "__main__":
    recette_1 = ElementFactory.creation_element(TypeElement.ALLERGENE, "Curry", 10, Unite.MILLIGRAMME)
    recette_2 = ElementFactory.creation_element(TypeElement.INGREDIENT, "Piment", 20, Unite.MILLIGRAMME)
    recette_3 = ElementFactory.creation_element(TypeElement.ADDITIF, "E101", 50, Unite.MICROGRAMME)
    recette_4 = ElementFactory.creation_element(TypeElement.AUTRES, "sucre", 47, Unite.MICROGRAMME)

    print(recette_1)
    print(recette_2)
    print(recette_3)
    print(recette_4)
