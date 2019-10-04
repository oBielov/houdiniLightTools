def getAllLights():
    allnodes = hou.node("/").allSubChildren()
    lights = [x for x in allnodes if x.type().name()=="arnold_light"]
    return lights

def getLights():

   lights = hou.selectedNodes()

   if not lights:
       hou.ui.displayMessage("PLEASE SELECT LIGHTS")

   for l in lights:
       if l.type().name() != "arnold_light":
           raise Exception(hou.ui.displayMessage("SELECT LIGHTS ONLY!"))
   return lights

def chooseState():

   user_selection = hou.ui.displayMessage("Select operation",close_choice = 5, title = "Light Switcher", buttons = ("Turn On", "Turn Off", "Switch", "Turn all off", "Turn all on" , "Close"))
   return user_selection

def setIntensity(state):
   
   if state == 0:
       lights = getLights()
       for l in lights:
           l.parm("ar_intensity").set(1)
   if state == 1:
       lights = getLights()
       for l in lights:
           l.parm("ar_intensity").set(0)
   if state == 2:
       lights = getLights()
       for l in lights:
           value = l.parm("ar_intensity").eval()
           if value != 0:
               l.parm("ar_intensity").set(0)
           else:
               l.parm("ar_intensity").set(1)
   if state == 3:
        lights = getAllLights()
        for l in lights:
            if l.parm("ar_intensity") == None:
                pass
            else:
                l.parm("ar_intensity").set(0)
        hou.ui.displayMessage("ALL LIGHTS TURNED OFF!")

   if state == 4:
        lights = getAllLights()
        for l in lights:
            if l.parm("ar_intensity") == None:
                pass
            else:
                l.parm("ar_intensity").set(1)
        hou.ui.displayMessage("ALL LIGHTS TURNED ON!")
setIntensity(chooseState())
