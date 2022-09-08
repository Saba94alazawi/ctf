from ping3 import ping
from fines.models import DeviceInfo





devStatus = DeviceInfo.objects.all()   

def IPcheck():
    for st in devStatus:
        print(f'{st.deviceIP} is {st.status}')
        if st.deviceIP != None:
            resp = ping(st.deviceIP)
            if resp == True:
                st.status = True
                st.save()
            else:
                st.status = False
                st.save()
