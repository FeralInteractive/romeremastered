bl_info = {
    "name": "Feral - RR",
    "description": "Feral modding tools for Campaigns map preparation and export.",
    "author": "LorenzoFeral",
    "version": (1, 0, 4),
    "blender": (2, 92, 0),
    "location": "",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": "3D View"
}


###############   IMPORTS
import bpy
from bpy.utils import previews
import os
import math
import bmesh


#######   Feral - RR


#######     PANELS


class FERAL_PT_Feral__Campaign_Tools(bpy.types.Panel):
    bl_label = "Feral - Campaign Tools"
    bl_idname = "FERAL_PT_Feral__Campaign_Tools"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = 'Feral - Rome'
    bl_order = 0


    @classmethod
    def poll(cls, context):
        return True

    def draw_header(self, context):
        try:
            layout = self.layout
        except Exception as exc:
            print(str(exc) + " | Error in Feral - Campaign Tools panel header")

    def draw(self, context):
        try:
            layout = self.layout
        except Exception as exc:
            print(str(exc) + " | Error in Feral - Campaign Tools panel")


class FERAL_PT_Slice_Tool(bpy.types.Panel):
    bl_label = "Slice Tool"
    bl_idname = "FERAL_PT_Slice_Tool"
    bl_parent_id = "FERAL_PT_Feral__Campaign_Tools"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"


    @classmethod
    def poll(cls, context):
        return True

    def draw_header(self, context):
        try:
            layout = self.layout
        except Exception as exc:
            print(str(exc) + " | Error in Slice Tool subpanel header")

    def draw(self, context):
        try:
            layout = self.layout
            col = layout.column(align=False)
            col.enabled = True
            col.alert = False
            col.scale_x = 1.0
            col.scale_y = 1.0
            box = col.box()
            box.enabled = True
            box.alert = False
            box.scale_x = 1.0
            box.scale_y = 1.0
            row = box.row(align=True)
            row.enabled = True
            row.alert = False
            row.scale_x = 1.0
            row.scale_y = 1.0
            row.prop(bpy.context.scene,"x_tiles",icon_value=0,text=r"Tiles X",emboss=True,slider=False,)
            row = box.row(align=True)
            row.enabled = True
            row.alert = False
            row.scale_x = 1.0
            row.scale_y = 1.0
            row.prop(bpy.context.scene,"y_tiles",icon_value=0,text=r"Tiles Y",emboss=True,slider=False,)
            col.separator(factor=1.0)
            op = col.operator("feral_campaign.slice",text=r"Slice Map",emboss=True,depress=False,icon_value=0)
        except Exception as exc:
            print(str(exc) + " | Error in Slice Tool subpanel")


class FERAL_PT_Export_Tool(bpy.types.Panel):
    bl_label = "Export Tool"
    bl_idname = "FERAL_PT_Export_Tool"
    bl_parent_id = "FERAL_PT_Feral__Campaign_Tools"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"


    @classmethod
    def poll(cls, context):
        return True

    def draw_header(self, context):
        try:
            layout = self.layout
        except Exception as exc:
            print(str(exc) + " | Error in Export Tool subpanel header")

    def draw(self, context):
        try:
            layout = self.layout
            op = layout.operator("feral_campaign.export_from_single_root",text=r"Export from Single Root",emboss=True,depress=False,icon_value=0)
            op = layout.operator("feral_campaign.export_selected",text=r"Export Selected",emboss=True,depress=False,icon_value=0)
        except Exception as exc:
            print(str(exc) + " | Error in Export Tool subpanel")


class FERAL_PT_Scene_Root_Tool(bpy.types.Panel):
    bl_label = "Scene Root Tool"
    bl_idname = "FERAL_PT_Scene_Root_Tool"
    bl_parent_id = "FERAL_PT_Feral__Campaign_Tools"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"


    @classmethod
    def poll(cls, context):
        return True

    def draw_header(self, context):
        try:
            layout = self.layout
        except Exception as exc:
            print(str(exc) + " | Error in Scene Root Tool subpanel header")

    def draw(self, context):
        try:
            layout = self.layout
            op = layout.operator("feral_campaign.add_scene_root_to_each",text=r"Add Scene Root to Each Selected",emboss=True,depress=False,icon_value=0)
            op = layout.operator("feral_campaign.add_single_scene_root",text=r"Add Single Scene Root to Selected",emboss=True,depress=False,icon_value=0)
        except Exception as exc:
            print(str(exc) + " | Error in Scene Root Tool subpanel")


#######     OPERATORS


class FERAL_OT_Slice(bpy.types.Operator):
    bl_idname = "feral_campaign.slice"
    bl_label = "slice"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        return bpy.context.mode == 'OBJECT' and len(context.selected_objects) > 0


    @staticmethod
    def FERAL_FUNCTION_Slice_Map(map_geometry, tile_x, tile_y):
        size_x = map_geometry.dimensions.x
        size_y = map_geometry.dimensions.y
        
        step_x = size_x / tile_x
        step_y = size_y / tile_y
        
        bpy.ops.object.mode_set(mode='EDIT')

        bm = bmesh.from_edit_mesh(map_geometry.data)

        edges = []

        i = step_x
        while i < size_x:
            ret = bmesh.ops.bisect_plane(bm, geom=bm.verts[:]+bm.edges[:]+bm.faces[:], plane_co=(i,0,0), plane_no=(-1,0,0))
            bmesh.ops.split_edges(bm, edges=[e for e in ret['geom_cut'] if isinstance(e, bmesh.types.BMEdge)])
            i += step_x
            
        i = step_y
        while i < size_y:
            ret = bmesh.ops.bisect_plane(bm, geom=bm.verts[:]+bm.edges[:]+bm.faces[:], plane_co=(0,i,0), plane_no=(0,1,0))
            bmesh.ops.split_edges(bm, edges=[e for e in ret['geom_cut'] if isinstance(e, bmesh.types.BMEdge)])               
            i += step_y

        bmesh.update_edit_mesh(map_geometry.data)

        bpy.ops.mesh.separate(type='LOOSE')
        bpy.ops.object.mode_set(mode='OBJECT')


    @staticmethod
    def FERAL_FUNCTION_UV_Tiles(context, tiles):
        bpy.ops.object.select_all(action='DESELECT')

        ## First we make the viewport to top view for the project from view to work. 
        ## Calling bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1) is discouraged in the documentation
        ## and implementing a modal operator may be preferable, but yolo

        for area in bpy.context.screen.areas:
            if area.type == 'VIEW_3D':
                for region in area.regions:
                    if region.type == 'WINDOW':
                        override = {'area': area, 'region': region, 'edit_object': bpy.context.edit_object}
                        bpy.ops.view3d.view_axis(override, type='TOP', align_active=False, relative=False)
                        bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1)
        
        for obj in tiles:
            context.view_layer.objects.active = obj
            obj.select_set(True)
            
            bpy.ops.object.mode_set(mode = 'EDIT')
            bpy.ops.mesh.select_all(action= 'SELECT')
            
            for area in context.screen.areas:
                if area.type == 'VIEW_3D':
                    for region in area.regions:
                        if region.type == 'WINDOW':
                            override = {'area': area, 'region': region, 'edit_object': context.edit_object}
                            bpy.ops.uv.project_from_view(override, orthographic=True, camera_bounds=False, correct_aspect=True, scale_to_bounds=True)
            
            bpy.ops.object.mode_set(mode = 'OBJECT')
            
            obj.select_set(False)
            context.view_layer.objects.active = None
            
        for obj in tiles:
            obj.select_set(True)
            
        context.view_layer.objects.active = tiles[0]


    @staticmethod
    def FERAL_FUNCTION_Rename_Tiles(tiles, x_tiles):

        bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY', center='BOUNDS')
        tiles.sort(key=lambda tile: ( math.floor(tile.location.y), -math.floor(tile.location.x) ) )
        #tiles.sort( key=lambda tile: (tile.location.y) )

        for number, tile in enumerate(tiles):
            tile.name = tile.name.split('.')[0] + '_' + '{:0>3}'.format(number + 1)

        bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
            

    def execute(self, context):
        try:
            self.FERAL_FUNCTION_Slice_Map(context.active_object, context.scene.x_tiles, context.scene.y_tiles)

            self.FERAL_FUNCTION_UV_Tiles(context, context.selected_objects)

            self.FERAL_FUNCTION_Rename_Tiles(context.selected_objects, context.scene.x_tiles)

        except Exception as exc:
            print(str(exc) + " | Error in execute function of slice")
        return {"FINISHED"}

    def invoke(self, context, event):
        try:
            pass
        except Exception as exc:
            print(str(exc) + " | Error in invoke function of slice")
        return self.execute(context)


class FERAL_OT_Export_Selected(bpy.types.Operator):
    bl_idname = "feral_campaign.export_selected"
    bl_label = "export_selected"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}


    @classmethod
    def poll(cls, context):
        allow_export = True

        for obj in context.selected_objects:
            if not (obj.type == 'EMPTY' or obj.type == 'ARMATURE'):
                allow_export = False
                break

        return bpy.context.mode == 'OBJECT' and allow_export

    def execute(self, context):
        try:

            save_path = bpy.path.abspath('//.\\Campaign_Tiles\\')

            if not os.path.exists(save_path):
                os.mkdir( save_path )

            roots = [obj for obj in context.selected_objects]

            bpy.ops.object.select_all(action='DESELECT')
            context.view_layer.objects.active = None
                    
            for scene_root in roots:

                scene_root.select_set(True)
                context.view_layer.objects.active = scene_root
                
                root_name = scene_root.name                
                scene_root.name = 'Scene_Root'        
                
                bpy.ops.object.select_hierarchy(direction='CHILD', extend=True)

                ## Removed offset as it seems to cause misalignemnt with mods

                # scene_root.children[0].location[0] -= 0.5
                # scene_root.children[0].location[1] -= 0.5

                bpy.ops.transform.rotate(value=3.14159, orient_axis='Z', orient_type='GLOBAL', orient_matrix=((-1, 0, 0), (0, -1, -0), (-0, 0, -1)), orient_matrix_type='VIEW', mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
                bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
                
                bpy.ops.export_scene.fbx(filepath= (save_path + '\\' + scene_root.children[0].name +'.fbx'),
                                        use_selection=True,
                                        apply_scale_options='FBX_SCALE_NONE',
                                        object_types={'EMPTY','MESH','ARMATURE'},
                                        add_leaf_bones=False,
                                        bake_anim_use_all_bones = True,
                                        bake_anim_use_nla_strips = False,
                                        bake_anim_use_all_actions = False,
                                        bake_anim_force_startend_keying = False)
                
                scene_root.name = root_name


                bpy.ops.transform.rotate(value=3.14159, orient_axis='Z', orient_type='GLOBAL', orient_matrix=((-1, 0, 0), (0, -1, -0), (-0, 0, -1)), orient_matrix_type='VIEW', mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)

                ## Removed offset as it seems to cause misalignemnt with mods

                # scene_root.children[0].location[0] -= 0.5
                # scene_root.children[0].location[1] -= 0.5

                bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)


                bpy.ops.object.select_all(action='DESELECT')
                context.view_layer.objects.active = None

        except Exception as exc:
            print(str(exc) + " | Error in execute function of export_selected")
        return {"FINISHED"}

    def invoke(self, context, event):
        try:
            pass
        except Exception as exc:
            print(str(exc) + " | Error in invoke function of export_selected")
        return self.execute(context)


class FERAL_OT_Export_From_Single_Root(bpy.types.Operator):
    bl_idname = "feral_campaign.export_from_single_root"
    bl_label = "export_from_single_root"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}


    @classmethod
    def poll(cls, context):
        allow_export = True

        for obj in context.selected_objects:
            if not (obj.type == 'EMPTY' or obj.type == 'ARMATURE'):
                allow_export = False
                break

        return bpy.context.mode == 'OBJECT' and allow_export and len(context.selected_objects) == 1

    def execute(self, context):
        try:

            save_path = bpy.path.abspath('//.\\Campaign_Tiles\\')

            if not os.path.exists(save_path):
                os.mkdir( save_path )

            scene_root = context.active_object
            scene_root.select_set(True)

            ## Align piece to in Rome world space

            bpy.ops.object.select_hierarchy(direction='CHILD', extend=True)

            bpy.ops.transform.rotate(value=3.14159, orient_axis='Z', orient_type='VIEW', orient_matrix=((-1, 0, 0), (0, -1, -0), (-0, 0, -1)), orient_matrix_type='VIEW', mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
            bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)

            bpy.ops.object.select_all(action='DESELECT')


            ## Export Process

            scene_root.select_set(True)
            context.view_layer.objects.active = scene_root

            scene_root_name = scene_root.name
            scene_root.name = 'Scene_Root'

            for obj in scene_root.children:
                
                if not obj.visible_get():
                    continue
                
                obj.select_set(True)

                bpy.ops.export_scene.fbx(filepath = (save_path + '\\' + obj.name + '.fbx'),
                                        axis_up='Y',
                                        use_selection=True,
                                        object_types={'EMPTY','MESH','ARMATURE'},
                                        add_leaf_bones=False,
                                        bake_anim_use_all_bones = True,
                                        bake_anim_use_nla_strips = False,
                                        bake_anim_use_all_actions = False,
                                        bake_anim_force_startend_keying = False,
                                        apply_scale_options='FBX_SCALE_NONE')
                
                obj.select_set(False)

            scene_root.name = scene_root_name


            ## Reset Alignment to Blender space

            bpy.ops.object.select_hierarchy(direction='CHILD', extend=True)

            bpy.ops.transform.rotate(value=3.14159, orient_axis='Z', orient_type='VIEW', orient_matrix=((-1, 0, 0), (0, -1, -0), (-0, 0, -1)), orient_matrix_type='VIEW', mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)

            bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)

        except Exception as exc:
            print(str(exc) + " | Error in execute function of export_from_single_root")
        return {"FINISHED"}

    def invoke(self, context, event):
        try:
            pass
        except Exception as exc:
            print(str(exc) + " | Error in invoke function of export_from_single_root")
        return self.execute(context)


class FERAL_OT_Add_Scene_Root_To_Each(bpy.types.Operator):
    bl_idname = "feral_campaign.add_scene_root_to_each"
    bl_label = "add_scene_root_to_each"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}


    @classmethod
    def poll(cls, context):
        return bpy.context.mode == 'OBJECT'

    def execute(self, context):
        try:
            
            pieces = [obj for obj in context.selected_objects]
            bpy.ops.object.select_all(action='DESELECT')

            for piece in pieces:
                bpy.ops.object.empty_add(type='PLAIN_AXES', align='WORLD', location=(0, 0, 0))
                scene_root = context.active_object

                scene_root.name = 'Scene_Root_' + piece.name
                piece.parent = scene_root

        except Exception as exc:
            print(str(exc) + " | Error in execute function of add_scene_root_to_each")
        return {"FINISHED"}

    def invoke(self, context, event):
        try:
            pass
        except Exception as exc:
            print(str(exc) + " | Error in invoke function of add_scene_root_to_each")
        return self.execute(context)


class FERAL_OT_Add_Single_Scene_Root(bpy.types.Operator):
    bl_idname = "feral_campaign.add_single_scene_root"
    bl_label = "add_single_scene_root"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}


    @classmethod
    def poll(cls, context):
        return bpy.context.mode == 'OBJECT'

    def execute(self, context):
        try:

            pieces = [obj for obj in context.selected_objects]
            bpy.ops.object.select_all(action='DESELECT')

            bpy.ops.object.empty_add(type='PLAIN_AXES', align='WORLD', location=(0, 0, 0))
            scene_root = context.active_object

            scene_root.name = 'Map_Scene_Root'

            for piece in pieces:
                piece.parent = scene_root

        except Exception as exc:
            print(str(exc) + " | Error in execute function of add_single_scene_root")
        return {"FINISHED"}

    def invoke(self, context, event):
        try:
            pass
        except Exception as exc:
            print(str(exc) + " | Error in invoke function of add_single_scene_root")
        return self.execute(context)



###############   REGISTER PROPERTIES
def register_properties():
    bpy.types.Scene.x_tiles = bpy.props.IntProperty(name='x_tiles',description='',subtype='NONE',options=set(),default=1,min=1)
    bpy.types.Scene.y_tiles = bpy.props.IntProperty(name='y_tiles',description='',subtype='NONE',options=set(),default=1,min=1)

def unregister_properties():
    del bpy.types.Scene.x_tiles
    del bpy.types.Scene.y_tiles


###############   REGISTER ADDON
def register():
    register_properties()

    bpy.utils.register_class(FERAL_PT_Feral__Campaign_Tools)
    bpy.utils.register_class(FERAL_PT_Slice_Tool)
    bpy.utils.register_class(FERAL_PT_Scene_Root_Tool)
    bpy.utils.register_class(FERAL_PT_Export_Tool)

    bpy.utils.register_class(FERAL_OT_Slice)
    bpy.utils.register_class(FERAL_OT_Add_Scene_Root_To_Each)
    bpy.utils.register_class(FERAL_OT_Add_Single_Scene_Root)
    bpy.utils.register_class(FERAL_OT_Export_From_Single_Root)
    bpy.utils.register_class(FERAL_OT_Export_Selected)
    


###############   UNREGISTER ADDON
def unregister():
    unregister_properties()

    bpy.utils.unregister_class(FERAL_OT_Export_Selected)
    bpy.utils.unregister_class(FERAL_OT_Export_From_Single_Root)
    bpy.utils.unregister_class(FERAL_OT_Add_Single_Scene_Root)
    bpy.utils.unregister_class(FERAL_OT_Add_Scene_Root_To_Each)
    bpy.utils.unregister_class(FERAL_OT_Slice)

    bpy.utils.unregister_class(FERAL_PT_Scene_Root_Tool)
    bpy.utils.unregister_class(FERAL_PT_Export_Tool)
    bpy.utils.unregister_class(FERAL_PT_Slice_Tool)
    bpy.utils.unregister_class(FERAL_PT_Feral__Campaign_Tools)
