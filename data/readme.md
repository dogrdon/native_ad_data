Native Ad Data Description
==========================

### ./in/native_ad_data.csv

This is the raw data dump from 3 months (2017-03-27 to 2017-07-07) of collecting native ad data from around the web via crawler.

#### Schema

**_id**: mongodb unique id for record

**headline**: The headline text associated with with the ad content

**link**: The URL of the native ad content as rendered from the site it is found at

**img**: img src url for the image associated with the native ad content

**provider**: The Native ad content provider (e.g., Taboola, Outbrain, Zergnet, or Revcontent)

**source**: The website where the native ad was first found (e.g., http://www.tmz.com, http://breitbart.com)

**img_file**: A hash of the `img` column and file extension for the file as it sits on the filesystem it was downloaded to

**date**: Date the item was collected

**final_link**: If link to the actual native ad content redirected to another url, it should be this, but this was not always successfully obtained

**orig_article**: The url to the article where the native ad content was found


### ./out/2017-08-30-01_47_native_ad_data_deduped.csv

csv dump of native ad data above after it was loaded into the [analysis notebook]() and processed and cleaned for analysis including deduping and generating addional columns from existing columns.

#### Schema

**_id**: mongodb unique id for record

**headline**: The headline text associated with with the ad content

**link**: The URL of the native ad content as rendered from the site it is found at

**img**: img src url for the image associated with the native ad content

**provider**: The Native ad content provider (e.g., Taboola, Outbrain, Zergnet, or Revcontent)

**source**: The website where the native ad was first found (e.g., http://www.tmz.com, http://breitbart.com)

**img_file**: A hash of the `img` column and file extension for the file as it sits on the filesystem it was downloaded to

**date**: Date the item was collected

**final_link**: If link to the actual native ad content redirected to another url, it should be this, but this was not always successfully obtained

**orig_article**: The url to the article where the native ad content was found

**img_host**: Host only from the url at `img`

**link_host**: Host only for the url at `link`

**source_class**: A roughly estimated political classification based on the source of the content where the native ad was found (e.g., Left, Right, Center, Tabloid)*

*A note on the classfications: Left = Left or progressive leaning, Right = Right or conservative learning, Center = Attempts to report without clear political bias, Tabloid = Website that reports largely on entertainment and lifestyle news, without concern for political affiliation.


### ./out/headlines_grouped_data.json

JSON file where each record is a unique entry from the `headline` column in the deduped csv file and associated entries from other columns are grouped in lists.


	{
	    "20 Cool Moments From Joe Biden\u2019s Time In Office": {
	        "img_urls": [
	            "https://console.brax-cdn.com/creatives/98c6400e-f2fc-4c28-8e00-6c45914e36d5/TB15_1b309a68a23702cb95e743cea5d60029.600x500.png"
	        ],
	        "dates": [
	            "2017-03-27T12:59:09.279Z"
	        ],
	        "sources": [
	            "http://tmz.com"
	        ],
	        "providers": [
	            "taboola"
	        ],
	        "classifications": [
	            "tabloid"
	        ],
	        "imgs": [
	            "876aa5e83f6fb81a81908db3c02fdcc00d444000.png"
	        ],
	        "locations": [
	            "http://scribol.com/a/news-and-politics/ways-joe-biden-made-vice-presidency-cool-again-americas-uncle/?utm_source=Taboola&utm_medium=CPC&utm_campaign=Joe_Biden_Cool_VP_US_Desktop&utm_content=tmz"
	        ]
	    },
	    "25 Pics Donald Trump Doesn't Want You To See": {
	        "img_urls": [
	            "http://cdn.taboolasyndication.com/libtrc/static/thumbnails/b13e719e4aff1daf7284c9bdb61e65a1.png"
	        ],
	        "dates": [
	            "2017-03-27T12:59:13.038Z"
	        ],
	        "sources": [
	            "http://tmz.com"
	        ],
	        "providers": [
	            "taboola"
	        ],
	        "classifications": [
	            "tabloid"
	        ],
	        "imgs": [
	            "d3a3f2f50c84529c08bb8314ae3aa66280f0cbc7.png"
	        ],
	        "locations": [
	            "http://detonate.com/pictures-that-trump-would-rather-keep-secret/?utm_source=8b4&utm_campaign=8b4_US_desktop_Trump_12_54f7_20160725_mm_3407&utm_term=tmz&utm_medium=cpc"
	        ]
	    }
	}

### ./out/images_grouped_data.json

JSON file where each record is a unique entry from the `img_file` column in the deduped csv file and associated entries from other columns are grouped in lists.

	{
	    "876aa5e83f6fb81a81908db3c02fdcc00d444000.png": {
	        "url": "https://console.brax-cdn.com/creatives/98c6400e-f2fc-4c28-8e00-6c45914e36d5/TB15_1b309a68a23702cb95e743cea5d60029.600x500.png",
	        "dates": [
	            "2017-03-27T12:59:09.279Z"
	        ],
	        "sources": [
	            "http://tmz.com"
	        ],
	        "providers": [
	            "taboola"
	        ],
	        "classifications": [
	            "tabloid"
	        ],
	        "headlines": [
	            "20 Cool Moments From Joe Biden\u2019s Time In Office"
	        ],
	        "locations": [
	            "http://scribol.com/a/news-and-politics/ways-joe-biden-made-vice-presidency-cool-again-americas-uncle/?utm_source=Taboola&utm_medium=CPC&utm_campaign=Joe_Biden_Cool_VP_US_Desktop&utm_content=tmz"
	        ]
	    },
	    "d3a3f2f50c84529c08bb8314ae3aa66280f0cbc7.png": {
	        "url": "http://cdn.taboolasyndication.com/libtrc/static/thumbnails/b13e719e4aff1daf7284c9bdb61e65a1.png",
	        "dates": [
	            "2017-03-27T12:59:13.038Z"
	        ],
	        "sources": [
	            "http://tmz.com"
	        ],
	        "providers": [
	            "taboola"
	        ],
	        "classifications": [
	            "tabloid"
	        ],
	        "headlines": [
	            "25 Pics Donald Trump Doesn't Want You To See"
	        ],
	        "locations": [
	            "http://detonate.com/pictures-that-trump-would-rather-keep-secret/?utm_source=8b4&utm_campaign=8b4_US_desktop_Trump_12_54f7_20160725_mm_3407&utm_term=tmz&utm_medium=cpc"
	        ]
	    }
	}