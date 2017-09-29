from qa import storage,weather

built_in_type=['map']
third_party_service=['weather']



def get_answer(t,slots):
    if t in built_in_type:
        answer=storage.query(t,slots)
    elif t in third_party_service:
        answer= thrid_party_map[t](slots)
    else:
        answer='unsupported type'

    if answer is None:
        answer='error'
    return answer


def get_weather(slots):
    data=weather.today_weather(slots['city'],slots['day'])

    if data is None:
        answer='error'
    else:
        answer=data['weather']

    return answer


thrid_party_map = {
    'weather': get_weather
}



