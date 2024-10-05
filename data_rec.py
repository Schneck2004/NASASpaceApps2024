import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# Define the directory containing the CSV files
data_dir = 'C:/Users/guilh/Downloads/space_apps_2024_seismic_detection/space_apps_2024_seismic_detection/data/lunar/training/data/S12_GradeA'

# Define the list of file extensions to consider
file_extensions = ['csv']

# Initialize an empty DataFrame to store the data from all the files
data = pd.DataFrame()

print("Merging training data...")
# Iterate over all the files in the directory
for filename in os.listdir(data_dir):
    if any(filename.endswith(ext) for ext in file_extensions):
        print(f"Joining {filename}")
        # Read the data from the file
        file_data = pd.read_csv(os.path.join(data_dir, filename))

        # Append the data to the main DataFrame
        data = pd.concat([data, file_data])

# Assuming the first column is the label (0 for noise, 1 for seismic activity)
# and the rest of the columns are the features

# Define the list of columns to use as features
feature_columns = list(range(1, data.shape[1]))  # Assuming the first column is the label

X = data.iloc[:, feature_columns]
y = data.iloc[:, 0]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("Training...")
# Train a Random Forest Classifier
model = RandomForestClassifier(n_estimators=10, max_depth= 5, random_state=42, max_leaf_nodes=20, n_jobs=5, warm_start=True)
print("Model Fit...")
model.fit(X_train, y_train)

print("Evaluating...")
# Evaluate the model on the test set
accuracy = model.score(X_test, y_test)
print(f'Accuracy: {accuracy * 100:.2f}%')

print("Exporting...")
# Export the trained model
joblib.dump(model, 'data_recognizer.exe')

# Define the directory containing the input files
input_dir = 'C:/Users/guilh/Documents/Guilherme/Hackaton/NASASpaceApps2024/NASASpaceApps2024/input'

# Iterate over all the files in the input directory
for filename in os.listdir(input_dir):
    if filename.endswith('.csv'):
        # Read the input file
        input_data = pd.read_csv(os.path.join(input_dir, filename), sep='\t')

        # Extract the start times of the quakes
        start_times = input_data['Start Time']

        # Process the start times (e.g., convert to seconds, remove outliers)
        # For example, let's assume we want to remove any start times that are more than 10 seconds apart
        start_times = start_times[(start_times.diff() < 10).cumsum()]

        # Print the start times of the quakes
        print("Start times of the quakes:")
        print(start_times)