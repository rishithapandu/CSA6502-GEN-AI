from sklearn.metrics.pairwise import cosine_similarity

doc1 = [[1, 2, 3, 4]]
doc2 = [[2, 3, 4, 5]]

similarity = cosine_similarity(doc1, doc2)

print("Cosine Similarity:", similarity[0][0])

if similarity[0][0] > 0.8:
    print("The documents are highly similar.")
elif similarity[0][0] > 0.5:
    print("The documents are moderately similar.")
else:
    print("The documents are not similar.")
