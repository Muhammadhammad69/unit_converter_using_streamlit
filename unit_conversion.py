from units import all_units
from decimal import Decimal
# for unit in all_units:
# print(unit)


def convert_temperature(value, from_unit, to_unit):
    get_value = value
    
    from_data = all_units.get("temperature").get(from_unit)
    to_data = all_units.get("temperature").get(to_unit)

    

    # Convert input to Celsius first
    if from_unit == "fahrenheit":
        value = (value - from_data["offset"]) / from_data["value"]
    elif from_unit == "kelvin":
        value = value - from_data["offset"]

    # Convert from Celsius to target unit
    if to_unit == "fahrenheit":
        value = (value * to_data["value"]) + to_data["offset"]
    elif to_unit == "kelvin":
        value = value + to_data["offset"]
     # Already in Celsius

    return {"message": f"The {get_value} {from_data["unit"]} = {value} {to_data["unit"]}", "answer_value": value}

def unit_conversion_func(unit_category, from_unit, to_unit, value):
    unit_category = unit_category.strip().lower().replace(" ", "_")
    from_unit = from_unit.strip().lower().replace(" ", "_")
    to_unit = to_unit.strip().lower().replace(" ", "_")
    
    from_unit_value = 0
    to_unit_value = 0
    from_unit_symbol = ""
    to_unit_symbol = ""
    if unit_category == "temperature":
        print("temperature")
        return convert_temperature(value, from_unit, to_unit)
    
    for unit in all_units:
        print("tep")
        if unit == unit_category:
            # print("unit")
            for sub_unit in all_units[unit]:
                if sub_unit == from_unit:
                    # print("sub")
                    from_unit_value = all_units[unit][sub_unit]["value"] * value
                    from_unit_symbol = all_units[unit][sub_unit]["unit"]
                if sub_unit == to_unit:
                    to_unit_value = all_units[unit][sub_unit]["value"]
                    to_unit_symbol = all_units[unit][sub_unit]["unit"]
    result = from_unit_value / to_unit_value
    final_value = result if result < 1 else round(result,4)
    conversion_info = {
        "message": f"The {value} {from_unit_symbol} = {final_value} {to_unit_symbol}",
        "answer_value": result
    }
    return conversion_info


# result = unit_conversion("area","square_kilometer","hectare",20)
# print(result)
