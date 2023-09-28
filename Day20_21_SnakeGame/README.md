# Snake Game with Tkinter 🐍🕹️

## Demo Video

<img src="https://github.com/JessieChiu1/Angela_Yu_Python/blob/main/Day20_21_SnakeGame/Snake-game-demo.gif" width="800px" alt="Snake Game Demo"/>

## Introduction

Welcome to the Snake Game! This classic Snake game is built using Python and the Tkinter library for the graphical user interface. It provides a fun and nostalgic gaming experience where you control a snake to collect food and grow longer without running into the walls or yourself.

The game is developed using object-oriented programming principles, making it easy to understand and extend.

## Main Game Code (main.py)

The heart of the Snake Game lies in the `main.py` script. Here's a brief overview of its key components:

- **Screen Setup & Variables**: The game's screen is initialized, and variables are set up, including the snake, food, and scoreboard.

- **Class Setup**: Instances of the Snake, Food, and Scoreboard classes are created to manage game objects and scoring.

- **Screen Event Listener**: The game listens for keyboard input to control the snake's direction (Up, Down, Right, Left).

- **Gameplay Loop**: The game runs in a loop, where the snake moves, and collisions with food, walls, and the snake's own body are detected.

    - When the snake collides with food, it extends its length, and the player's score increases.
    
    - Collisions with walls or the snake's body result in the game being reset.

- **High Score Feature**: The game includes a high score feature that saves the player's best score to a `data.txt` file.

- The game loop continues until the player chooses to exit.

## Future Improvements / Potential Features

While the game is fully functional, there is always room for improvement. Here are some potential areas for future enhancements:

- **Improved Graphics**: Tkinter's pixel system, while functional, could be refined for a more visually appealing game.

- **Additional Gameplay Features**: Consider adding new features or challenges to make the game even more engaging.

