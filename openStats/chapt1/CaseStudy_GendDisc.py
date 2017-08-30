"""Chapter case study on a gender discrimation experiment
file can be found at '../Data from openintro.org/genderDiscrimination.txt' 
Set in the context of personal decisions within a bank, study was carried out in the 1970s.
And aims to answer the question:
Are females unfairly discriminated against in promotion decisions made by male managers?

There were 48 male banke supervisors to decide wether a file should get promotion or not.

the files were identical except half of them indicated the candidate was male and another half
indicated female. Then randomly assigned to the subjects"""


import math
import random

#set the record straight
sum_tats = {
	'males' :{'count': 0, 'promoted': 0, 'promoted_not': 0, 'promote_ratio': 0.00},
	'females' :{'count':0, 'promoted': 0, 'promoted_not': 0, 'promote_ratio': 0.00}	
}

#load the data
with open('../Data from openintro.org/genderDiscrimination.txt') as gender_handle:
	bod = gender_handle.readlines()[1:]
	for row in bod:
		row = row.split('\t')
		if row[0] == 'female':
			sum_tats['females']['count'] +=1
			if row[-1].strip() == 'promoted':
				sum_tats['females']['promoted'] += 1
			else:
				sum_tats['females']['promoted_not'] += 1
		else:
			sum_tats['males']['count'] += 1
			if row[-1].strip() == 'promoted':
				sum_tats['males']['promoted'] += 1
			else:
				sum_tats['males']['promoted_not']+= 1
sum_tats['females']['promote_ratio'] = sum_tats['females']['promoted']/float(sum_tats['females']['count'])
sum_tats['males']['promote_ratio'] = sum_tats['males']['promoted']/ float(sum_tats['males']['count'])

# print(sum_tats)
# {'males': {'count': 24, 'promoted': 21,
#  'promoted_not': 3, 'promote_ratio': 0.875},
#  'females': {'count': 24, 'promoted': 14, 
#  'promoted_not': 10, 'promote_ratio': 0.5833333333333334}}

if sum_tats['males']['promote_ratio'] > sum_tats['females']['promote_ratio']:
	promotion_diff = str(sum_tats['males']['promote_ratio'] - sum_tats['females']['promote_ratio']) + " in favor of men" 
else: 
	promotion_diff = str(sum_tats['females']['promote_ratio'] - sum_tats['males']['promote_ratio']) + " in favor of women" 
print(promotion_diff)

##############################################################################
############
########### 		Simulate the experiment
###########
#################################################################################
res = []
def runsim():
	male_sim = ("male,"*24).split(',')[:-1]
	female_sim = ('female,'*24).split(',')[:-1]
	pop = male_sim + female_sim
	pop_copy =  pop.copy()
	random.shuffle(pop_copy)

	#we imagine 2 stacks but will be using dicts
	#Now after shuffling the copy, we deal it to the 2 stacks representing the fvaor/unfavor decisions observed
	#just a nice way of having the fav resp and unfav resp counts without hardcoding it
	favor_notes = sum_tats['males']['promoted'] + sum_tats['females']['promoted']
	unfavor_notes = sum_tats['males']['promoted_not'] + sum_tats['females']['promoted_not']

	favor_stack =[]
	unfavor_stack = []
	for i in range(len(pop_copy)):
		if i < favor_notes:
			favor_stack.append(pop_copy[i])
		else:
			unfavor_stack.append(pop_copy[i])


	#Detemine fraction of promoted males and promoted females
	male_sim_prom = [i for i in favor_stack if i == 'male']
	female_sim_prom = [i for i in favor_stack if i == 'female']
	male_sim_noprom = [i for i in unfavor_stack if i == 'male']
	female_sim_noprom = [i for i in unfavor_stack if i == 'female']
	res.append([{'sim_prom_m': len(male_sim_prom), 
		'sim_prom_f': len(female_sim_prom), 
		'sim_count_m': len(male_sim_prom + male_sim_noprom),
		'sim_count_f': len(female_sim_prom + female_sim_noprom),
		'sim_no_prom_f': len(female_sim_noprom),
		'sim_no_prom_m': len(male_sim_noprom),
		#ratio is in percentage
		'sim_mf_ratio_diff': (len(male_sim_prom)/24* 100) - (len(female_sim_prom) /24 * 100)		
		}])

for i in range(100):
	if i == 1:
		print(res)
	runsim()
def summarize_experiment():
	board ={
	'man_prom': 0,
	'lady_prom': 0,
	}
	# [{'sim_no_prom_m': 6, 'sim_count_m': 24, 'sim_prom_f': 17,
	#  'sim_prom_m': 18, 'sim_count_f': 24, 'sim_no_prom_f': 7}]

	for i in res:
		board['man_prom'] += i[0]['sim_prom_m']
		board['lady_prom'] += i[0]['sim_prom_f']
	return board
score_board = summarize_experiment()

#Number of experiments we ran
NUM_EXPERIMENTS = 100
#Since we shuffled from 24 m and 24 f, we always have 24 m and 24 f
GENDER_SIZE = 24

#now we get the ratio from the 100 experiments we ran
score_board['man_prom_ration'] = score_board['man_prom'] / 24
score_board['lady_prom_ration'] = score_board['lady_prom'] / 24
score_board['diff_ratio_m_f'] = score_board['man_prom_ration'] - score_board['lady_prom_ration']


stock = []
#proceed now to get the ratios from res and plot them
for i in res:
	stock.append(i[0]['sim_mf_ratio_diff'])	
from matplotlib import pyplot as plt 
plt.scatter([i for i in range(len(stock))], stock)
plt.show()