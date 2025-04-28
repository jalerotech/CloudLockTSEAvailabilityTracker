from typing import Tuple, Any
from cltTackerMainClass.cLTrackerClass import cLTrackerBlob as cLb
from cltTackerMainClass.shiftTimeDataClass import ShifttimeData
import logging
from messageHandler.msgPoster import sendMessageToWxT

logging.basicConfig(
    format='%(asctime)s %(levelname)s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')


def alertshiftstart() -> tuple[Any, Any]:
    shift_data = ShifttimeData().theatre_shift_time()
    """
    Post messages to WxT when shift starts at 03:00 and ends at 11:00  (APAC)
    or
    Post messages to WxT when shift starts at 11:00 and ends at 19:30  (EMEA)
    or 
    Post messages to WxT when shift starts at 15:00 and ends at 23:30  (US EAST)
    or 
    Post messages to WxT when shift starts at 18:00 and ends at 03:00  (US WEST)
    
    :param shift_data
    :return: None
    """

    if shift_data:
        logger = logging.getLogger('Alerting shift start/stop.')
        logger.info(f"Shift data produced -> {shift_data}")
        logger.info(f"Posting {shift_data['theatre']} Shift {shift_data['status']} message.")
        theatre_label = _retTheatreName(shift_data['theatre'])
        if shift_data['status'] == "started 🎬":
            data = {
                "text": f"Time is now {shift_data['shift_time']}, {theatre_label} shift is now starting 🎬. \n "
                        f"\n "
                        f"\n "
                        f"Reminder: Please set your [CSOne profile]({cLb().quickURL}) "
                        f"to _Available_ for the remainder of your shift.",
                "markdown": f"**Time is now {shift_data['shift_time']}, {theatre_label} shift is now starting 🎬.** "
                            f"\n "
                            f"\n "
                        f"**Reminder: Please set your [CSOne profile]({cLb().quickURL})"
                            f" to _Available_ for the remainder of your shift.**"
            }
            logger.info(f"{theatre_label} shift {shift_data['status']}.")
            sendMessageToWxT(data)
            logger.info(f"Posting Shift {shift_data['status']} message. -> COMPLETED")
            return shift_data['theatre'], shift_data['status']
        if shift_data['status'] == "ended 🏁":
            data = {
                "text": f"Time is now {shift_data['shift_time']}, {theatre_label} shift is now ending 🏁. \n "
                        f"\n "
                        f"\n "
                        f"Reminder: Please set your [CSOne profile]({cLb().quickURL})"
                        f" to _Unavailable_ for the remainder of your shift.",
                "markdown": f"**Time is now {shift_data['shift_time']}, {theatre_label} shift is now ending 🏁.** \n"
                            f" \n "
                            f" \n "
                            f"**Reminder: Please set your [CSOne profile]({cLb().quickURL}) to _Unavailable_ for the "
                            f"remainder of your shift.**"
            }
            logger.info(f"{shift_data['theatre']} shift {shift_data['status']}.")
            sendMessageToWxT(data)
            logger.info(f"Posting Shift {shift_data['status']} message. -> COMPLETED")
            return shift_data['theatre'], shift_data['status']


def _retTheatreName(theatre):
    split_theatre_label = theatre.split('_')
    if len(split_theatre_label) > 2:
        return f"{split_theatre_label[1]}_{split_theatre_label[2]}"
    else:
        return split_theatre_label[1]


def weekendAlert() -> bool:
    """
    posts weekend alert when conditions are met.
    :return: None
    """
    shift_data = ShifttimeData().weekendAlertData()
    # logger = logging.getLogger('Generating Weekend Alert.')
    if shift_data:
        logger = logging.getLogger('Generating Weekend Alert.')
        logger.info(f"Data produced -> {shift_data}")
        logger.info(f"Posting {shift_data['status']} Alert for ALL {shift_data['theatre']} message. -> STARTED")
        data = {
            "text": f"Time is now {shift_data['shift_time']}, it's {shift_data['status']} for ALL theatres.",
            "markdown": f"**Time is now {shift_data['shift_time']}, it's {shift_data['status']} for ALL theatres**."
        }
        logger.info(f"{shift_data['theatre']} with status {shift_data['status']}.")
        sendMessageToWxT(data)
        logger.info(f"Posting {shift_data['status']} Alert for ALL {shift_data['theatre']} message. -> COMPLETED")
        return True


if __name__ == '__main__':
    alertshiftstart()
    # weekendAlert()
