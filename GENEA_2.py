def generate_separator(tee):
    source = tee.split("\n")
    for i in source:
        i = i.split(" ")
        yield i


def main():
    q = generate_separator("BUDDYBBUDDUUDBDUBDUDBUDBUDBUDBU\nBDBUDBUDBUBDUBDUDBDUBUDBUD")
    for j in q:
        print(j)

if __name__ == "__main__":
  main()
