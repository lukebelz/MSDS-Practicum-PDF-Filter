import sys
import re
import pandas as pd
import pdfkit

class Practicum:
	def __init__(self, company, international, website, firstName, lastName, modality, modalityOther,  primaryAddress, secondaryAddress, extraWorkRequired, extraWorkRequiredExplination, description, dataLocation, dataLocationOther, dataSize, dataSizeOther, technologies, technologiesOther, pythonPrimary, pythonRatio, primaryProjectName, primaryProjectDesc, secondaryProjectDesc, allProjects, allProjectsOther, support, title, titleOther, interveiwRequired, interveiwRequiredOther, interveiwTopics):
		
		self.company = company
		self.international = international
		self.website = website
		self.firstName = firstName
		self.lastName = lastName
		self.modality = modality
		self.modalityOther = modalityOther
		self.primaryAddress = primaryAddress
		self.secondaryAddress = secondaryAddress
		self.extraWorkRequired = extraWorkRequired
		self.extraWorkRequiredExplination = extraWorkRequiredExplination
		self.description = description
		self.dataLocation = dataLocation
		self.dataLocationOther = dataLocationOther
		self.dataSize = dataSize
		self.dataSizeOther = dataSizeOther
		self.technologies = technologies
		self.technologiesOther = technologiesOther
		self.pythonPrimary = pythonPrimary
		self.pythonRatio = pythonRatio
		self.primaryProjectName = primaryProjectName
		self.primaryProjectDesc = primaryProjectDesc
		self.secondaryProjectDesc = secondaryProjectDesc
		self.allProjects = allProjects
		self.allProjectsOther = allProjectsOther
		self.support = support
		self.title = title
		self.titleOther = titleOther
		self.interveiwRequired = interveiwRequired
		self.interveiwRequiredOther = interveiwRequiredOther
		self.interveiwTopics = interveiwTopics

	def _cleanURL(self):
		if "http:" in self.website or "https:" in self.website:
			return self.website
		return "https://"+self.website

	def _cleanCompanyName(self):
		if "(" in self.company:
			return re.sub(r'\(.*?\)', '', self.company)
		return self.company

	def toHTML(self):
		html = f"""
		<div class="container">
			<h1><a href='{self._cleanURL()}'>{self.company}</a></h1>

			<div class="info">
				<center><a href='https://www.linkedin.com/search/results/companies/?keywords={self._cleanCompanyName()}'>LinkedIn</a> | <a href='https://www.indeed.com/companies/search?q={self._cleanCompanyName()}'>Indeed</a> | <a href='https://www.glassdoor.com/Search/results.htm?keyword={self._cleanCompanyName()}'>Glass Door</a> | <a href='https://www.comparably.com/search?q={self._cleanCompanyName()}'>Comparably</a></center><br />
			</div>

			<div class="info">
				<strong>Contact:</strong> {self.firstName} {self.lastName}<br />
				<strong>Location:</strong> {self.primaryAddress}<br />
				{"" if self.secondaryAddress == "Unknown" else "<strong>Other Locations ok?</strong> "+self.secondaryAddress+""}<br />
				<strong>Work Type:</strong> {self.modality if self.modalityOther == "Unknown" else self.modalityOther}<br />
				
				<p><strong>Team Description:</strong> {self.description}</p>
			</div>

			<div class="section">
				<h2>{self.primaryProjectName}</h2>
				<p><strong>Title:</strong> {self.title}</p>
				{"" if self.titleOther == "Unknown" else "<p><strong>Other Title:</strong> {}</p>".format(self.titleOther)}
				<p><strong>Project Description:</strong> {self.primaryProjectDesc}</p>

				{"" if self.secondaryProjectDesc == "Unknown" else "<p><strong>Other Project: </strong> {}</p>".format(self.secondaryProjectDesc)}
			</div>

			<div class="section">
				<h2>Details</h2>
				<p><strong>Python Not Main Language?</strong></span>  {self.pythonPrimary}</p>
				{"" if self.pythonRatio == "Unknown" else "<p><strong>Python Ratio: </strong> {}</p>".format(self.pythonRatio)}
				<p><strong>Data Location: </strong> {self.dataLocation if self.dataLocation != "Other:" else self.dataLocationOther}</p>
				{"" if self.dataLocationOther == "Unknown" and self.dataLocation != "Other:" else "<p><strong>Other Data Location: </strong> "+self.dataLocationOther+"</p>"}
				<p><strong>Data Size:</strong> {self.dataSize}</p>
				<p><strong>Technologies:</strong> {self.technologies}</p>
			</div>

			<div class="section">
				<h2>Extra Information</h2>
				<p><strong>International:</strong> {self.international}</p>
				<p><strong>Additional work required:</strong> {self.extraWorkRequired}</p>
				<p>{self.extraWorkRequiredExplination if self.extraWorkRequired == "Yes" else ""}</p>

				<p><strong>Work on all projects?</strong> {self.allProjects if self.allProjectsOther == "Unknown" else self.allProjectsOther}</p>
			</div>

			<div class="section">
				<h2>Interview and Support</h2>
				<p><strong>Interview Required:</strong> {self.interveiwRequiredOther if self.interveiwRequired == "Other:" else self.interveiwRequired}</p>
				<p><strong>Topics:</strong> {self.interveiwTopics}</p>
				<p><strong>Support Level:</strong> {self.support}</p>
			</div>
		</div>
		"""

		return html

def generateHTML(practicums):
	html = f"""<!DOCTYPE html>
		<html lang="en">
		<head>
			<meta charset="UTF-8">
			<meta name="viewport" content="width=device-width, initial-scale=1.0">
			<style>
				body {{
					font-family: Arial, sans-serif;
					margin: 0;
					padding: 20px;
					background-color: #f4f4f4;
				}}
				.container {{
					background-color: #ffffff;
					border-radius: 8px;
					padding: 20px;
					box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
					max-width: 800px;
					margin: auto;
				}}
				h1 {{
					text-align: center;
					color: #333;
				}}
				.section {{
					margin-bottom: 20px;
				}}
				.section h2 {{
					border-bottom: 2px solid #333;
					padding-bottom: 5px;
					color: #555;
				}}
			</style>
		</head>
		<body>"""

	for practicum in practicums:
		html += practicum.toHTML()
		html += "<br /><br />"

	html += f"""
		</body>
		</html>
		"""
	return html

def skipRow(row):
	if "-i" in sys.argv:
		if(row[1] == "No"):
			return True

	# Only pick one of these flags
	if "-mle" in sys.argv:
		if("Machine Learning Engineer" not in row[26] and "Machine Learning Engineer" not in row[27]):
			return True

	if "-ds" in sys.argv:
		if("Data Science" not in row[26] and "Data Science" not in row[27] and "Data Scientist" not in row[26] and "Data Scientist" not in row[27]):
			return True

	if "-o" in sys.argv:
		if("Data Science" in row[26] or "Data Science" in row[27] or "Data Scientist" in row[26] or "Data Scientist" in row[27] or "Machine Learning Engineer" in row[26] or "Machine Learning Engineer" in row[27]):
			return True
	#

	# Only pick one of these flags
	if "-p" in sys.argv:
		if(row[18] == "Yes"):
			return True

	if "-notp" in sys.argv:
		if(row[18] == "No"):
			return True
	#

	# Only pick one of these flags
	if "-remote" in sys.argv:
		if(row[5] != "Fully Remote" and row[5] != "Student Choice"):
			return True

	if "-hybrid" in sys.argv:
		if(row[5] != "Hybrid" and row[5] != "Student Choice" and row[5] != "Other:"):
			return True
	#

	# Only pick one of these flags
	if "-aws" in sys.argv:
		if("AWS" not in row[12]):
			return True

	if "-azure" in sys.argv:
		if("Azure" not in row[12]):
			return True

	if "-gcp" in sys.argv:
		if("GCP" not in row[12]):
			return True
	#

	if "-noExtraWork" in sys.argv:
		if(row[9] == "Yes, Explain:"):
			return True

	if "-noInterveiw" in sys.argv:
		if(row[28] != "No"):
			return True

	return False

if __name__ == '__main__':
	try:
		if(".xlsx" in sys.argv[1]):
			df = pd.read_excel(sys.argv[1])
		elif(".csv" in sys.argv[1]):
			df = pd.read_csv(sys.argv[1])
		else:
			print("Error: file arguement missing or incorrect")
			sys.exit(0)
	except FileNotFoundError as e:
		print(f"Error: {e}")
		sys.exit(0)
	except Exception as e:
		print(f"Error: {e}")
		sys.exit(0)

	pdfName = "Practicum 2024.pdf"
	df = df.fillna('Unknown')
	practicums = []

	for row in df.values:
		if skipRow(row):
			continue

		practicums.append(Practicum(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[19], row[20], row[21], row[22], row[23], row[24], row[25], row[26], row[27], row[28], row[29], row[30]))
	
	html = generateHTML(practicums)

	try:
		pdfkit.from_string(html, pdfName)
		print(f"PDF generated and saved at {pdfName}")
	except Exception as e:
		print(f"PDF generation failed: {e}")