import re

def process_and_filter_file(file_path, output_file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        file_contents = file.read()

    kann_list = file_contents.split()

    def contains_digits(word):
        return any(char.isdigit() for char in word)

    listt = [word for word in kann_list if not contains_digits(word)]

    filtered_list = [re.sub(r'^_NN$', '', word) for word in listt]

    filtered_list = [word for word in filtered_list if word]

    cleaned_list = [word.replace("_NN", "") for word in filtered_list]

  
    i = 0
    while i < len(cleaned_list):
        if re.search(r'[A-Za-z!@#?$\'%^&*();_=,.+|]', cleaned_list[i]):
            cleaned_list.pop(i)
        else:
            i += 1

    final_list = [word for word in cleaned_list if len(word) != 1 and len(word) != 2]

    with open(output_file_path, "w", encoding="utf-8") as output_file:
        for word in final_list:
            output_file.write(word + "\n")
        
# def assign_page_numbers(doc_txt, noun_txt, output_file='output.csv'):

#     with open(doc_txt, 'r', encoding='utf-8') as doc_file:
#         doc_content = doc_file.read()

#     with open(noun_txt, 'r', encoding='utf-8') as noun_file:
#         nouns = noun_file.read().split() 
#     words_per_page = 4000
#     pages = [doc_content[i:i + words_per_page] for i in range(0, len(doc_content), words_per_page)]

#     noun_page_mapping = {}

#     for noun in nouns:
#         if noun not in noun_page_mapping:
#             noun_page_mapping[noun] = set()  
#         for i, page in enumerate(pages, start=1):
#             if noun in page:
#                 noun_page_mapping[noun].add(i)

#     with open(output_file, 'w', encoding='utf-8', newline='') as csvfile:
#         csv_writer = csv.writer(csvfile)
#         csv_writer.writerow(['Word', 'Page Numbers'])
#         for noun, page_numbers in noun_page_mapping.items():
#             try:
#                 page_numbers_str = ', '.join(map(str, page_numbers))
#                 csv_writer.writerow([noun, page_numbers_str])
#             except UnicodeEncodeError:
#                 print(f"Unable to write: {noun} - {page_numbers_str}")

# import re
# import csv

# import csv
# import re

# def assign_page_numbers(doc_txt, noun_txt, output_file='output.csv'):
#     with open(doc_txt, 'r', encoding='utf-8') as doc_file:
#         doc_content = doc_file.read()

#     with open(noun_txt, 'r', encoding='utf-8') as noun_file:
#         nouns = noun_file.read().split() 

#     # Define the pattern using regular expression to match anything between <>
#     pattern = re.compile(r'<*>')
    
#     # Split the document content based on the pattern
#     pages = re.split(pattern, doc_content)
#     print(len(pages))
#     noun_page_mapping = {}

#     for noun in nouns:
#         if noun not in noun_page_mapping:
#             noun_page_mapping[noun] = set()  
#         for i, page in enumerate(pages, start=1):
#             if noun in page:
#                 noun_page_mapping[noun].add(i)

#     with open(output_file, 'w', encoding='utf-8', newline='') as csvfile:
#         csv_writer = csv.writer(csvfile)
#         csv_writer.writerow(['Word', 'Page Numbers'])
#         for noun, page_numbers in noun_page_mapping.items():
#             try:
#                 page_numbers_str = ', '.join(map(str, page_numbers))
#                 csv_writer.writerow([noun, page_numbers_str])
#             except UnicodeEncodeError:
#                 print(f"Unable to write: {noun} - {page_numbers_str}")


file_path = 'output/kannada_tags.txt'
output_file_path = "output/filtered_words_final.txt"
input_filepath="output_kan.txt"
process_and_filter_file(file_path,output_file_path)
# assign_page_numbers(input_filepath, output_file_path, 'output/output_final_600.csv')
