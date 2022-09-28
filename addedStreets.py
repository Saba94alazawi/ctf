


data = []

def addedCoordinates(Xa,Ya,Xb,Yb,speed,fine,i):
    ## Determining the Slope ##
    slope = round((Yb-Ya)/(Xb-Xa), 8)

    ## Determining the Shift ##
    shift = Ya -(Xa * slope)
    dataset = {'id':i, 'xA':Xa, 'yA':Ya, 'xB':Xb, 'yB':Yb, 'Slope':slope, 'Shift':shift, 'Speed':speed, 'Fine': fine}
    data.append(dataset)
    return data