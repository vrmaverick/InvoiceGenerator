# Invoice Generator

This project is a Python-based invoice generator that creates PDF invoices from HTML templates. It uses Jinja2 for templating and pyhtml2pdf for HTML to PDF conversion.

![Invoice](invoice1.png)

## Features

* Generates PDF invoices from HTML templates.
* Uses Jinja2 for flexible template design.
* Converts HTML to PDF using WeasyPrint (via pyhtml2pdf).
* Randomly generates a word for the HTML file name.
* Includes sample invoice template (`templates/invoice.html`).

## Prerequisites

* Python 3.x
* pip (Python package installer)
* Jinja2: `pip install Jinja2`
* pyhtml2pdf: `pip install pyhtml2pdf`
* A webdriver for the browser in use
* (Optional) A local web server for testing HTML templates (e.g., Python's `http.server` or VS Code's Live Server).  However, this project is designed to *not* require a web server for PDF generation.

## Installation

1. Clone the repository:

   ```bash
   git clone [https://github.com/vrmaverick/InvoiceGenerator](https://www.google.com/search?q=https://github.com/your-username/invoice-generator.git)
   
2. Go to the project directory:
   
    ```bash
   cd InvoiceGenerator
    
4. Create and activate a virtual environment

    ```bash
    python3 -m venv .venv 
    .venv\Scripts\activate  # Activate (Windows)

5. Install the required packages:

    ```bash
    pip install -r requirements.txt

6. Execute:

    ```bash
    python main.py  # Or python3 main.py

# Project Structure:
invoice-generator/
├── main.py        # Main script
├── pdf.py         # PDF conversion functions
├── templates/     # HTML templates
│   └── invoice.html # Invoice template
├── requirements.txt # Dependencies
├── qr.jpeg # For template
└── README.md      # This file

# Working:
When the main file is executed the functions are used to create a dynamic template which will be named randomly and will appear in the directory , which is an HTML file that is personalized Invoice which can be then used in other projects using Selenium or a web-driver. 

Do let me know, if you have any queries, reach me out through my portfolio website.

   
