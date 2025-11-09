import tkinter as tk
from ossp_conventer_model import ConventerModel
from ossp_conventer_controller import VolumeController
from ossp_conventer_view_tk import VolumeView

if __name__ == '__main__':
    root = tk.Tk()
    model = ConventerModel()
    view = VolumeView(root, None, model.get_supported_units())
    controller = VolumeController(model, view)
    view.controller = controller

    root.mainloop()