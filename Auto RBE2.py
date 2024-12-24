#This journal creates RBE2 elements on selected faces and collects their center nodes in the "RBE2 center Nodes" Group.

#Before running this journal, you need to create a Group with polygon faces in your .fem part and name the Group "Auto RBE2 Faces".

import math
import NXOpen
import NXOpen.CAE
def main() : 

    theSession  = NXOpen.Session.GetSession()
    workFemPart = theSession.Parts.BaseWork
    displayFemPart = theSession.Parts.BaseDisplay

    fEModel1 = workFemPart.FindObject("FEModel")
 
#Create information window 
    lw = theSession.ListingWindow

    lw.SelectDevice(NXOpen.ListingWindowDeviceType.Window,"")
    
    lw.Open()
    
#Create MeshCollector where RBE2 elements will be stored in
    meshManager1 = fEModel1.Find("MeshManager")
   
    meshCollectorBuilder4 = meshManager1.CreateCollectorBuilder(NXOpen.CAE.MeshCollector.Null, "Rigid Link Collector")
    
    MeshColName = "Auto RBE2"

#Check, if MeshCollector "Auto RBE2" already exists
    try:

        nameTest = meshManager1.FindObject("MeshCollector["+MeshColName+"]")
        
        lw.WriteFullline("Mesh collector [Auto RBE2] already exists")

#if not -> create it
    except NXOpen.NXException as ex:
        
        meshCollectorBuilder4.CollectorName = MeshColName
            
        nXObject1 = meshCollectorBuilder4.Commit()
        
        lw.WriteFullline("Mesh collector [Auto RBE2] was created")
        

    meshCollectorBuilder4.Destroy()


#Check, if Group "Auto RBE2 Faces" already exists    
    try:
        
        caeGroup1 = workFemPart.CaeGroups.FindObject("Auto RBE2 Faces")
        lw.WriteFullline("Group [Auto RBE2 Faces] was found")
    
    except NXOpen.NXException as ex:    
        
        lw.WriteFullline("Group [Auto RBE2 Faces] wasn't found")
        exit()
    
    Faces = caeGroup1.GetEntities() #Get list of faces
   
#Change default MeshCollector color to Red   
    meshCollector1 = meshManager1.FindObject("MeshCollector["+MeshColName+"]")
    meshCollectorDisplayDefaults1 = meshCollector1.GetMeshDisplayDefaults()
    meshCollectorDisplayDefaults1.Color = workFemPart.Colors.Find("Red")
    meshCollectorDisplayDefaults1.Dispose()
    
#Create RBE2 elements using ConnectionBuilder  
    cAEConnectionBuilder1 = fEModel1.CaeConnections.CreateConnectionBuilder(NXOpen.CAE.CAEConnection.Null)

    i = 0
    for each in Faces:
        
        cAEConnectionBuilder1.ElementType.DestinationCollector.ElementContainer = NXOpen.CAE.MeshCollector.Null
        
        cAEConnectionBuilder1.ElementTypeRbe3.DestinationCollector.ElementContainer = NXOpen.CAE.MeshCollector.Null
        
        cAEConnectionBuilder1.ElementType.ElementDimension = NXOpen.CAE.ElementTypeBuilder.ElementType.Connection
        
        cAEConnectionBuilder1.ElementTypeRbe3.ElementDimension = NXOpen.CAE.ElementTypeBuilder.ElementType.Spider
        
        
        cAEConnectionBuilder1.MidNode = True
        
        cAEConnectionBuilder1.MethodType = NXOpen.CAE.CAEConnectionBuilder.MethodTypeEnum.SpiderConnection
        
        
        cAEConnectionBuilder1.ApplyWeightsRbe3 = True
        
        cAEConnectionBuilder1.SpiderConnectionMethodType = NXOpen.CAE.CAEConnectionBuilder.SpiderConnectionMethodTypeEnum.AverageNode
        
        cAEConnectionBuilder1.ElementType.ElementTypeName = "RBE2"
        
        cAEConnectionBuilder1.ElementType.DestinationCollector.ElementContainer = meshCollector1 #MeshCollector
        
        cAEConnectionBuilder1.ElementType.DestinationCollector.AutomaticMode = False
        
        # ----------------------------------------------
        #   Dialog Begin Smart Selector Methods
        # ----------------------------------------------

        seeds1 = [NXOpen.CAE.CAEFace.Null] * 1 
        seeds1[0] = Faces[i]
        relatedNodeMethod1 = workFemPart.SmartSelectionMgr.CreateNewRelatedNodeMethodFromFaces(seeds1, True, False)
            
        added1 = cAEConnectionBuilder1.TargetNodesSelection.Add(relatedNodeMethod1)
        
        relatedNodeMethod1.Dispose()
        
        cAEConnectionBuilder1.NodeFaceProximity = 0.0
        
        cAEConnectionBuilder1.SearchDistance = 100.0
        
        nXObject1 = cAEConnectionBuilder1.Commit()
        
        i = i + 1

    cAEConnectionBuilder1.Destroy()
    
    lw.WriteFullline("RBE2 Elements created: " + str(i))
 

 
#Collect RBE2 center nodes into [RBE2 center Nodes] group   

    #Get Elements from MeshCollector[Auto RBE2]
    seeds1 = meshCollector1.GetMeshes()

    relatedNodeMethod1 = workFemPart.SmartSelectionMgr.CreateRelatedElemMethod(seeds1, True)
     
    Elements = relatedNodeMethod1.GetElements()
        
    relatedNodeMethod1.Dispose()    

    #Get center nodes of each RBE2 element in MeshCollector[Auto RBE2]
    CenterNodes = []
    i = 0
    for each in Elements:
        
        ElementNodes = Elements[i].GetNodes()
        
        CenterNodes.append(ElementNodes[0])
        
        #lw.WriteFullline(str(CenterNodes[i].Label))
        
        i = i + 1


#Collect RBE2 center nodes into [RBE2 center Nodes] group   
    #Check, if group [RBE2 center Nodes] already exists
    try:
    
        caeGroupRBE2 = workFemPart.CaeGroups.FindObject("RBE2 center Nodes")
        caeGroupRBE2.AddEntities(CenterNodes)
        lw.WriteFullline("Group [RBE2 center Nodes] already exists")
        
    except NXOpen.NXException as ex:
    
        caeGroupRBE2 = workFemPart.CaeGroups.CreateGroup("RBE2 center Nodes", CenterNodes)
        lw.WriteFullline("Group [RBE2 center Nodes] was created")
    
    lw.Close()
  

if __name__ == '__main__':
    main()
