import pickle
tokenizer = pickle.load(open("models/cv.pkl","rb"))
model = pickle.load(open("models/clf.pkl","rb"))


def make_pred(email_text):
    email_tokenized = tokenizer.transform([email_text])
    predictions = model.predict(email_tokenized)
    predictions = 1 if predictions == 1 else -1