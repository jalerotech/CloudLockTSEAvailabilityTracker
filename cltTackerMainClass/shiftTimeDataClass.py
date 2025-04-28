import logging
from datetime import datetime
logging.basicConfig(
    format='%(asctime)s %(levelname)s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')


class ShifttimeData:
    def __init__(self):
        self.logger = logging.getLogger('ShifttimeData')
        self.currentDateAndTime = datetime.now()
        self.today = self.currentDateAndTime.strftime('%A')

    def theatre_shift_time(self) -> dict:
        """
        Produces the theatre name, and shift time needed to send the start and stop of shift alert.
        """

        '''
        
        Time Data:
        
        === UTC ===				        === CET ===          === Local time ===
        APAC: 0100 – 0900 				03:00 - 11:00        11:00 - 19:00  AEDT/AEST (DONE)
        EMEA: 0900 – 1730				11:00 - 19:30        11:00 - 19:30  (DONE)
        NA EAST: 1300 – 2130            15:00 - 23:30        09:00 - 17:30 EST/EDT (DONE)
        NA WEST: 1600 – 0100            18:00 - 03:00        12:00 - 21:00 (DONE

        '''
        # # Shift start
        # APAC
        # Except for Saturday and Sunday
        #  === UTC ===				        === CET ===          === Local time ===
        #  APAC: 0100 – 0900 				03:00 - 11:00        11:00 - 19:00  AEDT/AEST
        if self.today != "Saturday" and self.today != "Sunday":
            if (self.currentDateAndTime.hour == 3) and (self.currentDateAndTime.minute == 0):
                self.logger.info('Getting shift time and status...')
                shift_data = {
                    "theatre": "TSE_APAC",
                    "shift_time": "11:00 AEDT",
                    "status": "started 🎬"
                }
                return shift_data

            #  === UTC ===				        === CET ===          === Local time ===
            #  EMEA: 0900 – 1730				11:00 - 19:30        11:00 - 19:30
            if (self.currentDateAndTime.hour == 11) and (self.currentDateAndTime.minute == 1):
                self.logger.info('Getting shift time and status...')
                shift_data = {
                    "theatre": "TSE_EMEA",
                    "shift_time": "11:00 CET",
                    "status": "started 🎬"
                }
                return shift_data

            #  === UTC ===				        === CET ===          === Local time ===
            #  NA EAST: 1300 – 2130            15:00 - 23:30        09:00 - 17:30 EST/EDT
            if (self.currentDateAndTime.hour == 15) and (self.currentDateAndTime.minute == 0):
                self.logger.info('Getting shift time and status...')
                shift_data = {
                    "theatre": "TSE_US_EAST",
                    "shift_time": "09:00 EST/EDT",
                    "status": "started 🎬"
                }
                return shift_data

            #  === UTC ===				        === CET ===          === Local time ===
            #  NA WEST: 1600 – 0100            18:00 - 03:00        12:00 - 21:00
            if (self.currentDateAndTime.hour == 18) and (self.currentDateAndTime.minute == 0):
                self.logger.info('Getting shift time and status...')
                shift_data = {
                    "theatre": "TSE_US_WEST",
                    "shift_time": "12:00 EST/EDT",
                    "status": "started 🎬"
                }
                return shift_data
        ################ Shift end #################
        #  === UTC ===				        === CET ===          === Local time ===
        #  APAC: 0100 – 0900 				03:00 - 11:00        11:00 - 19:00  AEDT/AEST
        if self.today != "Saturday":
            if (self.currentDateAndTime.hour == 10) and (self.currentDateAndTime.minute == 59):
                self.logger.info('Getting shift time and status...')
                shift_data = {
                    "theatre": "TSE_APAC",
                    "shift_time": "19:00 AEDT",
                    "status": "ended 🏁"
                }
                return shift_data

            #  === UTC ===				        === CET ===          === Local time ===
            #  EMEA: 0900 – 1730				11:00 - 19:30        11:00 - 19:30
            if (self.currentDateAndTime.hour == 19) and (self.currentDateAndTime.minute == 30):
                self.logger.info('Getting shift time and status...')
                shift_data = {
                    "theatre": "TSE_EMEA",
                    "shift_time": "19:30 CET",
                    "status": "ended 🏁"
                }
                return shift_data

            #  === UTC ===				        === CET ===          === Local time ===
            #  NA EAST: 1300 – 2130            15:00 - 23:30        09:00 - 17:30 EST/EDT
            if (self.currentDateAndTime.hour == 23) and (self.currentDateAndTime.minute == 30):
                self.logger.info('Getting shift time and status...')
                shift_data = {
                    "theatre": "TSE_US_EAST",
                    "shift_time": "17:30 EDT/EST",
                    "status": "ended 🏁"
                }
                return shift_data

        # US-WEST (TSE_US_WEST (6pm CET-3:00am CET)) (except for Monday morning)
        #  === UTC ===				        === CET ===          === Local time ===
        #  NA WEST: 1600 – 0100            18:00 - 03:00        12:00 - 21:00
        if (self.currentDateAndTime.hour == 3) and (self.currentDateAndTime.minute == 0) and (self.today != "Monday"):
            self.logger.info('Getting shift time and status...')
            shift_data = {
                "theatre": "TSE_US_WEST",
                "shift_time": "21:00 EDT/EST",
                "status": "ended 🏁"
            }
            return shift_data

    def weekendAlertData(self):
        # Global weekend alert!
        if (self.currentDateAndTime.hour == 3) and (self.currentDateAndTime.minute == 1) and (
                self.today == "Saturday"):
            self.logger.info('Getting weekend time and status/message...')
            shift_data = {
                "theatre": "All",
                "shift_time": "21:00 EST/EDT, 03:00 CEST and 12:00 AEDT",
                "status": "weekend 😴"
            }
            return shift_data
