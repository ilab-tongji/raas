from db import conn


def query(t, slots):
    cursor = conn[t].find_one(slots)
    if cursor is None:
        return None
    return cursor['answer']


def save(t, slots, answer):
    slots['answer'] = answer
    conn[t].insert_one(slots)


if __name__ == '__main__':
    print query('map', {'location': 'toilet'})

