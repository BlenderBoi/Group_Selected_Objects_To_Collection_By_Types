import bpy
from . import pref_utils



ENUN_Method = [("MOVE","Move to Collection","Move"),("ADD","Add to Collection","Add")]


class COL_OT_Group_Selected_Objects_To_Collection_By_Types(bpy.types.Operator):

    """Group Selected Objects To Collection By Types"""
    bl_idname = "collection.group_selected_objects_to_collection_by_types"
    bl_label = "Group Selected Objects to Collection By Types"
    bl_options = {'REGISTER', 'UNDO'}


    Method: bpy.props.EnumProperty(items=ENUN_Method)

    Collection_Name: bpy.props.StringProperty(default="Collection")


    def draw(self, context):


        layout = self.layout
        layout.prop(self, "Method", text="Method", expand=True)
        layout.prop(self, "Collection_Name", text="Name")



    def invoke(self, context, event):

        selected_objects = context.selected_objects


        self.selected_types = {}

        for object in selected_objects:

            if not object.type in self.selected_types:
                self.selected_types[object.type] = [object]
            else:
                self.selected_types[object.type].append(object)

        return context.window_manager.invoke_props_dialog(self)

    def execute(self, context):


        preferences = pref_utils.get_addon_preferences()

        for type in self.selected_types:


            collection_name = self.Collection_Name + "_" + type
            collection = bpy.data.collections.get(collection_name)

            if collection == None:
                collection = bpy.data.collections.new(collection_name)

            collection.color_tag = getattr(preferences, type+"_Color")

            check_collection = [col for col in context.scene.collection.children]

            if not collection in check_collection:

                context.scene.collection.children.link(collection)



            objects = self.selected_types[type]

            for obj in objects:

                if self.Method == "MOVE":
                    for col in obj.users_collection:
                        col.objects.unlink(obj)

                check_objects = [obj for obj in collection.objects]

                if not obj in check_objects:
                    collection.objects.link(obj)

        return {'FINISHED'}


def Collection_Utility_Menu(self, context):
    self.layout.operator("collection.group_selected_objects_to_collection_by_types", text="Group Selected Objects To Collection By Types", icon="OUTLINER_COLLECTION")


classes = [COL_OT_Group_Selected_Objects_To_Collection_By_Types]

def register():


    for cls in classes:
        bpy.utils.register_class(cls)

    bpy.types.VIEW3D_MT_object.append(Collection_Utility_Menu)





def unregister():

    bpy.types.VIEW3D_MT_object.remove(Collection_Utility_Menu)

    for cls in classes:
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    register()








