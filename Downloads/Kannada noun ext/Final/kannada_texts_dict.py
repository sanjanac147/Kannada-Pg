import re


def kannada_to_english(kannada_num):
    
    kannada_numerals = "೦೧೨೩೪೫೬೭೮೯"
    english_numerals = "0123456789"
    translation_table = str.maketrans(kannada_numerals, english_numerals)
    return kannada_num.translate(translation_table)



def extract_kannada_text(filename):
    kannada_text = {}
    with open(filename, 'r', encoding='utf-8') as file:
        current_page = None
        previous_text = ''
        for line in file:
            page_match = re.search(r'<([^>]*)>', line)
            if page_match:
                
                if current_page is not None:
                   
                    english_page = kannada_to_english(current_page)
                    kannada_text[english_page] = previous_text.strip()
                # Set the current page number
                current_page = page_match.group(1)
                
                previous_text = ''
            else:
               
                previous_text += line
       
        if current_page is not None:
            
            english_page = kannada_to_english(current_page)
            kannada_text[english_page] = previous_text.strip()
    return kannada_text

# Example usage
filename = 'output_kan.txt'  # Change this to your file path
kannada_text_dict = extract_kannada_text(filename)
kannada_text_dict
