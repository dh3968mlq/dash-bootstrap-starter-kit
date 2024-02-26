from dash import register_page, dcc, html
from src.lorem import lorem

def body():
    layout = dcc.Markdown('''

# This is another page

This page has been rendered from markdown 
using dcc.Markdown()

## A sample image
                      
This is held as static content within this app
                      
![Example image](/static/sample_image.png)   
                      
## Repeated text to show scrolling

''' + 
    " ".join([lorem + "\n\n" for _ in range(30)])
    )
    return layout

def sidebar():
    sidelayout = html.H4("Custom sidebar layout")
    return sidelayout