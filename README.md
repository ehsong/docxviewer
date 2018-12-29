docxviewer
================

Copyright (c) 2018-2019 Eunhou Esther Song

This is a simple document previewer which allows users to preview
multiple .docx documents at once. The options and flags include number
of paragraphs to preview and number of documents to preview in a
directory. The output prints the file name and paragraphs in each .docx
file.

### Python Package Index

<https://pypi.org/project/docxviewer/>

### Installation

    pip3 install docxviewer

### Dependencies

  - Python 3
  - Click
  - ipython
  - docx

### Command Line Options

  - –help: see help page
  - –see: raise flag to view the name of all .docx files in a directory
  - –p\_num: set number of paragraphs to preview, the default is 3
  - –select: set number of documents to preview, the default is 3
  - –all: raise flag to display preview of all documents in a directory

### Examples

Displays names of all .docx files in a directory

    docxviewer --see

Displays the first three paragraphs of three documents in a directory,
selected by alaphabetical order.

    docxviewer

Displays the first three paragraphs of all documents in a directory.

    docxviewer --all

Displays the first six paragraphs of five documents in a directory.

    docxviewer --p_num 6 --select 5

### Output

    >>docxviewer
    
     125syllabus18fal.docx
    现代中国小说选读
    Chinese through Modern Fiction
    MWF 12:30pm -1:20pm
    
    
    
     FieldTrip01Overview(2018-10-13)-v02.docx
    Urban Studies 20
    LOGISTICAL SUMMARY
    for
    
    
    
     ch4.docx
    Memo on Data and Prelim Analysis 
    Data Collection
    Background
