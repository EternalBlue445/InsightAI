from PIL import Image
import google.generativeai as genai
import os


class GeminiOCR:
    def __init__(self):
        self.api_key = os.environ["GEMINI_API_KEY"] 
        self.model_name = 'gemini-2.5-flash'  
        self.initialize()
    
    def initialize(self):
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel(self.model_name)

    def summerize(self, paragraph, language):
        prompt = f"Summerize this following paragraph properly in {language}, remove all commas and quotes as well."
        combined_input = f"\"{paragraph}\"\n\n{prompt}"
        response = self.model.generate_content([combined_input])
        return response.text

    
    def extract_text(self, image_path, language, ):
        try:
            png_image = Image.open(image_path)
            prompt = f"Whats written in this image in {language}. Give me only the OCR text."
            response = self.model.generate_content([prompt, png_image])
            if response.text:
                return response.text.strip()
            return ""
        except ValueError as ve:
            print(f"Image conversion error: {str(ve)}")
            raise
        except Exception as e:
            print(f"Text extraction failed: {str(e)}")
            raise
    
    def verify_connection(self):
        try:
            test_model = genai.GenerativeModel('gemini-flash') 
            response = test_model.generate_content("Test connection")
            return True
        except Exception as e:
            print(f"API connection verification failed: {str(e)}")
            return False

