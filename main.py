from ursina import*
from ursina.prefabs.first_person_controller import FirstPersonController

from ursina.shaders import basic_lighting_shader



app = Ursina()      
from module import*
sky = Sky(texture='sky_sunset')
map = Map()
#map.new_map(size=30)
map.load()


# block = Entity(model='cube', texture='grass', position=(0,0,0), scale=2, rotation=(0,45,0))
# block2 = Entity(model='cube', texture='grass', position=(2,0,0))
# block2 = Entity(model='cube', texture='grass', position=(2,2,0))
# block4 = Entity(model='cube', texture='grass', position=(2,2,2))
# block.x = -1.4


#EditorCamera()

app.run()

