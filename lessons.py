import bpy

LESSONS = {}

LESSONS[1] = {
    "title": "Lesson 1: Blender Basics",
    "icon": "MESH_CUBE",
    
    "lecture": {
        "goal_title": "Goal",
        "goal_icon": "LIGHT",
        "goal_text": [
            "In this lesson, you will learn how to use the Blender screen.",
            "You will learn how to:",
            " - select an object",
            " - move an object",
            " - rotate an object",
            " - change the size of an object",
            " - rename an object",
            " - add a cube",
            " - delete an object",
            " - save your Blender project",
            "At the end, you will make the first part of your character: the body."
        ],
        "goal_image": None,
        "sections": [
            {
                "heading": "1. Open Blender",
                "icon": "SCENE_DATA",
                "content": [
                    "Open Blender 3.6.",
                    "You will see a scene with:",
                    " - a cube",
                    " - a camera",
                    " - a light",
                    "The cube is selected.",
                    "The large area in the middle is the 3D Viewport.",
                    "This is where you build your character.",
                    "On the right, you can see the Outliner.",
                    "The Outliner shows the objects in your scene.",
                    "You should see: Camera, Cube, Light"
                ],
                "image": None
            },
            {
                "heading": "2. Select an object",
                "icon": "RESTRICT_SELECT_OFF",
                "content": [
                    "Move your mouse over the cube.",
                    "Click the cube.",
                    "The cube becomes selected.",
                    "A selected object has an orange line around it."
                ],
                "image": None
            },
            {
                "heading": "3. Move an object",
                "icon": "ORIENTATION_GLOBAL",
                "content": [
                    "The Move tool changes the position of an object.",
                    "Select the cube.",
                    "Press: G",
                    "Move your mouse. The cube moves.",
                    "Click to stop.",
                    "You can also move the cube on one axis.",
                    "Press: G -> X",
                    "Now the cube moves only on the X axis.",
                    "Try: G -> Y, -> G -> Z",
                    "The X, Y, and Z axes are the three directions in 3D space."
                ],
                "image": None
            },
            {
                "heading": "4. Rotate an object",
                "icon": "DRIVER_ROTATIONAL_DIFFERENCE",
                "content": [
                    "The Rotate tool changes the direction of an object.",
                    "Select the cube.",
                    "Press: R",
                    "Move your mouse. Click to stop.",
                    "You can rotate on one axis:",
                    "R -> X, R -> Y, R -> Z"
                ],
                "image": None
            },
            {
                "heading": "5. Change the size",
                "icon": "FULLSCREEN_ENTER",
                "content": [
                    "The Scale tool changes the size of an object.",
                    "Select the cube.",
                    "Press: S",
                    "Move your mouse. Click to stop.",
                    "You can also change one direction:",
                    "S -> X, S -> Y, S -> Z"
                ],
                "image": None
            },
            {
                "heading": "6. Rename the cube",
                "icon": "OUTLINER_OB_MESH",
                "content": [
                    "We will use many objects later.",
                    "Good names will help us.",
                    "Select the cube.",
                    "In the Outliner, double-click the name Cube.",
                    "Change it to: Body",
                    "Press Enter.",
                    "Now the object is called Body."
                ],
                "image": None
            },
            {
                "heading": "7. Make the body",
                "icon": "MESH_CUBE",
                "content": [
                    "Select the Body.",
                    "Press: S -> Z",
                    "Move the mouse up a little. Click.",
                    "The body is now taller.",
                    "You can also use a number.",
                    "Press: S -> Z -> 2 -> Enter",
                    "Now the body is two times taller on the Z axis.",
                    "Try different values until the body looks like a simple human body.",
                    "Do not worry about making it perfect.",
                    " ",
                    "If you want delete object you can do it with:",
                    "Select object",
                    "Press: X -> Enter",
                    "Hint: Do not delete your Body."
                ],
                "image": None
            }
        ]
    },
    
    # PRACTICE PART
    "practice": {
        "task_title": "Task",
        "task_icon": "TOOL_SETTINGS",
        "task_text": [
            "Create the first body of your character.",
            "1. Select the cube.",
            "2. Rename it Body.",
            "3. Make it taller.",
            "4. Make it a little wider.",
            "5. Move it so it stands in the middle of the scene.",
            "6. Save the Blender file.",
            "Use: Ctrl + Shift + S",
            "Choose a folder.",
            "Give the file a name such as: LowPolyCharacter.blend"
        ],
        "checks": [
            {
                "text": "Create object named Body",
                "check": "check_body_exists",
                "hint": "Look in the Outliner. Do you see an object named 'Body'? If not, select your cube and rename it to 'Body' in the Outliner (double-click the name).",
                "icon": "OUTLINER_OB_MESH"
            },
            {
                "text": "Make Body taller",
                "check": "check_body_taller",
                "hint": "Select Body, press S -> Z to scale on Z axis only. Move mouse up or type a number like 2 and press Enter.",
                "icon": "FULLSCREEN_ENTER"
            },
            {
                "text": "Make Body wider",
                "check": "check_body_wider",
                "hint": "Select Body, press S -> X to scale on X axis. Move mouse to make it wider.",
                "icon": "FULLSCREEN_ENTER"
            },
            {
                "text": "Move Body to center",
                "check": "check_body_centered",
                "hint": "Select Body, press G to move it. Move it to the center of the scene (where X and Y are 0).",
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
            "In this lesson, you will learn how to change the shape of a cube.",
            "You will learn:",
            "Object Mode",
            "Edit Mode",
            "Vertex",
            "Edge",
            "Face",
            "Extrude",
            "Loop Cut",
            "Apply Scale",
            "You will use these tools to make a better body."
        ],
        "goal_image": None,
        "sections": [
            {
                "heading": "1. Object Mode and Edit Mode",
                "icon": "SCENE_DATA",
                "content": [
                    "Blender has different modes.",
                    "The two modes we need now are:",
                    "- Object Mode",
                    "You work with whole object.",
                    " - Edit Mode",
                    "You change the shape of the object.",
                    " ",
                    "Select your Body.",
                    "Press: Tab",
                    "You are now in Edit Mode.",
                    "Press: Tab",
                    "Again return to Object Mode."
                ],
                "image": None
            },
            {
                "heading": "2. Vertex, Edge and Face",
                "icon": "RESTRICT_SELECT_OFF",
                "content": [
                    "A cube has:",
                    "1. Vertices - points",
                    "2. Edges - lines",
                    "3. Faces - flat surfaces",
                    " ",
                    "In Edit Mode, you can select them.",
                    "At the top of the 3D Viewport, you can find the selection buttons.",
                    " ",
                    "You can also use:",
                    "`/1`/ - Vertex",
                    "`/2`/ - Edge",
                    "`/3`/ - Face",
                    " ",
                    "Make sure you are in Edit Mode.",
                    "Press: 3",
                    "You are now using Face Select.",
                    "Click a face of the cube.",
                    "The face becomes selected."
                ],
                "image": None
            },
            {
                "heading": "3. Extrude",
                "icon": "ORIENTATION_GLOBAL",
                "content": [
                    "Extrude - crestes new geometry from a face.",
                    "Select the top face of the body.",
                    "Press: E",
                    "Move tge mouse up.",
                    "Click.",
                    "You created new geometry.",
                    "This is one of the most important tools in character modeling.",
                    " ",
                    "We can use Extrude to create:",
                    "- neck",
                    "- arms",
                    "- legs",
                    "- feet",
                    "- other parts"
                ],
                "image": None
            },
            {
                "heading": "4. Apply Scale",
                "icon": "DRIVER_ROTATIONAL_DIFFERENCE",
                "content": [
                    "Before doing more modeling, we should apply the object's scale.",
                    "Press: Tab to go to Object Mode.",
                    "Select Body",
                    "Press: Ctrl + A",
                    "A menu appears",
                    "Choose: Scale",
                    "Now Blender considers the current size as the normal size.",
                    "This is useful when working with modifiers and other tools."
                ],
                "image": None
            },
            {
                "heading": "5. Add a Loop Cut",
                "icon": "FULLSCREEN_ENTER",
                "content": [
                    "A Loop Cut adds a new line around the model.",
                    "Go to Edit Mode.",
                    "Press: Tab",
                    "Than",
                    "Press: Ctrl + R",
                    "Move your mouse over the body.",
                    "A preview line appears.",
                    "Click.",
                    "Then click again to place line.",
                    "Now the body has another section.",
                    " ",
                    "If you make something wrong don't worry.",
                    "You can undo mistakes with",
                    "Press: Ctrl + Z",
                ],
                "image": None
            },
        ]
    },
    
    "practice": {
        "task_title": "Task - Improve the Body",
        "task_icon": "TOOL_SETTINGS",
        "task_text": [
            "Select Body",
            "Go to Edit Mode.",
            "Use Face Select.",
            "Add a Loop Cut.",
            "Select the top face.",
            "Extrude the top face.",
            "Make a small neck",
            "Shape the body so it looks like a simple human torso.",
            "Return to Object Mode.",
            "Save th file."
        ],
        "task_image": None,
        "checks": [
            {
                "text": "Create object named torso",
                "check": "check_body_improved",
                "hint": "The body should be larger and have more vertices than it had at the end of Lesson 1.",
                "icon": "OUTLINER_OB_MESH"
            },
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
            "Now we will create the main parts of the human.",
            "We need:",
            "- head",
            "- arms",
            "We will continue using cubes."
        ],
        "goal_image": None,
        "sections": [
            {
                "heading": "1. Create the head",
                "icon": "SCENE_DATA",
                "content": [
                    "Press: Shift + A",
                    "Choose: Mesh -> Cube",
                    "A new cube appears.",
                    "Rename it: Head",
                    "Move it above the body.",
                    "Use: G -> Z",
                    "Scale it until it has the size of a simple head."
                ],
                "image": None
            },
            {
                "heading": "2. Shape the head",
                "icon": "RESTRICT_SELECT_OFF",
                "content": [
                    "Select Head",
                    "Press: Tab",
                    "Go to Edit Mode.",
                    "Use Face Select.",
                    "Select faces and scale them.",
                    "You can make the head:",
                    "- wider",
                    "- smaller",
                    "- taller",
                    "Do not make a complicated face",
                    "We will paint the face later.",
                ],
                "image": None
            },
            {
                "heading": "3. Create one arm",
                "icon": "ORIENTATION_GLOBAL",
                "content": [
                    "Add another cube",
                    "Rename it: Arm.L",
                    "Move it to the left side of the body.",
                    "Scale it.",
                    "Press: Tab",
                    "Use Edit Mode to change its shape.",
                    "Add a Loop Cut if you need one.",
                    "You can make the arm slightly thinner near the hand."
                ],
                "image": None
            },
            {
                "heading": "4. Duplicate the arm",
                "icon": "DRIVER_ROTATIONAL_DIFFERENCE",
                "content": [
                    "We already made one arm.",
                    "We can make the other arm from it.",
                    "Check you in Object Mode.",
                    "Select: Arm.L",
                    "Press: Shift + D",
                    "Move the copy to the other side.",
                    "Click",
                    "Rename it: Arm.R",
                    "Now we have two arms."
                ],
                "image": None
            },
        ]
    },
    
    "practice": {
        "task_title": "Task - Create the complete basic character",
        "task_icon": "TOOL_SETTINGS",
        "task_text": [
            "You should have:",
            "- Head",
            "- Neck",
            "- Body",
            "- Arm.L",
            "- Arm.R",
            "- Leg.L",
            "- Leg.R",
            " ",
            "Use cubes.",
            "Edit the cubes.",
            "Change their shape.",
            "Move them into the correct positions."
        ],
        "task_image": None,
        "checks": [
            {
                "text": "Create object named Head",
                "check": "check_head_exists",
                "hint": "Look in the Outliner. Do you see an object named 'Head'? If not, select your cube and rename it to 'Head' in the Outliner (double-click the name).",
                "icon": "OUTLINER_OB_MESH"
            },
            {
                "text": "Create object named Arm.L",
                "check": "check_arm_left_exists",
                "hint": "Look in the Outliner. Do you see an object named 'Arm.L'? If not, select your cube and rename it to 'Arm.L' in the Outliner (double-click the name).",
                "icon": "OUTLINER_OB_MESH"
            },
            {
                "text": "Create object named Arm.R",
                "check": "check_arm_right_exists",
                "hint": "Look in the Outliner. Do you see an object named 'Arm.R'? If not, select your cube and rename it to 'Arm.R' in the Outliner (double-click the name).",
                "icon": "OUTLINER_OB_MESH"
            },
            {
                "text": "Create object named Leg.L",
                "check": "check_leg_left_exists",
                "hint": "Look in the Outliner. Do you see an object named 'Leg.L'? If not, select your cube and rename it to 'Leg.L' in the Outliner (double-click the name).",
                "icon": "OUTLINER_OB_MESH"
            },
            {
                "text": "Create object named Leg.R",
                "check": "check_leg_right_exists",
                "hint": "Look in the Outliner. Do you see an object named 'Leg.R'? If not, select your cube and rename it to 'Leg.R' in the Outliner (double-click the name).",
                "icon": "OUTLINER_OB_MESH"
            },
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
            "You already made both sides of the arms.",
            "Now you will learn a faster way, and use for legs.",
            "This tool is called the \"Mirror Modifier\".",
            "Mirror can copy one side of an object to the other side."
        ],
        "goal_image": None,
        "sections": [
            {
                "heading": "1. What is Modifier?",
                "icon": "SCENE_DATA",
                "content": [
                    "A modifier changes and object without directly changing its original geometry.",
                    "You can add a modifier from the \"Modifiers\" tab.",
                ],
                "image": None
            },
            {
                "heading": "2. Add Mirror Modifier",
                "icon": "RESTRICT_SELECT_OFF",
                "content": [
                    "For this lesson, make a simple test cube.",
                    "Select the cube.",
                    "Go to the Modifiers tab.",
                    "Click: \"Add Modifier\"",
                    "Choose: \"Mirror\"",
                    "You will see another side of the object.",
                    "The Mirror Modifier is using an axis.",
                    "Usually we use the: X axis",
                    "for character symmetry."
                ],
                "image": None
            },
            {
                "heading": "3. Why use Mirror?",
                "icon": "ORIENTATION_GLOBAL",
                "content": [
                    "A human character is usually symmetrical.",
                    "The left side and right side are similar.",
                    "Instead of making both sides separately: \"Left side + Right side\".",
                    "We can make: One side -> Mirror -> Two sides",
                    "This saves time.",
                    "Because, if only duplicate when change one side other side not changed, and need to change manualy or delete side, duplicate and place to other side."
                ],
                "image": None
            },
            {
                "heading": "4. Mirror and the object origin",
                "icon": "DRIVER_ROTATIONAL_DIFFERENCE",
                "content": [
                    "Mirror uses the object's \"Origin\".",
                    "The origin is the small orange point connected to the object.",
                    "If the origin is in the wrong place, Mirror may create the copy in the wrong place.",
                    "This is why object position and origin are important."
                ],
                "image": None
            },
            {
                "heading": "5. Create one leg",
                "icon": "FULLSCREEN_ENTER",
                "content": [
                    "Add a cube",
                    "Rename it: Leg.L",
                    "Move to below the body.",
                    "Scale it.",
                    "Edit the cube until it looks like a simple leg."
                ],
                "image": None
            },
            {
                "heading": "6. Duplicate the leg using Mirror Modifier",
                "icon": "FULLSCREEN_ENTER",
                "content": [
                    "Select: Leg.L",
                    "Go to the Modifiers tab.",
                    "Click: \"Add Modifier\"",
                    "Choose: \"Mirror\"",
                    "Click: Origin -> Body"
                ],
                "image": None
            },
        ]
    },
    
    "practice": {
        "task_title": "Task - Create the complete basic character",
        "task_icon": "TOOL_SETTINGS",
        "task_text": [
            "You should have:",
            "- Head",
            "- Neck",
            "- Body",
            "- Arm.L",
            "- Arm.R (Completed in previous lessons)",
            "- Leg.L",
            "- Leg.R",
            " ",
            "Use cubes.",
            "Edit the cubes.",
            "Change their shape.",
            "Move them into the correct positions."
        ],
        "task_image": None,
        "checks": [
            {
                "text": "Create object named Leg.L",
                "check": "check_leg_left_exists",
                "hint": "Look in the Outliner. Do you see an object named 'Leg.L'? If not, select your leg and rename it to 'Leg.L' in the Outliner (double-click the name).",
                "icon": "OUTLINER_OB_MESH"
            },
            {
                "text": "Use Mirror for the other leg",
                "check": "check_leg_mirrored",
                "hint": "Select Leg.L, add a Mirror Modifier, and use the Body origin as the mirror object.",
                "icon": "MOD_MIRROR"
            },
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
            "Our character has the main body.",
            "Now we will add simple details.",
            "The character will still stay low-poly.",
            "You will learn:",
            " - What Low Poly means",
            " - How to shape hands",
            " - How to shape feet",
            " - How to add simple clothes",
            " - Flat vs Smooth shading"
        ],
        "goal_image": None,
        "sections": [
            {
                "heading": "1. What is Low Poly?",
                "icon": "SCENE_DATA",
                "content": [
                    "Low Poly means the model uses a small number of polygons.",
                    "Polygons are the faces that make the model.",
                    "Low-poly models are useful because they are:",
                    " - simple",
                    " - fast to render",
                    " - good for games",
                    " - easy to edit",
                    "We do not need thousands of faces for this character."
                ],
                "image": None
            },
            {
                "heading": "2. Shape the hands",
                "icon": "RESTRICT_SELECT_OFF",
                "content": [
                    "Select an arm.",
                    "Go to Edit Mode.",
                    "Add a Loop Cut if needed.",
                    "Use the faces to make a simple hand shape.",
                    "You do not need individual fingers.",
                    "The hand can be a simple shape."
                ],
                "image": None
            },
            {
                "heading": "3. Shape the feet",
                "icon": "ORIENTATION_GLOBAL",
                "content": [
                    "Select a leg.",
                    "Use Edit Mode.",
                    "Add a Loop Cut.",
                    "Select the bottom faces.",
                    "Move them forward.",
                    "Now the leg can look like:",
                    "Leg",
                    " |",
                    " |",
                    " └── Foot"
                ],
                "image": None
            },
            {
                "heading": "4. Add simple clothes",
                "icon": "DRIVER_ROTATIONAL_DIFFERENCE",
                "content": [
                    "We do not need to model complex clothes.",
                    "We can make simple shapes.",
                    "For example:",
                    " - shirt",
                    " - pants",
                    " - shoes",
                    "Some details will be added later with the texture."
                ],
                "image": None
            },
            {
                "heading": "5. Flat shading",
                "icon": "FULLSCREEN_ENTER",
                "content": [
                    "Select the character.",
                    "Right-click.",
                    "Choose: Shade Flat",
                    "This keeps the low-poly look.",
                    "You can also try: Shade Smooth",
                    "Look at the difference.",
                    "For this project, we will use the style that looks better for our character."
                ],
                "image": None
            }
        ]
    },
    
    "practice": {
        "task_title": "Task - Improve your character",
        "task_icon": "TOOL_SETTINGS",
        "task_text": [
            "Improve your character.",
            "Add:",
            " - simple hands",
            " - simple feet",
            " - simple clothes shapes",
            " - better proportions",
            "Do not add complex details.",
            "Apply Shade Flat to keep the low-poly look."
        ],
        "task-image": None,
        "checks": [
            {
                "text": "Arms have hand shapes",
                "check": "check_hands_exist",
                "hint": "Select an arm, go to Edit Mode. Select the end faces and scale/move them to create a simple hand shape.",
                "icon": "MESH_CUBE"
            },
            {
                "text": "Legs have feet shapes",
                "check": "check_feet_exist",
                "hint": "Select a leg, go to Edit Mode. Add a Loop Cut near the bottom, then move the bottom faces forward to create feet.",
                "icon": "MESH_CUBE"
            },
            {
                "text": "Flat shading applied",
                "check": "check_flat_shading",
                "hint": "Select your character, right-click and choose 'Shade Flat' to keep the low-poly look.",
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
            "Now we will add color.",
            "You will learn:",
            " - Material",
            " - Texture",
            " - UV",
            " - UV Editor",
            " - Texture Paint"
        ],
        "goal_image": None,
        "sections": [
            {
                "heading": "1. What is a Material?",
                "icon": "MATERIAL",
                "content": [
                    "A Material controls how a surface looks.",
                    "For example, we can change:",
                    " - color",
                    " - roughness",
                    " - metallic look"
                ],
                "image": None
            },
            {
                "heading": "2. Create a Material",
                "icon": "MATERIAL_DATA",
                "content": [
                    "Select the Body.",
                    "Open the Material Properties.",
                    "Click: New",
                    "You created a material.",
                    "Find: Base Color",
                    "Click the color.",
                    "Choose a color.",
                    "Now the body has a color."
                ],
                "image": None
            },
            {
                "heading": "3. Material or Texture?",
                "icon": "TEXTURE",
                "content": [
                    "They are different.",
                    "A material can give the character a color.",
                    "A texture is an image.",
                    "A texture can contain many details.",
                    "For example:",
                    " - Hair",
                    " - Eyes",
                    " - Mouth",
                    " - Shirt",
                    " - Pants",
                    " - Shoes",
                    "We can put all these details into a texture."
                ],
                "image": None
            },
            {
                "heading": "4. UV",
                "icon": "UV",
                "content": [
                    "A 3D model has three dimensions.",
                    "A texture is a 2D image.",
                    "UV tells Blender where each part of the 3D model goes on the 2D image.",
                    "Think of it like opening a 3D box and putting it on a flat paper."
                ],
                "image": None
            },
            {
                "heading": "5. UV Unwrap",
                "icon": "UV_SYNC_SELECT",
                "content": [
                    "Select the character.",
                    "Go to Edit Mode.",
                    "Select all faces.",
                    "Press: A",
                    "Press: U",
                    "Choose: Unwrap",
                    "Blender creates a UV layout.",
                    "Open the UV Editor to see it."
                ],
                "image": None
            },
            {
                "heading": "6. Create a texture",
                "icon": "IMAGE_DATA",
                "content": [
                    "Create a new image.",
                    "Give it a name: CharacterTexture",
                    "For this simple character, a small image is enough.",
                    "For example: 1024 x 1024"
                ],
                "image": None
            },
            {
                "heading": "7. Texture Paint",
                "icon": "BRUSH_DATA",
                "content": [
                    "Go to the Texture Paint workspace.",
                    "You can now paint on the character.",
                    "You can paint:",
                    " - skin",
                    " - hair",
                    " - eyes",
                    " - mouth",
                    " - shirt",
                    " - pants",
                    " - shoes"
                ],
                "image": None
            }
        ]
    },
    
    "practice": {
        "task_title": "Task - Paint the Character",
        "task_icon": "BRUSH_DATA",
        "task_text": [
            "Create the character texture.",
            "Paint:",
            "Face:",
            " - skin",
            " - hair",
            " - eyes",
            " - mouth",
            "Body:",
            " - shirt",
            "Legs:",
            " - pants",
            "Feet:",
            " - shoes",
            "Keep the design simple.",
            "Save your texture image.",
            "Use: Image -> Save As",
            "Save it as: CharacterTexture.png"
        ],
        "task-image": None,
        "checks": [
            {
                "text": "A material is created",
                "check": "check_material_exists",
                "hint": "Select an object, go to Material Properties. Do you see a material? If not, click 'New'.",
                "icon": "MATERIAL"
            },
            {
                "text": "UV Unwrap was performed",
                "check": "check_uv_unwrapped",
                "hint": "Select your character, go to Edit Mode, press A to select all, press U and choose 'Unwrap'.",
                "icon": "UV_SYNC_SELECT"
            },
            {
                "text": "Texture is painted",
                "check": "check_texture_painted",
                "hint": "Go to Texture Paint workspace and paint on your character. The character should have colors visible.",
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
            "Now we will make the character move.",
            "We need a rig.",
            "A rig is a skeleton for the character.",
            "The skeleton has bones.",
            "Bones control the character."
        ],
        "goal_image": None,
        "sections": [
            {
                "heading": "1. What is an Armature?",
                "icon": "ARMATURE_DATA",
                "content": [
                    "An Armature is Blender's skeleton system.",
                    "It contains bones.",
                    "A simple character can have:",
                    "Head",
                    " |",
                    "Spine",
                    " |",
                    "Hips",
                    " / \\",
                    "Leg Leg",
                    " |",
                    "Feet",
                    " ",
                    "Arms"
                ],
                "image": None
            },
            {
                "heading": "2. Add an Armature",
                "icon": "BONE_DATA",
                "content": [
                    "Go to Object Mode.",
                    "Press: Shift + A",
                    "Choose: Armature -> Single Bone",
                    "A bone appears.",
                    "Move it inside the character."
                ],
                "image": None
            },
            {
                "heading": "3. Edit the bones",
                "icon": "EDITMODE_HLT",
                "content": [
                    "Select the armature.",
                    "Press: Tab",
                    "You are now editing the bones.",
                    "Move the bone.",
                    "Create more bones by extruding.",
                    "Select the end of a bone.",
                    "Press: E",
                    "Move the mouse.",
                    "Click.",
                    "Now you have another bone.",
                    "Continue to create:",
                    " - hips",
                    " - spine",
                    " - head",
                    " - left arm",
                    " - right arm",
                    " - left leg",
                    " - right leg"
                ],
                "image": None
            },
            {
                "heading": "4. Name the bones",
                "icon": "OUTLINER_OB_ARMATURE",
                "content": [
                    "Good names help you understand the rig.",
                    "For example:",
                    "Hips",
                    "Spine",
                    "Head",
                    "Arm.L",
                    "Arm.R",
                    "Leg.L",
                    "Leg.R",
                    "Foot.L",
                    "Foot.R"
                ],
                "image": None
            },
            {
                "heading": "5. Test the rig",
                "icon": "POSE_HLT",
                "content": [
                    "Go to Pose Mode.",
                    "Select a bone.",
                    "Rotate it.",
                    "Press: R",
                    "Move it.",
                    "The bone moves.",
                    "At this point, the character mesh may not move with the bones.",
                    "We need to connect them."
                ],
                "image": None
            },
            {
                "heading": "6. Parent the character",
                "icon": "CONSTRAINT_BONE",
                "content": [
                    "Select the character mesh.",
                    "Then select the armature.",
                    "Use: Ctrl + P",
                    "Choose: With Automatic Weights",
                    "Blender will try to connect the character to the skeleton."
                ],
                "image": None
            },
            {
                "heading": "7. Test it",
                "icon": "POSE_HLT",
                "content": [
                    "Go to Pose Mode.",
                    "Select an arm bone.",
                    "Rotate it.",
                    "The arm should move.",
                    "Try a leg.",
                    "Try the head.",
                    "If the character moves correctly, the rig works."
                ],
                "image": None
            },
            {
                "heading": "8. If rigging is difficult",
                "icon": "INFO",
                "content": [
                    "Rigging can be difficult for a beginner.",
                    "If your character does not work correctly, do not stop the course.",
                    "You can use Mixamo to rig the character.",
                    "Mixamo can create a rig automatically and can also provide animations.",
                    "Later, after you practice more, you can return to Blender and learn manual rigging and weight painting."
                ],
                "image": None
            }
        ]
    },
    
    "practice": {
        "task_title": "Task - Rig your character",
        "task_icon": "ARMATURE_DATA",
        "task_text": [
            "Try to rig your character manually.",
            "Create the basic bones:",
            " - Hips",
            " - Spine",
            " - Head",
            " - Arm.L",
            " - Arm.R",
            " - Leg.L",
            " - Leg.R",
            " - Foot.L",
            " - Foot.R",
            "Connect the character with Automatic Weights.",
            "Test: arms, legs, head"
        ],
        "task-image": None,
        "checks": [
            {
                "text": "Armature exists",
                "check": "check_armature_exists",
                "hint": "Look in the Outliner. Do you see an Armature object? If not, add one with Shift+A -> Armature -> Single Bone.",
                "icon": "ARMATURE_DATA"
            },
            {
                "text": "Bones are named properly",
                "check": "check_bones_named",
                "hint": "Select the armature, go to Edit Mode. Check that bones have names like: Hips, Spine, Head, Arm.L, Arm.R, Leg.L, Leg.R.",
                "icon": "OUTLINER_OB_ARMATURE"
            },
            {
                "text": "Character is parented to armature",
                "check": "check_character_parented",
                "hint": "Select the character mesh, then Shift+Select the armature. Press Ctrl+P and choose 'With Automatic Weights'.",
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
            "Now we will animate the character.",
            "We will make a simple walking animation.",
            "You will learn:",
            " - What is animation",
            " - The Timeline",
            " - Keyframes",
            " - Walking poses"
        ],
        "goal_image": None,
        "sections": [
            {
                "heading": "1. What is animation?",
                "icon": "PLAY",
                "content": [
                    "Animation is a series of poses.",
                    "For example:",
                    "Pose 1",
                    "↓",
                    "Pose 2",
                    "↓",
                    "Pose 3",
                    "↓",
                    "Pose 4",
                    "↓",
                    "Pose 1",
                    "Blender plays these poses quickly.",
                    "This creates movement."
                ],
                "image": None
            },
            {
                "heading": "2. The Timeline",
                "icon": "TIME",
                "content": [
                    "At the bottom of Blender, you can see the Timeline.",
                    "The Timeline shows frames.",
                    "For example:",
                    "1  2  3  4  5  6  7  8  ...  24",
                    "A frame is one moment in the animation."
                ],
                "image": None
            },
            {
                "heading": "3. Keyframes",
                "icon": "KEYFRAME",
                "content": [
                    "A keyframe tells Blender:",
                    "> At this frame, the character has this pose.",
                    "We can create a keyframe with: I",
                    "Choose: LocRotScale",
                    "This saves the position, rotation, and scale.",
                    "For bones, we will mainly use rotation."
                ],
                "image": None
            },
            {
                "heading": "4. Walking reference",
                "icon": "VIEWZOOM",
                "content": [
                    "Use the walking reference image.",
                    "Look at the character's:",
                    " - left leg",
                    " - right leg",
                    " - left arm",
                    " - right arm",
                    " - body",
                    "We will copy the poses."
                ],
                "image": None
            },
            {
                "heading": "5. First pose",
                "icon": "POSE_HLT",
                "content": [
                    "Go to frame 1.",
                    "Create the first walking pose.",
                    "For example:",
                    " - left leg forward",
                    " - right leg backward",
                    " - right arm forward",
                    " - left arm backward",
                    "Select the bones.",
                    "Rotate them.",
                    "When the pose is ready:",
                    "Press: A",
                    "Select all the bones.",
                    "Press: I",
                    "Choose: LocRotScale",
                    "You created the first keyframe."
                ],
                "image": None
            },
            {
                "heading": "6. Second pose",
                "icon": "POSE_HLT",
                "content": [
                    "Go to frame 6.",
                    "Change the pose.",
                    "Move the legs.",
                    "Move the arms.",
                    "Create another keyframe."
                ],
                "image": None
            },
            {
                "heading": "7. Third pose",
                "icon": "POSE_HLT",
                "content": [
                    "Go to frame 12.",
                    "Create another pose.",
                    "Add a keyframe."
                ],
                "image": None
            },
            {
                "heading": "8. Fourth pose",
                "icon": "POSE_HLT",
                "content": [
                    "Go to frame 18.",
                    "Create another pose.",
                    "Add a keyframe."
                ],
                "image": None
            },
            {
                "heading": "9. Return to the first pose",
                "icon": "POSE_HLT",
                "content": [
                    "Go to frame 24.",
                    "Make the same pose as frame 1.",
                    "Add a keyframe.",
                    "Now the animation can repeat."
                ],
                "image": None
            },
            {
                "heading": "10. Play the animation",
                "icon": "PLAY",
                "content": [
                    "Press: Space",
                    "Watch your character.",
                    "The character should move through the different poses.",
                    "If the movement is too fast or too slow, move the keyframes."
                ],
                "image": None
            }
        ]
    },
    
    "practice": {
        "task_title": "Task - Create walking animation",
        "task_icon": "ACTION",
        "task_text": [
            "Create your walking animation.",
            "Use the reference image.",
            "Create the poses one by one.",
            "Frame 1: Start pose",
            "Frame 6: Step pose",
            "Frame 12: Mid-step pose",
            "Frame 18: Step pose (opposite side)",
            "Frame 24: Return to start pose",
            "Do not try to make it perfect.",
            "The goal is to understand:",
            "Pose -> Keyframe -> New Pose -> Keyframe -> Animation"
        ],
        "task-image": None,
        "checks": [
            {
                "text": "Keyframes are set",
                "check": "check_keyframes_exist",
                "hint": "In Pose Mode, move your character's bones, then press I and choose LocRotScale. You should see yellow diamonds on the timeline.",
                "icon": "KEYFRAME"
            },
            {
                "text": "Animation has at least 5 poses",
                "check": "check_animation_poses",
                "hint": "Create keyframes at frames 1, 6, 12, 18, and 24 with different walking poses.",
                "icon": "ACTION"
            },
            {
                "text": "Character moves when playing animation",
                "check": "check_character_moves",
                "hint": "Press Space to play the animation. The character should move through the different poses.",
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
            "Now we will finish the character.",
            "This is the final check before export.",
            "You will check:",
            " - Model",
            " - Texture",
            " - Rig",
            " - Animation"
        ],
        "goal_image": None,
        "sections": [
            {
                "heading": "1. Check the model",
                "icon": "MESH_CUBE",
                "content": [
                    "Look at the character from different directions.",
                    "Check:",
                    " - head",
                    " - body",
                    " - arms",
                    " - legs",
                    " - feet",
                    " - proportions",
                    "Fix anything that looks wrong."
                ],
                "image": None
            },
            {
                "heading": "2. Check the texture",
                "icon": "IMAGE_DATA",
                "content": [
                    "Check:",
                    " - face",
                    " - eyes",
                    " - hair",
                    " - clothes",
                    " - shoes",
                    "Make sure the texture is saved."
                ],
                "image": None
            },
            {
                "heading": "3. Check the rig",
                "icon": "ARMATURE_DATA",
                "content": [
                    "Go to Pose Mode.",
                    "Move:",
                    " - head",
                    " - arms",
                    " - legs",
                    "Check that the character moves correctly."
                ],
                "image": None
            },
            {
                "heading": "4. Check the animation",
                "icon": "ACTION",
                "content": [
                    "Play the walking animation.",
                    "Look for problems.",
                    "For example:",
                    " - arm moves in the wrong direction",
                    " - leg goes through the body",
                    " - character loses balance",
                    " - texture disappears",
                    " - character does not move",
                    "Fix the biggest problems."
                ],
                "image": None
            }
        ]
    },
    
    "practice": {
        "task_title": "Final Task - Complete your character",
        "task_icon": "FILE_TICK",
        "task_text": [
            "Finish your character.",
            "Your character should have:",
            "☐ Head",
            "☐ Body",
            "☐ Arms",
            "☐ Legs",
            "☐ Feet",
            "☐ Simple clothes",
            "☐ Hair",
            "☐ Eyes",
            "☐ Face",
            "☐ Material",
            "☐ UV",
            "☐ Texture",
            "☐ Rig",
            "☐ Walking animation",
            "Make one small change to your character without following the lesson.",
            "For example:",
            " - change the hair",
            " - change the clothes",
            " - change the colors",
            " - change the face",
            " - change the proportions",
            "This is your character."
        ],
        "task-image": None,
        "checks": [
            {
                "text": "All body parts exist",
                "check": "check_all_parts_exist",
                "hint": "Make sure you have: Head, Body, Arm.L, Arm.R, Leg.L, Leg.R, and Feet.",
                "icon": "OUTLINER_OB_MESH"
            },
            {
                "text": "Character has a texture",
                "check": "check_texture_applied",
                "hint": "Select your character, check that a texture is applied and visible in the viewport.",
                "icon": "IMAGE_DATA"
            },
            {
                "text": "Character has a rig",
                "check": "check_rig_complete",
                "hint": "Make sure your character has an armature with bones for: Hips, Spine, Head, Arms, and Legs.",
                "icon": "ARMATURE_DATA"
            },
            {
                "text": "Walking animation works",
                "check": "check_walk_cycle",
                "hint": "Press Space to play the animation. The character should look like it's walking.",
                "icon": "ACTION"
            }
        ]
    }
}

LESSONS[10] = {
    "title": "Lesson 10A: Export for a Game",
    "icon": "EXPORT",
    
    "lecture": {
        "goal_title": "Goal",
        "goal_icon": "LIGHT",
        "goal_text": [
            "Now we will export the character for a game.",
            "We will use FBX for the Unity example.",
            "You will learn:",
            " - How to save your project",
            " - How to check the character",
            " - How to export as FBX",
            " - How to import into Unity"
        ],
        "goal_image": None,
        "sections": [
            {
                "heading": "1. Save your Blender project",
                "icon": "FILE_BLEND",
                "content": [
                    "First save the Blender project.",
                    "Use: Ctrl + S",
                    "Make sure your project is saved."
                ],
                "image": None
            },
            {
                "heading": "2. Check the character",
                "icon": "VIEWZOOM",
                "content": [
                    "Before exporting, check:",
                    " - model",
                    " - texture",
                    " - rig",
                    " - animation",
                    "Play the animation one more time."
                ],
                "image": None
            },
            {
                "heading": "3. Select the character",
                "icon": "RESTRICT_SELECT_OFF",
                "content": [
                    "Select the objects that need to be exported.",
                    "For a rigged character, make sure the character mesh and armature are included."
                ],
                "image": None
            },
            {
                "heading": "4. Open Export",
                "icon": "EXPORT",
                "content": [
                    "Go to:",
                    "File -> Export -> FBX (.fbx)",
                    "A new window opens.",
                    "Choose where you want to save the file.",
                    "Use a name such as: LowPolyCharacter.fbx"
                ],
                "image": None
            },
            {
                "heading": "5. Export settings",
                "icon": "PREFERENCES",
                "content": [
                    "Check the FBX settings.",
                    "For a simple Unity character:",
                    " - Make sure 'Armature' is checked",
                    " - Make sure 'Animation' is checked",
                    " - Select 'NLA Strips' for animation",
                    "Then click: Export FBX"
                ],
                "image": None
            },
            {
                "heading": "6. Import into Unity",
                "icon": "IMPORT",
                "content": [
                    "Open your Unity project.",
                    "Put the FBX file into the Unity project folder.",
                    "Unity will import it.",
                    "Select the FBX.",
                    "Check:",
                    " - Model",
                    " - Rig",
                    " - Animation",
                    "You should be able to see your character and animation."
                ],
                "image": None
            }
        ]
    },
    
    "practice": {
        "task_title": "Task - Export your character",
        "task_icon": "EXPORT",
        "task_text": [
            "Export your character.",
            "1. Save your Blender project.",
            "2. Check the character is complete.",
            "3. Select the character mesh and armature.",
            "4. Go to File -> Export -> FBX (.fbx)",
            "5. Name it: LowPolyCharacter.fbx",
            "6. Check the settings.",
            "7. Click Export FBX.",
            "Then import it into a Unity project.",
            "Check that:",
            " - the character appears",
            " - the model has the correct size",
            " - the rig is detected",
            " - the walking animation is detected"
        ],
        "task-image": None,
        "checks": [
            {
                "text": "FBX file was created",
                "check": "check_fbx_exported",
                "hint": "Check your export folder. Do you see a file named LowPolyCharacter.fbx?",
                "icon": "EXPORT"
            },
            {
                "text": "Texture is embedded or included",
                "check": "check_texture_exported",
                "hint": "Make sure your texture is saved as a .png file and is in the same folder as your FBX.",
                "icon": "IMAGE_DATA"
            },
            {
                "text": "Animation is included",
                "check": "check_animation_exported",
                "hint": "In the FBX export settings, make sure 'Animation' is checked and 'NLA Strips' is selected.",
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
            "You can also use Blender to make a video.",
            "We will render the walking animation.",
            "You will learn:",
            " - How to add a camera",
            " - How to set up lighting",
            " - How to render an animation"
        ],
        "goal_image": None,
        "sections": [
            {
                "heading": "1. Add a camera",
                "icon": "CAMERA_DATA",
                "content": [
                    "Go to: Add -> Camera",
                    "Place the camera in front of the character.",
                    "Look through the camera.",
                    "You can use: Numpad 0",
                    "to look through the camera."
                ],
                "image": None
            },
            {
                "heading": "2. Set the camera",
                "icon": "CAMERA_DATA",
                "content": [
                    "Move the camera until the character is visible.",
                    "Try to keep the whole character inside the camera view."
                ],
                "image": None
            },
            {
                "heading": "3. Add a light",
                "icon": "LIGHT",
                "content": [
                    "You already have a light in the scene.",
                    "Move it if needed.",
                    "You can add another light with:",
                    "Shift + A -> Light",
                    "Use simple lighting.",
                    "You do not need a complicated setup."
                ],
                "image": None
            },
            {
                "heading": "4. Set the animation",
                "icon": "TIME",
                "content": [
                    "Make sure the Timeline contains your walking animation.",
                    "Set the start frame.",
                    "For example: 1",
                    "Set the end frame.",
                    "For example: 24"
                ],
                "image": None
            },
            {
                "heading": "5. Set the output",
                "icon": "OUTPUT",
                "content": [
                    "Open: Output Properties",
                    "Choose the resolution.",
                    "For example: 1920 x 1080",
                    "Choose the frame rate.",
                    "For example: 24 FPS",
                    "Choose where Blender should save the rendered frames/video."
                ],
                "image": None
            },
            {
                "heading": "6. Render",
                "icon": "RENDER_ANIMATION",
                "content": [
                    "Go to: Render -> Render Animation",
                    "Blender will render the animation.",
                    "Rendering can take some time.",
                    "Wait until it finishes."
                ],
                "image": None
            }
        ]
    },
    
    "practice": {
        "task_title": "Task - Create a video",
        "task_icon": "RENDER_ANIMATION",
        "task_text": [
            "Create a short video of your character walking.",
            "Your final scene should contain:",
            " - character",
            " - camera",
            " - light",
            " - walking animation",
            "Render the animation as a video file."
        ],
        "task-image": None,
        "checks": [
            {
                "text": "Camera is positioned correctly",
                "check": "check_camera_positioned",
                "hint": "Add a camera and position it so the character is visible in the viewport (press Numpad 0 to check).",
                "icon": "CAMERA_DATA"
            },
            {
                "text": "Animation is rendered",
                "check": "check_video_rendered",
                "hint": "Go to Render -> Render Animation. Check that a video file was created in your output folder.",
                "icon": "RENDER_ANIMATION"
            }
        ]
    }
}