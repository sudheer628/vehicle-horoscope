# Vehicle-Horoscope
This is a python program that will analyse whether vehicle registration number is suitable or not, based on your zodiac lucky number, date of birth.

To install please follow the next steps

1. Go to install dir
2. Create virtual environment
   1. `python3 -m venv .venv`
3. And activate
   1. `source .venv/bin/activate`
4. Install all dependencies (applies if the requirements.txt file exists)
   1. `python3 -m pip install -d requirements.txt`

**Total points - 11 (accumuated by sum of registration number, matching with zodiac lucky number, DoB lucky number, number quality..etc)**

**If the output gives 7 and above, that means the registration number is suitable according to your details given.**

## Single registration number - detailed output

Use `python3 LN_detailed.py` and enter desired registration number, DoB, lucky number so theat program will analyze compatibility.

## Bulk registration numbers - max points to each

Update bulk-num-list.csv file with list vehicle registration numbers and execute `python3 LN_bulk.py` which will ask for DoB, Lucky number, max points from the output (exp: print numbers only greater than 7 out of 11). this will analyze all the registration numbers from input file with customer DoB and lucky number, and print output based on given max points.
