import math
import NXOpen
import NXOpen.CAE
import NXOpen.UF

def main() : 

    theSession  = NXOpen.Session.GetSession()
    workFemPart = theSession.Parts.BaseWork
    displayFemPart = theSession.Parts.BaseDisplay
    
    #Selection Template
    theUI = NXOpen.UI.GetUI()
    
    selManager = theUI.SelectionManager
    
    SelectionScope = NXOpen.Selection.SelectionScope.AnyInAssembly
    
    SelectionMask = NXOpen.Selection.MaskTriple(31, 0, 0)
    
    SelectionMaskArray = []
    
    SelectionMaskArray.append(NXOpen.Selection.MaskTriple(NXOpen.UF.UFConstants.UF_pseudo_object_type, NXOpen.UF.UFConstants.UF_pseudo_CAE_subtype, NXOpen.UF.UFConstants.UF_pseudo_CAE_node))
    
    SelectionAction = NXOpen.Selection.SelectionAction.ClearAndEnableSpecific
    
#Return a tuple resp[0] is NXOpen.Selection.Response.(Cancel), resp[1] is tuple of entities
    resp = selManager.SelectTaggedObjects("Select Nodes", "Nodes Selection", SelectionScope, SelectionAction, False, False, SelectionMaskArray) 
    
    markId1 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
     
if __name__ == '__main__':
    main()
