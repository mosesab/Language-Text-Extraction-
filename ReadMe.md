
extract text.py 
version = 1 
Author : Bankole Moses

[![Repo visits](https://github-visit-counter.herokuapp.com/mosesab/Language-Text-Extraction-/edit/main/ReadMe.md/visits.svg)](#)

The extract text.py file works by extracting text from a corpus text
file then passing the extracted text through a couple of functions that
pass the text around filtering the text as it goes

The start_work function checks that the file-name or file-path points
to a .txt file before running the code.

The compare_sentences_with_list is the main function as the name
suggests it is used to compare the base word list and the tokenized
corpus sentences word by word for each sentence,
compare_sentences_with_list function does the main functions of
comparison, scoring and creating of text file documents where the
original sentences string are written to, it is also where the naming of
the text files to show their sentence score is done.

The create_sentence_list returns a list containing tokenized sentences
from the corpus, tokenized using the dot(full-stop) character, It can
easily be tweaked to become a recurrsive function in case of handling
large number of corpus text extractions simultaneously.

The program creates four text files if it runs successfully each file
contains sentences that match with the base word list at varying
percentages,each individual sentence is seperated by a new line, for a
group of words to be recognized as a sentence a full-stop must follow at
the end of the group of words.

The sentence_tokenizer.py , find_sentences function is the only
function imported and used in the extract text.py program as it is used
for basic sentence tokenization.

The python program is designed to only make use of the python standard
libraries so it can be easily ported to another system.

The program uses the current working directory extensively so the corpus
and the base word lists and sentence_tokenizer.py should be in the same
folder(directory) as the extract text.py .

The program also makes use of the python os library so that the program
can cross platformly run on windows,linux based computers without having
to worry about the file path differences i.e '/' and '\'.

