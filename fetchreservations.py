# -*- coding: utf-8 -*-
"""FetchReservations.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1NmDtnK0bkpTZg3nnAEUG6R881htsMJ3B
"""

!pip install --upgrade gspread google-auth

# Install required libraries
!pip install --upgrade gspread google-auth

# Import necessary libraries
from google.oauth2.service_account import Credentials
import gspread
import json

# Step 1: Authenticate with your Google Service Account
SERVICE_ACCOUNT_FILE = "service_account_key.json"  # Replace with your uploaded JSON key file

# Set up credentials and authorize the gspread client
creds = Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE,
    scopes=["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
)
client = gspread.authorize(creds)
print("Authentication successful!")

# Step 2: Access your Google Sheet
SPREADSHEET_ID = "1RN6xNReXS4l55peGUW5XJIamoD0jyh_sfbGD3FGtjwo"  # Replace with your Google Sheet ID

# Open the sheet
sheet = client.open_by_key(SPREADSHEET_ID).sheet1  # Access the first sheet

# Fetch all rows and columns
data = sheet.get_all_values()

# Display the fetched data
print("Google Sheet Data:")
for row in data:
    print(row)

# Step 3: Save the data to a JSON file
output_file = "google_sheet_data.json"
with open(output_file, "w") as f:
    json.dump(data, f, indent=4)

print(f"Data saved to {output_file}")