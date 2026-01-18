def main():
    print("12x Tables")
    for i in range(1, 13):
        for j in range(1, 13):
            print(f"{i * j:4}", end="")
        print()

main()