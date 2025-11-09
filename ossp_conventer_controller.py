
from ossp_conventer_model import ConventerModel

class VolumeController:
    def __init__(self, model: ConventerModel, view):
        self.model = model
        self.view = view

    def convert(self, value_str, from_unit, to_unit):
        try:
            value = float(value_str)
            result = self.model.convert_volume(value, from_unit, to_unit)

            text = f"{value} {from_unit} = {result} {to_unit}"
            color = "green"

        except ValueError as e:
            text = f"Помилка: {e}"
            color = "red"

        self.view.update_result(text, color)