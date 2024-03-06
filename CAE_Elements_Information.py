import math
import NXOpen
import NXOpen.CAE
import NXOpen.UF

def main() : 

    theSession  = NXOpen.Session.GetSession()
    workFemPart = theSession.Parts.BaseWork
    displayFemPart = theSession.Parts.BaseDisplay
    # ----------------------------------------------
    #   Menu: Information->Pre/Post->Node/Element...
    # ----------------------------------------------
    markId1 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    theUI = NXOpen.UI.GetUI()
    
    selManager = theUI.SelectionManager
    
    SelectionScope = NXOpen.Selection.SelectionScope.AnyInAssembly
    
    SelectionMaskArray = []

    SelectionMaskArray.append(NXOpen.Selection.MaskTriple(NXOpen.UF.UFConstants.UF_pseudo_object_type, NXOpen.UF.UFConstants.UF_pseudo_CAE_subtype, NXOpen.UF.UFConstants.UF_pseudo_CAE_element))
    
    SelectionAction = NXOpen.Selection.SelectionAction.ClearAndEnableSpecific
    
    resp = selManager.SelectTaggedObjects("Select Elements", "Elements Selection", SelectionScope, SelectionAction, False, False, SelectionMaskArray)
    
    caePart1 = workFemPart
    nodeElementInfoBuilder1 = caePart1.NodeElementInfoMgr.CreateNodeElementInfoBuilder()
    
    nodeElementInfoBuilder1.Csys = True
    
    nodeElementInfoBuilder1.Coordinates = True
    
    nodeElementInfoBuilder1.NodeConnectivity = True
    
    nodeElementInfoBuilder1.ElementType = True
    
    nodeElementInfoBuilder1.ElementConnectivity = True
    
    nodeElementInfoBuilder1.Mesh = True
    
    nodeElementInfoBuilder1.MeshCollector = True
    
    nodeElementInfoBuilder1.EntityOption = NXOpen.CAE.NodeElementInfoBuilder.EntityType.Element
    
    added1 = nodeElementInfoBuilder1.Element.Selection.Add(resp[1])
 
    nXObject1 = nodeElementInfoBuilder1.Commit()
    
    theSession.SetUndoMarkName(markId1, "Node/Element Information")
    
    nodeElementInfoBuilder1.Destroy()
    
    # ----------------------------------------------
    #   Menu: Tools->Journal->Stop Recording
    # ----------------------------------------------
    
if __name__ == '__main__':
    main()
