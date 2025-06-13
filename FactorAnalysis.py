import pandas as pd
from sklearn.decomposition import FactorAnalysis
import matplotlib.pyplot as plt
import seaborn as sns

# The dictionary with your data
data = {
    'Q1: I enjoy solving complex math problems.': [8, 2, 9, 3, 7, 4, 8, 1, 9, 2],
    'Q2: I prefer to learn through reading texts.': [3, 9, 2, 8, 4, 7, 3, 9, 2, 8],
    'Q3: I like to build things and work with my hands.': [7, 4, 8, 2, 9, 3, 8, 2, 9, 3],
    'Q4: I find abstract concepts in physics fascinating.': [9, 3, 8, 4, 8, 5, 9, 2, 8, 3],
    'Q5: I learn best by listening to lectures and discussions.': [4, 8, 3, 9, 5, 8, 4, 9, 3, 7],
    'Q6: I am good at hands-on troubleshooting.': [8, 3, 9, 4, 8, 2, 7, 3, 9, 4]
}

StudentLearning = pd.DataFrame(data)
StudentLearning.columns = ["Q1_Math", "Q2_Reading", "Q3_Building", "Q4_Physics", "Q5_Lectures", "Q6_Troubleshooting"]

print("--- Dataset ---")
print(StudentLearning)

# Initialize factor analysis with 2 components (latent variables)
fa = FactorAnalysis(n_components=2, random_state=10)
fa.fit(StudentLearning)

# Create the DataFrame of factor loadings
loadings = pd.DataFrame(fa.components_.T,
                        index=StudentLearning.columns,
                        columns=['Factor 1', 'Factor 2'])

print("\n--- Factor Loadings ---")
print(loadings)


# --- Visualization ---
plt.figure(figsize=(10, 8))
sns.set_theme(style="whitegrid")

# Create a scatter plot of the loadings
plt.scatter(loadings['Factor 1'], loadings['Factor 2'], s=100)

# Add labels for each point
for i, txt in enumerate(loadings.index):
    plt.annotate(txt, (loadings['Factor 1'][i], loadings['Factor 2'][i]),
                 xytext=(5, -5), textcoords='offset points')

# Add lines for the axes
plt.axhline(0, color='grey', lw=1, linestyle='--')
plt.axvline(0, color='grey', lw=1, linestyle='--')

# Set titles and labels
plt.title('Factor Loading Plot', fontsize=16)
plt.xlabel('Factor 1: Abstract Thinker', fontsize=12)
plt.ylabel('Factor 2: Applied Learner', fontsize=12)
plt.grid(True)
plt.show()