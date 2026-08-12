def predict_match_score():
    """
    Lesson 16: simple word-match score predictor.
    """
    print("=== Match-score Predictor (L16) ===")
    pairs = []
    for i in range(6):
        row = input(f"Row {i+1} (symptoms, disease): ")
        if "," in row:
            s, d = row.split(",", 1)
            pairs.append((s.strip().lower(), d.strip()))    #(symptom, disease)
            print(pairs)
    def score(user, row_sym):
        uw = user.split()
        rw = row_sym.split()
        return sum(1 for w in uw if w in rw)
    for t in range(2):
        user = input("Type symptoms: ").strip().lower()
        best_dis, best = "Not sure", 0
        for s, d in pairs:
            sc = score(user, s)
            if sc > best: best, best_dis = sc, d
        print("Predicted:", best_dis)


predict_match_score()