from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report

# Email samples
emails = [
    'Congratulations! You have won a lottery worth $1000.',
    'Get free entry to win an iPhone.',
    'Hi friend, how are you doing today?',
    'Meeting scheduled at 10 AM tomorrow.',
    'Earn money fast from home!!!',
    'Reminder: Project submission is due today.',
    'Free tickets available for you.',
    'Let’s catch up for lunch.',
    'Exclusive deal just for you, click now!',
    'Don’t forget our dinner tonight.'
]

# Labels (1 = Spam, 0 = Ham)
labels = [1, 1, 0, 0, 1, 0, 1, 0, 1, 0]

# Convert text data to numerical features
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(emails)

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, labels, test_size=0.3, random_state=42)

# Naive Bayes Model
nb_model = MultinomialNB()
nb_model.fit(X_train, y_train)
nb_preds = nb_model.predict(X_test)

print("Naive Bayes Classification Report:")
print(classification_report(y_test, nb_preds))
print("Naive Bayes Accuracy:", accuracy_score(y_test, nb_preds))

# Support Vector Machine (SVM) Model
svm_model = SVC(kernel='linear')
svm_model.fit(X_train, y_train)
svm_preds = svm_model.predict(X_test)

print("\nSVM Classification Report:")
print(classification_report(y_test, svm_preds))
print("SVM Accuracy:", accuracy_score(y_test, svm_preds))
