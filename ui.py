import bpy
import textwrap

class CoursePanel(bpy.types.Panel):
    bl_label = "Course Menu"
    bl_idname = "OBJECT_PT_course_menu"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Lecture"

    def draw(self, context):
        layout = self.layout
        step = context.scene.course_current_step

        layout.label(text=f"Step: {step}")

        if step == 0:
            label_text = "Blender Low-Poly Character Course"
            for line in textwrap.wrap(label_text, 25):
                row = layout.row()
                row.alignment = 'CENTER'
                row.label(text=line)

            layout.separator()
            layout.operator("object.simple_operator")
            layout.operator("object.info_operator")

        elif step == 1:
            layout.label(text="Course Info")
            layout.separator()
            layout.operator("object.backmain_operator")

def register():
    bpy.utils.register_class(CoursePanel)

def unregister():
    bpy.utils.unregister_class(CoursePanel)