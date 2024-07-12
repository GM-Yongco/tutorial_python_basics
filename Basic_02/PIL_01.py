# Description     : Code that will impress u ;)
# Author          : NxM Jules
# Date            : ur my date uwu
# HEAD ----------------------------------------------------------
from PIL import Image

# MAIN ----------------------------------------------------------
print("~~~~~~~~~~~~~~~~~~Layer - START~~~~~~~~~~~~~~~~~~\n")

BackGround = Image.open("00_References/NoSlash.png")
Todo = Image.open("00_References/SC_22-12-02.png")

area = (0, 0, 600, 1350)

BackGround1 = BackGround.crop((area))
BackGround1 = BackGround1.convert('RGBA')
Todo = Todo.convert('RGBA')

intermediate = Image.alpha_composite(BackGround1, Todo)

intermediate.save("00_References/Combined2.png")

print("\n~~~~~~~~~~~~~~~~~~~~END~~~~~~~~~~~~~~~~~~~~")

# REFERENCES ----------------------------------------------------
# https://stackoverflow.com/questions/33831572/get-image-mode-pil-python
# https://www.youtube.com/watch?v=hvy9msjJdMs
# https://www.youtube.com/watch?v=uR50xQX27-g
