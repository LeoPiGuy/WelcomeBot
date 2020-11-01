const Discord = require('discord.js');
const exec = require('child_process').execFile;
const client = new Discord.Client();

client.on('ready', () => {
  console.log(`Logged in as ${client.user.tag}!`);
});

client.on('message', msg => {
    if (msg.channel.id == 709914520914624573) {
        if (msg.embeds.length != 0) {
            if (msg.embeds[0].description.includes("h!trick")) {
                console.log("TRICK");
                trick();
            }
            if (msg.embeds[0].description.includes("h!treat")) {
                console.log("TREAT");
                treat();
            }
        }
    }
});

function trick() {
    exec('trick.exe', function(err, data) {  
        console.log(err)
        console.log(data.toString());                       
    });  
}

function treat() {
    exec('treat.exe', function(err, data) {  
        console.log(err)
        console.log(data.toString());                       
    });  
}

client.login('token_here');