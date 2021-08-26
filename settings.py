from pathlib import Path

BASE_PATH = Path(__file__).resolve().parent

########################################################################################################################
# Generate invitations. Change the values in this area according to your needs
TITLE = "MarioParty"
OUTPUT_DIRECTORY = BASE_PATH.joinpath('OUTPUT')
LANG = 'en'  # 'en' or 'da'
TEX_PATH = "C:\\texlive\\2021\\bin\\win32\\pdflatex"
########################################################################################################################
# Language settings for correct grammar

if LANG == 'da':
    from translations.da import *
else:
    from translations.en import *

INVITEES_FILE = BASE_PATH.joinpath('invitees.txt')
TEX_TEMPLATE_FILE = BASE_PATH.joinpath('template.tex')
