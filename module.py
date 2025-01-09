from ursina import*

class Blocks(Button):
    def __init__(self,block_type,pos, **kwargs):
        super().__init__(
            parent=scene, #батькіський обєкт - сцена гри
            model='cube' #модель куба
            texture='grass' #текстура трави
            position=pos, #корди обєкта
            scale=1, #розмір
            collider='box', #зіткення з гравцем
            orogin_y=0.5, #рівень землі
            color=color.color(0,0, random.uniform(0.9, 1))
            **kwargs
        )
