def tts_or_sim():
    try:
        import pyttsx3
    except Exception:
        pyttsx3 = None
    sent = input("Enter a prediction sentence: ")
    rate = input("Choose a rate (slow/normal/fast): ").strip().lower()
    if pyttsx3 is not None:
        try:
            engine = pyttsx3.init() # initionlize the enginepyth
            engine.setProperty("rate", 140 if rate=="slow" else 220 if rate=="fast" else 180)
            print("SPEAK:", sent)
            engine.say(sent)    # anailixe .the text and prepare for speach
            engine.runAndWait()      # read the text out loud
        except Exception:
            print("TTS engine not avalible, using simulation.")
            pyttsx3 = None
    if pyttsx3 is None:
        if rate=="slow":
            print("SPEAK (slow): "); [print(w) for w in sent.split()]
        elif rate=="fast":
            print("SPEAK (fast): >>", sent, ">>", sent)
        else:
            print("SPEAK (normal): ", sent)
    print("How TTS works (simple): text → phonetics → audio wavefrom.")

tts_or_sim()