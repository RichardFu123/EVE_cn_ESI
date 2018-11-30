import requests


base_address = "https://esi.evepc.163.com/"
latest_address = base_address + "latest/"
dev_address = base_address + "dev/"
legacy_address = base_address + "legacy/"


def character_id(name):
    return f"search/?categories=character&datasource=serenity&language=zh&search={name}&strict=true"


def character_info(character_id):
    return f"characters/{character_id}/?datasource=serenity"


def request(address):
    try:
        r = requests.get(address)
        if r.status_code != 200:
            print("request error")
            raise Exception
        result = eval(r.text)
        r.close()
        return result

    except Exception:
        print("can not get character id")
