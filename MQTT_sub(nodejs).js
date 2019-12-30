/////////////////////////////code by KANISHK MAHOR///////////////////////

var mqtt = require('mqtt')
var client = mqtt.connect('mqtt://192.168.75.xxx')

client.on('connect', function () {

client.subscribe('room/load/1m')
client.subscribe('client/dead') // subscribing to the topic for abruptly disconnecting
})


client.on('message', function (topic, message) {
  // message here is used as buffer

  console.log(message.toString())
})
