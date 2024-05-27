import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns 
from sklearn.tree import DecisionTreeClassifier, plot_tree 
from sklearn.model_selection import train_test_split #fonction pour tracer l'arbre de décision généré par l'algorithme de l'arbre de décision
from sklearn.metrics import accuracy_score #fonction pour évaluer les performances du modèle,
from sklearn.metrics import classification_report #fonction pour afficher tout les scores de précision 
from sklearn.metrics import confusion_matrix
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score


df = pd.read_csv('C:/Users/haila/OneDrive/Bureau/DATA/Dataset_Diabetes.csv')
print (df.head())
