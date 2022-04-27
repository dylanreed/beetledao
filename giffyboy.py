import os
import imageio
from pygifsicle import optimize

png_dir = 'images'
images = []
for file_name in sorted(os.listdir(png_dir)):
    if file_name.endswith('.png'):
        file_path = os.path.join(png_dir, file_name)
        images.append(imageio.imread(file_path))
imageio.mimsave('gif/movie.gif', images)

optimize('gif/movie.gif')