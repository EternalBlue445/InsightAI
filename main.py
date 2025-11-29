# Assuming a folder with Newspaper images will be provided to this script

from ocr_gemini import GeminiOCR
import pandas as pd
import os
from google_drive import upload_file_to_drive
import csv
import json

gem = GeminiOCR()

root_path = "./News"

# We don't need to remove stopwords as we are summerizing the text with Gemini
"""
stopwords = pd.read_excel("bangla_stopwords.xlsx")

with open("notes.txt","r",encoding="utf8") as f:
    txt = f.read()
    ani = txt
    for w in stopwords["word_list"]:
        if w in txt:
            txt = txt.replace(w,"।")
"""
# Just to fill up the title and link column (It has nothing to do with the main program)
def read_from_json(file_path):
    with open(file_path, "r", encoding="utf8") as file:
        data = json.load(file)
    return data
final_csv_data = []
json_data = read_from_json("title_link.json")


# Push data into csv
def push_into_csv(file_path, column, rows):
    with open(file_path, mode="w", newline="", encoding="utf8") as file:
        writer = csv.writer(file)
        writer.writerow(column)
        writer.writerows(rows)

summaries = []

# Main Part
# Image -> Text -> Summerized text (Using Gemini)
# Can be faster if threading is introduced, process multiple images simultaneously.
def generate_summary(root_path):
    for filename in os.listdir(root_path):
        text = gem.extract_text(os.path.join(root_path,filename),"Bangla")
        summarized_text = gem.summerize(text,"Bangla")
        summaries.append(summarized_text)

gen_and_create = False

if gen_and_create:
    generate_summary(root_path)

    # Preparing data for CSV file
    for i in range(len(json_data)):
        final_csv_data.append([json_data[i]['title'],json_data[i]['url'],summaries[i]])

    column_names = ["title","link","summary"]

    # Create the csv file with the data
    push_into_csv("summaries.csv",column_names,final_csv_data)

# Upload the file to drive in a specific folder
else:
    upload_file_to_drive(os.environ["FOLDER_ID"],"summaries.csv")

