import pandas as pd
import re

# Path to the CSV file
file_path = r'C:\Users\lucie\Desktop\abc.csv'
# Read the CSV file
df = pd.read_csv(file_path)
# Function to extract majors based on the degree
def extract_majors(majors_str, degree_level):
    if isinstance(majors_str, str):  # Ensure the input is a string
        # Regex to match the specific degree level (本科, 硕士, 博士)
        pattern = f"【{degree_level}】([^,]+)"
        return ','.join(re.findall(pattern, majors_str))
    return ''  # Return an empty string if the input is not valid
# Create new columns for '本科', '硕士', '博士'
df['本科'] = df['需求专业'].apply(lambda x: extract_majors(x, '本科'))
df['硕士'] = df['需求专业'].apply(lambda x: extract_majors(x, '硕士'))
df['博士'] = df['需求专业'].apply(lambda x: extract_majors(x, '博士'))
# Select the relevant columns: id, 本科, 硕士, 博士
new_df = df[['id', '本科', '硕士', '博士']]
# Save the new DataFrame to a new CSV file
output_file_path = r'C:\Users\lucie\Desktop\processed_abc.csv'
new_df.to_csv(output_file_path, index=False, encoding='utf-8-sig')
print("CSV file has been processed and saved as 'processed_abc.csv' on your desktop.")
