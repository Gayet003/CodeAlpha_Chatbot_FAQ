import re

# FAQ - Base de questions/réponses
faq = [
    {"question": "quels sont vos horaires", "answer": "Nous sommes ouverts de 9h à 18h."},
    {"question": "horaires", "answer": "Nous sommes ouverts de 9h à 18h."},
    {"question": "quand etes vous ouvert", "answer": "Nous sommes ouverts de 9h à 18h."},
    {"question": "comment contacter le support", "answer": "Envoyez un mail à support@exemple.com"},
    {"question": "contacter support", "answer": "Envoyez un mail à support@exemple.com"},
    {"question": "email support", "answer": "Envoyez un mail à support@exemple.com"},
    {"question": "livraison gratuite", "answer": "Oui pour toute commande supérieure à 50€."},
    {"question": "frais de livraison", "answer": "Oui pour toute commande supérieure à 50€."},
    {"question": "livraison offerte", "answer": "Oui pour toute commande supérieure à 50€."}
]

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    return text.split()

def jaccard_similarity(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    if not set1 or not set2:
        return 0
    intersection = set1.intersection(set2)
    union = set1.union(set2)
    return len(intersection) / len(union)

questions_clean = [clean_text(item['question']) for item in faq]

def get_response(user_input):
    user_tokens = clean_text(user_input)
    if not user_tokens:
        return "Veuillez poser une question valide."
    
    best_score = 0
    best_idx = 0
    for i, q_tokens in enumerate(questions_clean):
        score = jaccard_similarity(user_tokens, q_tokens)
        if score > best_score:
            best_score = score
            best_idx = i
    
    if best_score < 0.1:
        return "Désolé, je n'ai pas compris. Essayez : horaires, support, livraison"
    
    return faq[best_idx]['answer']

# Interface en ligne de commande
print("\n" + "="*50)
print("🤖 CHATBOT FAQ")
print("="*50)
print("Questions : horaires, support, livraison")
print("Tapez 'quit' pour quitter\n")

while True:
    user_input = input("🧑 Vous : ")
    if user_input.lower() in ['quit', 'exit', 'q']:
        print("🤖 Bot : Au revoir ! 👋")
        break
    if not user_input.strip():
        print("🤖 Bot : Veuillez écrire une question.")
        continue
    
    response = get_response(user_input)
    print("🤖 Bot : " + response)
    print("-"*40)
