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


def cltTSEAvailabilityTrackerMain():
    logger = logging.getLogger("Running cltTSEAvailabilityTrackerMain: ")
    while True:
        logger.info(f"Running Main Program...")
        weekendAlert()
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
        time.sleep(cLb().polling_interval)


if __name__ == '__main__':
    cltTSEAvailabilityTrackerMain()
    # weekendAlert()
