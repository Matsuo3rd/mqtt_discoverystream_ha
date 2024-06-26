"""Constants for MQTT Discovery Stream."""

from datetime import timedelta

from homeassistant.components.input_select import DOMAIN as INPUT_SELECT_DOMAIN
from homeassistant.const import Platform

ATTR_COLOR = "color"
ATTR_H = "h"
ATTR_S = "s"
ATTR_X = "x"
ATTR_Y = "y"
ATTR_R = "r"
ATTR_G = "g"
ATTR_B = "b"

ATTR_PRESET_COMMAND = "command_preset"
ATTR_MODE_COMMAND = "command_mode"
ATTR_TEMP_COMMAND = "command_temperature"
ATTR_SET_LIGHT = "set_light"
ATTR_SET = "set"
ATTR_JSON = "JSON"
ATTR_COLOR = "color"
ATTR_ATTRIBUTES = "attributes"
ATTR_CONFIG = "config"
ATTR_SUGGESTED_DISPLAY_PRECISION = "suggested_display_precision"

CONF_BASE_TOPIC = "base_topic"
CONF_COMMAND_TOPIC = "command_topic"
CONF_DISCOVERY_TOPIC = "discovery_topic"
CONF_LOCAL_STATUS = "local_status"
CONF_OFFLINE_STATUS = "offline_status"
CONF_ONLINE_STATUS = "online_status"
CONF_PUBLISH_ATTRIBUTES = "publish_attributes"
CONF_PUBLISH_TIMESTAMPS = "publish_timestamps"
CONF_PUBLISH_DISCOVERY = "publish_discovery"
CONF_PUBLISHED = "conf_published"
CONF_PUBLISH_RETAIN = "publish_retain"
CONF_REMOTE_STATUS = "remote_status"
CONF_REPUBLISH_TIME = "republish_time"

DEFAULT_LOOP_TIME = timedelta(minutes=5)
DEFAULT_RETAIN = False
DEFAULT_STATE_SLEEP = 1.5


DOMAIN = "mqtt_discoverystream"


STATE_CAPITAL_ON = "ON"
STATE_CAPITAL_OFF = "OFF"

# These constants are translated via abberviations in mqtt.abbreviations
CONF_AVTY = "avty"
CONF_AVTY_MODE = "avty_mode"
CONF_CMD_T = "cmd_t"
CONF_DEV = "dev"
CONF_DEV_CLA = "dev_cla"
CONF_ENT_CAT = "ent_cat"
CONF_JSON_ATTR_T = "json_attr_t"
CONF_OBJ_ID = "obj_id"
CONF_OPS = "ops"
CONF_STAT_T = "stat_t"
CONF_STAT_CLA = "stat_cla"
CONF_SUG_DSP_PRC = "sug_dsp_prc"
CONF_UNIQ_ID = "uniq_id"
CONF_UNIT_OF_MEAS = "unit_of_meas"

CONF_MDL = "mdl"
CONF_MF = "mf"
CONF_SW = "sw"
CONF_IDS = "ids"
CONF_CNS = "cns"
CONF_PL_ON = "pl_on"
CONF_PL_OFF = "pl_off"

SUPPORTED_ENTITY_TYPES = [
    Platform.BINARY_SENSOR,
    Platform.CLIMATE,
    Platform.COVER,
    Platform.DEVICE_TRACKER,
    Platform.LIGHT,
    Platform.SENSOR,
    Platform.SWITCH,
    INPUT_SELECT_DOMAIN,
]

SUPPORTED_COMMANDS = {
    Platform.BINARY_SENSOR: [],
    Platform.CLIMATE: [ATTR_MODE_COMMAND, ATTR_PRESET_COMMAND, ATTR_TEMP_COMMAND],
    Platform.COVER: [ATTR_SET],
    Platform.DEVICE_TRACKER: [],
    Platform.LIGHT: [ATTR_SET_LIGHT],
    Platform.SENSOR: [],
    Platform.SWITCH: [ATTR_SET],
    INPUT_SELECT_DOMAIN: [ATTR_SET],
}

OUTPUT_ENTITIES = {
    Platform.BINARY_SENSOR: Platform.BINARY_SENSOR,
    Platform.CLIMATE: Platform.CLIMATE,
    Platform.COVER: Platform.COVER,
    Platform.DEVICE_TRACKER: Platform.DEVICE_TRACKER,
    Platform.LIGHT: Platform.LIGHT,
    Platform.SENSOR: Platform.SENSOR,
    Platform.SWITCH: Platform.SWITCH,
    INPUT_SELECT_DOMAIN: Platform.SELECT,
}
