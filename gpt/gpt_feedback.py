from gpt.gpt import get_chatgpt_response
from database.datafuncs import get_user_conversation_session_data, get_last_summary_context, get_user_conversation_history
from prompts.prompt import get_feedback_conversation_prompt, get_feedback_summarizer_prompt, get_feedback_level_chouse





def generate_prompt_base(app,user, session):
    conversation_prompt = [{"role": c[4], "content": c[3]} for c in get_user_conversation_session_data(app, user, session)]
    context = get_last_summary_context(user,app)
    if len(context) == 0:
        clean_context = "Pas de contexte"
    else:
        clean_context = context[0][0]
    prompt = get_feedback_conversation_prompt(app,clean_context) + conversation_prompt
   

    # Ajouter les questions en fonction du niveau choisi
    #level_prompt = yml_feedback['prompts']['evaluation']['criteria'][0]['prompt']
    #prompt.append({"role": "assistant", "content": level_prompt})
    print(prompt)  
    

    # Ajouter les questions spécifiques au niveau choisi

    return prompt    
      
    

def generate_new_conversation_context(app,user):
    conversation_prompt = [c[4].capitalize() + ": " + c[3] for c in get_user_conversation_history(app, user)]
    prompt_summary = get_feedback_summarizer_prompt(app,'\n'.join(conversation_prompt))
    return get_chatgpt_response(prompt_summary, user, top_p_val=0.5)

def get_chatgpt_feedback_response(app,user, session, jawab):
    prompt = generate_prompt_base(app,user, session)
    prompt_with_temp_response = prompt + [{"role": "user", "content": jawab}]
    return get_chatgpt_response(prompt_with_temp_response, user, top_p_val=0.5)
