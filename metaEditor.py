import pydicom
import os

filepath = "/Users/neilmacphee/Code/Clients/Need/deid2/1.3.6.1.4.1.11129.5.1.285910283473783729255647243724941882338/1.3.6.1.4.1.11129.5.1.123271295159729605398977417949504799607"
newDir = "/Users/neilmacphee/Code/Clients/Need/deid2/Test/1.3.6.1.4.1.11129.5.1.123271295159729605398977417949504799607"
imageList = os.listdir(filepath)

# for img in imageList:
#     ds = pydicom.filereader.dcmread(filepath+"/"+img)
#     ds[0x8,0x60].value = "CT"
#     ds.save_as(newDir+"/"+img)


# for img in imageList:
#     ds = pydicom.filereader.dcmread(filepath+"/"+img)
#     ds[0x8,0x60].value = "OT"
#     ds.save_as(newDir+"/"+img)


for img in imageList:
    ds = pydicom.filereader.dcmread(filepath+"/"+img)
    ds.add_new('0x080021', 'DA', "20230712") #SeriesDate
    ds.add_new('0x080031', 'TM', "150000.000000") #SeriesTime
    ds.add_new('0x080022', 'DA', "20230712") #AcquisitionDate
    ds.add_new('0x080032', 'TM', "150000.000000") #AcquisitionTime
    ds.add_new('0x101030', 'DS', '83.3') #PatientWeight
    del ds[0x0018, 0x5100] #Remove PatientPosition
    ds.save_as(newDir+"/"+img)
