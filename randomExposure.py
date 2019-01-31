import random

def getLights():

    lights = hou.selectedNodes()
    
    if not lights:
        hou.ui.displayMessage("PLEASE SELECT LIGHTS")
        
    for l in lights:
        if l.type().name() != "arnold_light":
            raise Exception(hou.ui.displayMessage("SELECT LIGHTS ONLY!"))
    return lights
        
def getMinMaxExp():  
    input_num = hou.ui.readMultiInput("Enter exposure min and max value", input_labels = ("min", "max"), buttons = ("OK", "Cancel"))
    choice = input_num[0]
    if choice == 0:
        value = input_num[1]
        try:
            min = float(value[0])
            max = float(value[1])
            if min>max:
                hou.ui.displayMessage("Mininmum value must be lower than maximum value!")
            else:
                return min, max
        except ValueError:
            hou.ui.displayMessage("Value is not a number!")
            pass
    
        
        
        
    else:
        pass
        print "skipped"
    
   



def setRandExposure(min, max):
    lights = getLights()
    for l in lights:
        exposure = round(random.uniform(min,max), 2)
        l.parm("ar_exposure").set(exposure)
    print lights
    print min
    print max
    
setRandExposure(*getMinMaxExp())
    
    