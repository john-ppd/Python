#inheritance allows you to have one class inherit another classes functions, we will use chef1 and chef2 classes for this example

import inheritance_chef1
import inheritance_chef2
#forgot to include () in .chef1()
mychef1 = inheritance_chef1.Chef1()
mychef1.cook_fish()

mychef2 = inheritance_chef2.Chef2()
mychef2.cook_rice()
mychef2.cook_fish()

