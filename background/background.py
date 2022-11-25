import sys
sys.path.append("C:/Users/eorl6/Documents/golablur")
from diffusion import inpaint
class diffusion:
    def img(self,mask):
        model = inpaint.Image(mask)
        model.load()
        return "good"