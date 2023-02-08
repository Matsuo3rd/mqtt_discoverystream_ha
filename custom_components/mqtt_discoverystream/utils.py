"""Utilities for MQTT Discovery Stream."""
import json

from homeassistant.components import mqtt
from homeassistant.const import ATTR_STATE
from homeassistant.helpers.json import JSONEncoder

from .const import ATTR_ATTRIBUTES


async def async_publish_base_attributes(hass, new_state, mybase):
    """Publish the basic attributes for the entity state."""
    await mqtt.async_publish(hass, f"{mybase}{ATTR_STATE}", new_state.state, 1, True)

    attributes = dict(new_state.attributes.items())
    encoded = json.dumps(attributes, cls=JSONEncoder)
    await mqtt.async_publish(hass, f"{mybase}{ATTR_ATTRIBUTES}", encoded, 1, True)