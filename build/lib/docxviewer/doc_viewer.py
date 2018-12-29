import click
from IPython.display import display
from docx import Document


# Directory Listings

def directory_listing():
    import glob
    vals = []
    for filename in glob.glob("*." + 'docx'):
        vals.append(filename)
    return sorted(set(vals))

def display_directory_listing():
    display('\n'.join(directory_listing()))

# View the Doc
def doc_displayer(filename, p_num):
    my_text = Document(filename)
    alist = []
    for paragraph in my_text.paragraphs:
        if paragraph.text == "":
            pass
        else:
            alist.append(paragraph.text)
    display('\n'.join(alist[0:p_num]))

@click.command()
@click.option('--select', '-select', default=3, help="Number of documents to display.")
@click.option('--p_num', '-p_num', default=3, help="Number of paragraphs to display.")
@click.option('--all', is_flag=True, help = "Raise flag to display preview of all doc files in the folder")
@click.option('--see', is_flag=True, help = "Raise flag to display all .docx files in the directory")
def main(select, p_num, all, see):
    if see:
        display_directory_listing()
    else:
        if all:
            filenames = directory_listing()
            for filename in filenames:
                print('\n',filename), doc_displayer(filename,p_num), print('\n')
        else:
            filenames = directory_listing()[0:select]
            for filename in filenames:
                print('\n',filename), doc_displayer(filename,p_num), print('\n')
