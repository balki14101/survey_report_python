from fpdf import FPDF

from PIL import Image
import json

overall_score=55
overall_range="moderate"
# Step 1: Read the JSON file
with open('data.json') as file:
    data = json.load(file)

print(data["personalDetails"])
user_details = data["personalDetails"]

with open('styles.json') as file:
    styles = json.load(file)

with open('contants.json') as file:
    static = json.load(file)

# create a pdf object
pdf = FPDF()

#Page1:
pdf.add_page()
pdf.set_font(styles["font"]["arial"], styles["weight"]["bold"], styles["fontsize"]["large"])
pdf.cell(styles["width"]["large"], styles["height"]["large"], static["header_title"], styles["border"]["none"], styles["position"]["begin"], styles["align"]["center"])
# add logo
pdf.image(static["logo"]["source"], static["logo"]["x"], static["logo"]["y"], static["logo"]["w"])
# add a line
pdf.line(styles["line"]["x1"], styles["line"]["y1"], styles["line"]["x2"], styles["line"]["y2"])

# user details
pdf.set_font(styles["font"]["arial"], '', styles["fontsize"]["normal"])
pdf.cell(styles["width"]["large"], styles["height"]["medium"], f'Person Name: {data["response"]["Name"]}',  styles["border"]["none"], styles["position"]["begin"])
pdf.cell(styles["width"]["large"], styles["height"]["medium"], f'Survey Title: {data["response"]["SurveyName"]}',  styles["border"]["none"], styles["position"]["begin"])
pdf.cell(styles["width"]["large"], styles["height"]["medium"], f'Date: {data["response"]["Date"]}',  styles["border"]["none"], styles["position"]["begin"])

#page2
pdf.add_page()
# about survey
pdf.set_font(styles["font"]["arial"], styles["weight"]["bold"], styles["fontsize"]["medium"])
pdf.cell(styles["width"]["large"], styles["height"]["medium"], static["about_title"],  styles["border"]["none"], styles["position"]["begin"])
# add a multi-line text
pdf.set_font(styles["font"]["arial"], '', styles["fontsize"]["normal"])
pdf.multi_cell(styles["width"]["zero"], styles["height"]["small"], static["about_survey_content1"])
pdf.multi_cell(styles["width"]["zero"], styles["height"]["small"], static["about_survey_content2"])

# accurate
pdf.set_font(styles["font"]["arial"], styles["weight"]["bold"], styles["fontsize"]["medium"])
pdf.cell(styles["width"]["large"], styles["height"]["medium"], static["accurate_title"],  styles["border"]["none"], styles["position"]["begin"])

pdf.set_font(styles["font"]["arial"], '', styles["fontsize"]["normal"])
pdf.multi_cell(styles["width"]["zero"], styles["height"]["regular"], static["accurate_content"])

# Page:3
pdf.add_page()
pdf.set_font(styles["font"]["arial"], styles["weight"]["bold"], styles["fontsize"]["medium"])
pdf.cell(styles["width"]["large"], styles["height"]["medium"], f'{static["score"]}: {overall_score}', styles["border"]["none"], styles["position"]["begin"])
pdf.cell(styles["width"]["large"], styles["height"]["medium"], f'{static["level"]}: {overall_range}', styles["border"]["none"], styles["position"]["begin"])
pdf.set_font(styles["font"]["arial"], styles["weight"]["bold"], styles["fontsize"]["normal"])
pdf.cell(styles["width"]["large"], styles["height"]["medium"], static["range"], styles["border"]["none"], styles["position"]["begin"])
# pdf.line(10, 180, 200, 180)
pdf.set_font('Arial', '', 10)
pdf.cell(styles["width"]["small"], styles["height"]["medium"], 'Normal (0-30)',styles["border"]["thin"], styles["position"]["same"])
pdf.cell(styles["width"]["small"], styles["height"]["medium"], 'Moderate (31-70)', styles["border"]["thin"], styles["position"]["same"])
pdf.cell(styles["width"]["small"], styles["height"]["medium"], 'Severe (70-100)', styles["border"]["thin"], styles["position"]["same"])
# pdf.cell(40, 10, 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.', 0, 0)
# pdf.cell(40, 10, 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.', 0, 0)
# pdf.cell(40, 10, 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.', 0, 2)

pdf.ln()



#score analysis
pdf.set_font(styles["font"]["arial"], styles["weight"]["bold"], styles["fontsize"]["medium"])
# pdf.cell(40, 10, 'Score Analysis', 0, 2)
pdf.cell(styles["width"]["large"], styles["height"]["medium"], static["analysis"], styles["border"]["none"], styles["position"]["begin"])
# Add text "Domain Analysis"
pdf.set_font(styles["font"]["arial"], styles["weight"]["bold"], styles["fontsize"]["normal"])
# pdf.cell(40, 10, 'Domain Analysis', 0, 2)  # Move to the next line after the cell
pdf.cell(styles["width"]["large"], styles["height"]["medium"], static["domainAnalysis"], styles["border"]["none"], styles["position"]["begin"])


# Add chart for domain analysis
# pdf.image('domain_barchart.png', 10, None, 100)  # Move to the next line after the image
pdf.image(static["domain"]["source"], static["domain"]["x"], None, static["domain"]["w"])

# Add text "Sub-Domain Analysis"
pdf.set_font(styles["font"]["arial"], styles["weight"]["bold"], styles["fontsize"]["normal"])
# pdf.cell(40, 10, 'Domain Analysis', 0, 2)  # Move to the next line after the cell
pdf.cell(styles["width"]["large"], styles["height"]["medium"], static["subdomainAnalysis"], styles["border"]["none"], styles["position"]["begin"])
# pdf.set_font('Arial', 'B', 12)
# pdf.cell(40, 10, 'Sub-Domain Analysis', 0, 2)  # Move to the next line after the cell

# Add chart for sub-domain analysis
# pdf.image('subdomain_barchart.png', 10, None, 100)  
pdf.image(static["subdomain"]["source"], static["domain"]["x"], None, static["domain"]["w"])


# add text
# pdf.set_font('Arial', 'B', 14)
pdf.set_font(styles["font"]["arial"], styles["weight"]["bold"], styles["fontsize"]["medium"])

# pdf.cell(40, 10, 'Recommandation', 0, 2)
pdf.cell(styles["width"]["large"], styles["height"]["medium"], static["recommendation"], styles["border"]["none"], styles["position"]["begin"])
# pdf.set_font('Arial', '', 12)
pdf.set_font(styles["font"]["arial"], '', styles["fontsize"]["normal"])
pdf.multi_cell(0, 5, 'It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.\n\nThe point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using \'Content here, content here\', making it look like readable English.')


# add a footer
# pdf.set_y(-15)
# pdf.set_font('Arial', 'I', 8)
# pdf.cell(0, 10, 'Page %s' % pdf.page_no(), 0, 0, 'C')

# output the pdf
pdf.output('survey_report.pdf')

# #read your PDF
# with open("survey_report.pdf", "rb") as f:
#     pdf = PyPDF2.PdfFileReader(f)
#     page = pdf.getPage(0)
#     pdf_writer = PyPDF2.PdfFileWriter()
#     pdf_writer.addPage(page)

#     #add an image as watermark
#     watermark = Image.open("watermark.png")
#     watermark_width, watermark_height = watermark.size
#     page_width, page_height = page.mediaBox.upperRight
#     watermark_ratio = watermark_width / watermark_height
#     watermark_width = page_width * 0.2
#     watermark_height = watermark_width / watermark_ratio
#     x = (page_width - watermark_width) / 2
#     y = (page_height - watermark_height) / 2
#     watermark = watermark.resize((int(watermark_width), int(watermark_height)))
#     watermark.putalpha(128)
#     page.mergePage(watermark)

#     #write the watermarked pdf
#     with open("survey_report_watermarked.pdf", "wb") as output_file:
#         pdf_writer.write(output_file)