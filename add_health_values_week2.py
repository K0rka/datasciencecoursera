import pandas as pd
import numpy as np
import matplotlib.pyplot as pyplot

add_health = pd.read_csv("add_health.csv", low_memory=False)

#choose only columns, that makes interest
selected_part = add_health[['H1RE2', 'H1RE4', 'H1RE6', 'H1PR5', 'H1PF2']]

#Values for peoples trust in sacred scripts of their religion
sacred_scripts_values = pd.to_numeric(selected_part['H1RE2']).value_counts(sort = True)
sacred_scripts_values_norm = pd.to_numeric(selected_part['H1RE2']).value_counts(sort = True, normalize=True)

sacred_scripts_results = pd.DataFrame({"Count":sacred_scripts_values, "Count normalized" : sacred_scripts_values_norm})
print(sacred_scripts_results)

#how important is religion for me
add_health.loc[((add_health['H1RE4'] == 6) | (add_health['H1RE4'] == 7) | (add_health['H1RE4'] == 8)), 'H1RE4'] = 5
religion_importance_values = add_health['H1RE4'].value_counts(sort = True)
religion_importance_values_norm = add_health['H1RE4'].value_counts(sort = True, normalize = True)
religion_importance_results = pd.DataFrame({"Count":religion_importance_values, "Normalized Count" : religion_importance_values_norm})
#replace religion importance answers with thei description
religion_importance_results.at[1, "Description"] = "very important"
religion_importance_results.at[2, "Description"] = "fairly important"
religion_importance_results.at[3, "Description"] = "fairly unimportant"
religion_importance_results.at[4, "Description"] = "not important at all"
religion_importance_results.at[5, "Description"] = "other"
#set description of the answers as their index
religion_importance_results.index = religion_importance_results['Description']
religion_importance_results = religion_importance_results.drop("Description", axis=1)

print(religion_importance_results)

#print bar plot for religion importance
#make labels multilined
labels = ["very\nimportant", "fairly\nimportant","other", "fairly\nunimportant", "not important\nat all"]
fig, _ = pyplot.subplots(figsize=(15,5))
fig.suptitle('How important is religion for me?', fontsize=16)
pyplot.subplot(1, 2, 1)
pyplot.bar(labels, height = religion_importance_values)
pyplot.xlabel('')
pyplot.subplot(1, 2, 2)
pyplot.bar(labels, height = religion_importance_values_norm)

# How much do you feel that people in your family understand you? block
add_health.loc[((add_health['H1PR5'] == 96) | (add_health['H1PR5'] == 98)), 'H1PR5'] = 6
family_understanding_values = add_health['H1PR5'].value_counts(sort = True)
family_understanding_norm = add_health['H1PR5'].value_counts(sort = True, normalize = True)
family_understanding_results = pd.DataFrame({"Count":family_understanding_values, "Normalized Count" : family_understanding_norm})
#map numerical answers to their description
family_understanding_results.at[1, "Description"] = "not at all"
family_understanding_results.at[2, "Description"] = "very little"
family_understanding_results.at[3, "Description"] = "somewhat"
family_understanding_results.at[4, "Description"] = "quite a bit"
family_understanding_results.at[5, "Description"] = "very much"
family_understanding_results.at[6, "Description"] = "other"
family_understanding_results.index = family_understanding_results['Description']
family_understanding_results = family_understanding_results.drop("Description", axis=1)
print(family_understanding_results)
#plot understanding in family as bars
labels = ["quite a bit", "somewhat", "very\nmuch", "very\nlittle", "not\nat all", "other"]
fig, _ = pyplot.subplots(figsize=(15,5))
fig.suptitle('How much do you feel that people in your family understand you??', fontsize=16)
pyplot.subplot(1, 2, 1)
pyplot.bar(labels, height = family_understanding_values)
pyplot.subplot(1, 2, 2)
pyplot.bar(labels, height = family_understanding_norm)

#mom encourages to be independant
#merge everything appropriate to "other" section
add_health.loc[((add_health['H1PF2'] == 8) | (add_health['H1PF2'] == 7)), 'H1PF2'] = 6
mom_indep_values = add_health['H1PF2'].value_counts(sort = True)
mom_indep_norm = add_health['H1PF2'].value_counts(sort = True, normalize = True)
mom_indep_results = pd.DataFrame({"Count":mom_indep_values, "Normalized Count" : mom_indep_norm})
#map numerical answers to their description
mom_indep_results.at[1, "Description"] = "strongly agree"
mom_indep_results.at[2, "Description"] = "agree"
mom_indep_results.at[3, "Description"] = "neither agree nor disagree"
mom_indep_results.at[4, "Description"] = "disagree"
mom_indep_results.at[5, "Description"] = "strongly disagree"
mom_indep_results.at[6, "Description"] = "other"
mom_indep_results.index = mom_indep_results['Description']
mom_indep_results = mom_indep_results.drop("Description", axis=1)
print(mom_indep_results)
#plot values and normalized values as bar plot
labels = ["strongly\nagree", "agree", "neither agree\nnor disagree", "other", "disagree", "strongly\ndisagree"]
fig, _ = pyplot.subplots(figsize=(15,5))
fig.suptitle('Your mother encourages you to be independent.', fontsize=16)
pyplot.subplot(1, 2, 1)
pyplot.bar(labels, height = mom_indep_values)
pyplot.subplot(1, 2, 2)
pyplot.bar(labels, height = mom_indep_norm)
