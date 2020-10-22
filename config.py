DATA_PATH = r'C:\Users\Wondim\Desktop\sensors_bridge\data'
LAN_PORT = 50000
REMOVE_FILES_OLDER_THAN=3
PORT_INFO = {
    'COM3': {
        'name': 'co2procv',
        'byte_size': 72, 'baud_rate': 19200,
        'separator': r',',
        'header': ['start', 'year', 'month', 'day', 'hour',
                   'minute', 'second', 'zero_ad', 'current_ad', 'measured_co2',
                   'avarage_irga_temperature', 'humidity', 'humidity_sensor_temperature',
                   'gas_stream_pressure', 'igr_detector_temperature'],
'exclude':[]
    },
    'COM4': {
        'name': 'ecotriplet1',

        'byte_size': 48, 'baud_rate': 19200,
        'separator': r'\t+',
        'header': ['date', 'time', 'wavelength1', 'chl_raw',
                   'wavelength2', 'peryth_raw', 'wavelength3',
                   'pcyan_raw', 'wavelength4'],
'exclude':[]
    },
    'COM5': {
        'name': 'ecotriplet2',
        'byte_size': 44, 'baud_rate': 19200,
        'separator': r'\t+',
        'header': ['date', 'time', 'wavelength1', 'bb_470_raw',
                   'wavelength2', 'bb_532_raw', 'wavelength3',
                   'bb_650_raw', 'wavelength4'],
'exclude':[]
    },
    'COM6': {
        'name': 'ecotriplet3',
        'byte_size': 45, 'baud_rate': 19200,
        'separator': r'\t+',
        'header': ['date', 'time', 'wavelength1',
                   'turbidity_595_nm_raw', 'wavelength2',
                   'turbidity_700_nm_raw', 'wavelength3',
                   'cdom_460_nm_raw', 'wavelength4'],
'exclude':[]
    },
    'COM7': {
        'name': 'dissolvedoxygen',
        'byte_size': 72, 'baud_rate': 9600,
        'separator': r',',
        'header': [
            'raw_phase_delay', 'raw_thermistor_voltage', 'oxygen_ml_l', 'temperature'
        ],
'exclude':[]
    },
    'GPRMC': {
        'name': 'gpsposition',
        'header': [
            'timestamp', 'status', 'latitude', 'latitude_direction', 'longitude',
            'longitude_direction', 'speed_over_ground', 'true_course', 'date',
            'magnetic_variation', 'magnetic_variation_direction', 'mode_indicator'
        ],
        'exclude': []
    },
    'WIMDA': {
        'name': 'meteorology',
        'header': [
            'barometric_pressure_inches', 'inches_of_mercury', 'barometric_pressure_bars',
            'bars', 'air_temperature', 'air_degrees', 'water_temperature', 'air_degrees',
            'relative_humidity', 'absolute_humidity', 'dew_point', 'dew_degrees',
            'wind_direction_true', 'true', 'wind_direction_magnetic', 'magnetic',
            'wind_speed_knots', 'wind_knots', 'wind_speed_meter_per_second', 'meter_per_second'
        ],

        'exclude': ['inches_of_mercury', 'bars', 'air_degrees', 'water_temperature', 'air_degrees',
                    'relative_humidity', 'absolute_humidity', 'dew_point', 'dew_degrees',
                    'wind_direction_true', 'true', 'wind_direction_magnetic', 'magnetic',
                    'wind_speed_knots', 'wind_knots', 'wind_speed_mps', 'meter_per_second']
    },
    'WIMWV': {
        'name': 'wind',
        'header': ['wind_angle', 'reference', 'wind_speed', 'wind_speed_units', 'status'],
        'exclude': []
    },
}
