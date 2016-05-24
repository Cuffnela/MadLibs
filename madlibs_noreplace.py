#This project generates a Madlib based on input. Done with out using replace
#to practice find and string indexing.

#Input values
propernoun1 = "Jerry"
place1 = "carnival"
pluralnoun1 = "coconuts"
verb1 = "drove"
noun1 = "pizza"




#creates madlib
madlib = ("PROPERNOUN1 went to the PLACE1 to get some PLURALNOUN1. "
"While PROPERNOUN1 was at the PLACE1 they VERB1 into a NOUN1.")

#find all replacement indicies
first_propernoun1_start=madlib.find("PROPERNOUN1")
first_propernoun1_end= first_propernoun1_start + len("PROPERNOUN1")
first_place1_start=madlib.find("PLACE1")
first_place1_end = first_place1_start + len("PLACE1")
pluralnoun1_start = madlib.find("PLURALNOUN1")
pluralnoun1_end = pluralnoun1_start + len("PLURALNOUN1")
second_propernoun1_start = madlib.find("PROPERNOUN1",first_propernoun1_end)
second_propernoun1_end = second_propernoun1_start + len("PROPERNOUN1")
second_place1_start=madlib.find("PLACE1",first_place1_end)
second_place1_end = second_place1_start + len("PLACE1")
verb1_start = madlib.find("VERB1")
verb1_end = verb1_start +  len("VERB1")
noun1_start = madlib.find(" NOUN1")
noun1_end = noun1_start + len(" NOUN1")

#create all substrings
substring1 = madlib[:first_propernoun1_start]
substring2 = madlib[first_propernoun1_end:first_place1_start]
substring3 = madlib[first_place1_end:pluralnoun1_start]
substring4 = madlib[pluralnoun1_end:second_propernoun1_start]
substring5 = madlib[second_propernoun1_end:second_place1_start]
substring6 = madlib[second_place1_end:verb1_start]
substring7 = madlib[verb1_end:noun1_start]+ " "
substring8 = madlib[noun1_end:]


print (substring1 + propernoun1 + substring2 + place1 + substring3 + pluralnoun1
+ substring4 + propernoun1 + substring5 + place1 + substring6 + verb1 + substring7
+ noun1 + substring8)
