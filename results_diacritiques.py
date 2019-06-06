#Ouverture d'un fichier .txt avec liste de mots d'une langue
text_file = open("diacritiques.txt", "r",encoding="utf-8")
list1 = text_file.read().splitlines()

#Ouverture d'un fichier .txt pour imprimer les résultats
f_results = open("results_diacritiques.txt", "w",encoding="utf-8")

#Analyse des contextes

voyelles=['a','ã','ά','e','ẽ','ə','έ','i','ĩ','ɨ','ί','o','õ','ᴐ','u','ũ','ʊ','ώ']
glides=['w','j']
consonnes=['p','t','k','s','ʃ','ʧ','z','m','n','ɲ','ɳ','h','r','v','b','d','g','ʦ']
diacritique=['\'']

word_analysis=''
list_words = []

for n1,word1 in enumerate(list1):
	for lettre in word1:
		if lettre in voyelles:
			word_analysis = word_analysis + 'V'
		if lettre in glides:
			word_analysis = word_analysis + 'G'
		if lettre in consonnes:
			word_analysis = word_analysis + 'C'
		if lettre in diacritique:
			word_analysis = word_analysis + 'D'
		if lettre == ' ':
			word_analysis = word_analysis + 'S'
	list_words.append(word_analysis)
	word_analysis=''

nb_diac=0
count=[]

for n2,word2 in enumerate(list1):
	for n3,word3 in enumerate(word2):
		if word3 =='\'':
			nb_diac=nb_diac+1
			if word2[n3+1] in consonnes and word2[n3+2] not in glides:
				count.append(word2[n3+2])
			if word2[n3+1] in consonnes and word2[n3+2] in glides:
				count.append(word2[n3+3])
			if word2[n3+1] in voyelles:
				count.append(word2[n3+1])
all_freq = {} 
  
for word in count:
	for i in word:
		if i in all_freq:
			all_freq[i] += 1
		else:
			all_freq[i] = 1

f_results.write("Nb mots avec ':" + str(nb_diac) + "\n")

for k in sorted (all_freq.keys()):
    f_results.write("'%s':'%s', \n" % (k, all_freq[k]))

f_results.write ("\nVoyelles jamais accentuées: \n")
for word in voyelles:
	if word not in count:
		f_results.write(word + "\n")
