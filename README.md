# Flask Number Guessing Game

An interactive web application built using Flask, designed to provide a simple yet engaging number guessing game. The application generates a random number between 0 and 9, and players attempt to guess the correct number based on the feedback provided.

## Overview

The Flask Number Guessing Game is a demonstration of using Python's Flask framework to create a dynamic web application. It provides immediate feedback on each guess:
- If the guess is lower than the target number, the application will prompt the user to guess a higher number.
- If the guess is higher than the target number, the application will prompt the user to guess a lower number.
- If the guess matches the target number, the user is congratulated for finding the correct answer.

## Key Features

- **Real-Time Feedback**: The application evaluates the user's input and provides an instant response based on the guess.
- **Random Number Generation**: The target number is randomly generated upon server startup, providing a new challenge for each session.
- **Visual Feedback**: Each outcome (too high, too low, or correct) is accompanied by a different animated GIF, enhancing the user experience.
- **Lightweight and Modular**: The application is designed to be straightforward, making it an ideal starting point for learning Flask or web development.

## Prerequisites

- **Python 3.6+**: Ensure Python is installed on your system. You can download it from the official [Python website](https://www.python.org/downloads/).
- **Flask**: The web framework used to build this application.

## Installation

To set up and run the application locally, follow these steps:

1. **Clone the Repository**:
    ```bash
    git clone <your-repository-url>
    ```
   Replace `<your-repository-url>` with the actual GitHub repository URL.

2. **Navigate to the Project Directory**:
    ```bash
    cd flask-number-guessing-game
    ```

3. **Create a Virtual Environment (Recommended)**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

4. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Running the Application

To start the Flask development server, execute the following command:
```bash
python server.py
```

The application will be accessible at `http://127.0.0.1:5000/`. Open this URL in your web browser to interact with the game.

## Usage Instructions

1. **Start the Application**: Once the server is running, navigate to the root URL (`http://127.0.0.1:5000/`), where you'll be prompted to guess a number.
2. **Make a Guess**: Enter your guess directly in the URL path, like so: `http://127.0.0.1:5000/<your_guess>` (e.g., `http://127.0.0.1:5000/5` to guess the number 5).
3. **Receive Feedback**: The application will inform you if your guess is too high, too low, or correct, along with visual cues to guide you.

## Example URL Patterns

- **Guessing 3**: `http://127.0.0.1:5000/3`
- **Guessing 7**: `http://127.0.0.1:5000/7`

Each URL represents a different guess.

## Project Structure

The project follows a modular design for easy maintainability:
```
flask-number-guessing-game/
│
├── server.py               # Main application file
├── requirements.txt     # List of dependencies
└── README.md            # Project documentation
```

## Contributing

Contributions to this project are welcome and encouraged. If you wish to improve the application or add new features, please follow these steps:

1. Fork the repository.
2. Create a new branch (`feature-branch`).
3. Commit your changes.
4. Open a pull request describing the improvements made.

## License

This project is licensed under the MIT License, which permits open use, modification, and distribution of the codebase.

## Contact

For further information or queries, please contact:
- **Aditya Agarwal**: [aditya.agarwal1066@gmail.com](mailto:aditya.agarwal1066@gmail.com)

## Acknowledgements

- GIFs used in this application are sourced from Giphy.
