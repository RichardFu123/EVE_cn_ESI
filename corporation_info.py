import request_factory


def corporation_info(corporation_id):
    r = request_factory.request_factory(corporation_id, "corporation_info")
    return r.get()


if __name__ == "__main__":
    print(corporation_info(98021437))
