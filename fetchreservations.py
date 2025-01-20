# # -*- coding: utf-8 -*-
# """Fetch Reservations Script"""

# # Install necessary libraries
# # Removed Jupyter-specific pip install commands (!pip install)

# # Import necessary libraries
# from google.oauth2.service_account import Credentials
# import gspread
# import json

# # Step 1: Authenticate with your Google Service Account
# SERVICE_ACCOUNT_FILE = "service_account_key.json"  # Replace with your uploaded JSON key file

# # Set up credentials and authorize the gspread client
# creds = Credentials.from_service_account_file(
#     SERVICE_ACCOUNT_FILE,
#     scopes=["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
# )
# client = gspread.authorize(creds)
# print("Authentication successful!")

# # Step 2: Access your Google Sheet
# SPREADSHEET_ID = "1RN6xNReXS4l55peGUW5XJIamoD0jyh_sfbGD3FGtjwo"  # Replace with your Google Sheet ID

# # Open the sheet
# sheet = client.open_by_key(SPREADSHEET_ID).sheet1  # Access the first sheet

# # Fetch all rows and columns
# data = sheet.get_all_values()

# # Display the fetched data
# print("Google Sheet Data:")
# for row in data:
#     print(row)

# # Step 3: Save the data to a JSON file
# output_file = "google_sheet_data.json"
# with open(output_file, "w") as f:
#     json.dump(data, f, indent=4)

# print(f"Data saved to {output_file}")

# -*- coding: utf-8 -*-


# -*- coding: utf-8 -*-
"""Fetch Reservations Script"""

# Import necessary libraries
from google.oauth2.service_account import Credentials
import gspread
import json
import os

# Step 1: Authenticate with your Google Service Account
SERVICE_ACCOUNT_KEY = os.getenv("SERVICE_ACCOUNT_KEY")  # Load the key from the environment variable
if not SERVICE_ACCOUNT_KEY:
    raise ValueError("SERVICE_ACCOUNT_KEY environment variable is not set.")

# Parse the service account key from the environment variable
creds = Credentials.from_service_account_info(
    json.loads(SERVICE_ACCOUNT_KEY),
    scopes=["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
)

# Authorize the gspread client
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

