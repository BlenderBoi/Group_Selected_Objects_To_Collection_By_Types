import bpy
import os
import pathlib

from . import pref_utils


Object_Types = {"MESH": "Mesh", "CURVE": "Curve", "SURFACE": "Surface", "META": "Metaballs", "FONT": "Text", "VOLUME": "Volume", "GPENCIL":"Grease Pencil", "ARMATURE": "Armature", "LATTICE": "Lattice", "EMPTY": "Empty", "LIGHT": "Light", "LIGHT_PROBE":"Light Probe", "CAMERA":"Camera", "SPEAKER": "Speaker"}

def ENUM_Collection_Colors(self, context):
    items = []

    for index, color in enumerate(context.preferences.themes[0].collection_color):
        items.append(("COLOR_0" + str(index +1), "Color " + str(index +1) ,str(color), "COLLECTION_COLOR_0"+str(index+1), index))

    return items



class COL_user_preferences(bpy.types.AddonPreferences):

    bl_idname = pref_utils.get_addon_name()


    MESH_Color: bpy.props.EnumProperty(items=ENUM_Collection_Colors,name="Mesh", default=0)
    CURVE_Color: bpy.props.EnumProperty(items=ENUM_Collection_Colors, name="Curve", default=0)
    SURFACE_Color:bpy.props.EnumProperty(items=ENUM_Collection_Colors, name="Surface", default=0)
    META_Color:bpy.props.EnumProperty(items=ENUM_Collection_Colors, name="Metaballs", default=0)
    FONT_Color:bpy.props.EnumProperty(items=ENUM_Collection_Colors, name="Font", default=0)
    VOLUME_Color:bpy.props.EnumProperty(items=ENUM_Collection_Colors, name="Volume", default=1)
    GPENCIL_Color:bpy.props.EnumProperty(items=ENUM_Collection_Colors, name="Grease Pencil", default=0)
    ARMATURE_Color:bpy.props.EnumProperty(items=ENUM_Collection_Colors, name="Armature", default=2)
    LATTICE_Color:bpy.props.EnumProperty(items=ENUM_Collection_Colors, name="Lattice", default=3)
    EMPTY_Color:bpy.props.EnumProperty(items=ENUM_Collection_Colors, name="Empty", default=4)
    LIGHT_Color:bpy.props.EnumProperty(items=ENUM_Collection_Colors, name="Light", default=5)
    LIGHT_PROBE_Color:bpy.props.EnumProperty(items=ENUM_Collection_Colors, name="Light Probe", default=5)
    CAMERA_Color:bpy.props.EnumProperty(items=ENUM_Collection_Colors, name="Camera", default=6)
    SPEAKER_Color:bpy.props.EnumProperty(items=ENUM_Collection_Colors, name="Speaker", default=7)



    def draw(self, context):

        layout = self.layout

        col = layout.column(align=True)

        for type in Object_Types:
            
            icon = type + "_DATA"
            if type == "GPENCIL":
                icon = "GP_SELECT_STROKES"

            if type == "LIGHT_PROBE":
                icon = "OUTLINER_DATA_LIGHTPROBE"

            if type == "SPEAKER":
                icon = "OUTLINER_DATA_SPEAKER"



            row= layout.row(align=True)
            row.label(text=Object_Types[type], icon=icon)
            row.prop(self, type + "_Color", text="")





classes = [COL_user_preferences]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():

    for cls in classes:
        bpy.utils.unregister_class(cls)

if __name__ == "__main__":
    register()
