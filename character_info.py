import request_factory


def get_character_id(name):
    r = request_factory.request_factory(name, "character_id")
    return r.get()["character"][0]


def get_character_info(character_id):
    r = request_factory.request_factory(character_id, "character_info")
    return r.get()


if __name__ == "__main__":
    print(get_character_id("军用馒头"))
    print(get_character_info(get_character_id("军用馒头")))
