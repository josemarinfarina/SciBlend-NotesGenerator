bl_info = {
    "name": "NotesGenerator",
    "author": "Your Name",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "View3D > Sidebar > Notes Generator",
    "description": "Generate and manage annotations for scientific visualizations",
    "category": "3D View",
}

import bpy
from . import operators
from . import panels
from . import properties

def register():
    operators.register()
    panels.register()
    properties.register()

def unregister():
    panels.unregister()
    operators.unregister()
    properties.unregister()

if __name__ == "__main__":
    register()