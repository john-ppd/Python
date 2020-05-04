#from inheritance_chef1 import Chef1
import inheritance_chef1
#you put what you want to inherit inside class Chef2(in here)
class Chef2(inheritance_chef1.Chef1):
    def cook_rice(self):
        print("made rice")

    #because we want this shefs meat to be pork we will overwrite it
    def cook_meat(self):
        print("cooked pork")