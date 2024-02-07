import json

from SurveyAnalysisRecommendation import overall_score,overall_range

#Read static_config JSON
with open('config_static_component.json') as file:
    static_config = json.load(file)

#Read dynamic_config JSON
with open('data.json') as file:
    dynamic_config = json.load(file)    

#for inserting dynamic data in static JSON file
def insert_name_into_json(json_file_path, name,key1,key2):
    with open(json_file_path, 'r') as f:
        data = json.load(f)
    
    data[key1][key2] = name
    
    with open(json_file_path, 'w') as f:
        json.dump(data, f, indent=4)    

def get_font_style(config_data, style_name):
    print("from function",config_data.get(style_name, {}))
    return config_data.get(style_name, {})  


# def get_data_from_dynamic_component_json(json_file_path):
#     with open(json_file_path, 'r') as f:
#         data = json.load(f)
#         return data.get('personalDetails', {}).get('Name', '')

#combaining static and dynamic values
def combaining_static_dynamic_data(static_text,dynamic_text):
    dynamic_score_text = str(dynamic_text)  # Convert to string if not already
    combined_text = static_text + dynamic_score_text
    return combined_text



#dynamic data    
username =   dynamic_config['response']['Name']
surveyName =   dynamic_config["response"]["SurveyName"]
date =   dynamic_config["response"]["Date"]

insert_name_into_json('config_static_component.json',username,'username_value','txt')
insert_name_into_json('config_static_component.json',surveyName,'survey_value','txt')
insert_name_into_json('config_static_component.json',date,'date_value','txt')

score = combaining_static_dynamic_data("Score: ",overall_score)
insert_name_into_json('config_static_component.json',score,'score_cell','txt')

level = combaining_static_dynamic_data("Level: ",overall_range)
insert_name_into_json('config_static_component.json',level,'level_cell','txt')





# Page:1
header_title_style = get_font_style(static_config, 'header_title')
header_cell = get_font_style(static_config,'header_cell')
logo_image = get_font_style(static_config,'logo_image')
line = get_font_style(static_config,'line')
userDetails_style = get_font_style(static_config,'userDetails')
username_title = get_font_style(static_config,'username_title')
username_value = get_font_style(static_config,'username_value')
survey_title = get_font_style(static_config,'survey_title')
survey_value = get_font_style(static_config,'survey_value')
date_title = get_font_style(static_config,'date_title')
date_value = get_font_style(static_config,'date_value')

# Page:2
about_survey_title = get_font_style(static_config,'about_survey_title')
about_survey_title_cell = get_font_style(static_config,'about_survey_title_cell')
about_survey_content = get_font_style(static_config,'about_survey_content')
about_survey_content_multi_cell = get_font_style(static_config,'about_survey_content_multi_cell')
accurate_survey_title = get_font_style(static_config,'accurate_survey_title')
accurate_survey_title_cell = get_font_style(static_config,'accurate_survey_title_cell')
accurate_survey_content = get_font_style(static_config,'accurate_survey_content')
accurate_survey_content_multi_cell = get_font_style(static_config,'accurate_survey_content_multi_cell')

# Page:3
score_title = get_font_style(static_config,'score_title')
score_cell = get_font_style(static_config,'score_cell')
level_cell = get_font_style(static_config,'level_cell')

range_title = get_font_style(static_config,'range_title')
range_title_cell = get_font_style(static_config,'range_title_cell')

range_content = get_font_style(static_config,'range_content')
range_cell_1 = get_font_style(static_config,'range_cell_1')
range_cell_2 = get_font_style(static_config,'range_cell_2')
range_cell_3 = get_font_style(static_config,'range_cell_3')

analysis_title = get_font_style(static_config,'analysis_title')
analysis_title_cell = get_font_style(static_config,'analysis_title_cell')

domain_analysis_title = get_font_style(static_config,'domain_analysis_title')
domain_analysis_title_cell = get_font_style(static_config,'domain_analysis_title_cell')
domain_image = get_font_style(static_config,'domain_image')

subdomain_analysis_title = get_font_style(static_config,'subdomain_analysis_title')
subdomain_analysis_title_cell = get_font_style(static_config,'subdomain_analysis_title_cell')
subdomain_image = get_font_style(static_config,'subdomain_image')
# analysis_title_cell = get_font_style(static_config,'analysis_title_cell')

report_title = get_font_style(static_config,'report_title')
report_title_cell = get_font_style(static_config,'report_title_cell')
report_content_font = get_font_style(static_config,'report_content_font')
report_content_cell = get_font_style(static_config,'report_content_cell')
report_content_multi_cell = get_font_style(static_config,'report_content_multi_cell')

recommandation_title = get_font_style(static_config,'recommandation_title')
recommendation_title_cell = get_font_style(static_config,'recommendation_title_cell')
recommendation_content = get_font_style(static_config,'recommendation_content')
recommendation_content_multi_cell = get_font_style(static_config,'recommendation_content_multi_cell')













