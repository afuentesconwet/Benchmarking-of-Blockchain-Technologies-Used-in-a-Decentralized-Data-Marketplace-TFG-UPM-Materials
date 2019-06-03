const DatasetRegistry = require('../datasetRegistry')
const OfferingRegistry = require('../offeringRegistry')
const PaymentCompletedRegistry = require('../paymentCompleted')
const AgreementRegistry = require('../agreementRegistry')

const uuidv4 = require('uuid/v4');

const dataApiUri = "http://localhost:7000"

async function createNDatasets(n) {
    var data = require('./benchmark-assets/dataset')
    var req;
    var ids = []
    for(var i = 0; i < n; i++){
        ids.push(uuidv4().substr(0,6))
    }
    //console.log(ids)
    for (var i = 0; i < n; i++) {
        //console.log("UUUGH")
        var d = new DatasetRegistry()
        var jobId = uuidv4();
        data.$class = "org.conwet.biznet.CreateDataset"
        data.jobId = jobId
        data.datasetId = ids[i]
        req = {
            uri: dataApiUri + '/datasets/',
            body: data,
            method: 'POST',
            headers: {
                'Content-Type': "application/json"
            }
        };
        await d.createDataset(req, jobId)
    }
}

async function createNOfferings(n){
    var data = require('./benchmark-assets/offering')
    var req;
    var ids = []
    for(var i = 0; i < n; i++){
        ids.push(uuidv4().substr(0,6))
    }
    //console.log(ids)
    for (var i = 0; i < n; i++) {
        var o = new OfferingRegistry()
        var jobId = uuidv4();
        data.$class = "org.conwet.biznet.CreateOffering"
        data.jobId = jobId
        data.offeringId = ids[i]
        req = {
            uri: dataApiUri + '/offerings/',
            body: data,
            method: 'POST',
            headers: {
                'Content-Type': "application/json"
            }
        };
        //console.log("LLAMADA")
        await o.createOffering(req, jobId)
    }
}

async function createPaymentCompleted(){
    //console.log("pag")
    var data = require('./benchmark-assets/paymentcompleted')
    var jobId = uuidv4()
    data.jobId = jobId
    var p = new PaymentCompletedRegistry();
    var start = new Date()
    var simulateTime = 1000
    //console.log(data)
    var start = new Date()
    await p.completePayment(data, jobId)
}

async function createAcquisition(){
    var data = require('./benchmark-assets/onetimeaqc')
    var req;
    var a = new AgreementRegistry()
    var jobId = uuidv4();
    data.$class = "org.conwet.biznet.MakeAgreement"
    data.jobId = jobId
    data.agreementId = uuidv4().substr(0,6)
    req = {
        uri: dataApiUri + '/acquisitions/',
        body: data,
        method: 'POST',
        headers: {
            'Content-Type': "application/json"
        }
    };
    await
    a.createAgreement(req, jobId)
}

async function createAcceptAgreement(){
    var a = new AgreementRegistry()
    var start = new Date()
    var simulateTime = 1000
    var jobId = uuidv4();
    var start = new Date()
    await
        a.acceptAgreement("aydear5",jobId)
}

async  function createNOneTimeAgreements(n) {
    for(var i = 0; i < n; i++){
        await createAcquisition()
        await createPaymentCompleted()
        await createAcceptAgreement()
    }
}


var args = process.argv.slice(2)
if(args.length % 2 != 0) {
    console.log("ERR")
    process.exit(1)
}
args = args.reduce(function(result, value, index, array) {
    if (index % 2 === 0)
        result.push(array.slice(index, index + 2));
    return result;
}, []);

//console.log(args)

for (var i = 0; i < args.length; i++) {
    if (args[i][0] == '-d') {
        createNDatasets(args[i][1])
    } else if (args[i][0] == '-o') {
        createNOfferings(args[i][1])
    } else if (args[i][0] == '-ao') {
        createNOneTimeAgreements(args[i][1])
    } else if (args[i][0] == '-as') {
        createNSubscriptionAgreements(args[i][1])
    } else if (args[i][0] == '-au') {
        createNUsageAgreements(arg[i][1])
    }
}
