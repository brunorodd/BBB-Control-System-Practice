

#this is the initialization of variables that was put in the control_trial before
ADC_pin1 = "P9_33"
ADC_pin2 = "P9_35"

joystickCenter1 = [0]
joystickCenter2 = [0]
joystickForward = [0]
joystickBackward = [0]
joystickLeft = [0]
joystickRight = [0]
joystickDirectionList = [0]
joystickSpeedList = [0]

clbCenter = [0]

#this is the main calibration function which calibrates the center, direction and speed values
def calib(index):
    length = 50
    calibration_flag = True
    recalibration = False
    # for calibrating the center
    if index == 0:
        while calibration_flag:
            del joystickCenter1
            del joystickCenter2
            joystickCenter1 = []
            joystickCenter2 = []
            recalibration = False
            print("Calibrating Joystick Center...")
            input("Center the joystick and press Enter to continue: ")
            time.sleep(0.5)
            for i in range(length):
                if abs(joystickCenter1[i]-joystickCenter1[i-1]) > 10 or abs(joystickCenter2[i]-joystickCenter2[i-1]) > 10:
                    print("Error in Calibration. Recalibrating...")
                    recalibration = True
                    time.sleep(1)
                    break
                joystickCenter1.append(ADC.read_raw(ADC_pin1))
                joystickCenter2.append(ADC.read_raw(ADC_pin2))
                print(joystickCenter1[i])
                print(joystickCenter2[i])
                time.sleep(0.05)

            if recalibration:
                continue
            else:
                calibration_flag = False
                break

        return [sum(joystickCenter1)/len(joystickCenter1),sum(joystickCenter2)/len(joystickCenter2)]

# for calibrating the upper and lower bounds of each direction to map
    if index == 1:
        while calibration_flag:
            joystickForward[:] = []
            #joystickForward = []
            recalibration = False
            print("Calibrating Direction Threshold. Hold the Joystick all the way forward")
            input("Press Enter to Continue: ")
            time.sleep(0.5)
            for i in range(length):
                if abs(joystickForward[i]-joystickForward[i-1]) > 10:
                    print("Error in Calibration. Recalibrating...")
                    recalibration = True
                    time.sleep(1)
                    break
                joystickForward.append(ADC.read_raw(ADC_pin2))
                print(joystickForward[i])
                time.sleep(0.05)

            if recalibration:
                continue
            else:
                calibration_flag = False
                break
        # returns the average of the maximum values for the forward direction
        return sum(joystickForward)/length


    if index == 2:
        while calibration_flag:
            joystickBackward[:] = []
            recalibration = False
            print("Calibrating Direction Threshold. Hold the Joystick all the way backward")
            input("Press Enter to Continue")
            time.sleep(0.5)
            for i in range(length):
                if abs(joystickBackward[i]-joystickBackward[i-1]) > 10:
                    print("Error in Calibration. Recalibrating...")
                    recalibration = True
                    time.sleep(1)
                    break
                joystickBackward.append(ADC.read_raw(ADC_pin2))
                print(joystickBackward[i])
                time.sleep(0.05)

            if recalibration:
                continue
            else:
                calibration_flag = False
                break
        #returns the average of the maximum values for the backward direction
        return sum(joystickBackward)/length

    if index == 3:
        while calibration_flag:
            joystickLeft[:] = []
            recalibration = False
            print("Calibrating Speed threshold. Hold the joystick all the way left")
            input("Press Enter to Continue")
            time.sleep(0.5)
            for i in range(length):
                if abs(joystickLeft[i]-joystickLeft[i-1]) > 10:
                    print("Error in Calibration. Recalibrating...")
                    recalibration = True
                    time.sleep(1)
                    break
                joystickLeft.append(ADC.read_raw(ADC_pin1))
                print(joystickLeft[i])
                time.sleep(0.05)

            if recalibration:
                continue
            else:
                calibration_flag = False
                break
        #returns the average of the maximum values for the left direction
        return sum(joystickLeft)/length

    if index == 4:
        while calibration_flag:
            joystickRight[:] = []
            recalibration = False
            print("Calibratin Speed threshold. Hold the joystick all the way right")
            input("Press Enter to continue")
            time.sleep(0.5)
            for i in range(length):
                if abs(joystickRight[i]-joystickRight[i-1]) > 10:
                    print("Error in Calibration. Recalibrating...")
                    recalibration = True
                    time.sleep(1)
                    break
                joystickRight.append(ADC.read_raw(ADC_pin1))
                print(joystickLeft[i])
                time.sleep(0.05)

            if recalibration:
                continue
            else:
                calibration_flag = False
                break
        return sum(joystickRight)/length
