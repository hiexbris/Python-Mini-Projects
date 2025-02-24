from sklearn.feature_extraction.text import TfidfVectorizer
import csv
import time
import pandas as pd
import matplotlib.pyplot as plt

start_time = time.time()

professions = [
    "doctor",
    "lawyer",
    "teacher",
    "engineer",
    "accountant",
    "nurse",
    "police",
    "architect",
    "dentist",
    "pharmacist"
]

vectorizer = TfidfVectorizer(analyzer='char', ngram_range=(1, 1))
vectorizer.fit(professions)
n_gram = vectorizer.get_feature_names_out()

job_vector = []

for i in professions:
    x = []
    for j in n_gram:
        x.append(i.count(j))
    job_vector.append(x)

with open('TaskData.csv', 'r') as file:
    reader = csv.reader(file)
    data_list = list(reader)

form = [data[0].lower() for data in data_list]

form_vector = []

for i in form:
    x = []
    for j in n_gram:
        x.append(i.count(j))
    form_vector.append(x)

answer = []

for i in form_vector:
    jaccard = []
    for j in job_vector:
        numerator = 0
        denominator = 0
        for k in range(0, len(n_gram)):
            numerator += min(i[k], j[k])
            denominator += max(i[k], j[k])
        jaccard.append(numerator / denominator)

    answer.append(professions[jaccard.index(max(jaccard))])

count = {}

for item in answer:
    profession = item  # Access the first element (profession)
    if profession in count:
        count[profession] += 1  # Increment count for existing profession
    else:
        count[profession] = 1


final_data = pd.DataFrame(list(zip(form, answer)))
final_data.to_excel("fuzzy_writing.xlsx", index=False)

job = list(count.keys())
frequency = list(count.values())

end_time = time.time()

plt.figure(figsize=(10, 6))  # Set the figure size
plt.barh(job, frequency, color='skyblue')  # Create bars with a sky blue color
plt.ylabel('Professions')
plt.xlabel('Frequency')
plt.tight_layout()
plt.show()


print(count)
print(f"Compilation time: {end_time - start_time:.2f} seconds")
