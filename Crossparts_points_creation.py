#This code transfers points from .prt to .sim or .fem

#The code must be launched from .prt file and the name of the file to which points are transferred must be written in workSimPart variable (line 48). Both file must be opened in one session.

import math
import NXOpen
import NXOpen.CAE
import NXOpen.Preferences
import NXOpen.UF

def main() : 

    theSession  = NXOpen.Session.GetSession()
    workPart = theSession.Parts.BaseWork
    displaySimPart = theSession.Parts.BaseDisplay


#Open Information Window # Информационное окно в которое можно писать всякое

    lw = theSession.ListingWindow

    lw.SelectDevice(NXOpen.ListingWindowDeviceType.Window,"")
    
    lw.Open()
    
    lw.WriteFullline("Session Tag is: " + str(theSession.Tag))
    lw.WriteFullline("workPart Tag is: " + str(workPart.Tag))
    
   # workSimPart = theSession.Parts.FindObject("model1_sim1")
   # lw.WriteFullline("Parts: " + str(workSimPart.Name))
    
    
#Selecting points Создание "Выборщика точек"
    theUI = NXOpen.UI.GetUI()
    
    selManager = theUI.SelectionManager
    
    SelectionScope = NXOpen.Selection.SelectionScope.AnyInAssembly
    
    SelectionMaskArray = []
    
    SelectionMaskArray.append(NXOpen.Selection.MaskTriple(NXOpen.UF.UFConstants.UF_point_type, 0, 0))
    
    SelectionAction = NXOpen.Selection.SelectionAction.ClearAndEnableSpecific
    
    resp = selManager.SelectTaggedObjects("Select Points", "Points Selection", SelectionScope, SelectionAction, False, False, SelectionMaskArray) #В этот список записываются координаты подряд, чтобы их достать обращаемся к resp[1][i] 
    
    workSimPart = theSession.Parts.FindObject("model1_sim1")
    lw.WriteFullline("Parts: " + str(workSimPart.Name))
    
    for i in range(len(resp[1])):
        
        points = workSimPart.Points.CreatePoint(resp[1][i].Coordinates)	#Создание точки
        points.SetVisibility(NXOpen.SmartObjectVisibilityOption.Visible) #Делаем её видимой
    
    

if __name__ == '__main__':
    main()

    



