from models import Quote
import connect

quotes = Quote.objects()

def find_by_name(value):
    finding_quotes = []
    full_name = value.split(":")[1]
    for quote in quotes:
        if quote.author.fullname.lower() == full_name.lower():
            finding_quotes.append(quote.quote)
    print(finding_quotes)


def find_by_tag(value):
    finding_quotes = []
    tags = value.split(":")[1].split(",")
    for quote in quotes:
        for tag in tags:
            if tag in quote.tags:
                finding_quotes.append(quote.quote)
    print(finding_quotes)


while True:
    command = input("enter your 'command:value' ")

    if command.startswith("name"):
        find_by_name(command)
    elif command.startswith("tag"):
        find_by_tag(command)
    elif command.startswith("exit"):
        break
    else:
        print('wrong command')
        continue