
# Language-Text-Extraction ReadMe

[![Repo visits](https://github-visit-counter.herokuapp.com/mosesab/Language-Text-Extraction-/visits.svg)](#)

### 👩‍💻 Project BreakDown
The extract text.py is the main python file.

# 🔦 How the Code Works

* The code works by collecting a text file as an input, 
* The text in the file are cleaned and split into sentences, 
* The words in each sentence are matched with the language's lexicon and a score is given to a sentence,
* Based on the sentence score, the original sentence in text file (uncleaned) is written into a text file,
* The code outputs four text files with each file containing sentences based on their sentence score 
* The four text files contain sentences with 25, 50, 75, and 100 sentence score.


<details> 
	<summary># "🍿Tell me more about the four text files"</summary>
	<br>
  <p>
	  After running the code outputs four text files, 
	  The files are named based on their match with the words in the lexicon.  
  </p>
  <ul>
	<li>🔨 The 100 percent text files contain sentences that match with a 100 percent - 74 percent score with the lexicon's language.</li>
	<li>The 75 percent text files contain sentences that match with a 75 percent - 51 percent score </li>
	<li>The 50 percent text files tend to contain mixed results, </li>
	<li>The 25 percent text files usually contain sentences that are #NOT# the same language with the lexicon's language.</li>
  </ul>
</details>

# 📔 Note
 <ul>
	<li>The code cleans diacritics and digits from sentences before scoring them. See the cleanText.py file.</li>
	<li>The code identifies sentences in text by using full stop (.), 
		Edit the sentence_tokenizer.py if the desired language doesn't use dot to denote end of a sentence.</li>
  </ul>



# 💡 A Few Extra Features
 <ul>
	<li>The python program is designed to only make use of the python standard libraries so it can be easily ported to another system.</li>
	<li>The program also makes use of the python os library so that the program can cross platformly run on windows,linux based computers without having 
		to worry about the file path differences i.e '/' and '\'.</li>
  </ul>


# 👓 Author
Moses Bankole

