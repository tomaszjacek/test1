import igl
import numpy as np
import meshplot as mp
mp.offline()

#igl.readOBJ("../../tutorial/shared/lilium.obj", V, F)

(v2, _, _, f2, _, _) = igl.read_obj("G:/shared/blenderScripts/mesh/testMeshObjFormat.obj")
mp.plot(v2,f2)

v= np.array([
    [0.,0,0],
    [1,0,0],
    [1,1,1],
    [2,1,0]
])

f = np.array([
    [0,1,2],
    [1,3,2]
])
mp.plot(v,f)