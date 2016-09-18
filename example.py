from pythai_postaltracking import tracking_status

tracking_id = input('Input Your Tracking_id (EMS Only) : ')
date_status = tracking_status(tracking_id)
print ('%s %s %s'%(date_status[0],tracking_id,date_status[1]))
