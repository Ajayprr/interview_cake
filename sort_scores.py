def sort_scores(unsorted_scores, highest_score):
    score_counts = [0] * (highest_score + 1)
    sorted_scores = []
    for score in unsorted_scores:
        score_counts[score] += 1

    for score in range(len(score_counts)):
        count = score_counts[score]
        for occurrence in range(count):
            sorted_scores.append(score)
    return sorted_scores
