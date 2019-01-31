def getLights():

    lights = hou.selectedNodes()
    
    if not lights:
        hou.ui.displayMessage("PLEASE SELECT LIGHTS")
        
    for l in lights:
        if l.type().name() != "arnold_light":
            raise Exception(hou.ui.displayMessage("SELECT LIGHTS ONLY!"))
    return lights
    
def chooseState():

    user_selection = hou.ui.displayMessage("Select operation", buttons = ("Turn On", "Turn Off", "Switch"))
    return user_selection
    
def setIntensity(state):
    lights = getLights()
    if state == 0:
        for l in lights:
            l.parm("ar_intensity").set(1)
    if state == 1:
        for l in lights:
            l.parm("ar_intensity").set(0)
    if state == 2:
        for l in lights:
            value = l.parm("ar_intensity").eval()
            if value != 0:
                l.parm("ar_intensity").set(0)
            else:
                l.parm("ar_intensity").set(1)

state = chooseState()
setIntensity(state)