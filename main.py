from ursina import*
from ursina.prefabs.first_person_controller import FirstPersonController
app = Ursina()
sky = Sky(texture='sky_sunset')
ground = Entity(model='plane', collider='box', scale=100, texture='grass', texture_scale=(4,4), position=(0,-2,0))
player = FirstPersonController()
class 

block = Entity(model='cube', texture='grass', position=(0,0,0), scale=2, rotation=(0,45,0))
block2 = Entity(model='cube', texture='grass', position=(2,0,0))
block2 = Entity(model='cube', texture='grass', position=(2,2,0))
block4 = Entity(model='cube', texture='grass', position=(2,2,2))
block.x = -1.4


#EditorCamera()

app.run()

