# ApexTestCoverage

This is a simple Python3 Script to get Apex Test Coverage from Salesforce deployment ID.

Just got the inspiration from [How to get accurate code coverage from Metadata API](https://help.salesforce.com/articleView?id=How-to-get-accurate-code-coverage-from-Metadata-API&language=en_US&type=1).

The code will get the deployment ID(also known as asyncId) from the log file. So you need to generage a log file named "log.txt" during your salesforce running test task through [ant](http://ant.apache.org) and [Salesforce Force.com Migration Tool](https://developer.salesforce.com/docs/atlas.en-us.daas.meta/daas/meta_development.htm).

An easy way is to add a [record](https://ant.apache.org/manual/Tasks/recorder.html) in the ant task.

And once you have the log.txt, you can just get the code coverage by this script. The script need three parameters:

1. Salesforce username
2. Salesforce password
3. Salesforce security token



Thanks for: 

[sfdclib](https://github.com/rbauction/sfdclib):[Package Index](https://pypi.python.org/pypi/sfdclib)