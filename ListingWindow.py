#This code creates a Listing Window into which you can write information from NX sessions

﻿import math
import NXOpen
import NXOpen.CAE
import NXOpen.Preferences
import NXOpen.UF

def main() : 

    theSession  = NXOpen.Session.GetSession()
    workSimPart = theSession.Parts.BaseWork
    displaySimPart = theSession.Parts.BaseDisplay

#Selection Template
    theUI = NXOpen.UI.GetUI()
    
    selManager = theUI.SelectionManager
    
    SelectionScope = NXOpen.Selection.SelectionScope.AnyInAssembly
    
    SelectionMask = NXOpen.Selection.MaskTriple(31, 0, 0)
    
    SelectionMaskArray = []
    
    SelectionMaskArray.append(NXOpen.Selection.MaskTriple(NXOpen.UF.UFConstants.UF_point_type, 0, 0))
    
    SelectionAction = NXOpen.Selection.SelectionAction.ClearAndEnableSpecific
    
    resp = selManager.SelectTaggedObjects("Select Nodes", "Nodes Selection", SelectionScope, SelectionAction, False, False, SelectionMaskArray)



    lw = theSession.ListingWindow

    lw.SelectDevice(NXOpen.ListingWindowDeviceType.Window,"")
    
    lw.Open()

    for i in range(len(resp[1])):

        lw.WriteFullline(str(resp[1][i].Coordinates.X)+","+str(resp[1][i].Coordinates.Y)+","+str(resp[1][i].Coordinates.Z))
        

if __name__ == '__main__':
    main()
