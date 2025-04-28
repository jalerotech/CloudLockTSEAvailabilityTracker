from dotenv import load_dotenv
import os
load_dotenv()


class cLTrackerBlob:

    def __init__(self):
        # Content type for request headers
        self.contentType = 'application/json'

        # Loading AuthKeys via environment variables:
        # keys and Ids:
        self.bot_access_token = os.getenv('Bot_access_token')
        self.cloudlock_support_TSE_room_id = os.getenv('CloudLock_Support_TSE_room_id')
        self.dev_room_id = os.getenv('dev_room_id')

        self.quickURL = "https://scripts.cisco.com/app/quicker_backlog/#/?tab=Workmon&subTab=My%20Availability"
        # Set the url Webex API Endpoint
        self.webex_api_url = 'https://webexapis.com/v1/messages'

        # WebEx base URL:
        self.webex_base_url = 'https://webexapis.com/v1/'

        # Set the header Webex API Endpoint - Production.
        self.webex_headers = {
            'Content-Type': self.contentType,
            'Authorization': f'Bearer {self.bot_access_token}'
        }

        # Set the interval
        self.polling_interval = 60

        self.EMEA_region = ['GB', 'BE', 'PL', 'ES', 'PT']
        self.US_region = ['CR', 'US', 'CA']
        self.APAC_region = ['AU', 'CN', 'JP', 'IN']

        # TSE team members:
        self.GlobalCloudLockTeam = ["arataj@cisco.com", "beash@cisco.com", "cloupas@cisco.com", "harpraja@cisco.com",
                                    "kloxdale@cisco.com", "nucabral@cisco.com", "rosahni@cisco.com", "rysia@cisco.com",
                                    "bilbarne@cisco.com", "chetchan@cisco.com", "hmushtaq@cisco.com",
                                    "kmakarss@cisco.com", "surymish@cisco.com", "esgoyal@cisco.com",
                                    "aakindel@cisco.com", "janeandr@cisco.com", "pragagra@cisco.com",
                                    "tkeshinr@cisco.com", "dsaludes@cisco.com", "alihass@cisco.com",
                                    "danykhan@cisco.com", "jaishah2@cisco.com", "jonahtho@cisco.com",
                                    "skarimia@cisco.com"]

        # EMEA
        self.TSE_EMEA = ["arataj@cisco.com", "beash@cisco.com", "cloupas@cisco.com", "harpraja@cisco.com",
                         "kloxdale@cisco.com",
                         "nucabral@cisco.com", "rosahni@cisco.com", "rysia@cisco.com", "bilbarne@cisco.com"]
        # APAC
        self.TSE_APAC = ["chetchan@cisco.com", "hmushtaq@cisco.com", "kmakarss@cisco.com", "surymish@cisco.com",
                         "esgoyal@cisco.com"]

        # US-EAST
        self.TSE_NA_EAST = ["aakindel@cisco.com", "janeandr@cisco.com", "pragagra@cisco.com", "tkeshinr@cisco.com"]

        # US-WEST:
        self.TSE_NA_WEST = ["dsaludes@cisco.com", "alihass@cisco.com", "danykhan@cisco.com", "jaishah2@cisco.com",
                            "jonahtho@cisco.com", "skarimia@cisco.com"]
