class Format:
    def subheaderFormat(subheader):
        string_length = len(subheader)
        print(subheader)
        for _ in range(string_length):
            print("-", end='')
        # Print a newline
        print()

    def welcomeMessage(message):
        border = "=" * (len(message) + 4)
        blank = " " * len(message)
        print(f"{border}\n| {blank} |\n| {message} |\n| {blank} |\n{border}")
        # Print a newline
        print()
