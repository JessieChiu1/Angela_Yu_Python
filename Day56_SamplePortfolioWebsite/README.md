# Intro to Flask - Serving up Static and CSS Files

## Introduction

This is a small project aimed at learning how to create dynamic web applications with Flask by serving static files and CSS stylesheets. Instead of hardcoding HTML content, we will use Flask's `render_template` function to render HTML templates and build a simple website with a personalized name card. Here are some key guidelines to follow:

- **Template Organization**: All HTML templates should be placed in the `templates` folder within your Flask project directory.

- **Static Files**: All static files, including images and CSS files, must be stored in the `static` folder. It's important to note that Chrome can cache static files, so if you make changes to these files, you can force a refresh by holding down the SHIFT key and clicking the reload button in Chrome.

### Using HTML Templates

To get started, follow these steps:

1. Find an HTML template that suits your project's design requirements. You can explore websites like [html5up.net](https://html5up.net/) to find a wide variety of free templates.

2. Once you've chosen a template, integrate it into your Flask application by running your Flask app and rendering the selected HTML template using the `render_template` function.

3. To make development easier, you can enable the `contentEditable` property in the Chrome console by running `document.body.contentEditable=true`. This allows you to edit the webpage content directly in the browser. Remember to save the changes and replace your HTML file with the updated content.

## Required Libraries

Before you can run this project, you'll need to install the Flask library. You can do this by running the following command:

```bash
pip install Flask
```

## Challenges

After I ran `document.body.contentEditable=true` in the Chrome console, I tried to CTRL + S to save the new webpage to HTML but kept running into an issue where my file path changed to `./index_files/`. I ended up just copying the whole HTML in the dev console and pasting it into the `index.html` file.

I wonder if there is a frontend framework that goes with Flask so I don't need to hardcode stuff into the template. Something like React that can dynamically alter the webpage. I had to hardcode everything in vanilla HTML in the project tab.

## Potential Features

This is just a sample, but I can definitely find a template that works for me and flesh it out more.
