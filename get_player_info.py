import ESI_base


def get_character_id(name):
    try:
        https = ESI_base.latest_address + ESI_base.character_id(name)
        result = ESI_base.request(https)
        return result["character"][0]
    except Exception:
        print("can not get character id")


def get_character_info(character_id):
    try:
        https = ESI_base.latest_address + ESI_base.character_info(character_id)
        result = ESI_base.request(https)
        return result
    except Exception:
        print("can not get character info")


if __name__ == "__main__":
    print(get_character_id("军用馒头"))
    print(get_character_info(get_character_id("军用馒头")))
