from qa import storage

built_in_type=['map']
third_party_service=['weather']

def get_answer(t,slots):
    if t in built_in_type:
        answer=storage.query(t,slots)
    elif t in third_party_service:
        answer='unknown'
    else:
        answer='unsupported type'

    if answer is None:
        answer='error'
    return answer


