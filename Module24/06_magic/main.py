class Water:
    def __add__(self, other):
        if isinstance(other,Air):
            return Shtorm()
        elif isinstance(other,Earth):
            return Dirt()
        elif isinstance(other,Fire):
            return Steam()
        return None

class Air:
    def __add__(self, other):
        if isinstance(other,Fire):
            return Lightning
        elif isinstance(other,Earth):
            return Dust()
        elif isinstance(other,Water):
            return Shtorm()
        return None
class Earth:
    def __add__(self, other):
        if isinstance(other,Water):
            return Dirt()
        if isinstance(other,Fire):
            return Lava()
        elif isinstance(other,Air):
            return Dust
        return None
class Fire:
    def __add__(self, other):
        if isinstance(other,Water):
            return Steam()
        elif isinstance(other,Air):
            return Lightning()
        elif isinstance(other,Earth):
            return Lava()
        return None


class Shtorm:
    title = 'Шторм'
class Steam:
    title = 'Пар'
class Dirt:
    title = 'Грязь'
class Lightning:
    title = 'Молния'
class Dust:
    title = 'Пыль'
class Lava:
    title = 'Лава'

a = Air()
b = Fire()
c=a+b
print(c.title)