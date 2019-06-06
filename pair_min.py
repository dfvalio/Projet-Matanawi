#Ouverture d'un fichier .txt avec liste de mots d'une langue
text_file = open("lexique_matanawi.txt", "r",encoding="utf-8")
list1 = text_file.read().splitlines()

#Ouverture d'un fichier .txt pour imprimer les résultats
f_results = open("results_pairs.txt", "w",encoding="utf-8")

#Retrouver les paires minimales de la liste wordlist

f_results.write("Voici les paires minimales:\n")

for n1,word1 in enumerate(list1):
	for word2 in list1[n1+1:]:
		if len(word1)==len(word2):
			ndiff=0
			for n,letter in enumerate(word1):
				if word2[n]!=letter:
					ndiff+=1
			if ndiff==1:
				#print (word1, word2)
				f_results.write(word1 + " " + word2 + " ")
				for n,letter in enumerate(word1):
					if word2[n]!=letter:
						f_results.write(letter + "|" + word2[n] + "\n")


#Paires à analyser en termes de prosodie (liste de mots sans espace et sans diacritiques)
#Pour chaque paires, nous allons vérifier s'il y a une différence prosodique associée à une différence sémantique
f_results.write("\nPaires à analyser en termes de prosodie: \n")
for n1,word1 in enumerate(list1):
	for word2 in list1[n1+1:]:
		if len(word1)==len(word2):
			ndiff=0
			for n,letter in enumerate(word1):
				if word2[n]!=letter:
					ndiff+=1
			if ndiff==0:
				#print (word1, word2)
				f_results.write(word1 + " " + word2 + "\n")


#Retrouver les différents caractères de wordlist
list_char = []
for word in list1:
	for i in word:
		if i not in list_char:
			list_char.append(i)

f_results.write("\nLe nombre de caractères différens (avec espace) est:\n" + str(len(list_char)) + "\n")

all_freq = {} 
  
for word in list1:
	for i in word:
		if i in all_freq:
			all_freq[i] += 1
		else:
			all_freq[i] = 1

#print("Voici la fréquence de chaque graphème:\n")
f_results.write("\nVoici la fréquence de chaque caractère:\n")

for i in list_char:
	#print(i, all_freq[i])
	f_results.write(i + " " + str(all_freq[i]) + "\n")