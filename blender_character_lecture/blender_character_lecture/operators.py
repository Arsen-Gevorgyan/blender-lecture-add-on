import bpy
from . import checks
from . import lessons

class NextLessonOperator(bpy.types.Operator):
    bl_idname = "object.next_lesson"
    bl_label = "Next"

    def execute(self, context):
        step = context.scene.course_current_step
        if step in [4, 6, 8, 10, 12, 14, 16, 18, 20, 22]:
            lesson_num = (step - 2) // 2
            all_passed = self.check_lesson(context, lesson_num)

            if all_passed:
                context.scene.course_current_step += 1
                self.report({'INFO'}, f"Lesson {lesson_num} complete! Moving on!")
            else:
                self.report({'WARNING'}, "Complete all checks first!")
                return {'CANCELLED'}
        else:
            context.scene.course_current_step += 1
            self.report({'INFO'}, "Next")

        return {'FINISHED'}

    def check_lesson(self, context, lesson_num):
        lesson = lessons.LESSONS.get(lesson_num)
        if not lesson:
            return True

        all_passed = True
        for check in lesson["practice"]["checks"]:
            check_name = check["check"]
            check_func = getattr(checks, check_name, None)
            if check_func:
                if not check_func():
                    all_passed = False

        return all_passed

class BackOperator(bpy.types.Operator):
    bl_idname = "object.back_operator"
    bl_label = "Back"

    def execute(self, context):
        step = context.scene.course_current_step

        if step > 0:
            context.scene.course_current_step -= 1
            self.report({'INFO'}, "Back")
        else:
            self.report({'WARNING'}, "Already at start")

        return {'FINISHED'}

class InfoOperator(bpy.types.Operator):
    bl_idname = "object.info_operator"
    bl_label = "Info"

    def execute(self, context):
        context.scene.course_current_step = 1
        self.report({'INFO'}, "Showing course info!")
        return {'FINISHED'}

class StartCourseOperator(bpy.types.Operator):
    bl_idname = "object.start_course"
    bl_label = "Start Course"

    def execute(self, context):
        context.scene.course_current_step = 2
        self.report({'INFO'}, "Starting course!")
        return {'FINISHED'}

class ExportGameOperator(bpy.types.Operator):
    bl_idname = "object.export_game"
    bl_label = "Export for Game"

    def execute(self, context):
        context.scene.course_current_step = 11
        self.report({'INFO'}, "Export for Game")
        return {'FINISHED'}

class ExportVideoOperator(bpy.types.Operator):
    bl_idname = "object.export_video"
    bl_label = "Export for Video"

    def execute(self, context):
        context.scene.course_current_step = 12
        self.report({'INFO'}, "Export as Video")
        return {'FINISHED'}

def register():
    bpy.utils.register_class(NextLessonOperator)
    bpy.utils.register_class(BackOperator)
    bpy.utils.register_class(InfoOperator)
    bpy.utils.register_class(StartCourseOperator)
    bpy.utils.register_class(ExportGameOperator)
    bpy.utils.register_class(ExportVideoOperator)

def unregister():
    bpy.utils.unregister_class(ExportVideoOperator)
    bpy.utils.unregister_class(ExportGameOperator)
    bpy.utils.unregister_class(StartCourseOperator)
    bpy.utils.unregister_class(InfoOperator)
    bpy.utils.unregister_class(BackOperator)
    bpy.utils.unregister_class(NextLessonOperator)
    