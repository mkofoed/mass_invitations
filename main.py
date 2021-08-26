import os
import shutil

from settings import *


class GenerateInvitations:
    def __init__(self):
        self.tex_template = self.load_tex_template()
        self.invitees = self.load_invitees()
        self.create_directories()

    @staticmethod
    def load_invitees() -> str:
        with open(INVITEES_FILE) as f:
            invitees = f.readlines()
        yield from invitees

    @staticmethod
    def load_tex_template() -> str:
        with open(TEX_TEMPLATE_FILE, encoding='utf8') as f:
            return f.read()

    def generate_invitations(self):
        for names_line in self.invitees:
            names_line_list = [x.strip() for x in names_line.split(',')]
            file_name = names_line.replace(',', '').replace(' ', '_').replace('\n', '')
            file_name = f'{TITLE}__{file_name}.tex'
            tex = self.replace_text(names_line_list)
            self.save_pdf(file_name, tex)
        self.cleanup()

    @staticmethod
    def get_names_string(names: list) -> str:
        if len(names) == 1:
            return names[0]
        if len(names) == 2:
            return ' \& '.join(names)
        return ', '.join(names[:-2]) + ', ' + ' \& '.join(names[-2:])

    def replace_text(self, names: list) -> str:
        tex = self.tex_template.replace('{{ name }}', self.get_names_string(names))
        tex = tex.replace('{{ you }}', YOU_PLURAL if len(names) > 1 else YOU_SINGULAR)
        return tex

    @staticmethod
    def save_pdf(file_name: str, text: str):
        path = BASE_PATH.joinpath(file_name)
        with open(path, 'w', encoding='utf8') as out_file:
            out_file.write(text)
        os.system(f'{TEX_PATH} {path}')
        os.system(f'{TEX_PATH} {path}')
        shutil.copy(file_name.replace('.tex', '.pdf'), OUTPUT_DIRECTORY)

    @staticmethod
    def cleanup():
        [os.remove(_file) for _file in os.listdir(BASE_PATH) if
         _file.endswith('.log') or _file.endswith('.aux') or _file.endswith('.pdf') or (
                     _file.endswith('.tex') and 'template' not in _file)]

    @staticmethod
    def create_directories():
        if not os.path.exists(OUTPUT_DIRECTORY):
            os.makedirs(OUTPUT_DIRECTORY)


a = GenerateInvitations()
a.generate_invitations()
