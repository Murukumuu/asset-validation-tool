import bpy

for obj in bpy.context.view_layer.objects:
    if obj.type == 'ARMATURE':
        obj.select_set(True)
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.mode_set(mode='EDIT')
        break
    

if bpy.context.object and bpy.context.object.mode == 'EDIT':
    base_name = None 

    for b in bpy.context.object.data.edit_bones:
        if b.select:
            base_name = b.name.split('_')[0]  
            bpy.context.object.data.edit_bones.active = b
            bpy.ops.armature.select_linked()
            break
            
    if base_name:
        for i, b in enumerate(bpy.context.selected_editable_bones):
            b.name = f"{base_name}_{i}"  