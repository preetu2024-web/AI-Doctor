def before_after_accuracy():
    """
    Lesson 19 : compare accuracy before/after more data.
    """
    print("=== Before vs after Accuracy (L19) ===")
    base = [("fever cough", "flu", ),("runny nose","cold"),("hedache stress","stress"),
            ("rash itch","allergy"),("stomach pain", "food_poisioning"),("high fever rash","dengue")]
    extra = []
    for i in range(6):
        row = input(f"Extra {i+1} (symptoms and disease): ")
        if "," in row:
            s, d = row.split(",", 1)
            extra.append((s.strip().lower(), d.strip().lower()))
    def score(user, row_sym):
        uw = user.split()
        rw = row_sym.split()
        return sum(1 for w in uw if w in rw)
    def round_acc(pairs, title):
        print(title)
        correct = 0
        for t in range(3):
            user = input("Type symptoms: ").strip().lower()
            best_dis, best_sc = "not sure", 0
            for s, d in pairs:
                sc = score(user, s)
                if sc>best_sc: best_sc, best_dis = sc, d
            print("Predicted:", best_dis)
            if input("Was this correct? (y/n: )").strip().lower()=="y": correct+=1
        print("Accuracy", correct, "/3")
        return correct
    a = round_acc(base, "Round A (seed 6)")
    b = round_acc(base+extra, "Round B (seed + added 6)")
    print(f"Conclution: Round A={a}/3 vs Round B={b}/3. More data often helps.")

before_after_accuracy()
