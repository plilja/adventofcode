P = 20201227


def transform(subject, loop_size):
    x = 1
    for i in range(0, loop_size):
        x = (x * subject) % P
    return x


def get_loop_size(subject, public_key):
    x = 1
    for i in range(1, P + 1):
        x = (x * subject) % P
        if x == public_key:
            return i
    raise ValueError('Unable to break key')


def step1(card_public, door_public):
    door_loop_size = get_loop_size(7, door_public)
    return transform(card_public, door_loop_size)


card_public = int(input())
door_public = int(input())
print(step1(card_public, door_public))
# No step 2 this day
