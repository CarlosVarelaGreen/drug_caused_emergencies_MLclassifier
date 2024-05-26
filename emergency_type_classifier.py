import pandas as pd
import pickle
import sqlite3
import sys
from sqlite3 import Error

# Instructions for running this script located in the "instructions_to_run.pdf file"

def classifier(csv_file_path):
    # Load the saved Naive Bayes model:
    with open('naive_bayes_model.pkl', 'rb') as model_file:
        model = pickle.load(model_file)

    # Create a db name:
    database = 'patient_data.db'

    # Load new samples from the CSV file:
    new_samples = pd.read_csv(csv_file_path)

    # Extract the features (all columns except 'id' and 'TARGET'):
    X_new = new_samples.drop(['id', 'TARGET'], axis=1)

    # Predict the target for new samples:
    predictions = model.predict(X_new)

    # Store the predictions in a DataFrame
    results_df = new_samples.copy()
    results_df['Predicted_TARGET'] = predictions

    try:
        # Connect to SQLite database:
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        print('Connecting to database...')
        
        # Create a new table (if not exists):
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS model_predictions (
                id TEXT,
                class TEXT
            )
        ''')
        
        # Insert the results into the table:
        for _, row in results_df.iterrows():
            cursor.execute('INSERT INTO model_predictions (id, class) VALUES (?, ?)', (row['id'], row['Predicted_TARGET']))
        
        # Commit and close the connection:
        conn.commit()
        print('Data inserted successfully.')
    except Error as e:
        print(f"An error occurred: {e}")
    finally:
        if conn:
            conn.close()
            print('Database connection closed.')

def main():
    if len(sys.argv) != 2:
        print("Usage: python emergency_type_classifier.py <input_csv>")
        sys.exit(1)

    input_csv = sys.argv[1]
    classifier(input_csv)

if __name__ == "__main__":
    
    main()
