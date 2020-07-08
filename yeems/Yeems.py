import wx

class Yeems(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='Yeems')
        panel = wx.Panel(self)
        my_sizer = wx.BoxSizer(wx.VERTICAL)
        my_btn = wx.Button(panel, label='Dab')
        my_btn.Bind(wx.EVT_BUTTON, self.on_press)
        my_sizer.Add(my_btn, 0, wx.ALL | wx.CENTER, 5)
        panel.SetSizer(my_sizer)
        self.Show()

    def on_press(self, event):
        png = wx.Image('../Resources/Untitled.png', wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        wx.StaticBitmap(self, -1, png, (10, 5), (png.GetWidth(), png.GetHeight()))


if __name__ == '__main__':
    app = wx.App()
    frame = Yeems()
    app.MainLoop()