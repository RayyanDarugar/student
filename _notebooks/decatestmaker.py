import pandas as pd

# Replace 'your_file_path.csv' with the actual path to your CSV file
file_path = '_notebooks/Hospitality & Tourism Exam 5.csv'

# Read CSV data into a DataFrame
df = pd.read_csv(file_path, header=None)

# Remove extra commas
df = df.apply(lambda x: x.str.replace(',', ''))

# Consolidate text
df = df.apply(lambda x: ' '.join(x.dropna()), axis=1)

# Assign headers if needed
df.columns = ['Text']

# Add question numbers
df['QuestionNumber'] = df.index + 1

# Display the cleaned DataFrame
print(df)