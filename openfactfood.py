class Question:
	def __init__(self, question, choices**):
		#Stocker selfquestion & self choices
		pass
choices = ['pâte à tartiner', 'confiture', 'salé']
question = "veuillez choisir une catégorie: "

def menu(choices, question):
	choice = None

	print(question)

	for num, choice in enumerate(choices):
		print(str(num+1) + " : "+ choice)

	while True:
		try:
			choice = int(input())
			if choice in range(1, len(choices)+1):
				break
			else:
				raise
		except:
			print("Veuillez entrer un nombre entre 1 et " + str(len(choices)) + ".")
	return choice