import requests
import csv
import os
import re


def resturant_data():
    try:
        root_dir = os.path.dirname(os.path.abspath(__file__))
        src_url = "https://projects.sfchronicle.com/2020/restaurant-delivery/"

        url = "https://projects.sfchronicle.com/2020/restaurant-delivery/commons-14e18e523a3456e0bfaa.js?1587594222"
        req = requests.get(url)

        page_content = req.content.decode()

        columns = ["Name", "Cuisine", "Location", "Service Method", "Does Curbside Pick-Up?", "Address",
                   "City", "Zip Code", "Region", "Hours", "Phone", "Website", "details"]

        lst_str_1 = page_content.split(",OpFd:function(e){e.exports=JSON.parse('")[1]
        lst_str_2 = lst_str_1.split("')},SIeT:function(e,a,i)")[0]

        resturant_lst = re.findall(r'{(.*?)}', lst_str_2)


        with open(root_dir + "/sfchronicle.csv", "w", encoding="utf-8", newline='') as f:
            csv_writer = csv.writer(f, delimiter=',')
            csv_writer.writerow(columns)

            for data in resturant_lst[5:]:
                try:
                    data = data.replace('\\"', "\\'")
                    dict_data = eval("{" + data + "}")

                    try:
                        name = dict_data['Name'].strip()
                        if len(name) < 1:
                            name = 'N/A'
                    except:
                        name = 'N/A'
                        pass

                    try:
                        cuisine = dict_data['Cuisine'].strip()
                        if len(cuisine) < 1:
                            cuisine = 'N/A'
                    except:
                        cuisine = 'N/A'
                        pass

                    try:
                        location = dict_data['Location'].strip()
                        if len(location) < 1:
                            location = 'N/A'
                    except:
                        location = 'N/A'
                        pass

                    try:
                        service_method = dict_data['Service Method'].strip()
                        if len(service_method) < 1:
                            service_method = 'N/A'
                    except:
                        service_method = 'N/A'
                        pass

                    try:
                        does_curbside_pick_up = dict_data['Does Curbside Pick-Up?'].strip()
                        if len(does_curbside_pick_up) < 1:
                            service_method = 'N/A'
                    except:
                        service_method = 'N/A'
                        pass

                    try:
                        address = dict_data['Address'].strip()
                        if len(address) < 1:
                            address = 'N/A'
                    except:
                        address = 'N/A'
                        pass

                    try:
                        city = dict_data['City'].strip()
                        if len(city) < 1:
                            city = 'N/A'
                    except:
                        city = 'N/A'
                        pass

                    try:
                        zip_code = dict_data['Zip Code'].strip()
                        if len(zip_code) < 1:
                            zip_code = 'N/A'
                    except:
                        zip_code = 'N/A'
                        pass

                    try:
                        region = dict_data['Region'].strip()
                        if len(region) < 1:
                            region = 'N/A'
                    except:
                        region = 'N/A'
                        pass

                    try:
                        hours = dict_data['Hours'].strip()
                        if len(hours) < 1:
                            hours = 'N/A'
                    except:
                        hours = 'N/A'
                        pass

                    try:
                        phone = dict_data['Phone'].strip()
                        if len(phone) < 1:
                            phone = 'N/A'
                    except:
                        phone = 'N/A'
                        pass

                    try:
                        website = dict_data['Website'].strip()
                        if len(website) < 1:
                            website = 'N/A'
                    except:
                        website = 'N/A'
                        pass

                    try:
                        details = dict_data['Details'].strip()
                        if len(details) < 1:
                            details = 'N/A'
                    except:
                        details = 'N/A'
                        pass

                    col_values = [name, cuisine, location, service_method, does_curbside_pick_up, address,
                                  city, zip_code, region, hours, phone, website, details, src_url]

                    csv_writer.writerow(col_values)

                except:
                    pass

    except:
        pass



if __name__ == '__main__':
    resturant_data()
