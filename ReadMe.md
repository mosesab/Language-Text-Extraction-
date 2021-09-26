
# Language-Text-Extraction ReadMe

[![Repo visits](https://github-visit-counter.herokuapp.com/mosesab/Language-Text-Extraction-/visits.svg)](#)

### 👩‍💻 Project BreakDown
The extract text.py is the main python file 

# 🔦 How the Code Works

* The code works by collecting a text file as an input, 
* The text in the file are cleaned and split into sentences, 
* The words in each sentence are matched with the language's lexicon and a score is given to a sentence,
* Based on the sentence score, the original sentence in text file (uncleaned) is written into a text file,
* The code outputs four text files with each file containing sentences based on their sentence score 
* The four text files contain sentences with 25, 50, 75, and 100 sentence score.





<details> 
	<summary>"# 🍿Tell me more about the four text files"</summary>
	<br>
  <p>After running the code outputs four text files, The files are named based on their match with the words in the lexicon. 
    The 100 percent text file 
  
  </p>
	<ul>
	<li>*🔨 The 100 percent text files contain sentences that match with a 100 percent - 74 percent score with the lexicon's language.*</li>
    <li>The 75 percent text files contain sentences that match with a 75 percent - 51 percent score </li>
    <li> 50 percent text files tend to contain mixed results, </li>
		<li>*And the 25 percent text files usually contain sentences that are #NOT# the same language with the lexicon's language.*</li>
	</ul>
</details>



The code works by extracting text from a text
file then using the lexicon file to get the words in the language, The code then matches words in a sentence 
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

### 👓 Contributions
Author : Bankole Moses

