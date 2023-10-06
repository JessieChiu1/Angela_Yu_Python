# Intro to Flask

## Introduction

This is the first introduction to flask. I learned about the code to setup a basic flask app. I learned about Python decorator

### Project Tasks:
The primary goal of this project is to create a "Guess the Number" game website. Each `/<number>` route will provide the user with information about whether their guess is higher, lower, or correct.

## Required Libraries

To run this script, you'll need to install the following Python libraries using `pip`:

```bash
pip install Flask
```

## Challenges

I attempted to create a Python decorator to handle the button that leads to each `/<number>` page. While it worked for the `/` route, I encountered an issue when applying it to the `/<number>` routes. Specifically, I received an "AssertionError: View function mapping is overwriting an existing endpoint function: wrapper." This error only occurred when the decorator was attached to the `/<number>` route.

It's possible that I misunderstood when to use a Python decorator in Flask, but I ultimately resolved the issue by converting it into a helper function that each route calls. This approach successfully resolved the problem.