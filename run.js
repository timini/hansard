'use strict'
const spawn = require('child_process').spawn;
const exec = require('child_process').exec;


const events = spawn('docker', ['events', '-f', 'container=hansard_api'])
const compose = spawn('docker-compose', ['up'])

compose.stdout.on('data', (data) => {
  console.log(data.toString());
})

compose.stderr.on('data', (data) => {
  console.log(data.toString());
})

events.stdout.on('data', (data) => {
  if (data.toString().indexOf('attach') !== -1){
    exec('docker exec hansard_api_1 python api/manage.py migrate', (error, stdout, stderr) =>{
      console.log(stdout)
      console.log(stderr)
    })
  }
});
