import json, os

path_ = "save"
sav = os.path.abspath("save//profile.json")


def savs():
    if not os.path.exists(path_):
        os.mkdir(path_)


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
    savs()
    profile = json.dumps({'name': name_profile, 'many': many_profile}, sort_keys=True, indent=4)
    save(profile)
