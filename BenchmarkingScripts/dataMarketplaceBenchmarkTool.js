var request = require('request')
var updateBody = require('./bodyUpdate.json')

var val = 0
var orgName = "org1"


function updateData(){
	if(val == 65000)
		val = 0

	updateBody.rain.value = val;
	val++;

	var cuerpoStr = JSON.stringify(updateBody)
	var brokerTransaction = {
		uri: "http://localhost:1030/v2/entities/Weather/attrs/",
        	body: JSON.stringify(updateBody),
        	method: 'PATCH',
        	headers: {
        		'Content-Type': 'application/json',
        		'Fiware-Service': orgName,       //TODO: It is not received in the query through the channel. D:
        		'Content-Length': cuerpoStr.length
        	}
	}

	request(brokerTransaction)

}

setInterval(updateData, 1500)
