def filter_messages(messages):
    filtered_messages = []
    dang_counts = []

    for message in messages:
        print(message) # Debugging output
        words = message.split()
        count = words.count("dang")
        cleaned_words = [word for word in words if word != "dang"]
        cleaned_message = " ".join(cleaned_words)

        filtered_messages.append(cleaned_message)
        dang_counts.append(count)

    return filtered_messages, dang_counts