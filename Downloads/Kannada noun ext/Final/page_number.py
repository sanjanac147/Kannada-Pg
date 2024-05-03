
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
