
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

### 👓 Author
Moses Bankole

