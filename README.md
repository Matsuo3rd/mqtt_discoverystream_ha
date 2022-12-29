# MQTT DiscoveryStream integration for Home Assistant

This is an "extension" of the builtin [`mqtt_statestream`](https://www.home-assistant.io/integrations/mqtt_statestream/) integration.  
Besides the functionalities of the hereabove, it also allows to publish and handles an [MQTT "discovery"](https://www.home-assistant.io/docs/mqtt/discovery) setup.

## Supported entities
Provides discovery support for:
- Binary Sensor
- Climate
- Light
- Sensor
- Switch

## Pre-requisites

1. MQTT configured

## Installation

### HACS

1. Launch HACS
1. Navigate to the Integrations section
1. Add this repository as an Custom Repository (Integration) via the menu at top right (Only required if you wish to use this forked version).
1. Search for "MQTT DiscoveryStream"
1. Select "Install this repository"
1. Restart Home Assistant

### Home Assistant

The integration is configured via YAML only.

Example:

```yaml
mqtt_discoverystream:
  base_topic: test_HA
  publish_attributes: false
  publish_timestamps: true
  publish_discovery: true
  include:
    entities:
      - sensor.owm_hourly_humidity
      - sensor.jellyfin_cloud
      - light.wled_esp
  exclude:
    entities:
      - sensor.plug_xiaomi_1_electrical_measurement
```

## Configuration

### Options

This integration can only be configuration via YAML.
The base options are the same as the mqtt_statestream one. 

| key                | default | required | description                                                                  |
| ------------------ | ------- | -------- | ---------------------------------------------------------------------------- |
| base_topic         | none    | yes      | Base topic used to generate the actual topic used to publish.                |
| discovery_topic    | none    | no       | Topic where the configuration topics will be created. Defaults to base_topic |
| publish_attributes | false   | no       | Publish attributes of the entity as well as the state.                       |
| publish_timestamps | false   | no       | Publish the last_changed and last_updated timestamps for the entity.         |
| publish_discovery  | false   | no       | Publish the discovery topic ("config").                                      |
| include / exclude  | none    | no       | Configure which integrations should be included / excluded from publishing.  |

## Credits

- This custom component is based upon the `mqtt_statestream` one from HA Core.  
