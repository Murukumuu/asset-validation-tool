import bpy

for obj in bpy.context.view_layer.objects:
    if obj.type == 'ARMATURE':
        obj.select_set(True)
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.mode_set(mode='POSE')
        break
    
if bpy.context.object and bpy.context.object.mode == 'POSE':
    active = bpy.context.active_pose_bone

    bpy.ops.pose.select_hierarchy(direction='PARENT', extend=True)

    #For each bone in the variable
    for bone in bpy.context.selected_pose_bones:
        if bone.constraints.get('Wiggle') is None:
            # Creates the constraint itself
            constraint = bone.constraints.new(type='DAMPED_TRACK')
            constraint.name = 'Wiggle'
            constraint.influence = 0.5
            constraint.target = bpy.context.object 
            constraint.subtarget = active.name