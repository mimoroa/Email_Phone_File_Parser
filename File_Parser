#! /usr/bin/evn python 3
from Parser_Defs import Parser

parser = Parser()

unparsed = input("Please add the absolute path to the file being parsed: ")
email = input(f"Would you like to parse the email address from{unparsed}?\n Yes or NO? ").lower()
numbers = input(f"Would you like to parse the phone numbers from{unparsed}?\n Yes or NO? ").lower()


if email == "yes":
    print("EMAIL LIST")
    parser.email_parser(unparsed)
    print("COMPLETED")
if numbers == "yes":
    print("PHONE NUMBER LIST")
    parser.phone_number_parser(unparsed)
    print("COMPLETED")
