#!/usr/bin/env python
# -*- coding: utf-8 -*-


def order(values: list = None) -> list:
    if values is None:
        values = [input("Entrez un entier, float ou str: ") for _ in range(10)]

    return sorted(values)


def count_letter_occurences(word: str) -> dict:
    occurences = {}
    for c in word:
        if c in occurences:
            occurences[c] += 1
        else:
            occurences[c] = 1

    return occurences


def anagrams(words: list = None) -> bool:
    if words is None:
        words = [input("Entrez un mot: ") for _ in range(2)]

    assert len(words) == 2, "There should be 2 words in the list"
    return count_letter_occurences(words[0]) == count_letter_occurences(words[1])


def contains_doubles(items: list) -> bool:
    return len(items) != len(set(items))


def best_grades(student_grades: dict) -> dict:
    assert student_grades != {}, "No students in the dict"

    best_student = None
    best_average = 0.0
    for k, v in student_grades.items():
        average = sum(v) / len(v)
        if average > best_average:
            best_average = average
            best_student = k

    return {best_student: best_average}


def frequence(sentence: str) -> dict:
    return count_letter_occurences(sentence)


recipes = {}


def get_recipes() -> None:
    recipe_name = input("Le nom de la recette: ")
    ingredients = input(
        "Les ingrédients de la recette, séparé par des espaces: "
    ).split()

    global recipes
    recipes[recipe_name] = ingredients


def print_recipe(ingredients) -> None:
    recipe_name = input("Le nom de la recette: ")

    global recipes
    ingredients = recipes.get(recipe_name, None)
    if ingredients is None:
        print("There is no recipe")
    else:
        print(" ".join(ingredients))


def main() -> None:
    print(f"On essaie d'ordonner les valeurs...")
    order()

    print(f"On vérifie les anagrammes...")
    anagrams()

    my_list = [3, 3, 5, 6, 1, 1]
    print(f"Ma liste contient-elle des doublons? {contains_doubles(my_list)}")

    grades = {"Bob": [90, 65, 20], "Alice": [85, 75, 83]}
    best_student = best_grades(grades)
    print(
        f"{list(best_student.keys())[0]} a la meilleure moyenne: {list(best_student.values())[0]}"
    )

    sentence = (
        "bonjour, je suis une phrase. je suis compose de beaucoup de lettre. oui oui"
    )
    frequence(sentence)

    print("On enregistre les recettes...")
    recipes = get_recipes()

    print("On affiche une recette au choix...")
    print_recipe(recipes)


if __name__ == "__main__":
    main()
