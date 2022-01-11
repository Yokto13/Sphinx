from picotui.widgets import WLabel, Dialog
from typing import List


class MultiLineLabel:
    """ Label that can display multiline text. """
    def __init__(self, text: str, dialog: Dialog, x: int, y: int,w: int=0, lines: int=1):
        """ Inits all labels that together creates multiline label.

            Label are placed row by row. The first label is placed at x,y, the second at x,y+1, etc.

            @param text: string to be displayed as in regular label.
            @param dialog: Dialog instance to which all labels will be added.
            @param x: int coordinate.
            @param y: int coordinate.
            @param w: width of the line.
            @param lines: number of lines (labels).
        """
        self.raw_text = text
        self.w = w
        if not w:
            self.w = len(text)
        self.lines = lines
        self.labels: List[WLabel] = []
        for i in range(lines):
            self.labels.append(WLabel("", w=w))
        for i, label in enumerate(self.labels):
            dialog.add(x, y+i, label)
        self.set_text(text)

    def set_text(self, text):
        """ This should be called for updating the text.txt.

            redraw is done in this function, no need to call it later.
        """
        self.raw_text = text
        words = list(reversed(text.split()))
        parts = []
        for i in range(self.lines):
            parts.append([])
            used = 0
            for j in range(self.w):
                if not words:
                    break
                if len(words[-1]) + 1 + used <= self.w:
                    used += 1 + len(words[-1])
                    parts[-1].append(words[-1])
                    del words[-1]
                else:
                    break
        for i, label in enumerate(self.labels):
            label.t = " ".join(parts[i])
        self.redraw()

    def redraw(self):
        for label in self.labels:
            label.redraw()
