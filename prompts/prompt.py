import yaml

with open('prompts/Yaml_Files/prompt_Recruitment.yml', 'r', encoding='utf-8') as f:
    yml_Recruitment = yaml.safe_load(f)
with open('prompts/Yaml_Files/prompt_Technologie.yml', 'r', encoding='utf-8') as f:
    yml_Technologie = yaml.safe_load(f)
with open('prompts/Yaml_Files/prompt_Management.yml', 'r', encoding='utf-8') as f:
    yml_Management = yaml.safe_load(f)    
with open('prompts/Yaml_Files/prompt_Business.yml', 'r', encoding='utf-8') as f:
    yml_Business = yaml.safe_load(f)    
with open('prompts/Yaml_Files/prompt_Communication.yml', 'r', encoding='utf-8') as f:
    yml_Commmunication = yaml.safe_load(f)    
with open('prompts/Yaml_Files/prompt_Membership.yml', 'r', encoding='utf-8') as f:
    yml_Membership = yaml.safe_load(f)    
with open('prompts/Yaml_Files/prompt_Ownership.yml', 'r', encoding='utf-8') as f:
    yml_Ownership = yaml.safe_load(f)
with open('prompts/Yaml_Files/prompt_BrandEvangelism.yml', 'r', encoding='utf-8') as f:
    yml_BrandEvangelism = yaml.safe_load(f)     
with open('prompts/Yaml_Files/prompt_Process.yml', 'r', encoding='utf-8') as f:
    yml_Process = yaml.safe_load(f) 
with open('prompts/Yaml_Files/prompt_Community.yml', 'r', encoding='utf-8') as f:
    yml_Community = yaml.safe_load(f)        
with open('prompts/Yaml_Files/prompt_Methodology.yml', 'r', encoding='utf-8') as f:
    yml_Methodology = yaml.safe_load(f)         
with open('prompts/Yaml_Files/prompt_Mentorship.yml', 'r', encoding='utf-8') as f:
    yml_Mentorship = yaml.safe_load(f)             
########
# app
########
def return_yml(app):
    #À chaque fois qu'une nouvelle application est appelé, nous générons automatiquement le fichier YAML correspondant pour extraire la prompte associée.
    if app == 'Recruitment':
        yml =yml_Recruitment 
    elif app == 'Technologie':
        yml=yml_Technologie
    elif app == 'Ownership':
        yml=yml_Ownership   
    elif app == 'Business':
        yml=yml_Business          
    elif app == 'Membership':
        yml=yml_Membership       
    elif app == 'Communication':
        yml=yml_Commmunication
    elif app == 'Management':
        yml=yml_Management    
    elif app == 'BrandEvangelism':
        yml=yml_Management 
    elif app == 'Process':
        yml=yml_Process  
    elif app == 'Community':
        yml=yml_Community
    elif app == 'Methodology':
        yml=yml_Methodology
    elif app == 'Mentorship':
        yml=yml_Mentorship
    return yml
def get_feedback_conversation_prompt(app,context):
    #Cette méthode utilise la prompte qui concerne le fichier YAML associé.
    yml=return_yml(app)
    #extraire les descriptions des niveau 
    level1=yml['prompts']['levels']['level1']
    level2=yml['prompts']['levels']['level2']
    level3=yml['prompts']['levels']['level3']
    level4=yml['prompts']['levels']['level4']
    level5=yml['prompts']['levels']['level5']
    return [
        {"role": "system", "content": yml['prompts']['base']['system'].replace("$CONTEXTE", context).replace("$level1",level1).replace("$level2",level2).replace("$level3",level3).replace("$level4",level4).replace("$level5",level5)},
        {"role": "assistant", "content": yml['prompts']['base']['assistant']},
        ]

#methode qui retourne une simulation d'une conversation entre le recruteur et le consultant
def get_feedback_summarizer_prompt(app,conversation):
    yml=return_yml(app)
    return [{"role": "assistant", "content": yml['prompts']['monitoring']['summarizer'].replace("$level1","level1").replace("$level2","level2").replace("$level3","level3").replace("$level4","level4").replace("$level5","level5")}]
    
        
        
def get_feedback_level_chouse():
        return None

