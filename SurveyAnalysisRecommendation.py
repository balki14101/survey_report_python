from fpdf import FPDF
import json
import matplotlib.pyplot as plt

# Step 1: Read the JSON file
with open('data.json') as file:
    read_data = json.load(file)

user_details = read_data["personalDetails"]

# Parse JSON string into Python dictionary
# data = json.loads(response)
data = read_data["response"]

# Findoverall percentage
total_score = sum(question["Score"] for question in data["Question"])
max_possible_score = len(data["Question"])  # Assuming maximum score of 1
total_percentage = (total_score / max_possible_score) * 100
print("Total Percentage:", total_percentage)




# Find unique domain names
domain_names = set()
for question in data["Question"]:
    domain_names.add(question["Domain"])

print(domain_names)    

# Find unique subdomain names
sub_domain_names = set()
for question in data["Question"]:
    sub_domain_names.add(question["Subdomain"])

print(sub_domain_names)   

# Calculate domain percentages
domain_with_percentages = {}
for domain_name in domain_names:
    filtered_data = [question for question in data["Question"] if question["Domain"] == domain_name]
    correct_answers = sum(question["Score"] for question in filtered_data)
    total_questions = len(filtered_data)
    percentage = (correct_answers / total_questions) * 100
    domain_with_percentages[domain_name] = percentage
domain_percentages = list(domain_with_percentages.values())
#overall score
overall_score = sum(domain_percentages) / len(domain_percentages)



# Calculate subdomain percentages
sub_domain_with_percentages = {}
for subdomain_name in sub_domain_names:
    filtered_data = [question for question in data["Question"] if question["Subdomain"] == subdomain_name]
    correct_answers = sum(question["Score"] for question in filtered_data)
    total_questions = len(filtered_data)
    percentage = (correct_answers / total_questions) * 100
    sub_domain_with_percentages[subdomain_name] = percentage
    print(filtered_data,correct_answers,total_questions,percentage,sub_domain_with_percentages)
subdomain_percentages = list(sub_domain_with_percentages.values())


#Generating bar-chart
domain_categories = list(domain_with_percentages.keys())
domain_values = list(domain_with_percentages.values())
print("Keys:", domain_categories,domain_values)


fig, ax = plt.subplots(figsize=(10,5))  # Adjust the figure size as needed

ax.barh(domain_categories, domain_values, height=0.35, label='Score', color='green')


# Add labels and legend
ax.set_xlabel('Values')
ax.set_title('Domain - Analysis')
ax.legend()

ax.set_xlim(0, 100)

# plot
# Rotate y-axis labels
plt.yticks(rotation=45, ha='right')  # Rotate labels 45 degrees
plt.savefig("domain_barchart.png")
plt.close()


subdomain_categories = list(sub_domain_with_percentages.keys())
subdomain_values = list(sub_domain_with_percentages.values())
print("Keys:", subdomain_categories,subdomain_values)

fig, ax = plt.subplots(figsize=(10,5))  # Adjust the figure size as needed

ax.barh(subdomain_categories, subdomain_values, height=0.35, label='Stack 1', color='green')


# Add labels and legend
ax.set_xlabel('Values')
ax.set_title('SubDomain - Analysis')
ax.legend()

# plot
# Rotate y-axis labels
plt.yticks(rotation=45, ha='right')  # Rotate labels 45 degrees
plt.savefig("subdomain_barchart.png")
plt.close()



#recommandation mapping
#combine domain and subdomains percentages    
all_category = {**domain_with_percentages,**sub_domain_with_percentages}   
print(all_category) 

# Parse JSON string into Python dictionary
recommendation_data = read_data["recommendation"]

for i in recommendation_data["overall"]:
    # Access data from each row
    rating = i['Rating']
    range = i['Range']
    
    #split the range
    range = str(range)
    if "-" in range:
        lower = int(range.strip("%").split("-")[0])
        upper = int(range.strip("%").split("-")[1]) 
    elif ">" in range:
        lower = int(range.strip("%").strip(">"))
        upper = 100
    elif "<" in range:
        lower = 0
        upper = int(range.strip("%").strip("<"))
    else:
        lower = int(range.strip("%"))
        upper = lower 

    print(lower,upper,end="\n \n")    
    #check for overall range
    if lower <=  overall_score <= upper:
        print(rating,end="\n \n")
        overall_range = rating
    else:
        overall_range = "nil"





final_recommendations = {}

for i in recommendation_data["scale"]:
    # Access data from each row
    rating = i['Rating']
    range = i['Range']
    level = i['LevelName']
    
    #split the range
    range = str(range)
    if "-" in range:
        lower = int(range.strip("%").split("-")[0])
        upper = int(range.strip("%").split("-")[1]) 
    elif ">" in range:
        lower = int(range.strip("%").strip(">"))
        upper = 100
    elif "<" in range:
        lower = 0
        upper = int(range.strip("%").strip("<"))
    else:
        lower = int(range.strip("%"))
        upper = lower 

    print(lower,upper,end="\n \n")    
    #check for recommendation
    if lower <=  all_category[level] <= upper:
        print(rating,end="\n \n")
        final_recommendations[level] = rating
    else:
        final_recommendations[level] = "nil"


print(final_recommendations,end="\n \n")  
print(overall_range,end="\n \n")  

