```markdown
# ChatWithPDF

ChatWithPDF is a Python application that allows you to extract text from PDF files using OCR (Optical Character Recognition) technology and then interactively chat with the extracted text.

## Installation

To get started with ChatWithPDF, follow these simple steps:

1. Clone this repository to your local machine using the following command:
   ```
   git clone https://github.com/MythicalMAxX/ChatWithPDF.git
   ```

2. Navigate into the project directory:
   ```
   cd ChatWithPDF
   ```

3. Install the required dependencies using pip:
   ```
   pip install -r requirements.txt
   ```

4. Update the API key:
   - Obtain an API key for your preferred OCR service (e.g., Google Cloud Vision API, Microsoft Azure Computer Vision API).
   - Open the `config.py` file.
   - Replace `"YOUR_API_KEY"` with your actual API key.

5. Add PDF files:
   - Place your PDF files in the `PDF` folder within the project directory.
   - You can add multiple PDF files for text extraction.

## Usage

Once you have installed the dependencies, updated the API key, and added PDF files, you can run the application using the following command:
```
python main.py
```

The application will extract text from the PDF files and provide an interactive chat interface where you can ask questions or make comments about the extracted text.

Feel free to explore the code and customize the application to suit your needs!

```
