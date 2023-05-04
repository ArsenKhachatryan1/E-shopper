from bs4 import BeautifulSoup
import requests
import mysql.connector



def get_kurs():
    
    try:

        url = 'https://rate.am/'

        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        Comp = soup.find("tr", id="65351947-217c-4593-9011-941b88ee7baf")
        text = Comp.text.split('\n')
        USD = text[9]
        if USD:

            mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Arsen0495015@#",
            database="eshopper"
            )

            mycursor = mydb.cursor()

            sql = "UPDATE main_curency SET kurs_amd = %s WHERE id = 1"
            val = [
                (USD)
            ]
        mycursor.execute(sql, val)

        mydb.commit()

    except:
        pass
