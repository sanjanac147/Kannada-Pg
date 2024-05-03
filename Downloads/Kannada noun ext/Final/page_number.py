
all_words = set()
for text in kannada_text_dict.values():
    all_words.update(set(text.split()))

subwords = set()
complete_words = set()
for word in all_words:
    for i in range(len(word)):
        for j in range(i + 1, len(word) + 1):
            subwords.add(word[i:j])
    complete_words.add(word)

with open("filtered_words_final.txt", "r", encoding="utf-8") as f:
    filtered_nouns = [line.strip() for line in f]

noun_page_mapping = {}

for noun in filtered_nouns:
   
    page_numbers = []

    if noun in complete_words or any(noun in subword for subword in subwords):
       
        for page_number, text in kannada_text_dict.items():
           
            if noun in text.split():
            
                page_numbers.append(page_number)
        #
        if page_numbers:
            noun_page_mapping[noun] = page_numbers

with open("pagenumber_mapping.txt", "w", encoding="utf-8") as f:
    for noun, page_numbers in noun_page_mapping.items():
        
        page_numbers_str = ' '.join(page_numbers)
       
        f.write(f"{noun}- {page_numbers_str}\n")



#cleaning optional (based on the file)

with open('noun_page_mapping.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()


with open('finalpg.txt', 'w', encoding='utf-8') as new_file:
  
    for line in lines:
      
        if "ಮೂಲಕ) ದೇಶವೆಂಬ ಪ್ರಾಚೀನವಾದ ದೇಶವಾಚಕದ ಮೂಲಕವಾಗಿಯೇ ಈ ಹೆಸರು ಉಗಮಿಸಿರುವುದು ಬಲುಮಟ್ಟಿಗೆ ಸಂಭಾವ್ಯವಾದುದು. ಆ ಪ್ರದೇಶದ ಬ್ರಾಹ್ಮಣರ ಒಂದು ಶಾಖೆ ದಕ್ಷಿಣಾಪಥಕ್ಕೆ ವಲಸೆ ಬಂದು, ಕಡಪ ಜಿಲ್ಲೆಯ ಸುತ್ತಮುತ್ತ ನೆಲಸಿದ ಕಾರಣವಾಗಿಯೇ ಅದರ ಒಂದು ನಿಷ್ಪನ್ನರೂಪವಾಗಿ ಮೊದಲು ಮುಲಿಕಿ/ಮುಲ್ಕಿ ಎಂಬುದು ಕಾಣಿಸಿಕೊಂಡು, ಬಳಿಕ ಲ" in line:
           
            line = line.replace("ಮೂಲಕ) ದೇಶವೆಂಬ ಪ್ರಾಚೀನವಾದ ದೇಶವಾಚಕದ ಮೂಲಕವಾಗಿಯೇ ಈ ಹೆಸರು ಉಗಮಿಸಿರುವುದು ಬಲುಮಟ್ಟಿಗೆ ಸಂಭಾವ್ಯವಾದುದು. ಆ ಪ್ರದೇಶದ ಬ್ರಾಹ್ಮಣರ ಒಂದು ಶಾಖೆ ದಕ್ಷಿಣಾಪಥಕ್ಕೆ ವಲಸೆ ಬಂದು, ಕಡಪ ಜಿಲ್ಲೆಯ ಸುತ್ತಮುತ್ತ ನೆಲಸಿದ ಕಾರಣವಾಗಿಯೇ ಅದರ ಒಂದು ನಿಷ್ಪನ್ನರೂಪವಾಗಿ ಮೊದಲು ಮುಲಿಕಿ/ಮುಲ್ಕಿ ಎಂಬುದು ಕಾಣಿಸಿಕೊಂಡು, ಬಳಿಕ ಲ", "")

       
        new_file.write(line)

