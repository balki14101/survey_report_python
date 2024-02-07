from fpdf import FPDF

from SurveyAnalysisRecommendation import user_details,final_recommendations,overall_score,overall_range
import json

#Read data JSON
with open('data.json') as file:
    data = json.load(file)

#Read styles JSON
with open('styles.json') as file:
    styles = json.load(file)

#Read contant JSON
with open('contants.json') as file:
    static = json.load(file)

    
def get_font_style(config_data, style_name):
    print("from function",config_data.get(style_name, {}))
    return config_data.get(style_name, {})    



#generate pdf 
def create_pdf(content_dict, filename):
    # Create instance of FPDF class
    pdf = FPDF()

    header_title_style = get_font_style(styles, 'header_title')
    

    
# Page 1: General Information
    
    pdf.add_page()
    pdf.set_font(**header_title_style)
    # pdf.set_font(styles["font"]["arial"], styles["weight"]["bold"], styles["fontsize"]["large"])
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


# Page 2: Descriptions about Survey
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


    # Page 3: Survey Report
    pdf.add_page()
    pdf.set_font(styles["font"]["arial"], styles["weight"]["bold"], styles["fontsize"]["medium"])
    pdf.cell(styles["width"]["large"], styles["height"]["medium"], f'{static["score"]}: {overall_score}', styles["border"]["none"], styles["position"]["begin"])
    pdf.cell(styles["width"]["large"], styles["height"]["medium"], f'{static["level"]}: {overall_range}', styles["border"]["none"], styles["position"]["begin"])
    pdf.set_font(styles["font"]["arial"], styles["weight"]["bold"], styles["fontsize"]["normal"])
    pdf.cell(styles["width"]["large"], styles["height"]["medium"], static["range"], styles["border"]["none"], styles["position"]["begin"])

    #Range
    pdf.set_font(styles["font"]["arial"], '', styles["fontsize"]["small"])
    pdf.cell(styles["width"]["small"], styles["height"]["medium"], 'Normal (0-30)',styles["border"]["thin"], styles["position"]["same"])
    pdf.cell(styles["width"]["small"], styles["height"]["medium"], 'Moderate (31-70)', styles["border"]["thin"], styles["position"]["same"])
    pdf.cell(styles["width"]["small"], styles["height"]["medium"], 'Severe (70-100)', styles["border"]["thin"], styles["position"]["same"])
    # pdf.cell(40, 10, 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.', 0, 0)
    # pdf.cell(40, 10, 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.', 0, 0)
    # pdf.cell(40, 10, 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.', 0, 2)

    pdf.ln()

    #score analysis
    pdf.set_font(styles["font"]["arial"], styles["weight"]["bold"], styles["fontsize"]["medium"])
    pdf.cell(styles["width"]["large"], styles["height"]["medium"], static["analysis"], styles["border"]["none"], styles["position"]["begin"])
    # "Domain Analysis"
    pdf.set_font(styles["font"]["arial"], styles["weight"]["bold"], styles["fontsize"]["normal"])
    pdf.cell(styles["width"]["large"], styles["height"]["medium"], static["domainAnalysis"], styles["border"]["none"], styles["position"]["begin"])
    # Add chart for domain analysis
    pdf.image(static["domain"]["source"], static["domain"]["x"], None, static["domain"]["w"])
    
    #"Sub-Domain Analysis"
    pdf.set_font(styles["font"]["arial"], styles["weight"]["bold"], styles["fontsize"]["normal"])
    pdf.cell(styles["width"]["large"], styles["height"]["medium"], static["subdomainAnalysis"], styles["border"]["none"], styles["position"]["begin"])
    # Add chart for sub-domain analysis
    pdf.image(static["subdomain"]["source"], static["domain"]["x"], None, static["domain"]["w"])
   
    # Report
    pdf.set_font(styles["font"]["arial"], styles["weight"]["bold"], styles["fontsize"]["medium"])
    pdf.cell(styles["width"]["large"], styles["height"]["medium"], static["report"], styles["border"]["none"], styles["position"]["begin"])

    
    pdf.set_font(styles["font"]["arial"], '', styles["fontsize"]["normal"])

    for title, text in content_dict.items():
        pdf.cell(styles["width"]["large"], styles["height"]["small"], txt=title, ln=True)
        pdf.multi_cell(styles["width"]["zero"], styles["height"]["small"], txt=text)
        pdf.ln(4)

    # Recommendation
    pdf.set_font(styles["font"]["arial"], styles["weight"]["bold"], styles["fontsize"]["medium"])
    pdf.cell(styles["width"]["large"], styles["height"]["medium"], static["recommendation"], styles["border"]["none"], styles["position"]["begin"])        
    
    pdf.set_font(styles["font"]["arial"], '', styles["fontsize"]["normal"])
    pdf.multi_cell(styles["width"]["zero"], styles["height"]["small"], static["recommendation_content"])
    
    # Save the PDF to a file
    pdf.output(filename)


create_pdf(final_recommendations, "final_survey_report.pdf")
