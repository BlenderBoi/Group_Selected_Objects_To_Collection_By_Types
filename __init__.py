

bl_info = {
    "name": "Group Object Type To Collection",
    "author": "BlenderBoi",
    "version": (1, 0, 0),
    "blender": (3, 1, 0),
    "description": "Group Object Type into Collections",
    "warning": "",
    "wiki_url": "",
    "category": "Collection",
}


import bpy


from . import operators
from . import preferences

def register():

    operators.register()
    preferences.register()


def unregister():

    operators.unregister()
    preferences.unregister()

if __name__ == "__main__":
    register()
