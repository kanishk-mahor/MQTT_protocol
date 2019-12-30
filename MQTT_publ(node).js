/////////////////code to connect to broker /////////////////

var mqtt = require('mqtt')
var client= mqtt.connect('mqtt://localhost')
client.on('connect',function(){
console.log("client connected")


client.publish('/get:id',(req, res) => {
    // console.log(req.body)
      res.send(cal_load());
 })
})
