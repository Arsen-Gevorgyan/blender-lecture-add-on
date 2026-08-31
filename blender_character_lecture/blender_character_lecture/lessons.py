import bpy

LESSONS = {}

LESSONS[1] = {
    "title": "Lesson 1: Blender Basics",
    "icon": "MESH_CUBE",
    
    "lecture": {
        "goal_title": "Goal",
        "goal_icon": "LIGHT",
        "goal_text": [
            "Learn the Blender interface.",
            "Learn to move, rotate, and scale objects.",
            "Create the body of your character."
        ],
        "goal_image": "assets/images/1.png",
        "sections": [
            {
                "heading": "Step 1: Open Blender",
                "icon": "SCENE_DATA",
                "content": [
                    "Open Blender 3.6.",
                    "When Blender opens, you see a default scene.",
                    "In the MIDDLE of the screen is the 3D Viewport.",
                    "This is where you build and see your 3D objects.",
                    "",
                    "You see three objects in the scene:",
                    "1. Cube - a gray box in the center",
                    "2. Camera - looks like a triangle with lines",
                    "3. Light - shown as a small circle with lines",
                    "",
                    "On the RIGHT side of the screen is the Outliner.",
                    "The Outliner is a LIST of all objects in your scene.",
                    "You should see three names: Camera, Cube, Light.",
                    "",
                    "Click on the Cube in the 3D Viewport.",
                    "The cube gets an ORANGE outline.",
                    "This means the cube is SELECTED."
                ],
                "image": None
            },
            {
                "heading": "Step 2: Move an Object",
                "icon": "ORIENTATION_GLOBAL",
                "content": [
                    "Make sure the cube is selected (orange outline).",
                    "Press the G key on your keyboard.",
                    "G means Grab or Move.",
                    "Move your mouse around.",
                    "The cube follows your mouse!",
                    "",
                    "Click LEFT mouse button to place the cube.",
                    "The cube stays where you clicked.",
                    "",
                    "To move on ONE axis only:",
                    "Press G, then X - moves only left-right",
                    "Press G, then Y - moves only front-back",
                    "Press G, then Z - moves only up-down",
                    "",
                    "To move an EXACT amount:",
                    "Press G, then Z, then type 2, then press Enter.",
                    "The cube moves exactly 2 units up.",
                    "",
                    "Practice moving the cube in different directions."
                ],
                "image": None
            },
            {
                "heading": "Step 3: Rotate an Object",
                "icon": "DRIVER_ROTATIONAL_DIFFERENCE",
                "content": [
                    "Select the cube.",
                    "Press the R key on your keyboard.",
                    "R means Rotate.",
                    "Move your mouse around.",
                    "The cube rotates!",
                    "",
                    "Click LEFT mouse button to confirm rotation.",
                    "",
                    "To rotate on ONE axis:",
                    "Press R, then X - rotates around X axis",
                    "Press R, then Y - rotates around Y axis",
                    "Press R, then Z - rotates around Z axis",
                    "",
                    "To rotate an EXACT amount:",
                    "Press R, then Z, then type 45, then Enter.",
                    "The cube rotates exactly 45 degrees.",
                    "",
                    "Practice rotating the cube."
                ],
                "image": None
            },
            {
                "heading": "Step 4: Scale an Object",
                "icon": "FULLSCREEN_ENTER",
                "content": [
                    "Select the cube.",
                    "Press the S key on your keyboard.",
                    "S means Scale (change size).",
                    "Move your mouse toward the cube.",
                    "The cube gets smaller.",
                    "Move your mouse away from the cube.",
                    "The cube gets bigger.",
                    "",
                    "Click LEFT mouse button to confirm size.",
                    "",
                    "To scale on ONE axis:",
                    "Press S, then X - changes width",
                    "Press S, then Y - changes depth",
                    "Press S, then Z - changes height",
                    "",
                    "To scale an EXACT amount:",
                    "Press S, then Z, then type 2, then Enter.",
                    "The cube becomes 2 times taller.",
                    "",
                    "Practice scaling the cube."
                ],
                "image": None
            },
            {
                "heading": "Step 5: Rename Cube to Body",
                "icon": "OUTLINER_OB_MESH",
                "content": [
                    "Look at the Outliner on the RIGHT side.",
                    "Find the name 'Cube' in the list.",
                    "It has a small cube icon next to it.",
                    "",
                    "DOUBLE-CLICK on the word 'Cube'.",
                    "The name becomes editable (blue highlight).",
                    "Type: Body",
                    "Press Enter.",
                    "",
                    "The cube is now named 'Body'.",
                    "",
                    "Good names are important!",
                    "Later you will have many objects.",
                    "Names help you find them quickly.",
                    "",
                    "From now on, this object is called Body."
                ],
                "image": None
            },
            {
                "heading": "Step 6: Make Body Taller",
                "icon": "MESH_CUBE",
                "content": [
                    "Select the Body.",
                    "Press S, then Z.",
                    "Move your mouse up.",
                    "The Body gets taller.",
                    "Click LEFT mouse button to confirm.",
                    "",
                    "OR use exact value:",
                    "Press S, then Z, then type 2, then Enter.",
                    "The Body is now exactly 2 times taller.",
                    "",
                    "Try different values:",
                    "Press S, then Z, then type 1.5, then Enter.",
                    "The Body is now 1.5 times taller.",
                    "",
                    "The Body should look like a simple human torso.",
                    "Taller than wide.",
                    "Not a perfect cube anymore.",
                    "",
                    "Don't worry about making it perfect.",
                    "Simple shapes are good for now."
                ],
                "image": None
            },
            {
                "heading": "Step 7: Save Your File",
                "icon": "FILE_BLEND",
                "content": [
                    "Press Ctrl + Shift + S on your keyboard.",
                    "This opens the Save As window.",
                    "",
                    "In the file browser:",
                    "Choose a folder on your computer.",
                    "At the bottom, find the file name field.",
                    "Type: LowPolyCharacter",
                    "",
                    "Click the 'Save As' button.",
                    "Your file is saved.",
                    "",
                    "From now on, press Ctrl + S to save quickly.",
                    "Save often!",
                    "",
                    "You will continue working on this file in every lesson."
                ],
                "image": None
            }
        ]
    },
    
    "practice": {
        "task_title": "Task: Create the Body",
        "task_icon": "TOOL_SETTINGS",
        "task_text": [
            "Complete these steps:",
            "1. Select the default cube.",
            "2. Rename it to 'Body'.",
            "3. Make it taller (S then Z).",
            "4. Make it wider (S then X).",
            "5. Move it to scene center (G).",
            "6. Save the file as LowPolyCharacter.blend",
            "",
            "Your Body should look like a simple human torso.",
            "It should NOT look like a perfect cube anymore."
        ],
        "task_image": None,
        "checks": [
            {
                "text": "Object named 'Body' exists",
                "check": "check_body_exists",
                "hint": "In the Outliner (right panel), find your cube. Double-click its name and type 'Body'.",
                "icon": "OUTLINER_OB_MESH"
            },
            {
                "text": "Body is taller than original",
                "check": "check_body_taller",
                "hint": "Select Body. Press S then Z. Move mouse up to make it taller. Click to confirm.",
                "icon": "FULLSCREEN_ENTER"
            },
            {
                "text": "Body is wider than original",
                "check": "check_body_wider",
                "hint": "Select Body. Press S then X. Move mouse to make it wider. Click to confirm.",
                "icon": "FULLSCREEN_ENTER"
            },
            {
                "text": "Body is at center of scene",
                "check": "check_body_centered",
                "hint": "Select Body. Press G to move it. Move it to the center where X and Y lines cross.",
                "icon": "ORIENTATION_GLOBAL"
            }
        ]
    }
}

LESSONS[2] = {
    "title": "Lesson 2: Edit Mode and the Body",
    "icon": "MESH_CUBE",
    
    "lecture": {
        "goal_title": "Goal",
        "goal_icon": "LIGHT",
        "goal_text": [
            "Learn Object Mode and Edit Mode.",
            "Learn about vertices, edges, and faces.",
            "Learn Extrude and Loop Cut.",
            "Shape the body into a better torso."
        ],
        "goal_image": None,
        "sections": [
            {
                "heading": "Step 1: Object Mode vs Edit Mode",
                "icon": "SCENE_DATA",
                "content": [
                    "Blender has different MODES for working.",
                    "Mode changes what you can do with an object.",
                    "",
                    "OBJECT MODE:",
                    "- Work with the WHOLE object",
                    "- Move, rotate, scale the entire object",
                    "",
                    "EDIT MODE:",
                    "- Change the SHAPE of the object",
                    "- Work with vertices, edges, faces",
                    "",
                    "Select your Body object.",
                    "Press Tab on your keyboard.",
                    "You are now in EDIT MODE.",
                    "",
                    "You see DOTS on the corners of the Body.",
                    "These dots are called VERTICES.",
                    "",
                    "Press Tab again.",
                    "You return to OBJECT MODE.",
                    "",
                    "Practice switching modes several times.",
                    "Watch how the Body changes appearance."
                ],
                "image": None
            },
            {
                "heading": "Step 2: Vertices, Edges, Faces",
                "icon": "RESTRICT_SELECT_OFF",
                "content": [
                    "Every 3D object is made of three things:",
                    "",
                    "VERTICES:",
                    "- Points in space",
                    "- The corners of the object",
                    "- Shown as small dots",
                    "",
                    "EDGES:",
                    "- Lines between vertices",
                    "- The edges of the object",
                    "",
                    "FACES:",
                    "- Flat surfaces between edges",
                    "- What you see on the object",
                    "",
                    "In Edit Mode, you can select each type.",
                    "Look at the TOP of the 3D Viewport.",
                    "You see three small buttons:",
                    "1 = Vertex select (dot icon)",
                    "2 = Edge select (line icon)",
                    "3 = Face select (square icon)",
                    "",
                    "Press 3 on your keyboard (Face select).",
                    "Click on any face of the Body.",
                    "The face becomes ORANGE.",
                    "This means it's selected."
                ],
                "image": None
            },
            {
                "heading": "Step 3: Extrude",
                "icon": "ORIENTATION_GLOBAL",
                "content": [
                    "EXTRUDE creates new geometry from existing faces.",
                    "This is the MOST IMPORTANT modeling tool.",
                    "",
                    "Make sure you are in Edit Mode (press Tab).",
                    "Press 3 for Face select.",
                    "",
                    "Click the TOP face of the Body.",
                    "The top face becomes orange.",
                    "",
                    "Press E on your keyboard (Extrude).",
                    "Move your mouse UP.",
                    "New geometry appears from the top face!",
                    "",
                    "Click LEFT mouse button to confirm.",
                    "",
                    "You created new faces!",
                    "This is how you build shapes in Blender.",
                    "",
                    "Use Extrude to create:",
                    "- neck",
                    "- arms",
                    "- legs",
                    "- feet",
                    "- any shape"
                ],
                "image": None
            },
            {
                "heading": "Step 4: Apply Scale",
                "icon": "DRIVER_ROTATIONAL_DIFFERENCE",
                "content": [
                    "Before more modeling, you should APPLY SCALE.",
                    "This tells Blender the current size is normal.",
                    "",
                    "Press Tab to go to OBJECT MODE.",
                    "Select the Body.",
                    "",
                    "Press Ctrl + A on your keyboard.",
                    "A menu appears.",
                    "Choose 'Scale' from the menu.",
                    "",
                    "Nothing visible changes.",
                    "But Blender now considers this the normal size.",
                    "",
                    "This is important for:",
                    "- Modifiers",
                    "- UV unwrapping",
                    "- Animation",
                    "",
                    "Always apply scale after scaling objects."
                ],
                "image": None
            },
            {
                "heading": "Step 5: Loop Cut",
                "icon": "FULLSCREEN_ENTER",
                "content": [
                    "LOOP CUT adds a new line around your model.",
                    "This gives you more vertices to shape.",
                    "",
                    "Press Tab to go to EDIT MODE.",
                    "",
                    "Press Ctrl + R on your keyboard.",
                    "A PURPLE line appears on the Body.",
                    "",
                    "Move your mouse to position the line.",
                    "The line previews where the cut will be.",
                    "",
                    "Click LEFT mouse button once.",
                    "The line turns yellow.",
                    "Move mouse to slide the line.",
                    "",
                    "Click LEFT mouse button again to place.",
                    "",
                    "Now the Body has an extra section of faces.",
                    "This helps make better shapes.",
                    "",
                    "If you make a mistake:",
                    "Press Ctrl + Z to undo."
                ],
                "image": None
            },
            {
                "heading": "Step 6: Shape the Body",
                "icon": "MESH_CUBE",
                "content": [
                    "Now use what you learned to shape the Body.",
                    "",
                    "In Edit Mode, press 3 for Face select.",
                    "",
                    "Click the TOP face.",
                    "Press E to extrude upward.",
                    "Click to place.",
                    "This creates a NECK.",
                    "",
                    "Select SIDE faces.",
                    "Press S to scale them.",
                    "Make the body WIDER at shoulders.",
                    "Make it NARROWER at waist.",
                    "",
                    "Select the BOTTOM face.",
                    "Press S to make it smaller.",
                    "This makes the waist.",
                    "",
                    "Don't make it perfect.",
                    "Simple shapes are good for low-poly.",
                    "",
                    "Press Tab for Object Mode when done."
                ],
                "image": None
            }
        ]
    },
    
    "practice": {
        "task_title": "Task: Improve the Body",
        "task_icon": "TOOL_SETTINGS",
        "task_text": [
            "1. Select Body.",
            "2. Press Tab for Edit Mode.",
            "3. Press 3 for Face select.",
            "4. Press Ctrl + R to add Loop Cut.",
            "5. Select top face.",
            "6. Press E to extrude neck.",
            "7. Shape body like simple torso.",
            "8. Press Tab for Object Mode.",
            "9. Save file (Ctrl + S)."
        ],
        "task_image": None,
        "checks": [
            {
                "text": "Body has more than 8 vertices",
                "check": "check_body_improved",
                "hint": "Add a Loop Cut (Ctrl + R) or Extrude (E) to add more geometry to the Body.",
                "icon": "OUTLINER_OB_MESH"
            }
        ]
    }
}

LESSONS[3] = {
    "title": "Lesson 3: Head, Arms and Legs",
    "icon": "MESH_CUBE",
    
    "lecture": {
        "goal_title": "Goal",
        "goal_icon": "LIGHT",
        "goal_text": [
            "Create the head.",
            "Create the arms.",
            "Create the legs.",
            "Build a complete character body."
        ],
        "goal_image": None,
        "sections": [
            {
                "heading": "Step 1: Create the Head",
                "icon": "SCENE_DATA",
                "content": [
                    "Go to Object Mode (press Tab if in Edit Mode).",
                    "",
                    "Press Shift + A on your keyboard.",
                    "A menu appears at your mouse.",
                    "Choose 'Mesh'.",
                    "Another menu appears.",
                    "Choose 'Cube'.",
                    "",
                    "A NEW cube appears in the scene.",
                    "It appears at the 3D cursor location.",
                    "",
                    "Look at the Outliner (right panel).",
                    "The new cube is named 'Cube.001'.",
                    "",
                    "Double-click 'Cube.001'.",
                    "Type: Head",
                    "Press Enter.",
                    "",
                    "Now move the Head above the Body:",
                    "Select Head.",
                    "Press G, then Z.",
                    "Move mouse UP.",
                    "Click to place above the Body."
                ],
                "image": None
            },
            {
                "heading": "Step 2: Shape the Head",
                "icon": "RESTRICT_SELECT_OFF",
                "content": [
                    "Select the Head.",
                    "Press S to scale the whole head.",
                    "Move mouse to adjust size.",
                    "Click to confirm.",
                    "",
                    "A head should be SMALLER than the Body.",
                    "About 1/3 the size of the Body.",
                    "",
                    "To make the head rounder:",
                    "Press Tab for Edit Mode.",
                    "Press 3 for Face select.",
                    "Click the FRONT face.",
                    "Press S to scale it smaller.",
                    "This makes the face flatter.",
                    "",
                    "Press Tab for Object Mode when done.",
                    "",
                    "Simple cube head is fine for now.",
                    "We will paint the face later."
                ],
                "image": None
            },
            {
                "heading": "Step 3: Create Left Arm",
                "icon": "ORIENTATION_GLOBAL",
                "content": [
                    "In Object Mode, press Shift + A.",
                    "Choose Mesh, then Cube.",
                    "",
                    "Rename the new cube to: Arm.L",
                    "(L means Left)",
                    "",
                    "Move Arm.L to the LEFT side of Body:",
                    "Select Arm.L.",
                    "Press G, then X.",
                    "Move mouse LEFT.",
                    "Click to place.",
                    "",
                    "Scale the arm to look like an arm:",
                    "Press S, then Z to make it longer.",
                    "Press S, then X to make it thinner.",
                    "",
                    "The arm should be:",
                    "- Longer than it is wide",
                    "- Attached to the upper side of Body",
                    "- About the same length as the Body"
                ],
                "image": None
            },
            {
                "heading": "Step 4: Duplicate to Create Right Arm",
                "icon": "DRIVER_ROTATIONAL_DIFFERENCE",
                "content": [
                    "Make sure you are in Object Mode.",
                    "Select Arm.L.",
                    "",
                    "Press Shift + D on your keyboard.",
                    "This DUPLICATES the arm.",
                    "A copy follows your mouse.",
                    "",
                    "Move the copy to the RIGHT side.",
                    "Click LEFT mouse button to place.",
                    "",
                    "Look at the Outliner.",
                    "The copy is named 'Arm.L.001'.",
                    "",
                    "Double-click the name.",
                    "Type: Arm.R",
                    "Press Enter.",
                    "",
                    "Now you have two arms:",
                    "Arm.L = left arm",
                    "Arm.R = right arm"
                ],
                "image": None
            },
            {
                "heading": "Step 5: Create Left Leg",
                "icon": "FULLSCREEN_ENTER",
                "content": [
                    "In Object Mode, press Shift + A.",
                    "Choose Mesh, then Cube.",
                    "",
                    "Rename the new cube to: Leg.L",
                    "",
                    "Move Leg.L below the Body:",
                    "Select Leg.L.",
                    "Press G, then Z.",
                    "Move mouse DOWN.",
                    "Click to place under the Body.",
                    "",
                    "Scale the leg:",
                    "Press S, then Z to make it longer.",
                    "Press S, then X to make it thinner.",
                    "",
                    "The leg should be:",
                    "- Longer than the arm",
                    "- Slightly thicker than the arm",
                    "- Below the Body"
                ],
                "image": None
            },
            {
                "heading": "Step 6: Duplicate to Create Right Leg",
                "icon": "FULLSCREEN_ENTER",
                "content": [
                    "Select Leg.L.",
                    "Press Shift + D to duplicate.",
                    "Move the copy to the RIGHT side.",
                    "Click to place.",
                    "",
                    "Rename the copy to: Leg.R",
                    "",
                    "Now you have:",
                    "- Body",
                    "- Head",
                    "- Arm.L and Arm.R",
                    "- Leg.L and Leg.R",
                    "",
                    "This is your complete character!",
                    "",
                    "Check positions:",
                    "Head above Body.",
                    "Arms on left and right sides.",
                    "Legs below Body.",
                    "",
                    "Press Ctrl + S to save."
                ],
                "image": None
            }
        ]
    },
    
    "practice": {
        "task_title": "Task: Complete the Character",
        "task_icon": "TOOL_SETTINGS",
        "task_text": [
            "Your character should have:",
            "- Head",
            "- Body",
            "- Arm.L",
            "- Arm.R",
            "- Leg.L",
            "- Leg.R",
            "",
            "Move parts to correct positions:",
            "Head above Body.",
            "Arms on left and right sides.",
            "Legs below Body.",
            "",
            "Save your file (Ctrl + S)."
        ],
        "task_image": None,
        "checks": [
            {
                "text": "Head exists",
                "check": "check_head_exists",
                "hint": "Press Shift + A, choose Mesh then Cube. Rename it to 'Head' in the Outliner.",
                "icon": "OUTLINER_OB_MESH"
            },
            {
                "text": "Arm.L exists",
                "check": "check_arm_left_exists",
                "hint": "Press Shift + A, choose Mesh then Cube. Rename it to 'Arm.L' in the Outliner.",
                "icon": "OUTLINER_OB_MESH"
            },
            {
                "text": "Arm.R exists",
                "check": "check_arm_right_exists",
                "hint": "Duplicate Arm.L with Shift + D. Rename the copy to 'Arm.R'.",
                "icon": "OUTLINER_OB_MESH"
            },
            {
                "text": "Leg.L exists",
                "check": "check_leg_left_exists",
                "hint": "Press Shift + A, choose Mesh then Cube. Rename it to 'Leg.L' in the Outliner.",
                "icon": "OUTLINER_OB_MESH"
            },
            {
                "text": "Leg.R exists",
                "check": "check_leg_right_exists",
                "hint": "Duplicate Leg.L with Shift + D. Rename the copy to 'Leg.R'.",
                "icon": "OUTLINER_OB_MESH"
            }
        ]
    }
}

LESSONS[4] = {
    "title": "Lesson 4: Mirror Modifier",
    "icon": "MESH_CUBE",
    
    "lecture": {
        "goal_title": "Goal",
        "goal_icon": "LIGHT",
        "goal_text": [
            "Learn what Modifiers are.",
            "Learn the Mirror Modifier.",
            "Use Mirror to create symmetrical arms."
        ],
        "goal_image": None,
        "sections": [
            {
                "heading": "Step 1: What is a Modifier?",
                "icon": "SCENE_DATA",
                "content": [
                    "A MODIFIER changes an object without changing its original geometry.",
                    "You can add and remove modifiers anytime.",
                    "The original object stays the same.",
                    "",
                    "Find the Modifiers tab:",
                    "Look at the RIGHT panel.",
                    "Find the WRENCH icon.",
                    "Click it.",
                    "",
                    "This is the Modifiers tab.",
                    "Here you can add different modifiers.",
                    "",
                    "Modifiers are powerful tools.",
                    "You will use them often in Blender."
                ],
                "image": None
            },
            {
                "heading": "Step 2: Delete Arm.R",
                "icon": "TRASH",
                "content": [
                    "In Lesson 3, you created Arm.R by duplicating Arm.L.",
                    "Now we will use Mirror to create Arm.R AUTOMATICALLY.",
                    "This way, if you edit Arm.L, Arm.R updates too.",
                    "",
                    "First, delete the OLD Arm.R:",
                    "Select Arm.R.",
                    "Press X on your keyboard.",
                    "A menu appears.",
                    "Choose 'Delete'.",
                    "",
                    "Now you only have Arm.L.",
                    "We will recreate Arm.R with Mirror."
                ],
                "image": None
            },
            {
                "heading": "Step 3: Add Mirror Modifier to Arm.L",
                "icon": "MOD_MIRROR",
                "content": [
                    "Select Arm.L.",
                    "Go to the Modifiers tab (wrench icon).",
                    "",
                    "Click 'Add Modifier' button.",
                    "A menu appears with many modifiers.",
                    "Find 'Mirror' in the list.",
                    "Click it.",
                    "",
                    "You see the arm now has a MIRRORED copy!",
                    "The copy appears on the right side.",
                    "",
                    "In the Mirror settings:",
                    "Find 'Axis' section.",
                    "Make sure X is checked.",
                    "This mirrors left-right.",
                    "",
                    "The mirrored arm is now Arm.R!"
                ],
                "image": None
            },
            {
                "heading": "Step 4: Set Mirror Object to Body",
                "icon": "ORIENTATION_GLOBAL",
                "content": [
                    "Mirror needs to know WHERE to mirror from.",
                    "By default, it mirrors from Arm.L's own center.",
                    "We need it to mirror from the BODY center.",
                    "",
                    "In Mirror modifier settings:",
                    "Find 'Mirror Object' field.",
                    "Click the empty field.",
                    "A list appears.",
                    "Select 'Body' from the list.",
                    "",
                    "Now the arm mirrors from the Body center.",
                    "The mirrored arm is on the right side of the Body.",
                    "",
                    "If the mirrored arm is in the wrong place:",
                    "Check that Body is at the scene center.",
                    "Or adjust the Mirror Object."
                ],
                "image": None
            },
            {
                "heading": "Step 5: Test the Mirror",
                "icon": "EDITMODE_HLT",
                "content": [
                    "Select Arm.L.",
                    "Press Tab for Edit Mode.",
                    "",
                    "Select some vertices.",
                    "Press G to move them.",
                    "The mirrored arm updates in REAL-TIME!",
                    "",
                    "This is the power of Mirror!",
                    "Edit one side, the other side follows.",
                    "",
                    "Press Tab for Object Mode when done.",
                    "",
                    "Do the SAME for Leg.L if you want:",
                    "1. Delete Leg.R",
                    "2. Add Mirror Modifier to Leg.L",
                    "3. Set Mirror Object to Body",
                    "4. Check X axis",
                    "",
                    "Press Ctrl + S to save."
                ],
                "image": None
            }
        ]
    },
    
    "practice": {
        "task_title": "Task: Use Mirror on Arms and Legs",
        "task_icon": "TOOL_SETTINGS",
        "task_text": [
            "1. Delete Arm.R (select, X, Delete).",
            "2. Select Arm.L.",
            "3. Go to Modifiers tab (wrench icon).",
            "4. Add Mirror Modifier.",
            "5. Check X axis.",
            "6. Set Mirror Object to Body.",
            "7. Verify the mirrored arm appears.",
            "",
            "Then do the same for legs:",
            "8. Delete Leg.R.",
            "9. Select Leg.L.",
            "10. Add Mirror Modifier.",
            "11. Check X axis.",
            "12. Set Mirror Object to Body.",
            "",
            "Save file (Ctrl + S)."
        ],
        "task_image": None,
        "checks": [
            {
                "text": "Arm.L has Mirror Modifier",
                "check": "check_arm_mirrored",
                "hint": "Select Arm.L. Go to Modifiers tab (wrench icon). Click Add Modifier and choose Mirror.",
                "icon": "MOD_MIRROR"
            },
            {
                "text": "Leg.L has Mirror Modifier",
                "check": "check_leg_mirrored",
                "hint": "Select Leg.L. Go to Modifiers tab (wrench icon). Click Add Modifier and choose Mirror.",
                "icon": "MOD_MIRROR"
            }
        ]
    }
}

LESSONS[5] = {
    "title": "Lesson 5: Low-Poly Details",
    "icon": "MESH_CUBE",
    
    "lecture": {
        "goal_title": "Goal",
        "goal_icon": "LIGHT",
        "goal_text": [
            "Learn what Low Poly means.",
            "Shape simple hands and feet.",
            "Apply Flat Shading."
        ],
        "goal_image": None,
        "sections": [
            {
                "heading": "Step 1: What is Low Poly?",
                "icon": "SCENE_DATA",
                "content": [
                    "LOW POLY means few polygons.",
                    "Polygons are the faces that make the model.",
                    "",
                    "Low-poly models have:",
                    "- Few faces (hundreds, not millions)",
                    "- Simple shapes",
                    "- Angular look",
                    "",
                    "Low-poly models are GOOD because:",
                    "- Simple to make",
                    "- Fast to render",
                    "- Good for games",
                    "- Easy to edit",
                    "",
                    "We do NOT need thousands of faces.",
                    "Simple shapes are fine for this character.",
                    "",
                    "Your character should have simple shapes:",
                    "- Cube-like body",
                    "- Simple arms and legs",
                    "- Blocky head"
                ],
                "image": None
            },
            {
                "heading": "Step 2: Shape Simple Hands",
                "icon": "RESTRICT_SELECT_OFF",
                "content": [
                    "Select Arm.L.",
                    "Press Tab for Edit Mode.",
                    "Press 3 for Face select.",
                    "",
                    "Click the BOTTOM face of the arm.",
                    "The bottom face becomes orange.",
                    "",
                    "Press S to scale it smaller.",
                    "Move mouse toward the arm.",
                    "Click to confirm.",
                    "This makes the wrist.",
                    "",
                    "Press E to extrude.",
                    "Move mouse DOWN slightly.",
                    "Click to confirm.",
                    "",
                    "Press S to scale the new face smaller.",
                    "This makes a simple hand.",
                    "",
                    "Simple hand shape is fine.",
                    "No fingers needed.",
                    "Just a smaller block at the end of the arm.",
                    "",
                    "Press Tab for Object Mode."
                ],
                "image": None
            },
            {
                "heading": "Step 3: Shape Simple Feet",
                "icon": "ORIENTATION_GLOBAL",
                "content": [
                    "Select Leg.L.",
                    "Press Tab for Edit Mode.",
                    "Press 3 for Face select.",
                    "",
                    "Click the BOTTOM face of the leg.",
                    "Press E to extrude.",
                    "Move mouse FORWARD (Y direction).",
                    "Click to confirm.",
                    "",
                    "Scale the foot:",
                    "Press S, then X to make it wider.",
                    "Press S, then Y to make it longer.",
                    "",
                    "The foot should look like:",
                    "Leg",
                    " |",
                    " └── Foot (sticking forward)",
                    "",
                    "Now the leg has a simple foot.",
                    "Press Tab for Object Mode.",
                    "",
                    "Do the same for Leg.R (or use Mirror)."
                ],
                "image": None
            },
            {
                "heading": "Step 4: Apply Flat Shading",
                "icon": "FULLSCREEN_ENTER",
                "content": [
                    "Select your WHOLE character.",
                    "Hold Shift and click each part:",
                    "Body, Head, Arm.L, Arm.R, Leg.L, Leg.R.",
                    "",
                    "All parts should have orange outline.",
                    "",
                    "RIGHT-CLICK on the character.",
                    "A menu appears.",
                    "Choose 'Shade Flat'.",
                    "",
                    "FLAT SHADING:",
                    "- Shows each face clearly",
                    "- Gives the low-poly look",
                    "- Sharp edges",
                    "",
                    "SMOOTH SHADING:",
                    "- Makes surfaces look rounded",
                    "- Not good for low-poly style",
                    "",
                    "For this project, use Shade Flat.",
                    "It looks better for low-poly characters.",
                    "",
                    "Press Ctrl + S to save."
                ],
                "image": None
            }
        ]
    },
    
    "practice": {
        "task_title": "Task: Add Details",
        "task_icon": "TOOL_SETTINGS",
        "task_text": [
            "1. Select Arm.L.",
            "2. Edit Mode (Tab).",
            "3. Extrude hand shape (E).",
            "4. Select Leg.L.",
            "5. Extrude foot shape (E).",
            "6. Select all character parts.",
            "7. Right-click, choose Shade Flat.",
            "8. Save file (Ctrl + S)."
        ],
        "task_image": None,
        "checks": [
            {
                "text": "Arms have hand shapes",
                "check": "check_hands_exist",
                "hint": "Select Arm.L. Press Tab for Edit Mode. Extrude the bottom face to make a hand.",
                "icon": "MESH_CUBE"
            },
            {
                "text": "Legs have feet shapes",
                "check": "check_feet_exist",
                "hint": "Select Leg.L. Press Tab for Edit Mode. Extrude the bottom face forward to make a foot.",
                "icon": "MESH_CUBE"
            },
            {
                "text": "Flat shading applied",
                "check": "check_flat_shading",
                "hint": "Select your character. Right-click and choose 'Shade Flat'.",
                "icon": "SHADING_RENDERED"
            }
        ]
    }
}

LESSONS[6] = {
    "title": "Lesson 6: Materials, UV and Texture Painting",
    "icon": "MATERIAL",
    
    "lecture": {
        "goal_title": "Goal",
        "goal_icon": "LIGHT",
        "goal_text": [
            "Create a Material for your character.",
            "UV Unwrap the character so texture works.",
            "Create a texture image.",
            "Paint on the character.",
            "Save the texture."
        ],
        "goal_image": None,
        "sections": [
            {
                "heading": "Step 1: Select ALL Character Parts",
                "icon": "RESTRICT_SELECT_OFF",
                "content": [
                    "Go to Object Mode (press Tab if in Edit Mode).",
                    "Press A to deselect everything.",
                    "Now select all character parts:",
                    "Hold Shift and click each part:",
                    "- Body",
                    "- Head",
                    "- Arm.L",
                    "- Arm.R",
                    "- Leg.L",
                    "- Leg.R",
                    "",
                    "All parts should have orange outline.",
                    "We will add ONE material to ALL parts.",
                    "This way the whole character uses the same texture."
                ],
                "image": None
            },
            {
                "heading": "Step 2: Open Material Properties",
                "icon": "MATERIAL",
                "content": [
                    "Look at the RIGHT side of Blender.",
                    "There are small icons in a vertical row.",
                    "Find the RED SPHERE icon.",
                    "It looks like a beach ball.",
                    "Click it.",
                    "",
                    "This opens the Material Properties panel.",
                    "You see material settings here.",
                    "",
                    "If you don't see the icons:",
                    "Make sure your mouse is over the right panel.",
                    "The icons are at the top of the right panel."
                ],
                "image": None
            },
            {
                "heading": "Step 3: Create a New Material",
                "icon": "MATERIAL_DATA",
                "content": [
                    "In the Material Properties panel:",
                    "Find the button that says 'New'.",
                    "Click it.",
                    "",
                    "A new material appears.",
                    "You see many settings now:",
                    "- Base Color",
                    "- Metallic",
                    "- Roughness",
                    "",
                    "The material is named 'Material' by default.",
                    "Double-click the name to rename it.",
                    "Type: CharacterMaterial",
                    "Press Enter."
                ],
                "image": None
            },
            {
                "heading": "Step 4: Check Material on All Parts",
                "icon": "MATERIAL",
                "content": [
                    "With all parts still selected:",
                    "Look at the Material Properties panel.",
                    "You see your material at the top.",
                    "",
                    "Below the material list:",
                    "Find the 'Assign' button.",
                    "Click it.",
                    "This assigns the material to all selected parts.",
                    "",
                    "Now all parts share the same material.",
                    "They will all have the same color and texture."
                ],
                "image": None
            },
            {
                "heading": "Step 5: UV Unwrap All Parts",
                "icon": "UV",
                "content": [
                    "Make sure all character parts are selected.",
                    "Press Tab to enter Edit Mode.",
                    "",
                    "Press A to select ALL faces.",
                    "Everything turns orange.",
                    "",
                    "Press U on keyboard.",
                    "A menu appears.",
                    "Choose 'Unwrap' (first option).",
                    "",
                    "Blender creates UV coordinates.",
                    "UV tells Blender where to put texture on the 3D model.",
                    "",
                    "Press Tab to return to Object Mode."
                ],
                "image": None
            },
            {
                "heading": "Step 6: Switch to UV Editing Workspace",
                "icon": "UV_SYNC_SELECT",
                "content": [
                    "Look at the VERY TOP of Blender.",
                    "There are workspace tabs:",
                    "Layout, Modeling, Sculpting, UV Editing, etc.",
                    "",
                    "Click 'UV Editing' tab.",
                    "",
                    "Now your screen changes:",
                    "Left side = 3D Viewport (your character)",
                    "Right side = UV Editor (flat unwrapped view)",
                    "",
                    "In the UV Editor, you see the unwrapped faces.",
                    "They look like flat shapes on a grid."
                ],
                "image": None
            },
            {
                "heading": "Step 7: Create a Texture Image",
                "icon": "IMAGE_DATA",
                "content": [
                    "In the UV Editor (right side):",
                    "Click the 'Image' menu at the top.",
                    "Choose 'New Image'.",
                    "",
                    "A dialog opens:",
                    "Name: CharacterTexture",
                    "Width: 1024",
                    "Height: 1024",
                    "Color: Leave as black",
                    "",
                    "Click OK.",
                    "",
                    "The UV Editor now shows a BLACK square.",
                    "This is your texture canvas."
                ],
                "image": None
            },
            {
                "heading": "Step 8: Connect Texture to Material",
                "icon": "NODE_MATERIAL",
                "content": [
                    "Go back to Material Properties.",
                    "Find 'Base Color'.",
                    "Next to it, there is a small circle.",
                    "Click the circle.",
                    "Choose 'Image Texture'.",
                    "",
                    "Now you see:",
                    "- Image Texture node appears",
                    "- A field to select the image",
                    "",
                    "Click the image field.",
                    "Choose 'CharacterTexture'.",
                    "",
                    "Now the texture is connected to the material."
                ],
                "image": None
            },
            {
                "heading": "Step 9: Switch to Texture Paint Workspace",
                "icon": "BRUSH_DATA",
                "content": [
                    "Look at the top of Blender.",
                    "Click 'Texture Paint' workspace tab.",
                    "",
                    "Now you see:",
                    "Left = your character in 3D Viewport",
                    "Right = brush settings and color picker",
                    "",
                    "Your character should look WHITE or GRAY.",
                    "If it's BLACK, the texture is not connected.",
                    "Go back to Step 8 and reconnect.",
                    "",
                    "You are now ready to paint!"
                ],
                "image": None
            },
            {
                "heading": "Step 10: Paint the Character",
                "icon": "BRUSH_DATA",
                "content": [
                    "Find the COLOR picker on the right side.",
                    "Click the color bar.",
                    "Choose a skin color (light brown/tan).",
                    "",
                    "Move your mouse over the character.",
                    "You see a CIRCLE cursor.",
                    "This is your brush.",
                    "",
                    "Click and DRAG on the character to paint.",
                    "Hold left mouse button and move.",
                    "The character gets painted with skin color.",
                    "",
                    "To change brush size:",
                    "Press F key.",
                    "Move mouse left/right to change size.",
                    "Click to confirm.",
                    "",
                    "Paint the whole character with skin color first."
                ],
                "image": None
            },
            {
                "heading": "Step 11: Paint Clothes and Details",
                "icon": "BRUSH_DATA",
                "content": [
                    "Change color to blue or red for shirt.",
                    "Paint the Body (torso area).",
                    "",
                    "Change color to dark blue or black for pants.",
                    "Paint the legs.",
                    "",
                    "Change color to brown for hair.",
                    "Paint the top of the Head.",
                    "",
                    "Change color to white with small brush for eyes.",
                    "Click two dots on the face.",
                    "",
                    "Change color to dark red for mouth.",
                    "Draw a small line.",
                    "",
                    "Keep it simple!"
                ],
                "image": None
            },
            {
                "heading": "Step 12: Save the Texture Image",
                "icon": "FILE_TICK",
                "content": [
                    "In the UV Editor:",
                    "Click 'Image' menu.",
                    "Choose 'Save As'.",
                    "",
                    "A file browser opens.",
                    "Choose your project folder.",
                    "Name: CharacterTexture.png",
                    "Click 'Save As Image' button.",
                    "",
                    "The texture is now saved.",
                    "",
                    "Also save your Blender file:",
                    "Press Ctrl + S.",
                    "",
                    "You need BOTH files saved."
                ],
                "image": None
            }
        ]
    },
    
    "practice": {
        "task_title": "Task: Paint Your Character",
        "task_icon": "BRUSH_DATA",
        "task_text": [
            "1. Select all character parts.",
            "2. Open Material Properties (red sphere icon).",
            "3. Click New to create material.",
            "4. UV Unwrap all parts (Tab, A, U, Unwrap).",
            "5. Go to UV Editing workspace.",
            "6. Create 1024x1024 image 'CharacterTexture'.",
            "7. Connect texture to material Base Color.",
            "8. Go to Texture Paint workspace.",
            "9. Paint skin, clothes, hair, eyes, mouth.",
            "10. Save texture as PNG.",
            "11. Save Blender file.",
            "",
            "Your character should have colors now!"
        ],
        "task_image": None,
        "checks": [
            {
                "text": "Material exists on Body",
                "check": "check_material_exists",
                "hint": "Select Body. Go to Material Properties (red sphere icon on right panel). Click 'New' button.",
                "icon": "MATERIAL"
            },
            {
                "text": "UV Unwrap done",
                "check": "check_uv_unwrapped",
                "hint": "Select Body. Press Tab for Edit Mode. Press A to select all. Press U and choose Unwrap.",
                "icon": "UV_SYNC_SELECT"
            },
            {
                "text": "Texture is painted",
                "check": "check_texture_painted",
                "hint": "Go to Texture Paint workspace. Connect texture to material Base Color. Paint on character.",
                "icon": "BRUSH_DATA"
            }
        ]
    }
}

LESSONS[7] = {
    "title": "Lesson 7: Armature and Rigging",
    "icon": "ARMATURE_DATA",
    
    "lecture": {
        "goal_title": "Goal",
        "goal_icon": "LIGHT",
        "goal_text": [
            "Learn what an Armature is.",
            "Create bones for the character.",
            "Connect the character to the bones."
        ],
        "goal_image": None,
        "sections": [
            {
                "heading": "Step 1: What is an Armature?",
                "icon": "ARMATURE_DATA",
                "content": [
                    "An ARMATURE is a skeleton for your character.",
                    "It contains BONES.",
                    "Bones control how the character moves.",
                    "",
                    "Simple character bones:",
                    "- Hips (center of body)",
                    "- Spine (middle of body)",
                    "- Head (top)",
                    "- Arm.L and Arm.R",
                    "- Leg.L and Leg.R",
                    "",
                    "When you move a bone, the character part moves too.",
                    "This is called RIGGING."
                ],
                "image": None
            },
            {
                "heading": "Step 2: Add an Armature",
                "icon": "BONE_DATA",
                "content": [
                    "Go to Object Mode.",
                    "Press Shift + A.",
                    "Choose 'Armature'.",
                    "Then choose 'Single Bone'.",
                    "",
                    "A bone appears in the scene.",
                    "It looks like a line with two circles.",
                    "",
                    "Move the bone inside the Body:",
                    "Select the Armature.",
                    "Press G to move it.",
                    "Place it in the center of the Body.",
                    "Click to confirm.",
                    "",
                    "Scale the armature to fit the character:",
                    "Press S to scale.",
                    "Make it about the same height as the character.",
                    "Click to confirm."
                ],
                "image": None
            },
            {
                "heading": "Step 3: Edit the Bones",
                "icon": "EDITMODE_HLT",
                "content": [
                    "Select the Armature.",
                    "Press Tab for EDIT MODE.",
                    "",
                    "You see ONE bone.",
                    "The bone has two ends:",
                    "- Big end (root/top)",
                    "- Small end (tip/bottom)",
                    "",
                    "Click the SMALL end (tip).",
                    "It becomes highlighted.",
                    "",
                    "Press E to EXTRUDE a new bone.",
                    "Move mouse UP.",
                    "Click to place.",
                    "This is the SPINE bone.",
                    "",
                    "Extrude again:",
                    "Click the tip of the spine.",
                    "Press E.",
                    "Move mouse UP.",
                    "Click to place.",
                    "This is the HEAD bone.",
                    "",
                    "Now you have: Root, Spine, Head."
                ],
                "image": None
            },
            {
                "heading": "Step 4: Name the Bones",
                "icon": "OUTLINER_OB_ARMATURE",
                "content": [
                    "Good names help you find bones later.",
                    "",
                    "Click the first bone (bottom).",
                    "Look at the right panel.",
                    "Find the bone name field.",
                    "Double-click it.",
                    "Type: Hips",
                    "Press Enter.",
                    "",
                    "Click the middle bone.",
                    "Rename to: Spine",
                    "",
                    "Click the top bone.",
                    "Rename to: Head",
                    "",
                    "Now your bones have clear names."
                ],
                "image": None
            },
            {
                "heading": "Step 5: Create Arm Bones",
                "icon": "EDITMODE_HLT",
                "content": [
                    "In Edit Mode:",
                    "Click the TOP of the Spine bone.",
                    "Press E to extrude.",
                    "Move mouse LEFT.",
                    "Click to place.",
                    "This is Arm.L.",
                    "Rename it to: Arm.L",
                    "",
                    "Go back to the Spine.",
                    "Click the same point.",
                    "Press E to extrude.",
                    "Move mouse RIGHT.",
                    "Click to place.",
                    "Rename it to: Arm.R",
                    "",
                    "Now you have arm bones!"
                ],
                "image": None
            },
            {
                "heading": "Step 6: Create Leg Bones",
                "icon": "EDITMODE_HLT",
                "content": [
                    "In Edit Mode:",
                    "Click the BOTTOM of the Hips bone.",
                    "Press E to extrude.",
                    "Move mouse DOWN and LEFT.",
                    "Click to place.",
                    "Rename to: Leg.L",
                    "",
                    "Go back to the Hips.",
                    "Extrude DOWN and RIGHT.",
                    "Click to place.",
                    "Rename to: Leg.R",
                    "",
                    "You now have a simple skeleton!",
                    "Press Tab for Object Mode."
                ],
                "image": None
            },
            {
                "heading": "Step 7: Parent Character to Armature",
                "icon": "CONSTRAINT_BONE",
                "content": [
                    "Go to OBJECT MODE.",
                    "",
                    "First select ALL character parts:",
                    "Hold Shift and click Body, Head, Arm.L, Arm.R, Leg.L, Leg.R.",
                    "",
                    "LAST, select the Armature.",
                    "The Armature should be the ACTIVE object (brighter orange).",
                    "",
                    "Press Ctrl + P.",
                    "A menu appears.",
                    "Choose 'With Automatic Weights'.",
                    "",
                    "Blender calculates how the character moves with bones.",
                    "This may take a few seconds.",
                    "",
                    "The character is now connected to the skeleton!"
                ],
                "image": None
            },
            {
                "heading": "Step 8: Test the Rig",
                "icon": "POSE_HLT",
                "content": [
                    "Select the Armature.",
                    "At the TOP LEFT of 3D Viewport:",
                    "Find the Mode selector (shows 'Object Mode').",
                    "Click it.",
                    "Choose 'Pose Mode'.",
                    "",
                    "Click any bone.",
                    "Press R to rotate it.",
                    "Move mouse to rotate.",
                    "The character part moves with the bone!",
                    "",
                    "Test all bones:",
                    "- Rotate Head bone",
                    "- Rotate Arm.L bone",
                    "- Rotate Leg.L bone",
                    "",
                    "If the character moves, the rig works!",
                    "",
                    "Press Ctrl + S to save."
                ],
                "image": None
            }
        ]
    },
    
    "practice": {
        "task_title": "Task: Rig the Character",
        "task_icon": "ARMATURE_DATA",
        "task_text": [
            "1. Add an Armature (Shift + A).",
            "2. Edit bones to create skeleton.",
            "3. Create: Hips, Spine, Head, Arm.L, Arm.R, Leg.L, Leg.R.",
            "4. Parent character to armature (Ctrl + P).",
            "5. Choose 'With Automatic Weights'.",
            "6. Test in Pose Mode.",
            "7. Save file.",
            "",
            "Character should move when you rotate bones."
        ],
        "task_image": None,
        "checks": [
            {
                "text": "Armature exists",
                "check": "check_armature_exists",
                "hint": "Press Shift + A, choose Armature, then Single Bone.",
                "icon": "ARMATURE_DATA"
            },
            {
                "text": "Bones named correctly",
                "check": "check_bones_named",
                "hint": "In Edit Mode, name bones: Hips, Spine, Head. Use bone properties to rename.",
                "icon": "OUTLINER_OB_ARMATURE"
            },
            {
                "text": "Character parented to Armature",
                "check": "check_character_parented",
                "hint": "Select character, then armature. Press Ctrl + P. Choose With Automatic Weights.",
                "icon": "CONSTRAINT_BONE"
            }
        ]
    }
}

LESSONS[8] = {
    "title": "Lesson 8: Walking Animation",
    "icon": "ACTION",
    
    "lecture": {
        "goal_title": "Goal",
        "goal_icon": "LIGHT",
        "goal_text": [
            "Learn about animation and keyframes.",
            "Create a walking animation.",
            "Make the character move."
        ],
        "goal_image": None,
        "sections": [
            {
                "heading": "Step 1: What is Animation?",
                "icon": "PLAY",
                "content": [
                    "ANIMATION is a series of poses.",
                    "Blender plays poses quickly to create movement.",
                    "",
                    "Each pose is saved as a KEYFRAME.",
                    "Blender creates movement BETWEEN keyframes.",
                    "",
                    "For a walk cycle, you need about 4-5 poses:",
                    "1. Left leg forward",
                    "2. Middle position",
                    "3. Right leg forward",
                    "4. Middle position",
                    "5. Back to pose 1",
                    "",
                    "The poses repeat in a loop.",
                    "This creates the walking motion."
                ],
                "image": None
            },
            {
                "heading": "Step 2: The Timeline",
                "icon": "TIME",
                "content": [
                    "Look at the BOTTOM of Blender.",
                    "You see the TIMELINE.",
                    "It shows numbers: 1, 2, 3, 4, ...",
                    "These are FRAMES.",
                    "",
                    "Frame 1 is the start.",
                    "Frame 24 is one second (at 24 FPS).",
                    "",
                    "Click on any frame number to go there.",
                    "Or drag the blue line (playhead).",
                    "",
                    "The playhead shows the current frame.",
                    "",
                    "We will create poses at:",
                    "Frame 1, 6, 12, 18, and 24."
                ],
                "image": None
            },
            {
                "heading": "Step 3: Create First Pose",
                "icon": "POSE_HLT",
                "content": [
                    "Select the Armature.",
                    "Go to POSE MODE (top left mode selector).",
                    "",
                    "Click frame 1 on the Timeline.",
                    "",
                    "Pose the character in a walking position:",
                    "- Click Leg.L bone, press R, rotate forward",
                    "- Click Leg.R bone, press R, rotate backward",
                    "- Click Arm.R bone, press R, rotate forward",
                    "- Click Arm.L bone, press R, rotate backward",
                    "",
                    "This is the first walking pose."
                ],
                "image": None
            },
            {
                "heading": "Step 4: Save First Keyframe",
                "icon": "KEYFRAME",
                "content": [
                    "After posing the character:",
                    "Press A to select ALL bones.",
                    "All bones become highlighted.",
                    "",
                    "Press I on your keyboard.",
                    "A menu appears.",
                    "Choose 'LocRotScale'.",
                    "",
                    "A YELLOW DIAMOND appears on the Timeline.",
                    "This is your first keyframe.",
                    "",
                    "The keyframe saves the pose at this frame.",
                    "",
                    "Now the character remembers this pose!"
                ],
                "image": None
            },
            {
                "heading": "Step 5: Create Second Pose",
                "icon": "POSE_HLT",
                "content": [
                    "Click frame 6 on the Timeline.",
                    "",
                    "Pose the character in middle position:",
                    "- Legs straight (not forward or backward)",
                    "- Arms at sides",
                    "",
                    "Press A to select all bones.",
                    "Press I.",
                    "Choose 'LocRotScale'.",
                    "",
                    "You now have TWO poses.",
                    "Blender will animate between them."
                ],
                "image": None
            },
            {
                "heading": "Step 6: Create Third Pose",
                "icon": "POSE_HLT",
                "content": [
                    "Click frame 12 on the Timeline.",
                    "",
                    "Pose OPPOSITE of first pose:",
                    "- Leg.R forward",
                    "- Leg.L backward",
                    "- Arm.L forward",
                    "- Arm.R backward",
                    "",
                    "Press A to select all.",
                    "Press I.",
                    "Choose 'LocRotScale'.",
                    "",
                    "Now you have three poses."
                ],
                "image": None
            },
            {
                "heading": "Step 7: Create Fourth Pose",
                "icon": "POSE_HLT",
                "content": [
                    "Click frame 18 on the Timeline.",
                    "",
                    "Pose similar to frame 6:",
                    "- Legs in middle position",
                    "- Arms at sides",
                    "",
                    "Press A to select all.",
                    "Press I.",
                    "Choose 'LocRotScale'.",
                    "",
                    "Now you have four poses."
                ],
                "image": None
            },
            {
                "heading": "Step 8: Return to First Pose",
                "icon": "POSE_HLT",
                "content": [
                    "Click frame 24 on the Timeline.",
                    "",
                    "Pose EXACTLY like frame 1:",
                    "- Leg.L forward",
                    "- Leg.R backward",
                    "- Arm.R forward",
                    "- Arm.L backward",
                    "",
                    "Press A to select all.",
                    "Press I.",
                    "Choose 'LocRotScale'.",
                    "",
                    "Now the animation loops perfectly!",
                    "Frame 24 connects back to frame 1."
                ],
                "image": None
            },
            {
                "heading": "Step 9: Play the Animation",
                "icon": "PLAY",
                "content": [
                    "Press SPACEBAR on your keyboard.",
                    "The animation plays!",
                    "The character walks!",
                    "",
                    "Press Spacebar again to stop.",
                    "",
                    "If it looks wrong:",
                    "- Go to a keyframe (click yellow diamond).",
                    "- Adjust the pose.",
                    "- Press I to re-save keyframe.",
                    "",
                    "If too fast or slow:",
                    "- Move keyframes further apart = slower.",
                    "- Move keyframes closer together = faster.",
                    "",
                    "Press Ctrl + S to save."
                ],
                "image": None
            }
        ]
    },
    
    "practice": {
        "task_title": "Task: Create Walk Cycle",
        "task_icon": "ACTION",
        "task_text": [
            "1. Go to Pose Mode.",
            "2. Frame 1: First pose, insert keyframe (I).",
            "3. Frame 6: Second pose, insert keyframe.",
            "4. Frame 12: Third pose, insert keyframe.",
            "5. Frame 18: Fourth pose, insert keyframe.",
            "6. Frame 24: First pose again, insert keyframe.",
            "7. Press Space to play.",
            "8. Save file.",
            "",
            "Your character should look like it's walking."
        ],
        "task_image": None,
        "checks": [
            {
                "text": "Keyframes exist",
                "check": "check_keyframes_exist",
                "hint": "In Pose Mode, pose your character. Press A to select all bones. Press I and choose LocRotScale.",
                "icon": "KEYFRAME"
            },
            {
                "text": "Animation has 5+ poses",
                "check": "check_animation_poses",
                "hint": "Create keyframes at frames 1, 6, 12, 18, and 24 with different poses.",
                "icon": "ACTION"
            },
            {
                "text": "Character moves",
                "check": "check_character_moves",
                "hint": "Press Spacebar to play. The character should move through the poses.",
                "icon": "PLAY"
            }
        ]
    }
}

LESSONS[9] = {
    "title": "Lesson 9: Final Character",
    "icon": "FILE_BLEND",
    
    "lecture": {
        "goal_title": "Goal",
        "goal_icon": "LIGHT",
        "goal_text": [
            "Check the complete character.",
            "Fix any problems.",
            "Prepare for export."
        ],
        "goal_image": None,
        "sections": [
            {
                "heading": "Step 1: Check the Model",
                "icon": "MESH_CUBE",
                "content": [
                    "Rotate the view to see the character from all sides.",
                    "Hold MIDDLE MOUSE BUTTON and move mouse to rotate view.",
                    "",
                    "Check:",
                    "- Head is above body",
                    "- Arms are on sides",
                    "- Legs are below body",
                    "- Proportions look good",
                    "",
                    "If something looks wrong:",
                    "Select the part.",
                    "Press G to move it.",
                    "Or press S to scale it.",
                    "",
                    "Fix any big problems.",
                    "Small imperfections are fine."
                ],
                "image": None
            },
            {
                "heading": "Step 2: Check the Texture",
                "icon": "IMAGE_DATA",
                "content": [
                    "Look at the TOP RIGHT of 3D Viewport.",
                    "Find the shading mode buttons.",
                    "Click 'Material Preview' (sphere icon).",
                    "",
                    "You should see the colors on your character.",
                    "",
                    "Check:",
                    "- Face has eyes and mouth",
                    "- Body has shirt color",
                    "- Legs have pants color",
                    "",
                    "If texture is missing:",
                    "Go back to Lesson 6.",
                    "Make sure texture is connected to material.",
                    "",
                    "Check texture is saved as PNG file."
                ],
                "image": None
            },
            {
                "heading": "Step 3: Check the Rig",
                "icon": "ARMATURE_DATA",
                "content": [
                    "Select the Armature.",
                    "Go to POSE MODE.",
                    "",
                    "Test each bone:",
                    "- Click Head bone, press R to rotate",
                    "- Click Arm.L bone, press R to rotate",
                    "- Click Leg.L bone, press R to rotate",
                    "",
                    "The character should move naturally.",
                    "",
                    "If a part doesn't move:",
                    "The rig is broken.",
                    "Go back to Lesson 7.",
                    "Re-parent the character to the armature."
                ],
                "image": None
            },
            {
                "heading": "Step 4: Check the Animation",
                "icon": "ACTION",
                "content": [
                    "Press SPACEBAR to play the animation.",
                    "",
                    "Watch for problems:",
                    "- Arms moving wrong direction",
                    "- Legs going through body",
                    "- Character losing balance",
                    "- Texture disappearing",
                    "",
                    "If problems:",
                    "Adjust poses at keyframes.",
                    "",
                    "Don't try to make it perfect.",
                    "Simple walking is good enough.",
                    "",
                    "Your character is COMPLETE!",
                    "Press Ctrl + S to save."
                ],
                "image": None
            }
        ]
    },
    
    "practice": {
        "task_title": "Final Task: Complete Character",
        "task_icon": "FILE_TICK",
        "task_text": [
            "Your character should have:",
            "☐ Head",
            "☐ Body",
            "☐ Arms (left and right)",
            "☐ Legs (left and right)",
            "☐ Simple feet",
            "☐ Material with color",
            "☐ UV texture",
            "☐ Rig with bones",
            "☐ Walking animation",
            "",
            "Make one personal change to your character.",
            "Change hair color, clothes color, or proportions.",
            "",
            "Save your file."
        ],
        "task_image": None,
        "checks": [
            {
                "text": "All body parts exist",
                "check": "check_all_parts_exist",
                "hint": "Make sure you have: Head, Body, Arm.L, Arm.R, Leg.L, Leg.R.",
                "icon": "OUTLINER_OB_MESH"
            },
            {
                "text": "Texture applied",
                "check": "check_texture_applied",
                "hint": "Check Material Preview mode. Character should have colors.",
                "icon": "IMAGE_DATA"
            },
            {
                "text": "Rig complete",
                "check": "check_rig_complete",
                "hint": "Armature should have bones: Hips, Spine, Head.",
                "icon": "ARMATURE_DATA"
            },
            {
                "text": "Walk cycle works",
                "check": "check_walk_cycle",
                "hint": "Press Spacebar. Character should walk.",
                "icon": "ACTION"
            }
        ]
    }
}

LESSONS[10] = {
    "title": "Lesson 10A: Export for Game",
    "icon": "EXPORT",
    
    "lecture": {
        "goal_title": "Goal",
        "goal_icon": "LIGHT",
        "goal_text": [
            "Export the character as FBX.",
            "Import into Unity.",
            "Check that everything works."
        ],
        "goal_image": None,
        "sections": [
            {
                "heading": "Step 1: Save Your Project",
                "icon": "FILE_BLEND",
                "content": [
                    "Press Ctrl + S to save your Blender file.",
                    "Make sure the file is saved.",
                    "",
                    "Also check the texture is saved:",
                    "The CharacterTexture.png should be in the same folder.",
                    "",
                    "You need BOTH files for export:",
                    "- LowPolyCharacter.blend",
                    "- CharacterTexture.png"
                ],
                "image": None
            },
            {
                "heading": "Step 2: Select Everything",
                "icon": "RESTRICT_SELECT_OFF",
                "content": [
                    "In Object Mode:",
                    "Press A to select ALL objects.",
                    "Everything gets orange outline.",
                    "",
                    "Make sure these are selected:",
                    "- Body",
                    "- Head",
                    "- Arm.L, Arm.R",
                    "- Leg.L, Leg.R",
                    "- Armature",
                    "",
                    "If something is NOT selected:",
                    "Hold Shift and click it to add to selection."
                ],
                "image": None
            },
            {
                "heading": "Step 3: Export as FBX",
                "icon": "EXPORT",
                "content": [
                    "Go to FILE menu (top left corner).",
                    "Choose 'Export'.",
                    "Choose 'FBX (.fbx)'.",
                    "",
                    "A file browser opens.",
                    "Choose a folder for the export.",
                    "Name: LowPolyCharacter.fbx",
                    "",
                    "On the RIGHT panel of the file browser:",
                    "Find export settings:",
                    "- Make sure 'Selected Objects' is CHECKED",
                    "- Make sure 'Armature' is CHECKED",
                    "- Make sure 'Animation' is CHECKED",
                    "",
                    "Click 'Export FBX' button (bottom right).",
                    "",
                    "The FBX file is created!"
                ],
                "image": None
            },
            {
                "heading": "Step 4: Import into Unity",
                "icon": "IMPORT",
                "content": [
                    "Open Unity.",
                    "Create or open a project.",
                    "",
                    "In Windows Explorer:",
                    "Find your LowPolyCharacter.fbx file.",
                    "Find your CharacterTexture.png file.",
                    "",
                    "Select BOTH files.",
                    "Drag them into Unity's 'Assets' folder.",
                    "Or copy-paste them into the Assets folder.",
                    "",
                    "Unity automatically imports the character.",
                    "You see the files in the Project window."
                ],
                "image": None
            },
            {
                "heading": "Step 5: Check in Unity",
                "icon": "VIEWZOOM",
                "content": [
                    "In Unity, click the FBX file.",
                    "Look at the Inspector panel (right side).",
                    "",
                    "Check:",
                    "- Model tab: character appears",
                    "- Rig tab: rig is detected",
                    "- Animation tab: walk animation exists",
                    "",
                    "Drag the character from Assets into the Scene.",
                    "Click Play button.",
                    "The character should walk!",
                    "",
                    "If the character is gray:",
                    "Drag the texture PNG onto the character.",
                    "",
                    "Your character is now in Unity!"
                ],
                "image": None
            }
        ]
    },
    
    "practice": {
        "task_title": "Task: Export to Unity",
        "task_icon": "EXPORT",
        "task_text": [
            "1. Save Blender file.",
            "2. Select all objects.",
            "3. File > Export > FBX.",
            "4. Name: LowPolyCharacter.fbx.",
            "5. Check Selected Objects, Armature, Animation.",
            "6. Export.",
            "7. Import FBX and PNG into Unity.",
            "8. Check character appears with animation.",
            "",
            "Character should be in Unity."
        ],
        "task_image": None,
        "checks": [
            {
                "text": "FBX file created",
                "check": "check_fbx_exported",
                "hint": "File > Export > FBX. Save as LowPolyCharacter.fbx.",
                "icon": "EXPORT"
            },
            {
                "text": "Texture included",
                "check": "check_texture_exported",
                "hint": "Make sure CharacterTexture.png is saved and copied with the FBX.",
                "icon": "IMAGE_DATA"
            },
            {
                "text": "Animation included",
                "check": "check_animation_exported",
                "hint": "In FBX export settings, check Animation option.",
                "icon": "ACTION"
            }
        ]
    }
}

LESSONS[11] = {
    "title": "Lesson 10B: Export as Video",
    "icon": "RENDER_ANIMATION",
    
    "lecture": {
        "goal_title": "Goal",
        "goal_icon": "LIGHT",
        "goal_text": [
            "Add a camera.",
            "Set up lighting.",
            "Render the animation as video."
        ],
        "goal_image": None,
        "sections": [
            {
                "heading": "Step 1: Add a Camera",
                "icon": "CAMERA_DATA",
                "content": [
                    "Press Shift + A.",
                    "Choose 'Camera'.",
                    "A camera appears in the scene.",
                    "",
                    "Move the camera in FRONT of the character:",
                    "Select the camera.",
                    "Press G to move it.",
                    "Place it where it can see the character.",
                    "",
                    "Press Numpad 0 to see through the camera.",
                    "This shows what the camera sees.",
                    "",
                    "Adjust camera position until the character is in view.",
                    "The whole character should be visible.",
                    "",
                    "Press Numpad 0 again to exit camera view."
                ],
                "image": None
            },
            {
                "heading": "Step 2: Add Light",
                "icon": "LIGHT",
                "content": [
                    "Your scene already has a light.",
                    "If the character is too dark, add another:",
                    "",
                    "Press Shift + A.",
                    "Choose 'Light'.",
                    "Choose 'Point'.",
                    "",
                    "Move the light ABOVE the character:",
                    "Select the light.",
                    "Press G, then Z.",
                    "Move mouse up.",
                    "Click to place.",
                    "",
                    "Good lighting makes the character visible.",
                    "",
                    "You can also adjust light brightness:",
                    "Select the light.",
                    "Go to Light Properties (light bulb icon).",
                    "Increase 'Power' value."
                ],
                "image": None
            },
            {
                "heading": "Step 3: Set Output Settings",
                "icon": "OUTPUT",
                "content": [
                    "Look at the RIGHT panel.",
                    "Find the PRINTER icon.",
                    "Click it (Output Properties).",
                    "",
                    "Set Resolution:",
                    "- X: 1920",
                    "- Y: 1080",
                    "",
                    "Set Frame Rate: 24 FPS",
                    "",
                    "Find 'Output' section.",
                    "Click the folder icon to choose where to save.",
                    "Choose your project folder.",
                    "",
                    "Set File Format: FFmpeg video",
                    "Set Encoding: MPEG-4",
                    "",
                    "Now Blender knows where and how to save the video."
                ],
                "image": None
            },
            {
                "heading": "Step 4: Set Animation Range",
                "icon": "TIME",
                "content": [
                    "Look at the Timeline (bottom).",
                    "Set Start frame: 1",
                    "Set End frame: 24",
                    "",
                    "This tells Blender to render frames 1 to 24.",
                    "That's one second of animation at 24 FPS.",
                    "",
                    "For a longer video:",
                    "Set End frame to 48 (2 seconds).",
                    "Or 72 (3 seconds).",
                    "",
                    "The walk cycle will repeat during render."
                ],
                "image": None
            },
            {
                "heading": "Step 5: Render Animation",
                "icon": "RENDER_ANIMATION",
                "content": [
                    "Go to the TOP menu.",
                    "Click 'Render'.",
                    "Choose 'Render Animation'.",
                    "",
                    "Blender starts rendering.",
                    "This may take several minutes.",
                    "",
                    "You see progress at the bottom of the screen.",
                    "Each frame is rendered one by one.",
                    "",
                    "Wait until it finishes.",
                    "Do not close Blender during rendering.",
                    "",
                    "When done, the video is in your output folder.",
                    "The file name ends with .mp4",
                    "",
                    "Congratulations! You have a video of your character!"
                ],
                "image": None
            }
        ]
    },
    
    "practice": {
        "task_title": "Task: Create Video",
        "task_icon": "RENDER_ANIMATION",
        "task_text": [
            "1. Add a camera (Shift + A).",
            "2. Position camera to see character.",
            "3. Check lighting.",
            "4. Set Output Properties.",
            "5. Set animation range (1-24).",
            "6. Render > Render Animation.",
            "7. Find the video file.",
            "",
            "You should have a video of your character walking."
        ],
        "task_image": None,
        "checks": [
            {
                "text": "Camera exists",
                "check": "check_camera_positioned",
                "hint": "Press Shift + A, choose Camera. Press Numpad 0 to see through it.",
                "icon": "CAMERA_DATA"
            },
            {
                "text": "Video rendered",
                "check": "check_video_rendered",
                "hint": "Render > Render Animation. Check your output folder for the video file.",
                "icon": "RENDER_ANIMATION"
            }
        ]
    }
}
