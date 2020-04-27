import src.controllers.temperature_controller as temperature_controller
import src.controllers.volume_controller as volume_controller


def convert_temp(event, context):
    print(f"enter convert temp!")
    return temperature_controller.convert(event, context)


def convert_vol(event, context):
    print(f"enter convert vole!")
    return volume_controller.convert(event, context)
