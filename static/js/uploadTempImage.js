// const { google } = require('googleapis');
// const dotenv = require('dotenv');
// const path = require("path")
// const { fileURLToPath } = require('url')

import { google } from "googleapis"
import dotenv from 'dotenv';
import path from "path"
import { fileURLToPath } from 'url';

dotenv.config();

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const KEYFILEPATH = path.join(__dirname, "credentials.json");
const SCOPES = ["https://www.googleapis.com/auth/drive"];

const auth = new google.auth.GoogleAuth({
    keyFile: KEYFILEPATH,
    scopes: SCOPES,
});

export async function uploadFile (fileObject) {
    try {
        console.log(fileObject)
        const { data } = await google.drive({ version: "v3", auth }).files.create({
            media: {
                mimeType: fileObject.mimeType,
                body: fs.createReadStream(fileObject.path),
            },
            requestBody: {
                name: fileObject.filename,
                parents: [process.env.TEMP_FOLDER],
            },
            fields: "id,name",
        });

        console.log(`Uploaded file ${data.name} ${data.id}`);
    } catch (err) {
        console.log(err)
    }
};


// export default uploadFile