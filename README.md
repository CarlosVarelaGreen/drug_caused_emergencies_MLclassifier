# Naive-Bayes Classifier for Drug Consumption and Emergencies

This project covers the exploratory data analysis (EDA) and modeling of a Naive-Bayes classifier for a dataset related to drug consumption and emergencies among a cohort. The dataset is publicly available and was collected by Centro de Integración Juvenil, a Mexican non-profit association. The dataset involves records from 2024.

## Project Overview

The objective of this project is to analyze the dataset and try to build a Machine Learning classifier to predict emergency types based on drug consumption data. The analysis includes data cleaning, EDA, model training, and evaluation. The final model is stored and can be used to make predictions on new data.

## Repository Contents

- **instructions_to_run.pdf**: PDF with instructions on how to run the `emergency_type_classifier.py` script.
- **emergency_type_classifier.py**: Script for running the stored model and making predictions.
- **data_dictionary.xlsx**: Data dictionary for the dataset.
- **pacientes1erIngresoatratamiento.csv**: Original dataset downloaded from the official website.
- **test_samples.csv**: CSV file with samples to test the `emergency_type_classifier.py` script.
- **exploratory_data_analysis_modeling.ipynb**: Final notebook with EDA and model development pipeline.
- **naive_bayes_model.pkl**: Stored pickle model from the notebook.
- **cda_final_project_presentation.pdf**: Presentation for project deliverable.
- **patient_data.db**: Copy of the SQLite database used when testing and running the script.
- **dependencies_for_environment.txt**: List of environment pip dependencies from my development environment.

## Instructions

1. **Setup Environment**:
   - Create a virtual environment and install dependencies:
     ```sh
     python3 -m venv env
     source env/bin/activate
     make sure to pip install dependencies_for_environment.txt or other necessary dependencies
     ```

2. **Run the Classifier**:
   - Follow the steps in `instructions_to_run.pdf` to execute the `emergency_type_classifier.py` script.
   - Ensure the necessary files (e.g., `naive_bayes_model.pkl`, `test_samples.csv`) are in the appropriate directories as specified in the instructions.

4. **Explore the Data and Model**:
   - Open and run the `exploratory_data_analysis_modeling.ipynbb` notebook to see the EDA and model development process.

## Dataset

For this project we will be using a real-world dataset provided by Centro de Integracion Juvenil and Mexico´s Government. The dataset can be found in the following official link:
https://datos.gob.mx/busca/dataset/pacientes-de-primera-vez/resource/8a0005e9-cea9-402f-be72-df1cb51b5518

The dataset contians patient information attended for the first time for substance use and other mental health problems during the 1st quarter of 2024.

**Disclaimer**

The data has been marked as publically available and "free to use" as published in the Open Data Portal from the Government of Mexico: https://datos.gob.mx/busca/dataset

For any questions or issues, please open an issue on the repository or contact the maintainer.

