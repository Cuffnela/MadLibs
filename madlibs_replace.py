# The project generates a madlib using user input. Done using replace to practice
# inplementation of the replace method.

name = "Jerry"
place = "space"
noun1 = "camel"
noun2= "moutain"
verb1 = "climbed"
verb2 = "drove"
direction = "left"

madlib = ("NAME once went to PLACE to get some NOUN1. While NAME was on the "
"way to PLACE they VERB1 into a NOUN2. The NOUN2 VERB2 DIRECTION to let them "
"pass.")

madlib = madlib.replace("NAME", name)
madlib = madlib.replace("PLACE", place)
madlib = madlib.replace("NOUN1",noun1)
madlib = madlib.replace("NOUN2",noun2)
madlib = madlib.replace("VERB1",verb1)
madlib = madlib.replace("VERB2",verb2)
madlib = madlib.replace("DIRECTION",direction)

print madlib
