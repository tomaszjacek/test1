import bpy
from bpy import data as D, context as C
from mathutils import Matrix
import bmesh
import sys
import numpy
sys.path.append("G:/download/makehuman-master/makehuman/core/")
sys.path.append("G:/download/makehuman-master/makehuman/shared/")
sys.path.append("G:/download/makehuman-master/makehuman/lib/")
sys.path.append("G:/download/makehuman-master/makehuman/apps/")
import os
#import wavefront
import files3d
import module3d
 

collection = bpy.data.collections['Collection']
for obj in [o for o in collection.objects if o.type == 'MESH']:
    # Delete the object
    bpy.data.objects.remove( obj )


path = "G:/shared/blenderScripts/mesh/mh_testMeshObjFormat.obj"
name = os.path.basename(path)
objMH = module3d.Object3D(name)
 
objMH.path = path
 
#wavefront.loadObjFile(path, obj)
files3d.loadTextMesh(objMH, path)
 

#print(objMH.fvert)


edges = []
vertices = [tuple(elem) for elem in objMH.coord]
#print(vertices)
#print("----------------")
#print(objMH.vface)
faces = [tuple(elem) for elem in objMH.fvert] #numpy.delete (objMH.vface, numpy.s_[4::], 1)
print("----------------")
#print(faces)

# Create new mesh data.
mesh_name = "humanMesh"
mesh_data = D.meshes.new(mesh_name)
mesh_data.from_pydata(vertices, edges, faces)
# Create a new object which contains the mesh data.
mesh_obj = D.objects.new(mesh_data.name, mesh_data)
# Link the object to the scene collection.
C.collection.objects.link(mesh_obj)

bpy.context.view_layer.objects.active = mesh_obj
#bpy.ops.object.mode_set(mode = 'EDIT')
#bpy.ops.mesh.select_mode(type="FACE")

bm = bmesh.new()   # create an empty BMesh
bm.from_mesh(mesh_obj.data)   # fill it in from a Mesh
for v in bm.verts:
    v.co.x += 10.0
bm.to_mesh(mesh_obj.data)
bm.free()



mat = bpy.data.materials.new(name="mhSkinColor") #set new material to variable
mat.diffuse_color = (1, 0, 0, 1) #change color
mesh_obj.data.materials.append(mat) #add the material to the object


#bm.faces.ensure_lookup_table()
for face in mesh_obj.data.polygons:                                  # Iterate over all faces
    face.material_index = 0


fGroups = objMH.getFaceGroups()
print(fGroups)
print(objMH.getFaceGroup("base.obj"))
boFaceGroup=objMH.getFacesForGroups("base.obj")
print(boFaceGroup)
#bpy.ops.object.mode_set(mode = 'OBJECT')
#bm.to_mesh(mesh_obj.data)

#bmesh.update_edit_mesh(bm)


   