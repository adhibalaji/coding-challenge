#!/usr/bin/python3

import argparse
import requests
import xlsxwriter

def get_user_data(url):
  """Function to get user data for a provided URL"""
  response = requests.get(url)
  if response.status_code != 200:
    raise RuntimeError("API call to '{}' returned '{}' with status code: '{}'".format(url, response.text, response.status_code))

  json_response = response.json()
  user_data=[]

  for i in range(len(json_response['data'])):
    user_data.append([json_response['data'][i]['first_name'],json_response['data'][i]['last_name'],json_response['data'][i]['email']])

  return user_data

def generate_excel(data):
  """Function to generate a excel doc based on provided data list of lists"""
  workbook = xlsxwriter.Workbook('devops-user-data.xlsx')
  worksheet = workbook.add_worksheet()
  caption = 'Table with details of all users in the DevOps platform'

  worksheet.set_column('B:G', 24)

  worksheet.write('B1', caption)

  worksheet.add_table(2,1,len(data) + 2,3, {'data': data,
                               'columns': [{'header': 'First Name'},
                                           {'header': 'Last Name'},
                                           {'header': 'Email'},
                                           ]})
  workbook.close()

def generate_html(data):
  """Function to generate a html doc based on provided data list of lists"""
  content = ""
  for i in range(len(data)):
    content = content + "<tr><td>" + '</td><td>'.join(data[i]) + "</td></tr>"

  fp = open("devops-user-data.html","w+")

  # Write the table border styling for the html doc
  fp.write("<!DOCTYPE html><html><head><style>table, th, td { border: 1px solid black; }</style></head><body><h1>DevOps User Data</h1>")
  # Write the header
  fp.write("<table><tr><th>First Name</th><th>Last Name</th><th>Email</th></tr>")
  # Write the dynamic body of the doc
  fp.write("%s</table></body></html>" %content)

  fp.close()

parser = argparse.ArgumentParser(description='Get User data from a API url and generate doc')
parser.add_argument(
        '--url',
        help='API url for the user data',
        required=True
        )

if __name__ == '__main__':
  args = parser.parse_args()
  data = get_user_data(args.url)
  generate_excel(data)
  generate_html(data)