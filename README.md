# Assumptions

1. Only images are given in a folder.  
2. I was asked to provide titles and links alongside summaries in a CSV file. So, I included the news titles and links but I don't think they are relevant in this context.  
   * "title_link.json" contains the titles and links.

# Execution

- **main.py** -> Program starts here  
- **ocr_gemini.py** -> Used to extract text from given images and summarize it  
- **google_drive.py** -> Used to push CSV files to a specific folder on Google Drive using API

# Visualization
![visual](visualization.png)

# Preview of Output

- **index.html** is a GPT-generated file that takes CSV as input and generates a table on the browser with the contents of the CSV file.

# Output

- The **output** folder contains:  
  * `summaries.csv`  
  * `setup guide google drive integration.pdf`  
  * `video.mkv`
