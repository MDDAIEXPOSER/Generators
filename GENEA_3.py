def convei_value():
    for values in range(0,100):
        if values % 11 == 0:
            yield values


def main():
    print(list(convei_value()))

if __name__ == "__main__":
  main()
