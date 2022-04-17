import string
import os

chet = 1 #счетчик - курсор по строке
with open("example_old.txt", "r") as example:
    with open("delete.txt", "w+") as delete:
        strexample = example.read()
        delete.write("ALTER TABLE marketing events.country_region DELETE WHERE\n")
        while chet < len(strexample) - 2:
            numcou = strexample.find("==", chet) + 3 #страна начинается тут
            country_code = strexample[numcou:numcou + 2]
            delete.write("country_code = " + country_code + "\n")
            chet = numcou + 10
