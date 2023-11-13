import express from 'express'; 
import fs from 'fs'; 

const app = express(); 
app.use(express.static("pynums"))
app.get("/nums.txt", (req, res) => {
    fs.readFile("nums.txt", (err, data) => {
        if(err){
            res.writeHead(404, 'content-type', "text/plain"); 
            return res.end("404, not found"); 
        }
        res.writeHead(200, {'content-type': "text/plain"}); 
        res.write(data); 
        res.end();
    })
}).listen(8080, () => console.log("http://127.0.0.1:8080/nums.txt"));