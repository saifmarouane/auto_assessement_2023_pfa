from gpt.gpt import get_chatgpt_response
from database.datafuncs import get_user_conversation_session_data, get_last_summary_context, get_user_conversation_history
from prompts.prompt import get_feedback_conversation_prompt, get_feedback_summarizer_prompt, get_feedback_level_chouse



import yaml

with open('prompts/prompt_feedback.yml', 'r', encoding='utf-8') as f:
    yml_feedback = yaml.safe_load(f)

def generate_prompt_base(user, session):
    conversation_prompt = [{"role": c[4], "content": c[3]} for c in get_user_conversation_session_data('feedback', user, session)]
    context = get_last_summary_context(user)
    if len(context) == 0:
        clean_context = "Pas de contexte"
    else:
        clean_context = context[0][0]
    prompt = get_feedback_conversation_prompt(clean_context) + conversation_prompt
   

    # Ajouter les questions en fonction du niveau choisi
    level_prompt = yml_feedback['prompts']['evaluation']['criteria'][0]['prompt']
    prompt.append({"role": "assistant", "content": level_prompt})
    print(prompt)  

    # Ajouter les questions spécifiques au niveau choisi

    return prompt    
      
    

def generate_new_conversation_context(user):
    conversation_prompt = [c[4].capitalize() + ": " + c[3] for c in get_user_conversation_history('feedback', user)]
    prompt_summary = get_feedback_summarizer_prompt('\n'.join(conversation_prompt))
    return get_chatgpt_response(prompt_summary, user, top_p_val=0.5)

def get_chatgpt_feedback_response(user, session, jawab):
    prompt = generate_prompt_base(user, session)
    prompt_with_temp_response = prompt + [{"role": "user", "content": jawab}]
    return get_chatgpt_response(prompt_with_temp_response, user, top_p_val=0.5)
