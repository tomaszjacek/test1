import bpy
from bpy import data as D, context as C
from mathutils import Matrix
import bmesh
import sys
sys.path.append("G:/shared/blenderScripts/mesh/")
from fileUtils import ObjLoader
from fileUtils import TargetLoader

newMesh = ObjLoader("G:/shared/blenderScripts/mesh/mh_testMeshObjFormat.obj")
headTarget = TargetLoader("G:/download/makehuman-master/makehuman/data/targets/head/head-square_v2.txt")

print("----------------------------")
print(newMesh.vertices[0][0])
print("----------------------------")
print(newMesh.faces[1][1])
print("----------------------------")
#print(headTarget.indices)
# Create a new BMesh instance.

edges = []
#faces = []

# Create new mesh data.
mesh_name = "humanMesh"
mesh_data = D.meshes.new(mesh_name)
mesh_data.from_pydata(newMesh.vertices, edges, newMesh.faces)

#corrections = mesh_data.validate(
#  verbose=True,
#  clean_customdata=True)

#bmTmp = bmesh.new()
#bmTmp.from_mesh(mesh_data)

# Convert BMesh to mesh data, then release BMesh.
#bmTmp.to_mesh(mesh_data)
#bmTmp.free()

# Create a new object which contains the mesh data.
mesh_obj = D.objects.new(mesh_data.name, mesh_data)

# Link the object to the scene collection.
C.collection.objects.link(mesh_obj)


bpy.context.view_layer.objects.active = mesh_obj
bpy.ops.object.mode_set(mode = 'EDIT')

bm = bmesh.from_edit_mesh(mesh_obj.data)
#bm = bmesh.new()
#bm.from_mesh(mesh_obj.data)

bm.faces.ensure_lookup_table()



bm.faces[210].select = True
bm.faces[211].select = True
bm.faces[212].select = True
bm.faces[213].select = True
bm.faces[214].select = True
bm.faces[215].select = True
bm.faces[216].select = True
bm.faces[217].select = True
bm.faces[218].select = True
bm.faces[219].select = True

#bm.normal_update()
#bpy.ops.object.mode_set(mode = 'OBJECT')
#bm.to_mesh(mesh_obj.data)

#bm.free()
#

#mesh_obj.data.update()
#mesh_obj.data.update()
#bmesh.update_edit_mesh(mesh_obj.data)
bmesh.update_edit_mesh(bm) 
#for v in headTarget.indices:

#  bm.faces[v].select = True

