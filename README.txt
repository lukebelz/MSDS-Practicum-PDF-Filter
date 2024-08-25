Practicum Project
=================

Welcome to the Practicum Project repository! Follow the instructions below to get started.

Instructions
------------

1. Clone this repository:
   git clone <repository-url>

2. Install required libraries:
   You need to install `pdfkit`, `wkhtmltopdf`, and ensure `re` and `pandas` are installed (they should already be in your environment).

   pip install pdfkit
   brew install wkhtmltopdf

3. Download the practicum Excel sheet and place it in the same directory you cloned the repository to.

4. Navigate to the directory where you cloned the repository using the terminal.

5. Run the script using the command below based on your needs:


Usage
-----

python practicum.py <dataFile> <optional: flags>

Examples:
---------
- Basic usage:
  python practicum.py "Practicum 2024.xlsx"

- With an international flag:
  python practicum.py "Practicum 2024.xlsx" -i

- With multiple flags:
  python practicum.py "Practicum 2024.xlsx" -i -p -remote

- With specific role and cloud service flags:
  python practicum.py "Practicum 2024.xlsx" -mle -aws


Flags
-----

General Flags:
--------------
- -i : International only
- -noExtraWork : No extra work required (limited to 16 hours, within Monday/Wednesday times)
- -noInterveiw : No interview required

Title Flags (Pick only one):
----------------------------
- -mle : Machine Learning Engineer titles
- -ds : Data Science or Data Scientist titles
- -o : Other titles (not MLE or DS)

Python Focus Flags (Pick only one):
-----------------------------------
- -p : Python only
- -notp : Not only Python

Work Location Flags (Pick only one):
------------------------------------
- -remote : Fully remote
- -hybrid : Partial remote and in-person

Cloud Service Flags (Pick only one):
------------------------------------
- -aws : Data stored in Amazon Web Services
- -azure : Data stored in Microsoft Azure
- -gcp : Data stored in Google Cloud Services