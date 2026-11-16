from typing import Any


def NULL_not_found(object: Any) -> int:
    if object is None:
        label = "Nothing"
    elif isinstance(object, float) and object != object:
        label = "Cheese"
    elif object is False:
        label = "Fake"
    elif object == 0:
        label = "Zero"
    elif object == "":
        label = "Empty"
    else:
        print("Type not Found")
        return 1

    separator = "" if object == "" else " "
    print(f"{label}: {object}{separator}{type(object)}")
    return 0
