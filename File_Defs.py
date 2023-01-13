#! /usr/bin/env python3
import re


class Parser:

    def phone_number_parser(self, txt):
        # retrive the contact information from the text file
        with open(txt, "r") as my_file:
            content = my_file.read()
        # Use Regex to filter the list of numbers
        for match in re.findall(r"[1]?\(?\d{3}\)?\s?\.?\d{3}\.?\s?\d{4}", content):
            # filters spaces and special characters from the parsed phone numbers
            num = match.translate({ord(i): None for i in "()-."})
            parsed_numbers = re.sub(r"\s+", "", num)
            print(parsed_numbers)

    def email_parser(self, txt):
        # retrive the contact information from the text file
        with open(txt, "r") as my_file:
            content = my_file.read()
        # Use Regex to filter the list of emails
        for m in re.finditer(r"[a-zA-Z0-9-._]+@[a-zA-Z0-9-]+\.(com|edu|net|gov)", content):
            print(m.group(0))
