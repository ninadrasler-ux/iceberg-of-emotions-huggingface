import json

import emoji

from collections import Counter

from transformers import pipeline

classifier = pipeline("sentiment-analysis", model="distilbert/distilbert-base-uncased-finetuned-sst-2-english")

# Load Reddit comments
with open("titanic_comments.json", "r", encoding="utf-8") as f:
    reddit_json = json.load(f)

# Extract comment text
comments = []

for comment in reddit_json[1]["data"]["children"]:
    body = comment["data"].get("body")
    
    if body:
        comments.append(body)

# Sentiment and emoji counters
positive_comments = 0
negative_comments = 0


emoji_counter = Counter()

comments_with_emojis = 0


# Analyze comments

results = []

emoji_score_sum = 0
emoji_comment_count = 0

non_emoji_score_sum = 0
non_emoji_comment_count = 0

for comment in comments:

    # Emoji analysis
    emojis = emoji.emoji_list(comment)

    for match in emojis:
        symbol = match["emoji"]
        emoji_counter[symbol] += 1

    
    if emojis:
        comments_with_emojis += 1
        

    result = classifier(comment)

    label = result[0]["label"]

    if label == "POSITIVE":
        positive_comments += 1
    else:
        negative_comments += 1

    score = result[0]["score"]

    if emojis:
        emoji_score_sum += score
        emoji_comment_count += 1
    
    else:
        non_emoji_score_sum += score
        non_emoji_comment_count += 1

    results.append({
        "comment": comment,
        "label": label,
        "score": score
    })

avg_emoji_score = emoji_score_sum / emoji_comment_count
avg_non_emoji_score = non_emoji_score_sum / non_emoji_comment_count

print(f"Average score - comments with emojis: {avg_emoji_score:.4f}")
print(f"Average score - comments without emojis: {avg_non_emoji_score:.4f}")

lowest = sorted(results, key=lambda x: x["score"])[:10]

print("10 lowest:")

for i, result in enumerate(lowest, 1):
    print(f"{i}. {result['label']} | {result['score']:.4f}")
    print(result["comment"])
    print()

highest = sorted(results, key=lambda x: x["score"], reverse=True)[:10]

print("10 highest:")

for i, result in enumerate(highest, 1):
    print(f"{i}. {result['label']} | {result['score']:.4f}")
    print(result["comment"])
    print()
    


# Results
print(f"Total comments: {len(comments)}")
print(f"Comments with emojis: {comments_with_emojis}")

print()

print(f"Positive comments: {positive_comments}")
print(f"Negative comments: {negative_comments}")


print()

print("Most common emojis:")

for emoji_symbol, count in emoji_counter.most_common(10):
    print(f"{emoji_symbol}: {count}")
    


