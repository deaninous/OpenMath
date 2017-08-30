from matplotlib import pyplot as plt 

num_ch = []
mail_link = '../Data from openintro.org/email50.mine.txt'
with open(mail_link) as mail_handle:
	doc_body = mail_handle.readlines()[1:]
	for l in doc_body:
		for mail in doc_body:
			num_ch.append(float(mail.split('\t')[1]))
plt.boxplot(num_ch, showmeans=True)
plt.show()