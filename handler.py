import src.controllers.temperature_controller as temperature_controller
import src.controllers.volume_controller as volume_controller


def convert_temperatures(event, context):
    return temperature_controller.convert(event, context)


def convert_volumes(event, context):
    return volume_controller.convert(event, context)
