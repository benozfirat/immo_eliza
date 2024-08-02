# Real Estate Price Prediction Machine

Welcome to the **Real Estate Price Prediction Machine**! This application is designed to help you estimate the price of a property based on various features. Here’s a quick guide to help you understand and use the application effectively.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Inputs](#inputs)
- [Outputs](#outputs)
- [Technical Details](#technical-details)
- [Screenshots](#screenshots)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This application leverages machine learning to predict real estate prices. By inputting details about a property, you can get an estimated price based on a pre-trained model.

![Real Estate](https://miro.medium.com/v2/resize:fit:1200/0*NCO1DF14J42HEQWR.jpg)

## Features

- **User-Friendly Interface:** Easy-to-use interface built with Streamlit.
- **Detailed Inputs:** Provides detailed input fields to capture essential property features.
- **Instant Predictions:** Get instant price predictions with a single click.
- **Visual Feedback:** Warnings and success messages to guide user input and show results.

## 📦 Installation

To run this project, you need to have Python installed on your machine. You also need the following Python libraries:

### Required Libraries

- 🐼 **pandas**
- 🥒 **pickle**
- 🔴 **streamlit**

## Usage

1. **Launch the application:** Follow the installation steps to run the app.
2. **Enter property details:** Fill in the property details using the various input fields provided.
3. **Predict the price:** Click the "Predict 💡" button to get the estimated price.

## 🗂️ File Structure

 ```
IMMO_ELIZA/
│
├── Analysis/
│   ├── immo_eliza_analysis.ipynb
│   ├── data/
│   │   ├── change.py
│   │   ├── final_dataset.json
│   │   ├── formatted_json.json
│   │   ├── to_csv.py
│   │   ├── 2.immo_eliza_analysis.ipynb
│   │   ├── AnalysisAssignment.ipynb
│   │   ├── main.py
│   │   └── Untitled-1.ipynb
│   └── README.md
│
├── catboost_info/
│   ├── learn/
│   │   ├── events.out.tfevents
│   │   ├── tmp/
│   │   ├── learn_error.tsv
│   │   ├── time_left.tsv
│
├── ML/
│   ├── Encoder/
│   │   └── encoder.pkl
│   ├── Model/
│   │   ├── model.pkl
│   │   ├── model.py
│   ├── preprocessing/
│   │   └── preprocessing.py
│
├── Deployment/
│   └── deployment.py
│
├── .gitignore
├── README.md
└── requirements.txt
```

## Inputs

Here are the details you need to provide:

### Type 🏷️
- **Type of Sale:** Select between Sale or Rent.
- **Type of Property:** Choose between House or Apartment.
- **Subtype of Property:** Select the specific subtype of property from the dropdown list.

### Localisation 📍
- **Region:** Choose the region where the property is located.
- **Province:** Select the province from the dropdown list.
- **District:** Select the district from the dropdown list.
- **Postal Code:** Enter the postal code.

### General Infos 📄
- **State of Building:** Select the state of the building.
- **PEB:** Choose the PEB rating.
- **Flooding Zone:** Select the flooding zone status.

### Exterior 🌳
- **Number of Facades:** Enter the number of facades.
- **Surface of Plot:** Enter the surface area of the plot.
- **Swimming Pool:** Select if there is a swimming pool.
- **Terrace:** Select if there is a terrace.
- **Garden:** Select if there is a garden and its area.

### Interior 🛏️
- **Living Area:** Enter the living area.
- **Number of Bedrooms:** Use the slider to select the number of bedrooms.
- **Number of Bathrooms:** Use the slider to select the number of bathrooms.
- **Number of Showers:** Use the slider to select the number of showers.
- **Number of Toilets:** Use the slider to select the number of toilets.
- **Kitchen:** Select the type of kitchen.

## Outputs

- **Estimated Price:** The application will display the estimated price of the property based on the input details.

## Technical Details

- **Preprocessor:** A pre-trained encoder is used to preprocess the input data.
- **Model:** A pre-trained machine learning model is used to predict the property price.
- **Backend:** Streamlit is used for building the user interface.
- **Dependencies:** pandas, pickle, and streamlit are some of the key dependencies.


---

## Timeline 🕙

- **Day 1:** Setup and Installation

- **Day 2:**  Feature Implementation

- **Day 3:**  Testing and Optimization

- **Day 4:**  Deployment


--- 
Thank you for using the Real Estate Price Prediction Machine! If you have any questions or feedback, feel free to reach out. Happy predicting! 🏠💰
