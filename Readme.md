# ML-lib

A simple machine learning library for building regression and classification models with data preprocessing utilities.

## Overview

Codex provides essential tools for machine learning workflows. It includes implementations for regression algorithms, classification models, evaluation metrics, and data scaling techniques.

## Features

-> Regression algorithms: Linear regression, KNN regressor
-> Classification models: KNN classifier, Logistic regression
-> Evaluation metrics: Accuracy score, Mean squared error
-> Data preprocessing: MinMax scaler, Standard scaler
-> Data splitting: Train-test split with configurable ratios

## Project Structure

-> regression/: Regression and classification model implementations
-> metrics/: Model evaluation metrics
-> scaler/: Feature scaling utilities
-> split/: Data splitting functions
-> datasets/: Sample datasets for testing
-> basemodel.py: Base model class with core functionality

## Getting Started

1. Import the required module from the library
2. Load your dataset using the sample data or your own
3. Scale your features using scaler utilities
4. Split data into train and test sets
5. Train your model using regression or classification algorithms
6. Evaluate using metrics

## Available Models

-> Linear Regression: For continuous value prediction
-> KNN Classifier: For classification tasks
-> KNN Regressor: For regression using k-nearest neighbors
-> Logistic Regression: For binary classification

## Scaling Options

-> Standard Scaler: Normalize features using mean and standard deviation
-> MinMax Scaler: Scale features to a fixed range

## Requirements

Python 3.6 or higher with standard libraries
