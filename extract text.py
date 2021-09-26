
'''
extract text.py
version = 1.0
Author : Bankole Moses

requirements.txt : None
CrossPlatform Support : True
Tested on Android-Linux , python 3.8.3
All libraries used are part of the standard python library python 3.8.3 .
'''

import os 
from sentence_tokenizer import find_sentences
from cleanText import clean_text

def create_sentence_list(corpus_file_path, count = 0):
	"""
    cleans text and tokenizes the text into 
    a list of sentences(string)

    :param text: The filepath to the corpus.
    :type text: String.

    :returns: A list of sentences(strings)
    that have been cleaned
    :return type: list.
	"""
	my_word_list = []	
	# Read text File
	with open(corpus_file_path, 'r', encoding = 'utf-8') as fd: 
		input_str = str(fd.read())
		fd.close()		
	#removes diacritics and cleans text data
	string = clean_text(input_str)	
	return find_sentences(string)
		
def compare_sentences_with_list(corpus_file_path, corpus_name,lexicon_list,corpus_sentence_list):
        '''
	The compare_sentences_with_list is the main function as the name
	suggests it is used to compare the words in the lexicon_list and the sentences in the corpus_sentence_list 
	word by word for each sentence,
	compare_sentences_with_list function does the main functions of
	comparison, scoring and creating of text file documents where the
	original(uncleaned) sentences string are written to, it is also where the naming of
	the text files to show their sentence score is done.

	'''
        # open the original corpus doc and tokenize it to a token of sentences
	with open(corpus_file_path, 'r', encoding = 'utf-8') as fd: 
		input_str = str(fd.read())
		fd.close()
	original_string = find_sentences(input_str)
	# sentence_index is used to know the original sentence equivalent of a corpus_sentence_list element
	sentence_index = 0
	
	# score each sentence in corpus_sentence_list and 
	# write it's original corpus sentence equivalent to a text file based on its score.		
	for sentence in corpus_sentence_list:
		word_exists = 0
		sentence_length = 0
		
		for word in sentence.split():
			sentence_length += 1
			if word in lexicon_list:
				word_exists += 1
		if (word_exists == 0 or sentence_length == 0):
			sentence_score = 0
		else:
			sentence_score = int(round(word_exists * 100 / sentence_length))
			
		if (sentence_score >= 0):
			#"Print FORMAT:  , , "
			if (sentence_score <= 25):
				with open(f"m_25percent {corpus_name}", 'a', encoding = 'utf-8') as ab:
					try:				
						ab.write(original_string[sentence_index] + " \n ")
						ab.close()
					except IndexError:
						ab.close()		
				print(f"Sentence_Range(25): Sentence_Score: {sentence_score} , Word_Exists: {word_exists} ,SentenceLength: {sentence_length}, Sentence_Index: {sentence_index}" )
			elif (sentence_score <= 50):
				with open(f"m_50percent {corpus_name}", 'a', encoding = 'utf-8') as cd:
					try:				
						cd.write(original_string[sentence_index] + " \n ")
						cd.close()
					except IndexError:
						cd.close()			
				print(f"Sentence_Range(50): Sentence_Score: {sentence_score} , Word_Exists: {word_exists} ,SentenceLength: {sentence_length}, Sentence_Index: {sentence_index}" )
			elif (sentence_score <= 75):
				with open(f"m_75percent {corpus_name}", 'a', encoding = 'utf-8') as ef:
					try:				
						ef.write(original_string[sentence_index] + " \n ")
						ef.close()
					except IndexError:
						ef.close()		
				print(f"Sentence_Range(75): Sentence_Score: {sentence_score} , Word_Exists: {word_exists} ,SentenceLength: {sentence_length}, Sentence_Index: {sentence_index}" )
			elif (sentence_score <= 100):
				with open(f"m_100percent {corpus_name}", 'a', encoding = 'utf-8') as gh:
					try:				
						gh.write(original_string[sentence_index] + " \n ")
						gh.close()
					except IndexError:
						gh.close()			
				print(f"Sentence_Range(100): Sentence_Score: {sentence_score} , Word_Exists: {word_exists} ,SentenceLength: {sentence_length}, Sentence_Index: {sentence_index}" )
			else:
				print(f"ERROR:Invalid Percentage Score : {sentence_score} , {word_exists} , {sentence_length} " )
		else:			
			print(f"ERROR:Percentage Score less than zero: {sentence_score} , {word_exists} , {sentence_length} " )
		#increment the sentence_index
		sentence_index += 1
 
def start_work(lexicon_name, corpus_name):	
	# Check whether file is in text format or not
	if corpus_name.endswith(".txt"):
		corpus_file_path = os.path.join(os.getcwd(), corpus_name)
		
		lexicon_string = str(open(os.path.join(os.getcwd(),lexicon_name)).read())		
		
		lexicon_list = []
		lexicon_list.extend(lexicon_string.split())
		
		print("\n Loading... : Splitting the whole corpus into sentences \n")
		corpus_sentence_list = create_sentence_list(corpus_file_path)
		
		print("\n Working.... : Matching the words in each sentence with the lexicon \n\n")		
		compare_sentences_with_list(corpus_file_path,corpus_name,lexicon_list,corpus_sentence_list)
	else:
		print("ERROR: .txt is missing from the corpus file name")
		

#filenames must end with .txt
lexicon_txt = "Yoruba_lexicon.txt"
corpus_txt = "Yoruba_corpus.txt"

if __name__ == "__main__" :
    start_work(lexicon_txt, corpus_txt)
