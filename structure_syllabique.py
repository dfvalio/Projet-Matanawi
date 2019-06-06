#Ouverture d'un fichier .txt avec liste de mots d'une langue
text_file = open("lexique_matanawi.txt", "r",encoding="utf-8")
list1 = text_file.read().splitlines()

#Ouverture d'un fichier .txt pour imprimer les résultats
f_results = open("results_structure.txt", "w",encoding="utf-8")

#Analyse des contextes

voyelles=['a','ã','ά','e','ẽ','ə','έ','i','ĩ','ɨ','ί','o','õ','ᴐ','u','ũ','ʊ','ώ']
glides=['w','j']
consonnes=['p','t','k','s','ʃ','ʧ','z','m','n','ɲ','ɳ','h','r','v','b','d','g','ʦ']

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
		if lettre == ' ':
			word_analysis = word_analysis + 'S'
	list_words.append(word_analysis)
	word_analysis=''

#Types de structures des mots simples (sans espace)
list_struct=[]
for word in list_words:
	if word not in list_struct and 'S' not in word:
		list_struct.append(word)

f_results.write("Liste de structures des mots simples:\n")
for i in list_struct:
	f_results.write(i + "\n")

#Analyse du nombre de syllabes (nb voyelles) pour des mots simples (sans espace)
nb_syl=[]
for n1,word1 in enumerate(list_words):
	nb_syl.append(0)

for n1,word1 in enumerate(list_words):
	for lettre in word1:
		if lettre == 'V' and 'S' not in word1:
			nb_syl[n1]=nb_syl[n1]+1

f_results.write("Analyse du nombre de syllabes (nb voyelles) pour les mots simples\n")

monosyl=0
disyl=0
trisyl=0
tetrasyl=0
pentasyl=0

for i in nb_syl:
	if i == 1:
		monosyl=monosyl+1
	if i == 2:
		disyl=disyl+1
	if i == 3:
		trisyl=trisyl+1
	if i == 4:
		tetrasyl=tetrasyl+1
	if i == 5:
		pentasyl=pentasyl+1

nb_mots_simples=monosyl+disyl+trisyl+tetrasyl+pentasyl
f_results.write("Nombre de mots simples:\n" + str(nb_mots_simples))
f_results.write("\nNombre maximum de syllabes dans les mots simples:\n" + str(max(nb_syl)))		
f_results.write("\nNombre de mots avec 1 syllabe:\n" + str(monosyl))
f_results.write("\nNombre de mots avec 2 syllabes:\n" + str(disyl))
f_results.write("\nNombre de mots avec 3 syllabes:\n" + str(trisyl))
f_results.write("\nNombre de mots avec 4 syllabes:\n" + str(tetrasyl))
f_results.write("\nNombre de mots avec 5 syllabes:\n" + str(pentasyl) + "\n")



cc=0
ccc=0
vv=0
vvv=0
vvvv=0
gv=0
vg=0
gvv=0
vgv=0
vvg=0
gvvv=0
vgvv=0
vvgv=0
vvvg=0
ggv=0
gvg=0
vgg=0

list_cc=[]
list_ccc=[]
list_vv=[]
list_vvv=[]
list_vvvv=[]
list_gv=[]
list_vg=[]
list_gvv=[]
list_vgv=[]
list_vvg=[]
list_gvvv=[]
list_vgvv=[]
list_vvgv=[]
list_vvvg=[]
list_ggv=[]
list_gvg=[]
list_vgg=[]

for n1,word1 in enumerate(list_words):
	if 'CC' in word1:
		cc=cc+1
		list_cc.append(list1[n1])
	if 'CCC' in word1:
		ccc=ccc+1
		list_ccc.append(list1[n1])
	if 'VV' in word1:
		vv=vv+1
		list_vv.append(list1[n1])
	if 'VVV' in word1:
		vvv=vvv+1
		list_vvv.append(list1[n1])
	if 'VVVV' in word1:
		vvvv=vvvv+1
		list_vvvv.append(list1[n1])
	if 'GV' in word1:
		gv=gv+1
		list_gv.append(list1[n1])
	if 'VG' in word1:
		vg=vg+1
		list_vg.append(list1[n1])
	if 'GVV' in word1:
		gvv=gvv+1
		list_gvv.append(list1[n1])
	if 'VGV' in word1:
		vgv=vgv+1
		list_vgv.append(list1[n1])
	if 'VVG' in word1:
		vvg=vvg+1
		list_vvg.append(list1[n1])
	if 'GVVV' in word1:
		gvvv=gvvv+1
		list_gvvv.append(list1[n1])
	if 'VGVV' in word1:
		vgvv=vgvv+1
		list_vgvv.append(list1[n1])
	if 'VVGV' in word1:
		vvgv=vvgv+1
		list_vvgv.append(list1[n1])
	if 'VVVG' in word1:
		vvvg=vvvg+1
		list_vvvg.append(list1[n1])
	if 'GGV' in word1:
		ggv=ggv+1
		list_ggv.append(list1[n1])
	if 'GVG' in word1:
		gvg=gvg+1
		list_gvg.append(list1[n1])
	if 'VGG' in word1:
		vgg=vgg+1
		list_vgg.append(list1[n1])

		
		
f_results.write("nb mots CC: " + str(cc) + "\n")
f_results.write(str(list_cc) + "\n")
f_results.write("nb mots CCC: " + str(ccc) + "\n")
f_results.write(str(list_ccc) + "\n")
f_results.write("nb mots VV: " + str(vv) + "\n")
f_results.write(str(list_vv) + "\n")
f_results.write("nb mots VVV: " + str(vvv) + "\n")
f_results.write(str(list_vvv) + "\n")
f_results.write("nb mots VVVV: " + str(vvvv) + "\n")
f_results.write(str(list_vvvv) + "\n")
f_results.write("nb mots GV: " + str(gv) + "\n")
f_results.write(str(list_gv) + "\n")
f_results.write("nb mots VG: " + str(vg) + "\n")
f_results.write(str(list_vg) + "\n")
f_results.write("nb mots GVV: " + str(gvv) + "\n")
f_results.write(str(list_gvv) + "\n")
f_results.write("nb mots VGV: " + str(vgv) + "\n")
f_results.write(str(list_vgv) + "\n")
f_results.write("nb mots VVG: " + str(vvg) + "\n")
f_results.write(str(list_vvg) + "\n")
f_results.write("nb mots GVVV: " + str(gvvv) + "\n")
f_results.write(str(list_gvvv) + "\n")
f_results.write("nb mots VGVV: " + str(vgvv) + "\n")
f_results.write(str(list_vgvv) + "\n")
f_results.write("nb mots VVGV: " + str(vvgv) + "\n")
f_results.write(str(list_vvgv) + "\n")
f_results.write("nb mots VVVG: " + str(vvvg) + "\n")
f_results.write(str(list_vvvg) + "\n")
f_results.write("nb mots GGV: " + str(ggv) + "\n")
f_results.write(str(list_ggv) + "\n")
f_results.write("nb mots GVG: " + str(gvg) + "\n")
f_results.write(str(list_gvg) + "\n")
f_results.write("nb mots VGG: " + str(vgg) + "\n")
f_results.write(str(list_vgg) + "\n")


total = cc + ccc + vv + vvv + vvvv + gv + vg + gvv + vgv + vvg + gvvv + vgvv + vvgv + vvvg + ggv + gvg + vgg

f_results.write ("Total mots: " + str(total) + "\n")


#Mots avec V et G seulement

list_words_no_C=[]
words_no_C=0

for n1,word1 in enumerate(list_words):
	if 'C' not in word1:
		words_no_C=words_no_C+1
		list_words_no_C.append(list1[n1])
		
f_results.write ("\nMots sans consonne: \n")
f_results.write ("Nombre mots: \n" + str(words_no_C) + "\n")
f_results.write (str(list_words_no_C) + "\n")


#Mots avec C seulement

list_words_C=[]
words_C=0

for n1,word1 in enumerate(list_words):
	if 'V' not in word1 and 'G' not in word1:
		words_C=words_C+1
		list_words_C.append(list1[n1])
		
f_results.write ("\nMots formés seulement de consonnes: \n")
f_results.write ("Nombre mots: \n" + str(words_C) + "\n")
f_results.write (str(list_words_C) + "\n")

#Mots avec C et G

list_words_CG=[]
words_CG=0

for n1,word1 in enumerate(list_words):
	if 'V' not in word1:
		words_CG=words_CG+1
		list_words_CG.append(list1[n1])
		
f_results.write ("\nMots formés seulement de consonnes et glides: \n")
f_results.write ("Nombre mots: \n" + str(words_CG) + "\n")
f_results.write (str(list_words_CG) + "\n")

