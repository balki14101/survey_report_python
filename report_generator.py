from fpdf import FPDF

from SurveyAnalysisRecommendation import user_details,final_recommendations,overall_score,overall_range
from config import header_title_style,header_cell,logo_image,line,userDetails_style,username_title,username_value,survey_title,survey_value,date_title,date_value,about_survey_title,about_survey_title_cell,about_survey_content,about_survey_content_multi_cell,accurate_survey_title,accurate_survey_title_cell,accurate_survey_content,accurate_survey_content_multi_cell
from config import score_title,score_cell,level_cell,range_title,range_content,range_title_cell,range_cell_1,range_cell_2,range_cell_3,analysis_title,analysis_title_cell,domain_analysis_title,domain_analysis_title_cell,domain_image,subdomain_analysis_title,subdomain_analysis_title_cell,subdomain_image,report_title,report_title_cell,report_content_font,report_content_cell,report_content_multi_cell
from config import recommandation_title,recommendation_title_cell,recommendation_content,recommendation_content_multi_cell
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


#generate pdf 
def create_pdf(content_dict, filename):
    # Create instance of FPDF class
    pdf = FPDF()

# Page 1: General Information
    
    pdf.add_page()
    #header
    pdf.set_font(**header_title_style)
    pdf.cell(**header_cell)

    # add logo
    # pdf.image(**dummy_from_function)

    # add a line
    pdf.line(**line)

    # user details
    pdf.set_font(**userDetails_style)
    pdf.cell(**username_value)
    pdf.cell(**survey_value)
    pdf.cell(**date_value)


# Page 2: Descriptions about Survey
    pdf.add_page()

    # about survey
    pdf.set_font(**about_survey_title)
    pdf.cell(**about_survey_title_cell)
    pdf.set_font(**about_survey_content)
    pdf.multi_cell(**about_survey_content_multi_cell)

    # accurate
    pdf.set_font(**accurate_survey_title)
    pdf.cell(**accurate_survey_title_cell)
    pdf.set_font(**accurate_survey_content)
    pdf.multi_cell(**accurate_survey_content_multi_cell)


    # Page 3: Survey Report
    #Score
    pdf.add_page()
    pdf.set_font(**score_title)
    pdf.cell(**score_cell)
    pdf.cell(**level_cell)

    #Range
    pdf.set_font(**range_title)
    pdf.cell(**range_title_cell)

    pdf.set_font(**range_content)
    pdf.cell(**range_cell_1)
    pdf.cell(**range_cell_2)
    pdf.cell(**range_cell_3)
    pdf.ln()

    #score analysis
    pdf.set_font(**analysis_title)
    pdf.cell(**analysis_title_cell)
    # "Domain Analysis"
    pdf.set_font(**domain_analysis_title)
    pdf.cell(**domain_analysis_title_cell)
    # # Add chart for domain analysis
    pdf.image(**domain_image)

    #"Sub-Domain Analysis"
    pdf.set_font(**subdomain_analysis_title)
    pdf.cell(**subdomain_analysis_title_cell)
    # Add chart for sub-domain analysis
    pdf.image(**subdomain_image)
   
    # Report
    pdf.set_font(**report_title)
    pdf.cell(**report_title_cell)
    
    pdf.set_font(**report_content_font)

    for title, text in content_dict.items():
        pdf.cell(**report_content_cell,txt=title)
        pdf.cell(**report_content_multi_cell,txt=text)
        pdf.ln(4)

    # Recommendation
    pdf.set_font(**recommandation_title)
    pdf.cell(**recommendation_title_cell)    

    pdf.set_font(**recommendation_content)
    pdf.multi_cell(**recommendation_content_multi_cell)
    
    # Save the PDF to a file
    pdf.output(filename)


create_pdf(final_recommendations, "final_survey_report.pdf")
