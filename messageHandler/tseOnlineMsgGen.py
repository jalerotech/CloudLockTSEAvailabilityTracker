import logging

logging.basicConfig(
    format='%(asctime)s %(levelname)s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')


def genCloudLockTeams_shift_Msg(available_tse, theatre, status):
    logger = logging.getLogger('genCloudLockTeams_shift_Msg')
    """
    List of available TSEs from particular region.
    
    :param available_tse: dict of available cloudlock TSE
    :param theatre: Theatre tag
    :return: 
    """
    logger.info(f"Generating CloudLock TSE on shift message for {theatre} team.")

    joined_team_members = '\n'.join(available_tse[theatre])
    try:
        tos_msg_to_send = ""
        if status == "started 🎬":
            tos_msg_to_send = f"#### 🔔 Cloudlock TSE's on-shift _(BETA)_: \n " \
                              f"**{_retTheatreName(theatre)}**: \n " \
                              f"{joined_team_members} \n " \
                              f"\n "
        if status == "ended 🏁":
            tos_msg_to_send = f"#### 🔕 Cloudlock TSE's off-shift _(BETA)_: \n " \
                              f"**{_retTheatreName(theatre)}**: \n " \
                              f"{joined_team_members} \n " \
                              f"\n "
        data = {
            "text": tos_msg_to_send,
            "markdown": tos_msg_to_send
        }
        logger.info(f"Generated Cloudlock TSE on shift Message -> {tos_msg_to_send}")
        logger.info("Generating CloudLock TSE on shift message for {theatre} team - COMPLETED")
        return data
    except KeyError as k:
        logger.info(f"Key {k} Missing so no TSE from that region that's available.")


def _retTheatreName(theatre):
    split_theatre_label = theatre.split('_')
    if len(split_theatre_label) > 2:
        return f"{split_theatre_label[1]} {split_theatre_label[2]}"
    else:
        return split_theatre_label[1]
