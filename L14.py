def collect_in_memory():
    """
    Lesson 14: collect 10 'symptoms, disease' rows
    into two lists and preview unique diseases.
    """
    print("=== Build In-Memory Dataset (L14) ===")
    symptoms_list, disease_list = [], []
    for i in range(1, 11):
        row = input(f"Row {i} (symptoms, disease): ")       # fever cough, flu
        if "," not in row:
            print("Please include a comma; try again."); continue
        s, d = row.split(",", 1)
        symptoms_list.append(s.strip()); disease_list.append(d.strip())
    print("\nNo. | Symptoms                | Disease")
    print("-" * 44)
    for i, (s, d) in enumerate(zip(symptoms_list, disease_list), 1):
        print(f"{i:>2}  | {s[:22]:<22} | {d}")
    uniques = []
    for d in disease_list:
        if d not in uniques: uniques.append(d)
    print(f"\nTotal rows: {len(symptoms_list)} | Unique diseases: {len(uniques)}")
    print("Summary: Collected dataset in memory (lists only).")
 
collect_in_memory()