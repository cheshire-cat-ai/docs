import os
import re
import string
import logging
import mkdocs
from lxml import etree
from bs4 import BeautifulSoup
from mkdocs.plugins import BasePlugin


# ------------------------
# Constants and utilities
# ------------------------
RE_PATTERN = r'!\[(.*?)\]\((.*?.drawio)\)'

# Template changed, removed the EDIT button
SUB_TEMPLATE = string.Template(
        "<div class=\"mxgraph\" style=\"max-width:100%;border:1px solid transparent;\" data-mxgraph=\"{&quot;highlight&quot;:&quot;#0000ff&quot;,&quot;resize&quot;:true,&quot;toolbar&quot;:&quot;zoom layers tags lightbox&quot;,&quot;hide-pages&quot;:&quot;1&quot;,&quot;xml&quot;:&quot;$xml_drawio&quot;}\"></div>")

# ------------------------
# Plugin
# ------------------------
class DrawioFilePlugin(BasePlugin):
    """
    Plugin for embedding DrawIO Diagrams into your Docs
    """
    config_scheme = (
        (
            "file_extension",
            mkdocs.config.config_options.Type(str, default=".drawio"),
        ),
    )

    def __init__(self):
        self.log = logging.getLogger("mkdocs.plugins.diagrams")
        self.pool = None

    def on_post_page(self, output_content, config, page, **kwargs):
        if ".drawio" not in output_content.lower():
            # Skip unecessary HTML parsing
            return output_content

        soup = BeautifulSoup(output_content, 'html.parser')

        # search for images using drawio extension
        diagrams = soup.findAll('img', src=re.compile(r'.*\.drawio', re.IGNORECASE))
        if len(diagrams) == 0:
            return output_content

        # add drawio library to body
        lib = soup.new_tag("script", src="https://viewer.diagrams.net/js/viewer-static.min.js?hide-pages=1")
        soup.body.append(lib)

        # substitute images with embedded drawio diagram
        path = os.path.dirname(page.file.abs_src_path)

        for diagram in diagrams:
            diagram.replace_with(BeautifulSoup(self.substitute_image(path, diagram['src'], diagram['alt']), 'html.parser'))

        return str(soup)

    def substitute_image(self, path: str, src: str, alt: str):
        if src.startswith("../"):
            src = src[3:]

        diagram_xml = etree.parse(os.path.join(path, src))
        diagram = self.parse_diagram(diagram_xml, alt)
        escaped_xml = self.escape_diagram(diagram)

        return SUB_TEMPLATE.substitute(xml_drawio=escaped_xml)
    
    def parse_diagram(self, data, alt):
        if alt == None:
            return etree.tostring(data, encoding=str)

        mxfile = data.xpath("//mxfile")[0]

        try:
            # try to parse for a specific page by using the alt attribute
            page = mxfile.xpath(f"//diagram[@name='{alt}']")

            if len(page) == 1:
                parser = etree.XMLParser()
                result = parser.makeelement(mxfile.tag, mxfile.attrib)

                result.append(page[0])
                return etree.tostring(result, encoding=str)
            else:
                print(f"Warning: Found {len(page)} results for page name '{alt}'")
        except e:
            print(f"Error: Could not properly parse page name: '{alt}'")
        
        return etree.tostring(mxfile, encoding=str)

    def escape_diagram(self, str_xml: str):
        str_xml = str_xml.replace("&", "&amp;")
        str_xml = str_xml.replace("<", "&lt;")
        str_xml = str_xml.replace(">", "&gt;")
        str_xml = str_xml.replace("\"", "\&quot;")
        str_xml = str_xml.replace("'", "&apos;")
        str_xml = str_xml.replace("\n", "")
        return str_xml


drawioFilePlugin = DrawioFilePlugin()

# Wrapper for reusing of the plugin code
def on_post_page(output_content, config, page, **kwargs):
    return drawioFilePlugin.on_post_page(output_content, config, page, **kwargs)

