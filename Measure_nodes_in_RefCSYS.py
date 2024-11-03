#code with which you can select several nodes and a reference coordinate system, as a result, the coordinates of the selected points are displayed in the information window

import math
import NXOpen
import NXOpen.CAE
import NXOpen.Preferences
import NXOpen.UF

def main() : 

    theSession  = NXOpen.Session.GetSession()
    workSimPart = theSession.Parts.BaseWork
    displaySimPart = theSession.Parts.BaseDisplay

#Selecting nodes
    theUI = NXOpen.UI.GetUI()
    
    selManager = theUI.SelectionManager
    
    SelectionScope = NXOpen.Selection.SelectionScope.AnyInAssembly
    
    SelectionMaskArray = []
    
    SelectionMaskArray.append(NXOpen.Selection.MaskTriple(NXOpen.UF.UFConstants.UF_pseudo_object_type, NXOpen.UF.UFConstants.UF_pseudo_CAE_subtype, NXOpen.UF.UFConstants.UF_pseudo_CAE_node))
    
    SelectionAction = NXOpen.Selection.SelectionAction.ClearAndEnableSpecific
    
    resp = selManager.SelectTaggedObjects("Select Nodes", "Nodes Selection", SelectionScope, SelectionAction, False, False, SelectionMaskArray)


#Selecting CSYS

    SelectionMaskArrayCSYS = []
    
    SelectionMaskArrayCSYS.append(NXOpen.Selection.MaskTriple(NXOpen.UF.UFConstants.UF_coordinate_system_type, 0, 0))
    
    respcsys = selManager.SelectTaggedObject("Select CSYS", "CSYS Selection", SelectionScope, SelectionAction, False, False, SelectionMaskArrayCSYS)

    
#Creating a nodes measurement

    MeasureManager = workSimPart.MeasureManager


#Open Information Window

    lw = theSession.ListingWindow

    lw.SelectDevice(NXOpen.ListingWindowDeviceType.Window,"")
    
    lw.Open()
    
#Do Measurements

    obj = [] 
    
    if (len(resp[1]) == 0):
    
        return 0
    
    else:
    
        point3d = resp[1][0].Coordinates
        point = workSimPart.Points.CreatePoint(point3d)
        #points.SetVisibility(NXOpen.SmartObjectVisibilityOption.Visible)
        
        for i in range(len(resp[1])):
        
            point.SetCoordinates(resp[1][i].Coordinates)
        
            mp = MeasureManager.NewPoint(point, respcsys[1], False)
            Measure = mp.CreateFeature()
        
            exp = Measure.GetExpressions()
            pv = exp[0].PointValue 
            
            lw.WriteFullline(str(resp[1][i].Label) + "  " + str(pv.X) + "  " + str(pv.Y) + "   " + str(pv.Z))
            
            obj.append(workSimPart.Features.FindObject(Measure.JournalIdentifier))
            
        obj.append(point)
            
        nErrs1 = theSession.UpdateManager.AddObjectsToDeleteList(obj)    
        id1 = theSession.NewestVisibleUndoMark
        
        nErrs2 = theSession.UpdateManager.DoUpdate(id1)

if __name__ == '__main__':
    main()

    



