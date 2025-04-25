import requests
import logging
import json
from cltTackerMainClass.cLTrackerClass import cLTrackerBlob as cLb

logging.basicConfig(
    format='%(asctime)s %(levelname)s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')


def ret_available_team_members(theatre_label) -> dict:
    """
    Returns a list of available members of the cloudlock team with no OOO set.
    Produces a dict with a list of all available TSEs per region.
    """
    logger = logging.getLogger("Running ret_available_team_members: ")
    logger.info("Producing a list of available cloudlock team members.")
    cl_tse_on_shift = {
        theatre_label: []
    }
    country_list = []
    email_list, regions = _retListOfEmails(theatre_label)
    for email in email_list:
        params = {
            "email": email
        }
        url = f'{cLb().webex_base_url}people'
        webex_resp = requests.get(url, params=params, headers=cLb().webex_headers)
        for country in json.loads(webex_resp.content)['items'][0]['addresses']:
            country_list.append(country['country'])
        status = json.loads(webex_resp.content)['items'][0]['status']
        if status != 'OutOfOffice':
            atd_user = f"<@personEmail:{email}>"
            # cl_tse_on_shift[theatre_label].append(displayName)
            cl_tse_on_shift[theatre_label].append(atd_user)
    logger.info("Returning Dict of CloudLock TSEs that are available.")
    logger.info(f"Returned Dict -> {cl_tse_on_shift}.")
    return cl_tse_on_shift


def _retListOfEmails(theatre_label):
    if theatre_label == "TSE_US_EAST":
        return cLb().TSE_NA_EAST, cLb().US_region
    if theatre_label == "TSE_US_WEST":
        return cLb().TSE_NA_WEST, cLb().US_region
    if theatre_label == "TSE_EMEA":
        return cLb().TSE_EMEA, cLb().EMEA_region
    if theatre_label == "TSE_APAC":
        return cLb().TSE_APAC, cLb().APAC_region


if __name__ == '__main__':
    # print(cLb().GlobalCloudLockTeam)
    print(ret_available_team_members(cLb().GlobalCloudLockTeam))
