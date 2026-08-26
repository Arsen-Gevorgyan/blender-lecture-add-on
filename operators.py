import bpy

class NextLessonOperator(bpy.types.Operator):
    bl_idname = "object.next_lesson"
    bl_label = "Next Lesson"

    def execute(self, context):
        context.scene.course_current_step += 1
        self.report({'INFO'}, f"Moving to Lesson {context.scene.course_current_step - 2}!")
        return {'FINISHED'}

class BackMainOperator(bpy.types.Operator):
    bl_idname = "object.backmain_operator"
    bl_label = "Back to Main"

    def execute(self, context):
        context.scene.course_current_step = 0
        self.report({'INFO'}, "Returned to main menu!")
        return {'FINISHED'}

class InfoOperator(bpy.types.Operator):
    bl_idname = "object.info_operator"
    bl_label = "Info"

    def execute(self, context):
        context.scene.course_current_step = 1
        self.report({'INFO'}, "Showing course info!")
        return {'FINISHED'}

class SimpleOperator(bpy.types.Operator):
    bl_idname = "object.simple_operator"
    bl_label = "Start Lesson"

    def execute(self, context):
        context.scene.course_current_step = 2
        self.report({'INFO'}, "Starting Lesson 1!")
        return {'FINISHED'}

def register():
    bpy.utils.register_class(NextLessonOperator)
    bpy.utils.register_class(BackMainOperator)
    bpy.utils.register_class(SimpleOperator)
    bpy.utils.register_class(InfoOperator)

def unregister():
    bpy.utils.unregister_class(InfoOperator)
    bpy.utils.unregister_class(SimpleOperator)
    bpy.utils.unregister_class(BackMainOperator)
    bpy.utils.unregister_class(NextLessonOperator)
    