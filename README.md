# Breast Cancer Predictor Hmwk2

## Author
Saura Naderi

## Class
NU ANA 680

## Problem Statement
Cancer is a devastating disease that affects millions of people worldwide. Early detection and accurate prediction can significantly improve treatment outcomes. In this project, we aim to create a predictor for breast cancer using machine learning techniques.

## Description
This project utilizes the Wisconsin Breast Cancer Dataset from the UCI Machine Learning Repository. The dataset contains features that describe the characteristics of cell nuclei present in breast cancer biopsies. Our goal is to develop a predictive model that can classify tumors as benign or malignant based on these features.

## Methodology
### Data Cleaning
- Removed rows that did not contain integer values.
- Split the dataset into a training set (75%) and a test set (25%).

### Model
- We selected the Naive Bayes algorithm due to its superior accuracy compared to other models evaluated in the previous homework assignments.
- The trained model was exported as a pickle file.

### App Development
- Developed a web application using Flask to create a user-friendly interface for inputting data and viewing predictions.
- Deployed the application on Heroku for easy access and scalability.

## Support
I utilized ChatGPT to assist with writing and debugging the code, ensuring the application runs smoothly and meets the project requirements.

## Interesting to Note
During the development process, I encountered several challenges:
- The `.yml` file for GitHub Actions often started new lines for long code lines, causing the workflow to fail. This required multiple attempts to correct.
- Initial deployment issues on Heroku were resolved by reading the logs and identifying formatting issues in the `app.py` file.
- I had to manually adjust the class labels from `benign = 2` and `malignant = 4` to `0` and `1`, respectively, in the `app.py` file without retraining the model.

## References
Dua, D. and Graff, C. (2019). UCI Machine Learning Repository [https://archive.ics.uci.edu/ml/datasets/breast+cancer+wisconsin+(original)]. Irvine, CA: University of California, School of Information and Computer Science.
