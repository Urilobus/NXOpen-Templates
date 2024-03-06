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
    
    resp = selManager.SelectTaggedObjects("Select Nodes", "Nodes Selection", SelectionScope, SelectionAction, False, False, SelectionMaskArray) 
    
    # ----------------------------------------------
    #   Menu: Information->Pre/Post->Node/Element...
    # ----------------------------------------------
    markId1 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    caePart1 = workFemPart
    nodeElementInfoBuilder1 = caePart1.NodeElementInfoMgr.CreateNodeElementInfoBuilder()
    
    nodeElementInfoBuilder1.Csys = True
    
    nodeElementInfoBuilder1.Coordinates = True
    
    nodeElementInfoBuilder1.NodeConnectivity = True
    
    nodeElementInfoBuilder1.ElementType = True
    
    nodeElementInfoBuilder1.ElementConnectivity = True
    
    nodeElementInfoBuilder1.Mesh = True
    
    nodeElementInfoBuilder1.MeshCollector = True
    
    added1 = nodeElementInfoBuilder1.Node.Add(resp[1])
    
    nXObject1 = nodeElementInfoBuilder1.Commit()
    
    nodeElementInfoBuilder1.Destroy()
    
    # ----------------------------------------------
    #   Menu: Tools->Journal->Stop Recording
    # ----------------------------------------------
    
if __name__ == '__main__':
    main()
