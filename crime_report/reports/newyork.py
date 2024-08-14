# newyork.py

import requests
from datetime import datetime

# Define the headers for the data
HEADERS = [
    "Complaint Number", "Complaint From Date", "Complaint From Time",
    "Complaint To Date", "Complaint To Time", "Precinct Code", "Report Date",
    "Offense Code", "Offense Description", "Police Department Code", "Police Description",
    "Crime Attempt/Completed Code", "Law Category Code", "Borough Name",
    "Location of Occurrence Description", "Premises Type Description", "Jurisdiction Description",
    "Jurisdiction Code", "Parks Name", "HA Development", "Housing PSA",
    "X Coordinate", "Y Coordinate", "Suspect Age Group", "Suspect Race", "Suspect Sex",
    "Latitude", "Longitude", "Latitude (from lat_lon)", "Longitude (from lat_lon)"
]

def format_datetime(date_str, time_str):
    # Strip any leading or trailing spaces
    date_str = date_str.strip()
    time_str = time_str.strip()

    # Combine the date and time strings into a datetime object
    return datetime.strptime(f"{date_str} {time_str}", "%Y-%m-%d %H:%M").strftime("%Y-%m-%dT%H:%M:%S.000")

def construct_api_url(api_url, start_datetime, end_datetime):
    return f"https://{api_url}?$where=cmplnt_fr_dt >= '{start_datetime}' AND cmplnt_fr_dt <= '{end_datetime}'"

def fetch_data(api_url):
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": f"Failed to fetch data: {e}"}

def process_newyork_data(data):
    rows = []
    for item in data:
      
        rows.append([
            item.get('cmplnt_num', 'NA'),
            item.get('cmplnt_fr_dt', 'NA'),
            item.get('cmplnt_fr_tm', 'NA'),
            item.get('cmplnt_to_dt', 'NA'),
            item.get('cmplnt_to_tm', 'NA'),
            item.get('addr_pct_cd', 'NA'),
            item.get('rpt_dt', 'NA'),
            item.get('ky_cd', 'NA'),
            item.get('ofns_desc', 'NA'),
            item.get('pd_cd', 'NA'),
            item.get('pd_desc', 'NA'),
            item.get('crm_atpt_cptd_cd', 'NA'),
            item.get('law_cat_cd', 'NA'),
            item.get('boro_nm', 'NA'),
            item.get('loc_of_occur_desc', 'NA'),
            item.get('prem_typ_desc', 'NA'),
            item.get('juris_desc', 'NA'),
            item.get('jurisdiction_code', 'NA'),
            item.get('parks_nm', 'NA'),
            item.get('hadevelopt', 'NA'),
            item.get('housing_psa', 'NA'),
            item.get('x_coord_cd', 'NA'),
            item.get('y_coord_cd', 'NA'),
            item.get('susp_age_group', 'NA'),
            item.get('susp_race', 'NA'),
            item.get('susp_sex', 'NA'),
            item.get('latitude', 'NA'),
            item.get('longitude', 'NA'),
            item.get('lat_lon', {}).get('latitude', 'NA'),
            item.get('lat_lon', {}).get('longitude', 'NA'),

        ])

    return rows
