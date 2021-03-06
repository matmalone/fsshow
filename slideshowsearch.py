#!/usr/bin/python
"""
fsshow -- A simple slideshow generator for Flickr hosted images.
Copyright (C) 2006 Mat Malone

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
"""

import wx

class SlideshowSearchDialog(wx.Dialog):
    def __init__(self, parent, ID, title, size=wx.DefaultSize,
                 pos=wx.DefaultPosition, style=wx.DEFAULT_DIALOG_STYLE):

        # Instead of calling wx.Dialog.__init__ we precreate the dialog
        # so we can set an extra style that must be set before
        # creation, and then we create the GUI dialog using the Create
        # method.
        pre = wx.PreDialog()
        pre.SetExtraStyle(wx.DIALOG_EX_CONTEXTHELP)
        pre.Create(parent, ID, title, pos, size, style)

        # This next step is the most important, it turns this Python
        # object into the real wrapper of the dialog (instead of pre)
        # as far as the wxPython extension is concerned.
        self.PostCreate(pre)

        # Now continue with the normal construction of the dialog
        # contents
        sizer = wx.BoxSizer(wx.VERTICAL)

        #label = wx.StaticText(self, -1, "This is a wx.Dialog")
        #label.SetHelpText("This is the help text for the label")
        #sizer.Add(label, 0, wx.ALIGN_CENTRE|wx.ALL, 5)

        box = wx.BoxSizer(wx.HORIZONTAL)

        label = wx.StaticText(self, -1, "Flickr email, username\nor photo stream link:")
        #label.SetHelpText("This is the help text for the label")
        box.Add(label, 0, wx.ALIGN_CENTRE|wx.ALL, 5)

        self._searchString = wx.TextCtrl(self, -1, "m2@innerlogic.org", size=(300,-1))
        self._searchString.SetHelpText("Enter your search parameter here")
        box.Add(self._searchString, 1, wx.ALIGN_CENTRE|wx.ALL, 5)

        sizer.Add(box, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5)

        box = wx.BoxSizer(wx.HORIZONTAL)

        label = wx.StaticText(self, -1, "Minimum display time (seconds):")
        label.SetHelpText("This is the help text for the label")
        box.Add(label, 0, wx.ALIGN_CENTRE|wx.ALL, 5)

        self._slider = wx.Slider(self, -1, 5, 1, 100, (30, 60), (250, -1),
                                 wx.SL_HORIZONTAL | wx.SL_AUTOTICKS | wx.SL_LABELS)
        self._slider.SetTickFreq(6, 1)
        self._slider.SetHelpText("Minimum length of time for a slide to show. "
                               + "Large pictures may take longer due to bandwidth constraints.")
        box.Add(self._slider, 1, wx.ALIGN_CENTRE|wx.ALL, 5)

        sizer.Add(box, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5)

        line = wx.StaticLine(self, -1, size=(20,-1), style=wx.LI_HORIZONTAL)
        sizer.Add(line, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.TOP, 5)

        btnsizer = wx.StdDialogButtonSizer()
        
        if wx.Platform != "__WXMSW__":
            btn = wx.ContextHelpButton(self)
            btnsizer.AddButton(btn)
        
        btn = wx.Button(self, wx.ID_OK)
        btn.SetHelpText("Start the slideshow")
        btn.SetLabel("Start")
        btn.SetDefault()
        btnsizer.AddButton(btn)

        btn = wx.Button(self, wx.ID_CANCEL)
        btn.SetHelpText("Cancel the slideshow")
        btnsizer.AddButton(btn)
        btnsizer.Realize()

        sizer.Add(btnsizer, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5)

        self.SetSizer(sizer)
        sizer.Fit(self)
    def GetSearchString(self):
        return self._searchString.GetValue()
    
    def GetDisplayTime(self):
        return self._slider.GetValue()

if __name__ == "__main__":
    import slideshowview, util
    view = slideshowview.SlideshowView()
    dlg = SlideshowSearchDialog(view, -1, "New Slideshow", size=(470, 200),
        #style = wx.CAPTION | wx.SYSTEM_MENU | wx.THICK_FRAME)
        style = wx.DEFAULT_DIALOG_STYLE)
    dlg.CenterOnScreen()

    # this does not return until the dialog is closed.
    val = dlg.ShowModal()
    print dlg.GetSearchString(), dlg.GetDisplayTime()
    if val == wx.ID_OK:
        util.debugLog("You pressed OK\n")
    else:
        util.debugLog("You pressed Cancel\n")    
    
