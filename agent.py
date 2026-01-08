# agent.py
from llama_cpp import Llama
from tools import search_internet

# Model Yükleme
llm = Llama(
    model_path="./ai/models/qwen2.5-0.5b-instruct-q4_k_m.gguf",
    n_ctx=2048, # Hafızayı geniş tutalım
    n_threads=1,
    verbose=False
)

def run_agent(user_input):
    clean_input = user_input.strip()
    lower_input = clean_input.lower()
    
    triggers = ["search", "ara", "bul"]
    is_search = False
    query = ""

    for t in triggers:
        if lower_input.startswith(t + " "):
            is_search = True
            query = clean_input[len(t):].strip()
            break
            
    if is_search:
        # --- ARAMA MODU ---
        data = search_internet(query)
        
        if not data:
            return "Sonuç bulunamadı."
            
        context = data['summary']
        url = data['url']
        
        # Modele "Örnek" (Example) gösteriyoruz.
        prompt = f"""<|im_start|>system
            You are a helpful assistant.
            Task: Read the Search Results and answer the user's question in a COMPLETE SENTENCE.
            Do NOT just give a number or one word. Summarize the info.

            Example:
            User Question: How old is Biden?
            Search Results: Joe Biden was born in 1942.
            Answer: Joe Biden is currently 82 years old.

            Now it is your turn.<|im_end|>
            <|im_start|>user
            User Question: {query}
            Search Results:
            {context}

            Answer:<|im_end|>
            <|im_start|>assistant
            """
        
        # max_tokens arttırdım ki cümleyi yarım bırakmasın
        output = llm(prompt, max_tokens=200, stop=["<|im_end|>"], echo=False)
        generated_answer = output['choices'][0]['text'].strip()
        
        final_output = f"{generated_answer}\n\nResource: {url}"
        return final_output

    else:

        # Sohbet
        chat_prompt = f"""<|im_start|>system
            You are a friendly assistant. Answer in a complete sentence.<|im_end|>
            <|im_start|>user
            {clean_input}<|im_end|>
            <|im_start|>assistant
            """
        output = llm(chat_prompt, max_tokens=150, stop=["<|im_end|>"], echo=False)
        return output['choices'][0]['text'].strip()