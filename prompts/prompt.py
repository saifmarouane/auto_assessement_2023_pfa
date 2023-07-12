import yaml

with open('prompts/prompt_feedback.yml', 'r', encoding='utf-8') as f:
    yml_feedback = yaml.safe_load(f)

########
# FEEDBACK
########
def get_feedback_conversation_prompt(context):
    return [
        {"role": "system", "content": yml_feedback['prompts']['base']['system'].replace("$CONTEXTE", context)},
        {"role": "assistant", "content": yml_feedback['prompts']['base']['assistant']},
    
        ]

def get_feedback_summarizer_prompt(conversation):
    level1=str(yml_feedback['prompts']['levels']['level1'])
    level2=yml_feedback['prompts']['levels']['level2']
    level3=yml_feedback['prompts']['levels']['level3']
    level4=yml_feedback['prompts']['levels']['level4']
    level5=yml_feedback['prompts']['levels']['level5']
    return [{"role": "assistant", "content": yml_feedback['prompts']['monitoring']['summarizer'].replace("$CONVERSATION", conversation).replace("$level1",level1).replace("$level2",level2).replace("$level3",level3).replace("$level4",level4).replace("$level5",level5)}]

        
        
def get_feedback_level_chouse():
        yml_feedback['prompts']['evaluation']['criteria'][0]['prompt']

