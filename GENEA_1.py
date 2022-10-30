def filte(string):
    for symbol in string:
            yield''.join([let for let in string if let.isalpha()])

def main():
    res_string = filte(str(input()))
    print(next(res_string))
if __name__ == "__main__":
  main()
