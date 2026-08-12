def explain_prediction():
    print("=== Explain Prediction (L18) ===")
    pairs = []
    for i in range(6):
        row = input(f"Row {i+1} (symptoms, disease): ")
        if "," in row:
            s, d = row.split(",", 1)
            pairs.append(s.strip().lower(), d.strip().lower())
    legend = {"flu": "😷", "cold": "🤧", "stress": "🤕"}
    def score(user, row_sym):
        uw = user.split()
        rw = row_sym.split()
        return sum(1 for w in uw if w in rw)
    for t in range(2):
        user = input("Type symptoms: ").strip().lower()
        best_dis, best_sc = "not sure", 0
        best_row = 0
        for s, d in pairs:
            sc = score(user, s)
            if sc>best_sc: best_dis, best_row = sc, d, s
            uw = user.split(); rw = best_row.split()
            found = [w.upper() for w in uw if w in rw]
            not_found = [w for w in uw if w not in rw]
            print("User words:", uw)
            print("FOUND:", found)
            print("NOT FOUND:", not_found)
            print("Prediction:", best_dis, legend.get(best_dis, ""))
        print("This is not medical advice.")

explain_prediction()