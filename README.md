# 🎬 Titanic Sentiment with Hugging Face

Titanic already had its emotional moment in the spotlight. But what happens when we take the same Reddit comments and run them through a transformer model?
In my previous project, Titanic: Iceberg of Emotions, I explored emojis and sentiment using VADER. This time, I’m taking the same tiny pool of Titanic comments and giving them to Hugging Face’s DistilBERT to see how it reads their emotional tone — and how confident it is about what it sees.
Same comments. Different model. Let’s see if they tell the same story. 🚢


## ❓ What was I trying to understand?

### 🤖 **How does a transformer model classify Titanic comments?**

### 🎯 **How confident is the model in its predictions?**

### 😀 **Does model confidence differ between comments with and without emojis?**

### 🔄 **How does Hugging Face compare with VADER on the same comments?**


## 🧪 Method: How the data was collected and processed

- Used the same 98 top-level Reddit comments about *Titanic* as in the previous project.
- Extracted the comment text from the JSON data and ignored nested replies.
- Used the `emoji` library to identify emojis and split comments into two groups:
  - comments **with emojis**
  - comments **without emojis**
- Performed sentiment analysis using Hugging Face's `distilbert/distilbert-base-uncased-finetuned-sst-2-english` model.
- Recorded:
  - the predicted sentiment (**POSITIVE** or **NEGATIVE**)
  - the model's **confidence score**
- Calculated the average confidence score for comments with and without emojis.
- Compared the Hugging Face results with the previous VADER analysis.
- As a small exploratory check, inspected the 10 comments with the **highest** and **lowest** confidence scores.


## 📊 Results

### 🤖 Sentiment classification

- **67 positive comments**
- **31 negative comments**

### 🎯 Model confidence

- **Comments with emojis:** 0.9846
- **Comments without emojis:** 0.9745


## 📈 Key findings

### 🤖 1. The model classified most comments as positive

- **67 positive**
- **31 negative**

The Hugging Face model classified about two-thirds of the comments as positive.

### 🎯 2. The model was highly confident overall

- **Average confidence — comments with emojis: 0.9846**
- **Average confidence — comments without emojis: 0.9745**

The model was highly confident in both groups. Comments containing emojis had a slightly higher average confidence score, but the difference was very small.

### 🔄 3. Hugging Face and VADER told a similar — but not identical — story

Both approaches found a generally positive tone in the comments.

VADER classified **58 comments as positive, 17 as negative, and 23 as neutral**, while the Hugging Face model classified **67 as positive and 31 as negative**.

The difference is partly due to the models approaching sentiment differently: VADER provides a continuous sentiment score and includes a neutral category, while the Hugging Face model used here makes a binary positive/negative classification.

### 😀 4. Emojis did not make the model much less confident

The average confidence score was slightly higher for comments containing emojis (**0.9846**) than for comments without them (**0.9745**).

So, at least in this small dataset, the presence of emojis did not appear to confuse the model. If anything, the model was marginally more confident when emojis were present.

> **Note:** The Reddit data used in this project comes from the dataset collected for [*Titanic: Iceberg of Emotions*](https://github.com/ninadrasler-ux/iceberg-of-emotions).
