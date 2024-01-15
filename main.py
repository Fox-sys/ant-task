from ant import Ant
from field import Field
from PIL import Image
import numpy as np


field = Field(1024)
ant = Ant(512, 512, field)

while ant.step():
    ...


image = Image.fromarray((field.get_field()) * 255)
image.save('ant_path.png')
print(np.sum(1 - field.get_field()))
