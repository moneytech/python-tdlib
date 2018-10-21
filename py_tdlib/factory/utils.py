from simplejson import dumps
from .table import constructors as cs


def factorize(update):
    if isinstance(update, dict):
        c = update.get("@type")
        return cs[c](**update)

    if isinstance(update, list):
        return [*map(factorize, update)]

    return update


def list_passer(obj):
    result = []
    for x in obj:
        if isinstance(x, list):
            result.append(list_passer(x))

        elif hasattr(x, "to_dict"):
            result.append(x.to_dict())

        else:
            result.append(x)

    return result


class Obj:
    def to_dict(self):
        result = {"@type": type(self).__name__}

        for x in vars(self):
            attr = getattr(self, x)

            if hasattr(attr, "to_dict"):
                result[x] = attr.to_dict()

            elif isinstance(attr, list):
                result[x] = list_passer(attr)

            else:
                result[x] = attr

        return result

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            v = factorize(v)
            setattr(self, k, v)

    def __len__(self) -> int:
        return len(self.__str__())

    def __hash__(self):
        return hash(self.__str__())

    def __str__(self) -> str:
        return dumps(self.to_dict())


class Method(Obj):
    def run(self, client, wait = True):
        return client.send(self, wait)


class Type(Obj):
    pass
