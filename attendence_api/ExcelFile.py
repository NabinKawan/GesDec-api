import sys
from datetime import datetime


def register_attendance(name):
    with open('attendence_api/Attendance.csv', 'r+') as f:
        myDataList = f.readlines()
        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
        if name not in nameList:
            time_now = datetime.now()
            tStr = time_now.strftime('%H:%M:%S')
            dStr = time_now.strftime('%d/%m/%Y')
            status='Present'
            f.writelines(f'\n{name},{tStr},{dStr},{status}')


if __name__ == "__main__":
    name = sys.argv[1]
    register_attendance(name)
            
