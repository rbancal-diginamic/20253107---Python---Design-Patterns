from enum import Enum


class Unite(Enum):
    MICRO_GRAMMES = 1
    MILLI_GRAMMES = 2


class Element:
    def __init__(self, nom: str, valeur: float, unite: Unite):
        self.nom = nom
        self.valeur = valeur
        self.unite = unite

    def __str__(self):
        return f"{self.__class__.__name__}(nom={self.nom}, valeur={self.valeur}, unite={self.unite.name})"



class Ingredient(Element):
    pass


class Additif(Element):
    pass


class Allergene(Element):
    pass



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
    recette_1 = ElementFactory.creation_element(TypeElement.ALLERGENE, "Curry", 10, Unite.MILLI_GRAMMES)
    recette_2 = ElementFactory.creation_element(TypeElement.INGREDIENT, "Piment", 20, Unite.MILLI_GRAMMES)
    recette_3 = ElementFactory.creation_element(TypeElement.ADDITIF, "E101", 50, Unite.MICRO_GRAMMES)
    recette_4 = ElementFactory.creation_element(TypeElement.AUTRES, "sucre", 47, Unite.MICRO_GRAMMES)

    print(recette_1)
    print(recette_2)
    print(recette_3)
    print(recette_4)
