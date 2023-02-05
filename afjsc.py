import scrapy
import jsonlines
import json
import re
import requests
URL = "http://www.afalagi.biranaspace.com/back_end/add_job_and_notify"
arr = []
# with jsonlines.open('job_index.jl') as r:
#     for x in r.iter():
#         arr.append(x['title'] + x['datePosted'])
#with jsonlines.open('product.jl') as f:
class QuotesSpider(scrapy.Spider):ff
   name = "job_network_1"

   def start_requests(self):
       urls = [
           'https://www.ethiojobs.net/browse-by-category/Accounting%20and%20Finance/',
           'https://www.ethiojobs.net/browse-by-category/Admin%2C%20Secretarial%20and%20Clerical/',
           'https://www.ethiojobs.net/browse-by-category/Advertising%20and%20Media/',
           'https://www.ethiojobs.net/browse-by-category/Agriculture/',
           'https://www.ethiojobs.net/browse-by-category/Architecture%20and%20Construction/',
           'https://www.ethiojobs.net/browse-by-category/Automotive/',
           'https://www.ethiojobs.net/browse-by-category/Banking%20and%20Insurance/',
           'https://www.ethiojobs.net/browse-by-category/Business%20Development/',
           'https://www.ethiojobs.net/browse-by-category/Business%20and%20Administration/',
           'https://www.ethiojobs.net/browse-by-category/Civil%20Service%20and%20Government/',
           'https://www.ethiojobs.net/browse-by-category/Communications%2C%20PR%20and%20Journalism/',
           'https://www.ethiojobs.net/browse-by-category/Community%20Service/',
           'https://www.ethiojobs.net/browse-by-category/Consultancy%20and%20Training/',
           'https://www.ethiojobs.net/browse-by-category/Creative%20Arts/',
           'https://www.ethiojobs.net/browse-by-category/Customer%20Service/',
           'https://www.ethiojobs.net/browse-by-category/Development%20and%20Project%20Management/',
           'https://www.ethiojobs.net/browse-by-category/Economics/',
           'https://www.ethiojobs.net/browse-by-category/Education/',
           'https://www.ethiojobs.net/browse-by-category/Energy/',
           'https://www.ethiojobs.net/browse-by-category/Engineering/',
           'https://www.ethiojobs.net/browse-by-category/Entertainment/',
           'https://www.ethiojobs.net/browse-by-category/Environment%20and%20Natural%20Resource/',
           'https://www.ethiojobs.net/browse-by-category/Event%20Management/',
           'https://www.ethiojobs.net/browse-by-category/Health%20Care/',
           'https://www.ethiojobs.net/browse-by-category/Hotel%20and%20Hospitality/',
           'https://www.ethiojobs.net/browse-by-category/Human%20Resource%20and%20Recruitment/',
           'https://www.ethiojobs.net/browse-by-category/Information%20Technology/',
           'https://www.ethiojobs.net/browse-by-category/Inventory%20and%20Stock/',
           'https://www.ethiojobs.net/browse-by-category/Languages/',
           'https://www.ethiojobs.net/browse-by-category/Legal/',
           'https://www.ethiojobs.net/browse-by-category/Logistics%2C%20Transport%20and%20Supply%20Chain/',
           'https://www.ethiojobs.net/browse-by-category/Maintenance/',
           'https://www.ethiojobs.net/browse-by-category/Management/',
           'https://www.ethiojobs.net/browse-by-category/Manufacturing/',
           'https://www.ethiojobs.net/browse-by-category/Media%20and%20Journalism/',
           'https://www.ethiojobs.net/browse-by-category/Natural%20Sciences/',
           'https://www.ethiojobs.net/browse-by-category/Pharmaceutical/',
           'https://www.ethiojobs.net/browse-by-category/Purchasing%20and%20Procurement/',
           'https://www.ethiojobs.net/browse-by-category/Quality%20Assurance/',
           'https://www.ethiojobs.net/browse-by-category/Research%20and%20Development/',
           'https://www.ethiojobs.net/browse-by-category/Retail%2C%20Wholesale%20and%20Distribution/',
           'https://www.ethiojobs.net/browse-by-category/Sales%20and%20Marketing/',
           'https://www.ethiojobs.net/browse-by-category/Science%20and%20Technology/',
           'https://www.ethiojobs.net/browse-by-category/Security/',
           'https://www.ethiojobs.net/browse-by-category/Social%20Sciences%20and%20Community/',
           'https://www.ethiojobs.net/browse-by-category/Strategic%20Planning/',
           'https://www.ethiojobs.net/browse-by-category/Telecommunications/',
           'https://www.ethiojobs.net/browse-by-category/Travel%20and%20Tourism/',
           'https://www.ethiojobs.net/browse-by-category/Veterinary%20Services/',
           'https://www.ethiojobs.net/browse-by-category/Warehouse%2C%20Supply%20Chain%20and%20Distribution/',
           'https://www.ethiojobs.net/browse-by-category/Water%20and%20Sanitation/'
       ]
       i = 1
       for url in urls:
           yield scrapy.Request(url=url, callback=self.sub_sub, meta={'category': i,'urlx':urls[i-1]})
           i = i + 1

   def sub_sub(self, response):
       urlx = response.meta['urlx']
       schema = response.xpath('//script[@type="application/ld+json"]//text()').extract()
       script = ' '.join(response.xpath('//script[@type="application/ld+json"]/title//text()').extract())
       d =script.replace("</script>",",")[:-1]
       f = d.replace("<script type=\"application/ld+json\">", "")
       #myString = f.replace('\"','"').replace('\n\t\'','').replace(' ', '').replace('\t', '').replace('\n', '').replace('\"','')
       category = response.meta['category']
       for p in schema:
           title = p[p.find("\"title\" :"):p.find("\"description\" :")-5][11:]
           employmentType = p[p.find("\"employmentType\"") + 20:p.find("\"hiringOrganization\" :") - 3]
           description =  p[p.find("\"description\" :")+22:p.find("<p><strong>Educational Requirements:</strong>")-8]
           new_desc = p[p.find("\"description\" :")+22:p.find("<p><strong>Educational Requirements:</strong>")-8]
           educationalReq = p[p.find("<p><strong>Educational Requirements:</strong>")+46:p.find("<p><strong>Required Experience:</strong>")-9]
           requiredExperiance = p[p.find("<p><strong>Required Experience:</strong>")+46:p.find("</p>\"")-4]
           company = p[p.find("\"name\":")+9:p.find("\"value\":")-4]
           companyType = p[p.find("\"hiringOrganization\"")+32:p.find("\"hiringOrganization\"")+39]
            #check
           addressLocality = p[p.find("\"addressLocality\" : ")+21:p.find("\"addressRegion\" : ")-3]
           addressRegion = p[p.find("\"addressRegion\" : ")+23:p.find("\"addressCountry\":")-5]
           addressCountry ="ETH"
           datePosted = p[p.find("\"datePosted\" :")+16:p.find("\"validThrough\" : ")-3]
           validTrhrough = p[p.find("\"validThrough\" : ")+18:p.find("\"employmentType\"")-3]
           source ="EthioJobs"
           if (len(title) > 0):
               title = title.replace("'", " ")
               title = title.replace('"', " ")
               title = title.replace(':', " ")
               title = title.replace('&nbsp', " ")
               title = title.replace('&amp', "")
               title = title.replace(';', "")
               title = " ".join(title.split())
           if (len(employmentType) > 0):
               employmentType = employmentType.replace("'", " ")
               employmentType = employmentType.replace('"', " ")
               employmentType = employmentType.replace(':', " ")
               employmentType = employmentType.replace('&nbsp', " ")
               employmentType = employmentType.replace('&amo', "")
               employmentType = employmentType.replace(';', " ")
               employmentType = " ".join(employmentType.split())

           if (len(description) > 0):
               description = description.replace("'", " ")
               description = description.replace('"', " ")
               description = description.replace('<p>', " ")
               description = description.replace('</p>', " ")
               description = description.replace(':', " ")
               description = description.replace('&nbsp', " ")
               description = description.replace('&amp', "")
               description = description.replace(';', " ")
               description = description.replace('<strong>', " ")
               description = description.replace('</strong>', " ")
               description = " ".join(description.split())

           if (len(educationalReq) > 0):
               educationalReq = educationalReq.replace("'", " ")
               educationalReq = educationalReq.replace('"', " ")
               educationalReq = educationalReq.replace(':', " ")
               educationalReq = educationalReq.replace('&nbsp', " ")
               educationalReq = educationalReq.replace('&amp', " ")
               educationalReq = educationalReq.replace(';', " ")
               educationalReq = " ".join(educationalReq.split())

           if (len(requiredExperiance) > 0):
               requiredExperiance = requiredExperiance.replace("'", " ")
               requiredExperiance = requiredExperiance.replace('"', " ")
               requiredExperiance = requiredExperiance.replace(':', " ")
               requiredExperiance = requiredExperiance.replace('&nbsp', " ")
               requiredExperiance = requiredExperiance.replace('&amp', " ")
               requiredExperiance = requiredExperiance.replace(';', "")
               requiredExperiance = " ".join(requiredExperiance.split())

           if (len(company) > 0):
               company = company.replace("'", " ")
               company = company.replace('"', " ")
               company = company.replace(':', " ")
               company = company.replace('&nbsp', " ")
               company = company.replace('&amp', " ")
               company = company.replace(';', "")
               requiredExperiance = " ".join(requiredExperiance.split())

           if (len(companyType) > 0):
               companyType = companyType.replace("'", " ")
               companyType = companyType.replace(":", " ")
               companyType = companyType.replace('"', " ")
               companyType = companyType.replace('&nbsp', " ")
               companyType = companyType.replace('&amp', "")
               companyType = companyType.replace(';', " ")
               companyType = " ".join(companyType.split())

           if (len(addressLocality)):
               addressLocality = addressLocality.replace("'", " ")
               addressLocality = addressLocality.replace('"', " ")
               addressLocality = addressLocality.replace(':', " ")
               addressLocality = addressLocality.replace('&nbsp', " ")
               addressLocality = addressLocality.replace('&amp', "")
               addressLocality = addressLocality.replace(';', "")
               addressLocality = " ".join(addressLocality.split())

           if (len(addressRegion)):
               addressRegion = addressRegion.replace("'", " ")
               addressRegion = addressRegion.replace('"', " ")
               addressRegion = addressRegion.replace(':', " ")
               addressRegion = addressRegion.replace('&nbsp', " ")
               addressRegion = addressRegion.replace('&amp', " ")
               addressRegion = addressRegion.replace(';', " ")
               addressRegion = " ".join(addressRegion.split())

           if (len(addressCountry)):
               addressCountry = addressCountry.replace("'", " ")
               addressCountry = addressCountry.replace('"', " ")
               addressCountry = addressCountry.replace(':', " ")
               addressCountry = addressCountry.replace('&nbsp', " ")
               addressCountry = addressCountry.replace('&amp', " ")
               addressCountry = addressCountry.replace(';', "")
               addressCountry = " ".join(addressCountry.split())

           if (len(datePosted) > 0):
               datePosted = datePosted.replace("'", " ")
               datePosted = datePosted.replace('"', " ")
               datePosted = datePosted.replace('&nbsp', " ")
               datePosted = datePosted.replace('&amp', " ")
               datePosted = " ".join(datePosted.split())

           if (len(validTrhrough) > 0):
               validTrhrough = validTrhrough.replace("'", " ")
               validTrhrough = validTrhrough.replace('"', " ")
               validTrhrough = validTrhrough.replace(';', " ")
               validTrhrough = validTrhrough.replace('&nbsp', " ")
               validTrhrough = validTrhrough.replace('&amp', " ")
               validTrhrough = " ".join(validTrhrough.split())

           id_key = title+validTrhrough

           if id_key in arr:
              print(id_key)
           else:
            print("new ")
            with jsonlines.open('job_index_new3.jl', mode='a') as f:
                f.write({
                           "category": category,
                           "title": title,
                           "employmentType": employmentType,
                           "description": description,
                           "educationalReq": educationalReq,
                           "requiredExperiance": requiredExperiance,
                           "company": company,
                           "companyType": companyType,
                           "addressLocality": addressLocality,
                           "addressRegion": addressRegion,
                           "addressCountry": addressCountry,
                           "datePosted": datePosted,
                           "validTrhrough": validTrhrough,
                           "source": source
                       })
                data = {
                            'id': '1',
                            'category': category,
                           'title': title,
                           'employmentType': employmentType,
                           'description': description ,
                           'educationalReq': educationalReq,
                           'requiredExperiance': requiredExperiance,
                           'company': company,
                           'companyType': companyType,
                           'addressLocality': addressLocality,
                           'addressRegion': addressRegion,
                           'addressCountry': addressCountry,
                           'datePosted': datePosted,
                           'validTrhrough': validTrhrough,
                           'source': source
                       }
                r = requests.post(url="http://www.afalagi.biranaspace.com/back_end/add_job_and_notify",
                                  data=json.dumps(data),
                                  headers={
                                      'Content-type':'application/json',
                                      'Authorization': 'access_token myToken'
                                  })
                pastebin_url = r.text
                print("The pastebin URL is:%s" % pastebin_url)
           yield {
           "category":category,
           "title":title,
           "employmentType":employmentType,
           "description":description,
           "educationalReq":educationalReq,
           "requiredExperiance":requiredExperiance,
           "company":company,
           "companyType":companyType,
           # check
           "addressLocality":addressLocality,
           "addressRegion":addressRegion,
           "addressCountry":addressCountry,
           "datePosted":datePosted,
           "validTrhrough":validTrhrough,
           "source":source
           }
       next_page = response.css('ul.pagination a::attr(href)').get()
       if next_page is not None:
           nx = urlx+next_page
           yield scrapy.Request(url=nx, callback=self.sub_sub, meta={'category': category,'urlx':urlx})
