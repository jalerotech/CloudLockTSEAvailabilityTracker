from datetime import datetime
import time
import logging
from cLTSEMainPrograms.alertShiftStartStop import alertshiftstart, weekendAlert
from cltTackerMainClass.cLTrackerClass import cLTrackerBlob as cLb
from fetchWebExAvailability.getPersonDataWebEx import ret_available_team_members
from messageHandler.msgPoster import sendMessageToWxT
from messageHandler.tseOnlineMsgGen import genCloudLockTeams_shift_Msg

logging.basicConfig(
    format='%(asctime)s %(levelname)s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')

working_days = ["Tuesday", "Wednesday", "Thursday", "Friday"]


def cltTSEAvailabilityTrackerMain():
    logger = logging.getLogger("Running cltTSEAvailabilityTrackerMain: ")
    while True:
        logger.info(f"Running Main Program...")
        currentDateAndTime = datetime.now()
        today = currentDateAndTime.strftime('%A')
        currentTime = currentDateAndTime.strftime("%H:%M:%S")
        # Not working after 03:00 AM CEST on Saturday.
        # Allow 60 seconds more for the shift alert to be run to alert US shift end - As the last to be posted
        # before global weekend start.
        # Sunday is a full day of not running the scripts.
        # While the script should still run until after 3 am on Saturday.
        if (today == "Saturday" and (currentDateAndTime.hour >= 3 and currentDateAndTime.minute >= 0)) or (
                today == "Sunday"):
            logger.info(f"Shift to start at 03:00 CEST on Monday morning. It's weekend.")
            weekendAlert()
        else:
            # And to continue polling until Saturday as long as hour is less than 3:00 AM CEST -> since US shift ends
            # on Saturday at 03:00 (From CEST point of view).
            if today in working_days or (today == "Monday" and currentDateAndTime.hour >= 2) or (
                    today == "Saturday" and currentDateAndTime.hour <= 3):
                logger.info(f'The current time is {currentTime}')
                try:
                    theatre_label, status = alertshiftstart()
                    if theatre_label:
                        available_tse = ret_available_team_members(theatre_label)
                        if available_tse:
                            logger.info("TSEs are available, list received.")
                            genCloudLockTeams_shift_Msg(available_tse, theatre_label, status)
                            sendMessageToWxT(genCloudLockTeams_shift_Msg(available_tse, theatre_label, status))
                    else:
                        logger.info(f"No new shift data, no alerts needed, pausing for a little bit...")
                except TypeError as k:
                    logger.info(f"No new shift data")
                    logger.info(f"Pausing for {cLb().polling_interval} seconds. \n ")
            else:
                logger.info(f"Shift to start at 03:00 CEST on Monday morning. Sleeping for now")
        time.sleep(cLb().polling_interval)


if __name__ == '__main__':
    cltTSEAvailabilityTrackerMain()
    # weekendAlert()
