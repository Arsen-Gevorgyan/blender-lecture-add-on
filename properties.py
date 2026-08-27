import bpy

def register():
    bpy.types.Scene.course_current_step = bpy.props.IntProperty(
        name="Course Step",
        default=0,
        min=0,
        max=22
    )

    bpy.types.Scene.lesson1_complete = bpy.props.BoolProperty(
        name="Lesson 1 Completed",
        default=False
    )
    bpy.types.Scene.lesson2_complete = bpy.props.BoolProperty(
        name="Lesson 2 Completed",
        default=False
    )
    bpy.types.Scene.lesson3_complete = bpy.props.BoolProperty(
        name="Lesson 3 Completed",
        default=False
    )
    bpy.types.Scene.lesson4_complete = bpy.props.BoolProperty(
        name="Lesson 4 Completed",
        default=False
    )
    bpy.types.Scene.lesson5_complete = bpy.props.BoolProperty(
        name="Lesson 5 Completed",
        default=False
    )
    bpy.types.Scene.lesson6_complete = bpy.props.BoolProperty(
        name="Lesson 6 Completed",
        default=False
    )
    bpy.types.Scene.lesson7_complete = bpy.props.BoolProperty(
        name="Lesson 7 Completed",
        default=False
    )

    bpy.types.Scene.lesson8_complete = bpy.props.BoolProperty(
        name="Lesson 8 Completed",
        default=False
    )
    bpy.types.Scene.lesson9_complete = bpy.props.BoolProperty(
        name="Lesson 9 Completed",
        default=False
    )
    bpy.types.Scene.lesson10_complete = bpy.props.BoolProperty(
        name="Lesson 10 Completed",
        default=False
    )

def unregister():
    del bpy.types.Scene.course_current_step
    del bpy.types.Scene.lesson1_complete
    del bpy.types.Scene.lesson2_complete
    del bpy.types.Scene.lesson3_complete
    del bpy.types.Scene.lesson4_complete
    del bpy.types.Scene.lesson5_complete
    del bpy.types.Scene.lesson6_complete
    del bpy.types.Scene.lesson7_complete
    del bpy.types.Scene.lesson8_complete
    del bpy.types.Scene.lesson9_complete
    del bpy.types.Scene.lesson10_complete
    