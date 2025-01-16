from ursina import*
from perlin_noise import PerlinNoise
from random import randint
class Block(Button):
    def __init__(self,block_type,pos, **kwargs):
        super().__init__(
            parent=scene, #батькіський обєкт - сцена гри
            model='cube', #модель куба
            texture='grass', #текстура трави
            position=pos, #корди обєкта
            scale=1, #розмір
            collider='box', #зіткення з гравцем
            orogin_y=0.5, #рівень землі
            color=color.color(0,0, random.uniform(0.9, 1)),
            shader='basic_lighting_shader',
            **kwargs
        )


class Map(Entity):
    def __init__(self, **kwargs):
        super().__init__(model=None, colider=None, **kwargs)
        self.bedrock = Entity(model='plane', collider='box', scale=100, texture='grass', texture_scale=(4,4), position=(0,-2,0))
        self.blocks = {}
        self.noise = PerlinNoise(octaves=3, seed=4255)



    def new_map(self):
        for x in range(50):
            for z in range(50):
                
                y = floor(self.noise([x/24, z/24])*6)
                block = Block(0,(x, y ,z))