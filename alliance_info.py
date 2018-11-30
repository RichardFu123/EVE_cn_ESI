import request_factory


def alliance_info(alliance_id):
    r = request_factory.request_factory(alliance_id, "alliance_info")
    return r.get()


if __name__ == "__main__":
    print(alliance_info(403524217))
