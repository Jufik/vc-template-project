# -*- coding: utf-8 -*-

import markdown as md
from markdown.extensions import Extension
from markdown.treeprocessors import Treeprocessor


class NewTabLinksTreeProcessor(Treeprocessor):
    """
    class which add "target='_blank'" into markdown links

    """
    def link_process(self, element):
        """ Traverse the element tree. """
        children = element.getchildren()
        for child in children:
            if child.tag == 'a':
                child.attrib['target'] = '_blank'
            self.link_process(child)

    def run(self, root):
        self.link_process(root)
        return root


class NewTabLinksExtension(Extension):
    """ Makes links open in a new tab. """
    def extendMarkdown(self, md, md_globals):
        md.registerExtension(self)
        md.treeprocessors.add("newtablinks",
                              NewTabLinksTreeProcessor(self), "_end")


def markdown(text):
    """ Return markdown `text` rendered in HTML. """
    return md.markdown(text, [NewTabLinksExtension()])