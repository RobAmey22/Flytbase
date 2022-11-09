import time

from flyt_python import api
drone = api.navigation()

time.sleep(3.0)
drone.access_resquest()

print("Taking Off")
drone.take_off(10.0)

print("Projecting the trajectory")
drone.position_set(0, 10, 0, relative=True)
drone.position_set(10, -5, 0, relative=True)
drone.position_set(-10, -5, 0, relative=True)

print("Landing")
drone.land(async=False)

# shutdown the instance
drone.disconnect()
