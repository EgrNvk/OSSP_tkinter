class ConventerModel:
    def __init__(self):
        self.units_to_liters = {"l": 1, "ml": 0.001, "m3": 1000, "cm3": 0.001, "dm3": 1, "gal": 3.78541}

    def get_supported_units(self):
        return list(self.units_to_liters.keys())

    def convert_volume(self, value: float, from_unit: str, to_unit: str) -> float:
        from_unit = from_unit.lower()
        to_unit = to_unit.lower()

        if from_unit not in self.units_to_liters or to_unit not in self.units_to_liters:
            raise ValueError("Підтримуються лише одиниці: l, ml, m3, cm3, dm3, gal")

        liters = value*self.units_to_liters[from_unit]
        result = liters/self.units_to_liters[to_unit]
        return result