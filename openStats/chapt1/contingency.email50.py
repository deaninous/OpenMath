mail_link = '../Data from openintro.org/email.txt'
mail_seize = {'small_spam': 0, 'big_spam': 0, 'small_not_spam': 0, 'big_not_spam': 0,
'av_spam': 0, 'av_not_spam': 0}

i = 0 #this will help us get the height of the data. There should be a more intuitive way
with open(mail_link) as mail_handle:
	doc_body = mail_handle.readlines()[1:]
	for l in doc_body:
		i+= 1
		l = l.split()
		spam_status = int(l[0])
		spam_seize = l[-1]
		if spam_status == 0:
			if spam_seize == 'small':
				mail_seize['small_not_spam'] += 1
			elif spam_seize == 'big':
				mail_seize['big_not_spam'] += 1
			else:
				mail_seize['av_not_spam'] += 1
		elif spam_status == 1:
			if spam_seize == 'small':
				mail_seize['small_spam'] += 1
			elif spam_seize == 'big':
				mail_seize['big_spam'] += 1
			else:
				mail_seize['av_spam'] += 1
mail_seize['spams'] = mail_seize['small_spam'] + mail_seize['big_spam'] + mail_seize['av_spam']
mail_seize['not_spam'] = mail_seize['small_not_spam'] + mail_seize['big_not_spam'] + mail_seize['av_not_spam']
from matplotlib import pyplot as plt
categories = ['none', 'small', 'big']
#plotting spam vs not spam amounts in the above array line
plt.bar(range(len(categories)), [mail_seize['av_not_spam'], mail_seize['small_not_spam'], mail_seize['big_not_spam']],color='#d62728' )
plt.bar(range(len(categories)), [mail_seize['av_spam'], mail_seize['small_spam'], mail_seize['big_spam']] )
plt.show()

# plt.figure()
# plt.bar(range(len(categories)), [mail_seize['av_not_spam']/ mail_seize['av_spam'] * 100, 
# 	mail_seize['small_not_spam']/mail_seize['small_spam'] * 100,
# 	 mail_seize['big_not_spam']/mail_seize['big_spam'] * 100],color='#d62728' )

# plt.bar(range(len(categories)), [mail_seize['av_spam']/mail_seize['small_not_spam'] * 100,
# 	 mail_seize['small_spam']/mail_seize['small_not_spam']* 100,
# 	  mail_seize['big_spam']/mail_seize['big_not_spam'] * 100] )
# plt.show()

#commented out code did not produce the graph I wanted

