from ursina import*
from ursina.prefabs.first_person_controller import FirstPersonController

from ursina.shaders import basic_lighting_shader



app = Ursina()      
from module import*
sky = Sky(texture='assets/blocks/bone_block_side.png')
map = Map()
try:
    map.load()
except:
    map.new_map(size=30)
    map.player.y = (0,3,0)

#window.fullscreen = True
map.load()




app.run()

