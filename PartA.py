import FileUtils
import datetime

def consolidateData(cities, startDate, endDate, outputFileName):
    #format dates
    StartDate = datetime.datetime.strptime(startDate,'%Y-%m-%d') 
    EndDate = datetime.datetime.strptime(endDate,'%Y-%m-%d') 

    #list to write to file
    list = ["CITY,DATE,TEMPERATURE"]
    try:
        cityInfoFile = FileUtils.readIntoList("city_info.csv",1)
        #loop through cities sent in
        for city in cities:
            
            for line in cityInfoFile:
                values = line.split(",")
                cityName = values[1].strip('"')
                cityId = values[2]
                
                if city == cityName:
                     #open file matching citys 'ID'
                  
                    try:
                        fileName = cityId.strip('"') +".csv"
                      
                        
                        cityIdFile = FileUtils.readIntoList(fileName,1)
                 
                        for line in cityIdFile:
                            #skip line if has missing data
                            if 'NA' in line:
                                continue

                            values = line.split(",")
                            date = datetime.datetime.strptime(values[1],'%Y-%m-%d')
                            tmax = int(values[2])
                            tmin = int(values[3])
               
                            if date.date() >= StartDate.date() and date.date() <= EndDate.date():
                                #calculate avg temp 
                                avgTemp = (tmax + tmin)/ 2
        
                                #convert to celcius
                                temperature = (avgTemp - 32) * 0.5556

                                string = city + "," + str(date.date()) + "," + str(temperature)
                                #add string to list
                                list.append(string)
                              
                                try:
                                    FileUtils.writeListToFile(list, outputFileName)
                                    
                                except:
                                    print("could not write to file")
        
                    except:
                        print("File not found")

    except:
        print("File not found")



cities = ['Atlanta','Eugene','Fargo','Jacksonville','Phoenix','Toledo']

cities.sort()
startDate = '1961-01-01'
endDate = '2021-12-31'
outputFileName = 'consolidated1.csv'
consolidateData(cities, startDate, endDate, outputFileName)


