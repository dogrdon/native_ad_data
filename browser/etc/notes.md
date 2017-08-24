theothercontent browser notes:
==============================

### Import of data to mongo after deduped

Where we are running a mongo db `native_ads` with a collection called `ads` and a csv file named `native_ad_data_deduped.csv`

    mongoimport -d native_ads -c ads --type csv --file native_ad_data_deduped.csv --headerline

### Set up elasticsearch

#### Mac OSX

- Install on mac with `brew install elasticsearch`
- start service with `brew services start elasticsearch`
- make sure running at localhost:9200 (or whatever port if you change that)


### Create index (via command line, with elasticsearch running on machine)

	curl -XPUT 'localhost:9200/toc?pretty' -H 'Content-Type: application/json' -d'
	{
	    "settings" : {
	        "index" : {
	            "number_of_shards" : 1,
	            "number_of_replicas" : 1
	        }
	    }
	}'


### Insert a record

	curl -XPUT 'localhost:9200/toc/test/1?pretty' -H 'Conent-Type:application/json' -d'
	{
		"headline" : "20 Cool Moments From Joe Biden’s Time In Office",
		"link" : "http://scribol.com/a/news-and-politics/ways-joe-biden-made-vice-presidency-cool-again-americas-uncle/?utm_source=Taboola&utm_medium=CPC&utm_campaign=Joe_Biden_Cool_VP_US_Desktop&utm_content=tmz",
		"img" : "https://console.brax-cdn.com/creatives/98c6400e-f2fc-4c28-8e00-6c45914e36d5/TB15_1b309a68a23702cb95e743cea5d60029.600x500.png",
		"provider" : "taboola",
		"source" : "http://tmz.com",
		"img_file" : "876aa5e83f6fb81a81908db3c02fdcc00d444000.png",
		"final_link" : "http://scribol.com/a/news-and-politics/ways-joe-biden-made-vice-presidency-cool-again-americas-uncle/?utm_source=Taboola&utm_medium=CPC&utm_campaign=Joe_Biden_Cool_VP_US_Desktop&utm_content=tmz",
		"orig_article" : "",
		"date" : "2017-03-27",
		"img_host" : "console.brax-cdn.com",
		"link_host" : "scribol.com"
	}'

### Bulk index (see [./bulktest.json]() for format)

	curl -XPUT 'localhost:9200/toc/test/_bulk' -H 'Conent-Type:application/json' --data-binary @bulktest.json

### Perform some searches

`http://localhost:9200/toc/test/_search?pretty&q=link_host:*.*`
`http://localhost:9200/toc/test/_search?pretty&q=headline:lotto`
`http://localhost:9200/toc/test/_search?pretty&q=cool`

### Bulk index from mongo using python

run `python ./indexes.py`


