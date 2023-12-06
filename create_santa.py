from typing import List, Dict

import json
import random

NoneType = type(None)
Santa = Dict[str, str]


with open("participants.json") as f:
    _participants = json.load(f)
    PARTCIPANTS = list(map(lambda x: x.lower(), _participants.keys()))


with open("exceptions.json") as f:
    _exceptions = json.load(f)


EXCEPTIONS = {}
for key, value in _exceptions.items():
    key = key.lower()
    assert key in PARTCIPANTS
    if isinstance(value, str):
        value = [value]
    value = [name.lower() for name in value]
    assert set(value).issubset(set(PARTCIPANTS))
    EXCEPTIONS[key] = value


def choice(include: List[str], exclude: List[str]) -> str:
    choices = include.copy()
    for name in exclude:
        try:
            choices.remove(name)
        except ValueError:
            pass

    random.shuffle(choices)
    return choices[0]


def order_participant() -> List[str]:
    with_exce = sorted(list(EXCEPTIONS.keys()), reverse=True, key=lambda x: len(EXCEPTIONS[x]))
    no_exce = list(set(PARTCIPANTS) - set(with_exce))
    return with_exce + no_exce


def attribute() -> Santa:
    giver = order_participant()
    receiver = PARTCIPANTS.copy()
    santa = {}
    for name in giver:
        exception = EXCEPTIONS.get(name, [])
        exclude = [name] + exception
        to = choice(receiver, exclude)

        santa[name] = to
        receiver.remove(to)
    return santa


def check_pairs(santa: Santa) -> bool:
    for key, value in santa.items():
        if santa[value] == key:
            return True
    return False


def check_exceptions(santa: Santa) -> bool:
    for key, value in santa.items():
        if value in EXCEPTIONS.get(key, []):
            return True
    return False


def write_files(santa: Santa) -> NoneType:
    with open('message.txt') as f:
        message = f.read()

    for giver, receiver in santa.items():
        with open(f"packages/{giver}.txt", "w") as f:
            f.write(message.format(giver=giver.title(), receiver=receiver.title()))


if __name__ == '__main__':
    pairs = True
    exceptions = True
    i = 1
    while pairs | exceptions:
        print(f"{i} try")
        try:
            santa = attribute()
            pairs = check_pairs(santa)
            exceptions = check_exceptions(santa)
        except IndexError:
            pairs = True
            exceptions = True
        i += 1
        if i > 1500:
            print("Not OK with pairs restrictions")
            pairs = False

    write_files(santa)
    print("Files created :)")
