import os,sys
from sfdclib import SfdcSession,SfdcMetadataApi

if os.stat('log.txt').st_size == 0 :
	print('No Tests Run')
else:
	load_profile = open('log.txt', "r")
	read_it = load_profile.read()
	async_id = ""
	for line in read_it.splitlines():
	    if  "Request ID for the current deploy task:" in line:
	        async_id = line.split("Request ID for the current deploy task: ")[1]
	        break
	print("The deployment ID is %s" % async_id)
	_XML_NAMESPACES = {
	    'soapenv': 'http://schemas.xmlsoap.org/soap/envelope/',
	    'mt': 'http://soap.sforce.com/2006/04/metadata'
	}

	s = SfdcSession(
	    sys.argv[1],
	    sys.argv[2],
	    sys.argv[3],
	    True,# isSandbox
	    '40.0' # api version
	)
	s.login()
	metadata = SfdcMetadataApi(s)
	totalLines = 0
	notCoveredLines = 0
	result = metadata._retrieve_deploy_result(async_id)
	coverages = result.findall('mt:details/mt:runTestResult/mt:codeCoverage',_XML_NAMESPACES)
	print('===============================================================')
	for coverage in coverages:
		line = float(coverage.find('mt:numLocations',_XML_NAMESPACES).text)
		notCoveredLine = float(coverage.find('mt:numLocationsNotCovered',_XML_NAMESPACES).text)
		if line == 0:
			oneCov = 0.0
		else:
			oneCov = (1 - (notCoveredLine/line)) * 100
		print('%s coverage is %.2f' % (coverage.find('mt:name',_XML_NAMESPACES).text,oneCov))
		totalLines += line
		notCoveredLines += notCoveredLine
	codeCoverage = (1 - (notCoveredLines/totalLines)) * 100
	print('===============================================================')
	print('\n')
	print('**************************************')
	print('*                                    *')
	print('* Total Code Coverage:    %.2f      *' % codeCoverage)
	print('*                                    *')
	print('**************************************')