import express from 'express';
import path from 'path';
import bodyParser from 'body-parser';
import multer from 'multer';
import fs from 'fs';
import exec from 'child_process';
import ejs from 'ejs';

let JSONResult = '';
const upload = multer({
    dest: 'uploads/'
});
const app = express();
var urlencodedParser = bodyParser.urlencoded({ extended: false })
const __dirname = "./"
var type = upload.single('registry-path');
app.use(express.static(__dirname));
app.set('views', __dirname);
app.engine('html', ejs.renderFile);
app.set('view engine', 'ejs');

app.get('/', (req, res) => {
    res.render('index.ejs',{msg:JSON.stringify(JSONResult)} );
});

function execPythonApi(filepath, type, res) {
    console.log(`python api.py ${type} ${filepath}`);
    exec.exec(`python api.py ${type} ${filepath}`, (error, stdout, stderr) => {
        if (error) {
            console.log(`error: ${error.message}`);
            return;
        }
        if (stderr) {
            console.log(`stderr: ${stderr}`);
            return;
        }
        console.log(stdout);
        console.log(stdout.trim());
        if (stdout.trim() == 'success') {
            console.log("Success generate JSON file");
            let jsonFile = "";
            if (type == 'NTUSER'){
                jsonFile = 'ntuser_json.json';
            }
            else if (type == 'SYSTEM'){
                jsonFile = 'system_json.json';

            }
            else if (type == 'SOFTWARE'){
                jsonFile = 'software_json.json';

            }
            fs.readFile('./' + jsonFile, 'utf8', function (err, data) {
                if (err) {
                    return console.log(err);
                }else{
                    console.log(data);
                    JSONResult = data;
                }
            });
            res.send(`
                <img alt="Loading GIFs - Get the best GIF on GIPHY" class="n3VNCb" src="https://media2.giphy.com/media/3oEjI6SIIHBdRxXI40/200.gif" data-noaft="1" jsname="HiaYvf" jsaction="load:XAeZkd;" style="width: 200px; height: 200px; margin: 89.6px 0px;">
                <script>
                    alert('Upload Success! please wait to extract registry you will redirect to home')
                    setTimeout( ()=>{
                    document.location.href = document.location.origin+'?status=ready'
                    }, 3000);
                </script>`);
        } else {
            console.log("Failed to generate Json :(");
            return;
        }
    });
}

app.post('/upload', type, (req, res) => {
    if (req.body['registry-type'] != undefined && req.file['fieldname'] != undefined) {
        var file = path.join(__dirname, 'uploads', req.body['registry-type'] + ".dat")
        fs.rename(req.file.path, file, function (err) {
            if (err) {
                console.log(err);
            } else {
                let registryType = req.body['registry-type'];
                console.log(file);
                console.log(registryType);
                execPythonApi(file, registryType, res);
            }
        })
    } else {
        res.send(`
        <script>
            alert('Upload Failed!')
            document.location.href = document.location.origin
        </script>
        `)
    }
});

app.listen(3000, () =>
    console.log('Example app listening on port 3000!'),
);