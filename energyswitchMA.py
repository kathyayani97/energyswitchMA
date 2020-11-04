import requests
import json

zipcode_data = [['01603','1'],['01772','2'],['01013','3'],['01420','4'],['01420','5']]

for info in zipcode_data:
    parameters = {
            "customerClassId": "1",
            "distributionCompanyId": info[1],
            "distributionCompanyName": "",
            "monthlyUsage": 600,
            "zipCode": info[0]
            }

    main_url = 'https://www.energyswitchma.gov/consumers/compare'
    response = requests.post(url=main_url, json=parameters)
    to_extract = response.json()
    # print(to_extract)
    for data in to_extract:
        plans_info = {'SupplierID': data['supplierId'],
                      'SupplierName': data['supplierName'],
                      'PricePerUnit': data['pricePerUnit'],
                      'ContractTerm': data['contractTerm'],
                      'ContractTermEndDate': data['contractTermEndDate'],
                      'EstimatedCost': data['estimatedCost'],
                      'ApplicableYear': data['applicableYear'] }
        print(plans_info)
