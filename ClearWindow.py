class ClearWindow:
    menudefs = [
        ('options', [None,
                     ('Clear Shell Window', '<<clear-window>>'),
                     ]), ]
 
    def __init__(self, editwin):
        self.editwin = editwin
        self.text = self.editwin.text
        self.text.bind("<<clear-window>>", self.clear_window2)
 
        self.text.bind("<<undo>>", self.undo_event)  # add="+" doesn't work
 
    def undo_event(self, event):
        text = self.text
 
        text.mark_set("iomark2", "iomark")
        text.mark_set("insert2", "insert")
        self.editwin.undo.undo_event(event)
 
        # fix iomark and insert
        text.mark_set("iomark", "iomark2")
        text.mark_set("insert", "insert2")
        text.mark_unset("iomark2")
        text.mark_unset("insert2")
 
    def clear_window2(self, event):  # Alternative method
        # work around the ModifiedUndoDelegator
        text = self.text
        text.undo_block_start()
        text.mark_set("iomark2", "iomark")
        text.mark_set("iomark", 1.0)
        text.delete(1.0, "iomark2 linestart")
        text.mark_set("iomark", "iomark2")
        text.mark_unset("iomark2")
        text.undo_block_stop()
        if self.text.compare('insert', '<', 'iomark'):
            self.text.mark_set('insert', 'end-1c')
        self.editwin.set_line_and_column()
 
    def clear_window(self, event):
        # remove undo delegator
        undo = self.editwin.undo
        self.editwin.per.removefilter(undo)
 
        # clear the window, but preserve current command
        self.text.delete(1.0, "iomark linestart")
        if self.text.compare('insert', '<', 'iomark'):
            self.text.mark_set('insert', 'end-1c')
        self.editwin.set_line_and_column()
 
        # restore undo delegator
        self.editwin.per.insertfilter(undo)