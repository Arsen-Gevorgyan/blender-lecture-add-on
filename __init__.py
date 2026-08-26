bl_info = {
    "name": "Blender Character Lecture",
    "author": "Arsen-Gevorgyan",
    "version": (1, 0, 0),
    "blender": (3, 6, 0),
    "location": "View3D > Sidebar > Lecture",
    "description": "Guided course for creating a low-poly character",
    "category": "Learning",
}

import bpy
from . import properties
from . import checks
from . import lessons
from . import operators
from . import ui

def register():
    properties.register()
    operators.register()
    ui.register()

def unregister():
    ui.unregister()
    operators.unregister()
    properties.unregister()

if __name__ == "__main__":
    register()