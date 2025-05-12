def get_num_words(text):
    return len(text.split())


def get_character_count(text):
    character_dict = {}
    for character in text.lower():
        if character in character_dict:
            character_dict[character] += 1
        else:
            character_dict[character] = 1
    return character_dict


def sort_by_count(dict):
    return dict["num"]


def sort_dictonary_by_count(character_dict):
    characters = []
    for dict in character_dict:
        characters.append({"char": dict, "num": character_dict[dict]})
    characters.sort(key=sort_by_count, reverse=True)
    return characters
