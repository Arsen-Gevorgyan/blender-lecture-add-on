# Blender Character Lecture

## What is this?

This is a Blender add-on. It teaches beginners how to make a low-poly character step by step.

The add-on works like a teacher inside Blender. You read a lesson, you do the task, the add-on checks your work. If you did it right, you go to the next lesson. If not, you get a hint.

## Why did I make this?

I made this add-on because I wanted to help people learn Blender. Many tutorials are too hard for beginners. They use difficult words. They skip steps.

My add-on is different. It uses simple words. It explains every step. It checks your work automatically.

## What does it teach?

You learn how to make a low-poly character:

1. **Blender Basics** - move, rotate, scale objects
2. **Edit Mode** - change shapes with vertices, edges, faces
3. **Head, Arms, Legs** - build the complete body
4. **Mirror Modifier** - make symmetrical parts automatically
5. **Low-Poly Details** - simple hands and feet
6. **Materials and Texture** - paint your character
7. **Rigging** - add bones to make it move
8. **Animation** - make the character walk
9. **Final Check** - finish and review
10. **Export** - for game or video

## How does it work?

Every lesson has two parts:

- **Lecture** - you read and learn
- **Practice** - you do the task

The add-on checks your work automatically. For example:
- Do you have an object named "Body"? Yes or no.
- Is the Body taller than before? Yes or no.
- Is the Body in the center? Yes or no.

If all checks pass, you can go to the next lesson. If not, you get a helpful hint.

## Installation

1. Download the ZIP file
2. Open Blender 3.6
3. Go to Edit > Preferences > Add-ons
4. Click Install
5. Select the ZIP file
6. Enable "Blender Character Lecture"

## How to use

1. Press N in the 3D Viewport
2. Find the "Lecture" tab
3. Click "Start Course"
4. Read the lesson
5. Do the practice
6. Click "Next" when all checks are green

## What I used

I used Python to make this add-on. I used Blender's Python API.

The add-on has separate files:
- `__init__.py` - starts the add-on
- `properties.py` - saves progress
- `checks.py` - checks your work
- `lessons.py` - all lesson text
- `operators.py` - buttons and navigation
- `ui.py` - panels and display

## Features

- Text wraps on any panel size
- Automatic task checking
- Hints when you need help
- Progress tracking
- Simple English
- Step-by-step instructions
- Lecture and Practice system

## What I wanted to add

I wanted to add images to the lessons. But I had problems showing images in Blender panels. Blender has limitations for images in side panels. If people like this add-on and give good feedback, I will try to add images again.

## The hardest part

The hardest part was the project structure. At first, my code was very dirty. Everything was in one file. It was hard to find things and fix bugs.

I had to learn how to split the code into separate files. Each file has one job. This makes the code cleaner and easier to update.

Making the structure clean was a big challenge. But I learned a lot from it.

## About me

I am Arsen. I am also a beginner in Blender. I made a few models before. The biggest one is a ship that I used in a game. It is not very good, but I learned from it.

This is my first real project in Python. I learned Python while making this add-on.

## Problems I had

- Texture painting was hard to explain
- Image display in Blender panels was difficult
- Making lessons work for complete beginners
- Project structure was messy at first

## What I learned

I learned:
- Python for Blender
- How to make add-ons
- How to structure code cleanly
- How to write for beginners
- How to test and fix bugs
- How to plan a big project

## Time spent

This project took about 10 hours of coding time.

I tracked my time with Hackatime:
https://hackatime.hackclub.com/?project=blender_character_lecture

## Next steps

- Add images if people want them
- Add more lessons
- Add sound or video
- Translate to other languages
- Improve the code structure more

## This project was made for

This project was made for Hack Club Wrangler:
https://wrangler.hackclub.com/

## Author

Made by Arsen-Gevorgyan

## License

Free to use. If you share it, please give credit.