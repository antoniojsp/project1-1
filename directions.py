import requests
import configparser
config = configparser.ConfigParser()
config.read("credentials.ini")

# location = [44.587662,-123.256691]
def get_name_tamu(lat, long, state):
    origen = "http://geoservices.tamu.edu/Services/ReverseGeocoding/WebService/v04_01/Rest/?lat=" + str(lat) + "&lon=" + str(long) + "&state=" + str(state) + "&apikey=" + config["DEFAULT"]["key_tamu"] + "&format=json&notStore=false&version=4.10"#service provided by tamu.

    answer = ""#storage only the name of the street.
    response = requests.get(origen).json()
    result = response['StreetAddresses'][0]['StreetAddress']#only gets the address of the avenue or street
    # print(response)
    # remove the addres number, leaving only the street or avenue name.
    signal = 0
    for i in result:
        if i == ' ':#exeption if the name of the street has numbers i.e 19th avenue, Eugene
            signal = 1
        if i not in "0123456789" or signal == 1:#deletes the first numbers house. i.e. 1790 Alder St. is converted to Alder St.
            answer += i

    return answer[1:]

# print(get_name_tamu(location[0],location[1],"or"))
