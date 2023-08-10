import shaders
from obj import Obj
from gl import Renderer

width = 960    
height = 540   

rend = Renderer(width, height)


rend.vertexShader = shaders.vertexShader
rend.fragmentShader = shaders.fragmentShader

rend.glLookAt(camPos=(0, 0,0),
              eyePos=(0, 0, -5))

 

rend.glLoadModel(filename = "model.obj",              
                 textureName = "model.bmp",           
                 translate = (0,0,-5),                
                 rotate = (0,0,35),                    
                 scale = (1.5,1.5,1.5))


rend.glRender()

rend.glFinish("output3.bmp")
