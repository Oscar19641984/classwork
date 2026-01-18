def bottles_song(start=10):
    for n in range(start, 0, -1):

        bottle_word = "bottle" if n == 1 else "bottles"
        next_bottle_word = "bottle" if n-1 == 1 else "bottles"

        print(f"{n} green {bottle_word} hanging on the wall,")
        print(f"{n} green {bottle_word} hanging on the wall,")
        print("And if one green bottle should accidentally fall,")
        print(f"There'll be {n-1} green {next_bottle_word} hanging on the wall.\n")

bottles_song(10)