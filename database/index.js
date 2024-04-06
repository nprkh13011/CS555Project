const express = require('express')
const mongoose = require('mongoose')
const cors = require('cors')
const UserModel = require('./models/Users')
// const bcrypt = require('bcrypt');

const app = express()
app.use(cors())
app.use(express.json())

mongoose.connect("mongodb://127.0.0.1:27017/lie-detector")

app.post('/signup', async (req, res) => {
    UserModel.create(req.body)
    .then(users => res.json(users))
    .catch(err => res.json(err))
})

app.post('/check-email', async (req, res) => {
    const { email } = req.body;
    try {
        const user = await UserModel.findOne({ email });
        if (user) {
            res.json({ exists: true });
        } else {
            res.json({ exists: false });
        }
    } catch (err) {
        res.json(err);
    }
})
app.post('/login', async (req, res) => {
    const { email, password } = req.body;
    try {
        const user = await UserModel.findOne({ email });
        if (user) {
            console.log(password)
            
            if (user.password !== password){
                console.log("hi")
                res.json({ exists: false });
            }
            else{
                res.json({ exists: true });
            }
        } else {
            
            res.json({ exists: false });
        }
    } catch (err) {
        res.json(err);
    }
})

app.listen(3001, () => {
    console.log("Server is running on http://localhost:3001")
})