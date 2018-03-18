# REVIEWOR.org testing tools and steps

[REVIEWOR.org](https://www.reviewor.org) is a website for reviewing technology services
such as web hosting and wordpress providers. This project contains the testing methodology
and tools for reviewing technology services with a data-driven approach.

## Wordpress hosting review approach
A wordpress host is reviewed on following criteria:
* Performance
* Uptime
* Price
* Usability
* Support

For each provider the following steps will be taken:
1. Deploy wordpress with sample data(posts, pages, comments etc)
1. Run locust for a load test to simulate concurrent users
1. Run GTMetrix to gather data on speed of actual user
1. Setup checkup to do continious uptime monitoring for additional website
1. File a support ticket asking the provider to change the theme

The results of running above steps will be stored in this repository.

## Importing test data into WordPress
[Source docs](https://codex.wordpress.org/Theme_Unit_Test)
1. Import test data(test-data.xml) into your WordPress install by going to Tools => Import => WordPress
1. Select the XML file from your computer
1. Click on "Upload file and import".
1. Under "Import Attachments," check the "Download and import file attachments" box and click submit.
