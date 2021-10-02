

from mathutils import Matrix, Vector
from math import pi
import bmesh

# Create separate matrix for each transformation.
translate = Matrix.Translation(Vector((0.5, -0.25, 0.25)))
print(translate)