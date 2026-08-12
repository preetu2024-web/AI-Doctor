def examples_list():
    """
    Lesson 13
     - Print title
     - Collect 5 pairs (input label) using input()
     - Store in two lists (inputs, labels)
     - Print a neat table, then ask for 1 new input and  exact-match predict
     - Print 3 lines about how examples teach a computer
    """
    print("=== Examples List (L13) ===")
    inputs, labels = [], []
    for i in range(1, 6):
        pair = input(f"Pair {i} (e.g., dog, wolf): ").strip()    # fever cough, flu
        if "," in pair:
            a, b = pair.split(",", 1)
            inputs.append(a.strip())
            labels.append(b.strip())
    print("\nNo. | Input        | Label")
    print("-" * 26)
    for i, (a, b) in enumerate(zip(inputs, labels), 1):
        print(f"{1:>2}  | {a:<12} | {b}")
    q = input("\nTry a new input to predict: ").strip()
    if q in inputs:
        idx = inputs.index(q)
        print("Prediction:", labels[idx])
    else:
        print("Prediction: Not sure yet")
    print("-" * 40)
    print("Learning note 1: We gave examples as input → correct output.")
    print("Learning note 2: The computer can use examples to guess for new inputs.")
    print("Learning note 3: More examples usually improve guesses.")

examples_list()