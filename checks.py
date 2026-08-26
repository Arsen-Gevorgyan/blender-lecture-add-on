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
            return len(arm.data.verification) > 8
    return False

def chekc_feet_exist():
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
