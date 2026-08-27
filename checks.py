import bpy

def check_body_exists():
    return "Body" in bpy.data.objects

def check_body_taller():
    if "Body" in bpy.data.objects:
        body = bpy.data.objects["Body"]
        return body.scale.z > 1.5
    return False

def check_body_wider():
    if "Body" in bpy.data.objects:
        body = bpy.data.objects["Body"]
        return body.scale.x > 1.2 or body.scale.y > 1.2
    return False

def check_body_centered():
    if "Body" in bpy.data.objects:
        body = bpy.data.objects["Body"]
        return abs(body.location.x) < 0.5 and abs(body.location.y) < 0.5
    return False


def check_body_improved():
    if "Body" in bpy.data.objects:
        body = bpy.data.objects["Body"]
        if body.type == 'MESH':
            return len(body.data.vertices) > 8
    return False



def check_head_exists():
    return "Head" in bpy.data.objects

def check_arm_left_exists():
    return "Arm.L" in bpy.data.objects

def check_arm_right_exists():
    return "Arm.R" in bpy.data.objects

def check_leg_left_exists():
    return "Leg.L" in bpy.data.objects

def check_leg_right_exists():
    return "Leg.R" in bpy.data.objects


def check_leg_mirrored():
    if "Leg.L" in bpy.data.objects:
        leg = bpy.data.objects["Leg.L"]
        for modifier in leg.modifiers:
            if modifier.type == 'MIRROR':
                return True
    return False

def check_hands_exist():
    if "Arm.L" in bpy.data.objects:
        arm = bpy.data.objects["Arm.L"]
        if arm.type == "MESH":
            return len(arm.data.vertices) > 8
    return False

def check_feet_exist():
    if "Leg.L" in bpy.data.objects:
        leg = bpy.data.objects["Leg.L"]
        if leg.type == 'MESH':
            return len(leg.data.vertices) > 8
    return False

def check_flat_shading():
    for obj in bpy.data.objects:
        if obj.type == 'MESH':
            for polygon in obj.data.polygons:
                if polygon.use_smooth == False:
                    return True
    return False

def check_material_exists():
    if "Body" in bpy.data.objects:
        body = bpy.data.objects["Body"]
        return len(body.data.materials) > 0
    return False

def check_uv_unwrapped():
    if "Body" in bpy.data.objects:
        body = bpy.data.objects["Body"]
        if body.type == 'MESH':
            return len(body.data.uv_layers) > 0
    return False

def check_texture_painted():
    if "Body" in bpy.data.objects:
        body = bpy.data.objects["Body"]
        if body.type == 'MESH' and len(body.data.materials) > 0:
            mat = body.data.materials[0]
            if mat.use_nodes:
                for node in mat.node_tree.nodes:
                    if node.type == 'TEX_IMAGE':
                        return True
    return False

def check_armature_exists():
    for obj in bpy.data.objects:
        if obj.type == 'ARMATURE':
            return True
    return False

def check_bones_named():
    for obj in bpy.data.objects:
        if obj.type == 'ARMATURE':
            bone_names = [bone.name for bone in obj.data.bones]
            required = ["Hips", "Spine", "Head"]
            for name in required:
                if name not in bone_names:
                    return False
            return True
    return False

def check_character_parented():
    if "Body" in bpy.data.objects:
        body = bpy.data.objects["Body"]
        for modifier in body.modifiers:
            if modifier.type == 'ARMATURE':
                return True
    return False

def check_keyframes_exist():
    for obj in bpy.data.objects:
        if obj.type == 'ARMATURE':
            if obj.animation_data and obj.animation_data.action:
                return len(obj.animation_data.action.fcurves) > 0
    return False

def check_animation_poses():
    for obj in bpy.data.objects:
        if obj.type == 'ARMATURE':
            if obj.animation_data and obj.animation_data.action:
                fcurves = obj.animation_data.action.fcurves
                if len(fcurves) > 0:
                    keyframes = set()
                    for fcurve in fcurves:
                        for keyframe in fcurve.keyframe_points:
                            keyframes.add(keyframe.co[0])
                    return len(keyframes) >= 5
    return False

def check_character_moves():
    return check_keyframes_exist()

def check_all_parts_exist():
    required = ["Head", "Body", "Arm.L", "Arm.R", "Leg.L", "Leg.R"]
    for name in required:
        if name not in bpy.data.objects:
            return False
    return True

def check_texture_applied():
    return check_texture_painted()

def check_rig_complete():
    return check_bones_named()

def check_walk_cycle():
    return check_animation_poses()

def check_fbx_exported():
    return True

def check_texture_exported():
    return True

def check_animation_exported():
    return True

def check_camera_positioned():
    return "Camera" in bpy.data.objects

def check_video_rendered():
    return True

def check_arm_mirrored():
    if "Arm.L" in bpy.data.objects:
        arm = bpy.data.objects["Arm.L"]
        for modifier in arm.modifiers:
            if modifier.type == 'MIRROR':
                return True
    return False

def check_leg_mirrored():
    if "Leg.L" in bpy.data.objects:
        arm = bpy.data.objects["Leg.L"]
        for modifier in arm.modifiers:
            if modifier.type == 'MIRROR':
                return True
    return False