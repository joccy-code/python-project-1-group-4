# # 5)	Create a basic quiz game that:
# # •	Asks the user a series of multiple-choice questions.
# # •	Tracks the user's score based on correct answers.
# # •	Provides feedback after each question and a final score at the end of the quiz.
my_quiz = [{

        "question": "The battle of Adwa is a battle between which two countries?",
        "options": ["Ethiopia and Italy", "Ethiopia and France", "Ethiopia and Britain"],
        "correct_answer": "Ethiopia and Italy",
        "explanation": "The Battle of Adwa was a significant battle fought on March 1, 1896, between the Ethiopian Empire and the Kingdom of Italy. The battle took place near the town of Adwa in northern Ethiopia. The Ethiopian forces. led by Emperor Menelik II, successfully defeated the Italian forces, marking a significant victory for Ethiopia and a major setback for Italian colonial ambitions in Africa. The Battle of Adwa is often regarded as a symbol of African resistance against European colonization and is celebrated as a national holiday in Ethiopia."
        
    },
    {   "question": "Who was mahatam gandhi?",
        "options": ["An Indian independence leader", "A South African civil rights activist", "A British politician"],
        "correct_answer": "An Indian independence leader",
        "explanation": "Mahatma Gandhi was an Indian independence leader who led the country's struggle for independence from British rule. He is known for his philosophy of non-violent resistance and his efforts to promote social justice and equality."
    },
    {
        "question": "What was the outcome Lichemeda agreement in 1878?",
        "options": ["Accepttance of Yohaness II as king of king", "Menelik II becomes king of Ethiopia", "Italy gains control of Eritrea"],
        "correct_answer": "Accepttance of Yohaness II as king of king",
        "explanation": "The Lichemeda agreement in 1878 resulted in the acceptance of Yohaness II as the king of Ethiopia. This agreement was a significant event in Ethiopian history as it solidified Yohaness II's position as the ruler of Ethiopia and helped to maintain the country's independence during a time of increasing European colonization in Africa."
    },
    {   "question": "Who wrote the novel 'Sememen'?",
        "options": ["Fikremarkos desta", "Sisay Negusu", "Abe Gubegnaw"],
        "correct_answer": "Sisay Negusu",
        "explanation": "Sisay Negusu is the author of the novel 'Sememen'. The novel is a significant work in Ethiopian literature and explores themes of love, identity, and social issues. Sisay Negusu is known for his unique storytelling style and has contributed greatly to the literary scene in Ethiopia."
    },
    {   "question": "Nelson Mandela was imprisoned for how many years?",
        "options": ["27 years", "30 years", "25 years"],
        "correct_answer": "27 years",
        "explanation": "Nelson Mandela was imprisoned for 27 years. He was arrested in 1962 and released in 1990. During his imprisonment, he became a symbol of the anti-apartheid movement. Mandela's release marked a significant turning point in South Africa's history, leading to the end of apartheid and the establishment of a democratic government. He later became the first black president of South Africa in 1994."
    },
    {
        "question": "who is Kuwame Nkrumah?",
        "options": ["first president of Ghana", "first president of Nigeria", "first president of Kenya"],
        "correct_answer": "first president of Ghana",
        "explanation": "Kwame Nkrumah was the first president of Ghana. He played a crucial role in Ghana's independence movement and is considered one of the founding fathers of modern Africa. Nkrumah was a strong advocate for Pan-Africanism and worked towards the unity and development of African nations. He served as Ghana's president from 1957 until 1966, when he was overthrown in a coup d'état."
    },
    {
        "question": "What is the historical background of Goree Island?",
        "options": ["A former slave trading post", "A former colonial administrative center", "A former military fort"],
        "correct_answer": "A former slave trading post",
        "explanation": "Goree Island, located off the coast of Dakar, Senegal, has a significant historical background as a former slave trading post. During the transatlantic slave trade, Goree Island served as a major hub for the capture and export of enslaved Africans to the Americas. The island's history is marked by the suffering and resilience of those who were forcibly taken from their homeland. Today, Goree Island stands as a symbol of remembrance and education about the atrocities of the slave trade."
    },
    {
        "question": "What is the solomonic dynasty?",
        "options": ["A dynasty that ruled Ethiopia from the 13th to the 20th century", "A dynasty that ruled Egypt from the 10th to the 15th century", "A dynasty that ruled Greece from the 5th to the 1st century BC"],
        "correct_answer": "A dynasty that ruled Ethiopia from the 13th to the 20th century",
        "explanation": "The Solomonic dynasty was a ruling dynasty in Ethiopia that claimed descent from King Solomon and Queen of Sheba. This dynasty ruled Ethiopia from the 13th to the 20th century and played a significant role in the country's history."
    }]
score = 0
for q in my_quiz:
    print(q["question"])
    for i, option in enumerate(q["options"]):
        print(f"{i + 1}. {option}")
    user_answer = input("Enter your answer (1, 2, or 3): ")
    if user_answer == str(q["options"].index(q["correct_answer"]) + 1):
        print("Correct!")
        score += 1
    else:
        print("Incorrect.")
print(f"Your final score is: {score}/{len(my_quiz)}")
print("you are a great historian!")
print("Thank you for playing the quiz game!")