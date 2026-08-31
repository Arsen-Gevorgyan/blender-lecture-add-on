# Blender Character Lecture

<p align="center">
  <a href="https://github.com/Arsen-Gevorgyan/blender-lecture-add-on/blob/main/blender_character_lecture.zip?raw=true">
    <strong>Download Blender Character Lecture</strong>
  </a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Blender-3.6-orange" alt="Blender 3.6">
  <img src="https://img.shields.io/badge/Python-3.10-blue" alt="Python 3.10">
  <img src="https://img.shields.io/badge/License-MIT-green" alt="MIT License">
</p>

<p align="center">
  A beginner-friendly Blender add-on that teaches you how to make a low-poly character step by step.
</p>

---

## Download

**Download the Add-on ZIP**

[![Download ZIP](https://img.shields.io/badge/Download-ZIP-blue)](https://github.com/Arsen-Gevorgyan/blender-lecture-add-on/blob/main/blender_character_lecture.zip?raw=true)

Download the ZIP file above and install it directly in Blender.

The add-on is made for **Blender 3.6**.

---

## Installation

1. Download **`blender_character_lecture.zip`**.
2. Open **Blender 3.6**.
3. Go to **Edit → Preferences**.
4. Open **Add-ons**.
5. Click **Install...**.
6. Select `blender_character_lecture.zip`.
7. Click **Install Add-on**.
8. Enable **Blender Character Lecture**.

You do **not** need to extract the ZIP before installing it.

---

## What is this?

This is a Blender add-on that teaches beginners how to make a low-poly character step by step.

The add-on works like a teacher inside Blender.

You read a lesson, do the task, and the add-on checks your work.

If you did it correctly, you can continue to the next lesson. If something is wrong, the add-on gives you a hint.

---

## Why did I make this?

I made this add-on because I wanted to help people learn Blender.

Many tutorials are difficult for beginners. They use difficult words or skip important steps.

My add-on is different.

It uses simple English, explains the steps, and checks your work automatically.

---

## What does it teach?

You learn how to make a low-poly character:

1. **Blender Basics** — move, rotate, and scale objects
2. **Edit Mode** — change shapes with vertices, edges, and faces
3. **Head, Arms, and Legs** — build the complete body
4. **Mirror Modifier** — make symmetrical parts automatically
5. **Low-Poly Details** — create simple hands and feet
6. **Materials and Texture** — add materials and paint your character
7. **Rigging** — add bones to make the character move
8. **Animation** — make the character walk
9. **Final Check** — finish and review your character
10. **Export** — export the character for a game or video

---

## How does it work?

Every lesson has two parts:

### Lecture

You read the explanation and learn the Blender concepts.

### Practice

You follow the instructions and build the character yourself.

The add-on checks your work automatically.

For example:

* Do you have an object named `Body`?
* Is the Body the correct size?
* Is the Body in the correct position?
* Did you create the required objects?
* Did you complete the required task?

If all checks pass, you can continue to the next lesson.

If something is wrong, the add-on gives you a helpful hint.

---

## How to use

After installing the add-on:

1. Open the **3D Viewport**.
2. Press **N** to open the sidebar.
3. Find the **Lecture** tab.
4. Click **Start Course**.
5. Read the lesson.
6. Complete the practice task.
7. Run the checks.
8. Fix anything that is wrong.
9. Continue when all checks are complete.

---

## Features

* Beginner-friendly lessons
* Simple English
* Step-by-step instructions
* Automatic task checking
* Hints when something is wrong
* Progress tracking
* Lecture and Practice system
* Text wrapping for different panel sizes
* Separate code files for easier development

---

## Project Structure

The add-on is separated into different Python files:

```text
blender_character_lecture/
├── __init__.py
├── assets/
├── checks.py
├── lessons.py
├── operators.py
├── properties.py
└── ui.py
```

### What the files do

* `__init__.py` — starts and registers the add-on
* `properties.py` — stores course progress and properties
* `checks.py` — checks the user's work
* `lessons.py` — contains the lesson content
* `operators.py` — handles buttons and course navigation
* `ui.py` — creates the Blender interface
* `assets/` — contains project assets

---

## What I wanted to add

I wanted to add images to the lessons.

However, I had problems displaying images inside Blender panels. Blender has some limitations when displaying images in side panels.

If people like this add-on and give good feedback, I would like to try adding images again.

---

## The hardest part

The hardest part was the project structure.

At first, my code was very messy. Most things were in one file, which made it difficult to find things and fix bugs.

I had to learn how to split the project into separate files.

Each file now has its own job.

This makes the code cleaner and easier to update.

Making the project structure clean was a big challenge, but I learned a lot from it.

---

## About me

I am Arsen.

I am also a beginner in Blender. I made a few models before. The biggest one is a ship that I used in a game.

It is not perfect, but I learned a lot from making it.

This is my first real project in Python. I learned Python while making this add-on.

---

## Problems I had

Some of the problems I had while making this project:

* Texture painting was difficult to explain
* Displaying images inside Blender panels was difficult
* Making the lessons simple enough for complete beginners
* Keeping the project structure clean
* Creating automatic checks for the user's work

---

## What I learned

While making this project, I learned:

* Python for Blender
* Blender's Python API
* How to make Blender add-ons
* How to structure code cleanly
* How to write lessons for beginners
* How to test and fix bugs
* How to plan a larger project

---

## Time spent

This project took about **10 hours of coding time**.

I tracked my time with Hackatime:

**[Hackatime Project](https://hackatime.hackclub.com/?project=blender_character_lecture)**

---

## Next steps

In the future, I would like to:

* Add images to the lessons
* Add more lessons
* Add sound or video
* Translate the lessons into other languages
* Improve the code structure
* Add more automatic checks

---

## Made for Hack Club Wrangler

This project was made for **Hack Club Wrangler**.

**[Hack Club Wrangler](https://wrangler.hackclub.com/)**

---

## Author

Made by **Arsen-Gevorgyan**

---

## License

Free to use.

If you share or modify this project, please give credit to the original author.