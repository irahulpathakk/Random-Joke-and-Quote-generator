# Random Quote & Joke Generator

    A simple Python-based console application that displays random **jokes**
    using `pyjokes` and **quotes** using `pyquotegen`.

## Features

    -   Random jokes in multiple languages (`en`, `de`, `es`, `it`, `gl`,
    `eu`)
    -   Joke categories: `neutral`, `chuck`, `all`
    -   Random quotes with categories: motivational, inspirational,
    attitude, success, technology, coding, friendship, funny, nature
    -   Menu-driven interface
    -   Terminal-based program

## Requirements

    Install dependencies:

    pip install pyjokes pyquotegen

##  How to Run

    Save the script, then run:

    python main.py

##  Code Structure

### random_joke()

Uses:

    pyjokes.get_joke(language=lng, category=cat)

### random_quote()

Uses:

    pyquotegen.get_quote(category=cat)

### main()

Displays menu and handles user choices.

## Sample Output

    __________________________________________

         RANDOM QUOTE AND JOKE GENERATOR

    __________________________________________

    Choose your option
    1. Joke
    2. Quote
    3. quit
    Enter your choice : 1
    choose category
    neutral --> Neutral geeky jokes
    chuck --> Chuck-style jokes
    all --> All types of joke
    Enter category code : neutral

    > Here's your joke!

##  License

For educational and personal use.
