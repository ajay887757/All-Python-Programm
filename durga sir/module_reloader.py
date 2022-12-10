from time import *
import module2
from imp import reload
module2.add(10,20)

sleep(10)
reload(module2)
module2.product(10,20)
