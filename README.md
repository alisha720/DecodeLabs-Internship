# Tech Stack Recommender

## Description

This project is a simple AI-based Tech Stack Recommendation System built using Python.

It takes a user's technical skills as input and recommends suitable job roles based on the similarity between the user's skills and the required skills for different roles.

## Features

- Takes user skills as input
- Reads role and skill data from a CSV file
- Uses TF-IDF Vectorizer for text representation
- Uses Cosine Similarity to compare skills
- Recommends suitable job roles
- Displays similarity scores

## Technologies Used

- Python
- Scikit-learn
- CSV

## How to Run

1. Make sure Python is installed.
2. Install Scikit-learn:

   pip install scikit-learn

3. Keep recommender.py and raw_skills.csv in the same folder.
4. Run the program:

   python recommender.py

5. Enter your skills when asked.

## Example Input

Python, SQL, Machine Learning

## Example Output

Recommended Roles:
- Data Scientist
- Machine Learning Engineer
- Backend Developer

## Algorithm Used

- TF-IDF Vectorization
- Cosine Similarity