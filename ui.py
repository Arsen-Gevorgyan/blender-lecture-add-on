import bpy
import textwrap
from . import lessons
from . import checks

class CoursePanel(bpy.types.Panel):
    bl_label = "Course Menu"
    bl_idname = "OBJECT_PT_course_menu"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Lecture"

    def draw(self, context):
        layout = self.layout
        step = context.scene.course_current_step

        if step == 0:
            self.draw_welcome(context)
        elif step == 1:
            self.draw_info(context)
        elif step == 2:
            self.draw_intro(context)
        elif step >= 3 and step <= 22:
            self.draw_lesson(context, step)
        else:
            layout.label(text=f"Unknown step: {step}")

    def draw_welcome(self, context):
        layout = self.layout
        wrap_width = max(10, int(context.region.width / 13))
        
        label_text = "Blender Low-Poly Character Course"
        for line in textwrap.wrap(label_text, wrap_width):
            row = layout.row()
            row.alignment = 'CENTER'
            row.label(text=line)
        
        layout.separator()
        
        info_box = layout.box()
        info_text = "Simple Lecture Add-on what teach beginners create character, add materials/textures, add rig, animate and export"
        for line in textwrap.wrap(info_text, wrap_width):
            row = info_box.row()
            row.alignment = 'CENTER'
            row.label(text=line)
        
        layout.separator()
        layout.operator("object.start_course")
        layout.operator("object.info_operator")

    def draw_info(self, context):
        layout = self.layout
        wrap_width = max(10, int(context.region.width / 13))
        
        box_text = "Blender Low-Poly Character Course - INFO"
        for line in textwrap.wrap(box_text, wrap_width):
            row = layout.row()
            row.alignment = 'CENTER'
            row.label(text=line)
        
        layout.separator()
        
        info_box = layout.box()
        info_lines = [
            "Blender version: 3.6",
            "Level: Absolute beginner",
            "Final project: Simple low-poly human character with texture, rig, and walking animation."
        ]
        for line in info_lines:
            for wrapped in textwrap.wrap(line, wrap_width):
                row = info_box.row()
                row.alignment = 'LEFT'
                row.label(text=wrapped)
        
        layout.separator()
        layout.operator("object.back_operator")

    def draw_intro(self, context):
        layout = self.layout
        wrap_width = max(10, int(context.region.width / 13))
        
        lesson_text = "Introduction"
        for line in textwrap.wrap(lesson_text, wrap_width):
            row = layout.row()
            row.alignment = 'CENTER'
            row.label(text=line)
        
        layout.separator()
        
        content_box = layout.box()
        content_text = "Welcome to Blender Character Lecture! This add-on will teach you to create a character step by step. Each lesson teaches you something new. After learning, you complete a task. The add-on checks if you did it correctly. At the end you will have a character with materials, textures, rigging, and animation."
        for line in textwrap.wrap(content_text, wrap_width):
            row = content_box.row()
            row.alignment = 'CENTER'
            row.label(text=line)
        
        layout.separator()
        
        row = layout.row()
        row.operator("object.back_operator")
        row.operator("object.next_lesson")

    def draw_lesson(self, context, step):
        layout = self.layout
        lesson_num = (step - 1) // 2
        is_practice = step % 2 == 0
        
        lesson = lessons.LESSONS.get(lesson_num)
        if not lesson:
            layout.label(text="Lesson not found")
            return
        
        if is_practice:
            self.draw_practice(context, lesson, lesson_num)
        else:
            self.draw_lecture(context, lesson)

    def draw_lecture(self, context, lesson):
        layout = self.layout
        wrap_width = max(10, int(context.region.width / 13))
        
        title_lines = textwrap.wrap(lesson["title"], wrap_width)
        for i, line in enumerate(title_lines):
            row = layout.row()
            row.alignment = 'CENTER'
            if i == 0:
                row.label(text=line, icon=lesson.get("icon", "NONE"))
            else:
                row.label(text=line)
        
        layout.separator()
        
        goal_box = layout.box()
        goal_title_lines = textwrap.wrap(lesson["lecture"]["goal_title"], wrap_width)
        for i, g_line in enumerate(goal_title_lines):
            row = goal_box.row()
            row.alignment = 'CENTER'
            if i == 0:
                row.label(text=g_line, icon=lesson["lecture"].get("goal_icon", "NONE"))
            else:
                row.label(text=g_line)
        
        for line in lesson["lecture"]["goal_text"]:
            for wrapped in textwrap.wrap(line, wrap_width):
                row = goal_box.row()
                row.alignment = 'LEFT'
                row.label(text=wrapped)
        
        layout.separator()
        
        for section in lesson["lecture"]["sections"]:
            section_box = layout.box()
            heading_lines = textwrap.wrap(section["heading"], wrap_width)
            for i, h_line in enumerate(heading_lines):
                row = section_box.row()
                if i == 0:
                    row.label(text=h_line, icon=section.get("icon", "NONE"))
                else:
                    row.label(text=h_line)
            
            for line in section["content"]:
                for wrapped in textwrap.wrap(line, wrap_width):
                    row = section_box.row()
                    row.alignment = 'LEFT'
                    row.label(text=wrapped)
            
            layout.separator()
        
        row = layout.row()
        row.operator("object.back_operator")
        row.operator("object.next_lesson")

    def draw_practice(self, context, lesson, lesson_num):
        layout = self.layout
        wrap_width = max(10, int(context.region.width / 13))
        
        title_lines = textwrap.wrap(lesson["title"] + " - Practice", wrap_width)
        for i, line in enumerate(title_lines):
            row = layout.row()
            row.alignment = 'CENTER'
            if i == 0:
                row.label(text=line, icon="TOOL_SETTINGS")
            else:
                row.label(text=line)
        
        layout.separator()
        
        task_box = layout.box()
        task_title_lines = textwrap.wrap(lesson["practice"]["task_title"], wrap_width)
        for i, t_line in enumerate(task_title_lines):
            row = task_box.row()
            row.alignment = 'CENTER'
            if i == 0:
                row.label(text=t_line, icon=lesson["practice"].get("task_icon", "NONE"))
            else:
                row.label(text=t_line)
        
        for line in lesson["practice"]["task_text"]:
            for wrapped in textwrap.wrap(line, wrap_width):
                row = task_box.row()
                row.alignment = 'LEFT'
                row.label(text=wrapped)
        
        layout.separator()
        
        checks_box = layout.box()
        checks_title_lines = textwrap.wrap("Checks:", wrap_width)
        for i, c_line in enumerate(checks_title_lines):
            row = checks_box.row()
            row.alignment = 'CENTER'
            if i == 0:
                row.label(text=c_line, icon="CHECKBOX_HLT")
            else:
                row.label(text=c_line)
        
        all_passed = True
        for check in lesson["practice"]["checks"]:
            check_text = check["text"]
            check_name = check["check"]
            
            check_func = getattr(checks, check_name, None)
            if check_func:
                passed = check_func()
            else:
                passed = False
            
            if not passed:
                all_passed = False
            
            row = checks_box.row()
            icon = "CHECKBOX_HLT" if passed else "CHECKBOX_DEHLT"
            row.label(text=check_text, icon=icon)
            
            if not passed and "hint" in check:
                hint_box = checks_box.box()
                for wrapped in textwrap.wrap(check["hint"], wrap_width):
                    hint_row = hint_box.row()
                    hint_row.label(text=wrapped)
        
        layout.separator()
        
        row = layout.row()
        row.operator("object.back_operator")
        if all_passed:
            row.operator("object.next_lesson")
        else:
            row.label(text="Complete all checks!", icon="ERROR")

def register():
    bpy.utils.register_class(CoursePanel)

def unregister():
    bpy.utils.unregister_class(CoursePanel)