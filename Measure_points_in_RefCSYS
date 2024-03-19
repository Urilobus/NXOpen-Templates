#code with which you can select several points and a reference coordinate system, as a result, the coordinates of the selected points are displayed in the information window

import math
import NXOpen
import NXOpen.CAE
import NXOpen.Preferences
import NXOpen.UF

def main() : 

    theSession  = NXOpen.Session.GetSession()
    workSimPart = theSession.Parts.BaseWork
    displaySimPart = theSession.Parts.BaseDisplay

#Selecting points
    theUI = NXOpen.UI.GetUI()
    
    selManager = theUI.SelectionManager
    
    SelectionScope = NXOpen.Selection.SelectionScope.AnyInAssembly
    
    SelectionMaskArray = []
    
    SelectionMaskArray.append(NXOpen.Selection.MaskTriple(NXOpen.UF.UFConstants.UF_point_type, 0, 0))
    
    SelectionAction = NXOpen.Selection.SelectionAction.ClearAndEnableSpecific
    
    resp = selManager.SelectTaggedObjects("Select Points", "Points Selection", SelectionScope, SelectionAction, False, False, SelectionMaskArray)


#Selecting CSYS

    SelectionMaskArrayCSYS = []
    
    SelectionMaskArrayCSYS.append(NXOpen.Selection.MaskTriple(NXOpen.UF.UFConstants.UF_coordinate_system_type, 0, 0))
    
    respcsys = selManager.SelectTaggedObject("Select CSYS", "CSYS Selection", SelectionScope, SelectionAction, False, False, SelectionMaskArrayCSYS)

    
#Creating a point measurement

    MeasureManager = workSimPart.MeasureManager


#Open Information Window

    lw = theSession.ListingWindow

    lw.SelectDevice(NXOpen.ListingWindowDeviceType.Window,"")
    
    lw.Open()
    
#Doing Measurements

    obj = [] 

    for i in range(len(resp[1])):

        mp = MeasureManager.NewPoint(resp[1][i], respcsys[1], False)
        Measure = mp.CreateFeature()
    
        exp = Measure.GetExpressions()
        pv = exp[0].PointValue 
        
        lw.WriteFullline(str(pv.X) + "," + str(pv.Y) + "," + str(pv.Z))
        
        obj.append(workSimPart.Features.FindObject(Measure.JournalIdentifier))
        
        
    nErrs1 = theSession.UpdateManager.AddObjectsToDeleteList(obj)    
    id1 = theSession.NewestVisibleUndoMark
    
    nErrs2 = theSession.UpdateManager.DoUpdate(id1)

if __name__ == '__main__':
    main()
