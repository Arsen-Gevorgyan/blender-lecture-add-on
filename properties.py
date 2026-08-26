import bpy

def register():
    bpy.types.Scene.course_current_step = bpy.props.IntProperty(
        name="Course Step",
        default=0,
        min=0,
        max=12
    )

    bpy.types.Scene.lesson1_body_exists = bpy.props.BoolProperty(
        name="Body Exists",
        default=False
    )

    bpy.types.Scene.lesson1_body_taller = bpy.props.BoolProperty(
        name="Body Taller",
        default=False
    )

    bpy.types.Scene.lesson1_body_wider = bpy.props.BoolProperty(
        name="Body Wider",
        default=False
    )

    bpy.types.Scene.lesson1_body_centered = bpy.props.BoolProperty(
        name="Body Centered",
        default=False
    )

def unregister():
    del bpy.types.Scene.course_current_step
    del bpy.types.Scene.lesson1_body_exists
    del bpy.types.Scene.lesson1_body_taller
    del bpy.types.Scene.lesson1_body_wider
    del bpy.types.Scene.lesson1_body_centered
    