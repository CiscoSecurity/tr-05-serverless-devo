import json


class Config:
    settings = json.load(open('container_settings.json', 'r'))
    VERSION = settings["VERSION"]

    SUPPORTED_TYPES = [
        'amp_computer_guid',
        'certificate_common_name',
        'certificate_issuer',
        'certificate_serial',
        'cisco_mid',
        'cisco_uc_id',
        'device',
        'domain',
        'email',
        'email_messageid',
        'email_subject',
        'file_name',
        'file_path',
        'hostname',
        'imei',
        'imsi',
        'ip',
        'ipv6',
        'mac_address',
        'md5',
        'ms_machine_id',
        'mutex',
        'ngfw_id',
        'ngfw_name',
        'odns_identity',
        'odns_identity_label',
        'orbital_node_id',
        'pki_serial',
        'process_name',
        'registry_key',
        'registry_name',
        'registry_path',
        's1_agent_id',
        'sha1',
        'sha256',
        'swc_device_id',
        'url',
        'user',
        'user_agent'
    ]

    DEFAULT_CTR_ENTITIES_LIMIT = 100
    TOO_MANY_MSGS_WARNING_LIMIT = DEFAULT_CTR_ENTITIES_LIMIT + 1

    USER_AGENT = ('SecureX Threat Response Integrations '
                  '<tr-integrations-support@cisco.com>')

    DEFAULT_TIMEOUT = 25
    DEFAULT_RETRIES = 2
