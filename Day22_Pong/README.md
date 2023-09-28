# Pong Game with  Tkinter 🏓🕹️

## Demo Video

<img src="https://github.com/JessieChiu1/Angela_Yu_Python/blob/main/Day22_Pong/Pong-game-demo.gif" width="800px" alt="Pong Game Demo"/>

## Introduction

Welcome to the Pong Game! This classic Pong game is built using Python and the Tkinter library for the graphical user interface. It offers a fun and competitive gaming experience for two players. Player 1 controls the paddle using the 'W' and 'S' keys, while Player 2 controls the paddle with the 'Up' and 'Down' arrow keys.

## Main Game Code (main.py)

The core of the Pong Game can be found in the `main.py` script. Here's a brief overview of its key components:

- **Screen Setup & Variables**: The game's screen is initialized, and variables are set up, including the paddles, ball, and scoreboard.

- **Class Setup**: Instances of the Paddle, Ball, and Scoreboard classes are created to manage game objects and scoring.

- **Screen Event Listener**: The game listens for keyboard input to control the paddles' movements.

- **Game Loop**: The game runs in a loop, where the ball moves, collisions with walls and paddles are detected, and scores are updated.

    - If the ball hits the top or bottom wall, it bounces.
    
    - If the ball collides with a paddle, it bounces off accordingly.
    
    - If the ball goes out of bounds on one of the player's sides, the opposing player scores a point, and the ball is reset.

- The game loop continues until the players decide to exit.

## Future Improvements / Potential Features

While the game is functional, there is room for potential enhancements:

- **Initial Ball Speed**: Consider adjusting the initial ball speed to make the game faster or slower, based on player preferences.

- **Graphics and Animations**: Enhance the visual appeal of the game with improved graphics and animations.

- **Sound Effects**: Add sound effects to enhance the gaming experience.

