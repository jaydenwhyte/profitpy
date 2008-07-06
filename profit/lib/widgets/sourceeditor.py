#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2007 Troy Melhase <troy@gci.net>
# Distributed under the terms of the GNU General Public License v2

from PyQt4.QtGui import QFrame
try:
    from Qsci.qsciscintilla import QsciScintilla
except (ImportError, ):
    import new, sys
    try:
        import PyQt4.Qsci
        sys.modules['Qsci'] = new.module('Qsci')
        sys.modules['Qsci.qsciscintilla'] = new.module('Qsci.qsciscintilla')
        sys.modules['Qsci.qsciscintilla'].QsciScintilla = PyQt4.Qsci.QsciScintilla
    except (ImportError, ):
        pass
try:
    raise ImportError('')
    from profit.lib.widgets.ui_advancededitor import Ui_AdvancedEditor as Editor
except (ImportError, ):
    from profit.lib.widgets.ui_basiceditor import Ui_BasicEditor as Editor
try:
    from PyQt4.Qsci import QsciLexerPython
except (ImportError, ):
    QsciLexerPython = None

## wha?
QsciLexerPython = None

from profit.lib.core import Signals


class SourceEditor(QFrame, Editor):
    def __init__(self, parent=None):
        QFrame.__init__(self, parent)
        self.setupUi(self)
        if QsciLexerPython:
            self.textEdit.setLexer(QsciLexerPython(self.textEdit))
        self.connect(
            self.textEdit, Signals.textChangedEditor,
            self, Signals.textChangedEditor)

    def text(self):
        return self.textEdit.text()

    def setText(self, text):
        return self.textEdit.setText(text)