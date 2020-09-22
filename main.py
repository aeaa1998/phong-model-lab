from lib import *
from sphere import *
from math import pi, tan
from ray import *
platinumPlaastic = Material(diffuse=color(229, 228, 226), albedo=(0.4, 0.1, 0.05, 0), spec=380)
redPlastic = Material(diffuse=color(80, 0, 0), albedo=(0.9, 0.2, 0.05, 0.05, 0), spec=380)
whiteBearFur = Material(diffuse=color(255,255,255), albedo=(1, 0, 0,0), spec=5)
voidBlack = Material(diffuse=color(0,0,0), albedo=(0.1, 1, 0,0), spec=5)
darkBFur = Material(diffuse=color(103,52,8), albedo=(1, 0, 0,0), spec=500)
lightFur = Material(diffuse=color(192,116,18), albedo=(0.6, 0, 0,0), spec=500)
r = Raytracer(1000, 1000)

r.light = Light(
  position=V3(5, -8, 50),
  intensity=2.5
)

r.background_color = color(222, 222, 222)

r.scene = [
  #lE
Sphere(V3(-2.2, 1, -6), 0.35, whiteBearFur),
  #rE
Sphere(V3(-0.7, 1, -6), 0.35, whiteBearFur),
  #head
Sphere(V3(-1.5, 0.4, -6), 0.85, whiteBearFur),
  #nose
Sphere(V3(-1.25, 0, -5.3), 0.3, whiteBearFur),
  #nose black
Sphere(V3(-1.15, 0, -5), 0.07, voidBlack),
  #right eye
Sphere(V3(-0.9, 0.4, -5), 0.07, voidBlack),
  #left eye
Sphere(V3(-1.5, 0.4, -5), 0.07, voidBlack),
  #body
  Sphere(V3(-2.5, -1.3, -10), 1.7, platinumPlaastic),
#leftArm
Sphere(V3(-3.7, -0.5, -8.5), 0.55, whiteBearFur),
#leftLeg
Sphere(V3(-3.7, -2.3, -8.5), 0.55, whiteBearFur),
#rightArm
Sphere(V3(-1, -0.5, -9), 0.6, whiteBearFur),
#rightLeg
Sphere(V3(-1, -2.3, -9), 0.6, whiteBearFur),


  #lE
Sphere(V3(0.9, 1, -6), 0.35, darkBFur),
  #rE
Sphere(V3(2.4, 1, -6), 0.35, darkBFur),
  #head
Sphere(V3(1.6, 0.4, -6), 0.85, lightFur),
  #nose
Sphere(V3(1.35, 0, -5.3), 0.3, darkBFur),
  #nose black
Sphere(V3(1.25, 0, -5), 0.07, voidBlack),
  #right eye
Sphere(V3(1.5, 0.4, -5), 0.07, voidBlack),
  #left eye
Sphere(V3(1, 0.4, -5), 0.07, voidBlack),
#body
  Sphere(V3(2.5, -1.5, -10), 1.7, redPlastic),
#leftArm
Sphere(V3(0.95, -0.5, -9), 0.6, lightFur),
#leftLeg
Sphere(V3(0.95, -2.3, -9), 0.6, lightFur),
#right
Sphere(V3(3.7, -0.5, -9), 0.6, lightFur),
#rightLeg
Sphere(V3(3.7, -2.3, -9), 0.6, lightFur),

]
r.render()
r.write('out.bmp')