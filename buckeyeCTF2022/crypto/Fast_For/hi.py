from PIL import Image
import numpy as np
x = np.asarray(Image.open("IMG.png"))
print(np.fft.fftn(x))
print(np.std(np.fft.fftn(x)))
