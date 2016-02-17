import json, os

sav = os.path.abspath("profile.json")

def save(profile):
    """Эта функция сохраняет профиль
    :param profile:
    """
    f = open(sav, 'w')
    f.write(profile)
    f.close()

def load():
    """Эта функция загружает профиль"""
    try:
        with open(sav) as p:
            return json.load(p)
    except:
        pass

def create(name_profile, many_profile):
    """Эта функция создает профиль профиль
    :param many_profile:
    :param name_profile:
    """
    profile = json.dumps({'name': name_profile, 'many': many_profile}, sort_keys=True, indent=4)
    save(profile)
