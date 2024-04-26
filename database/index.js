const express = require('express')
const mongoose = require('mongoose')
const cors = require('cors')
const UserModel = require('./models/Users')
const ProfessorModel = require('./models/Professor')
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
            
            if (user.password !== password){
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
app.post('/update-professor', async (req, res) => {
    const { professorIndex, hasSeenProfessor } = req.body;
    try {
        let professor = await ProfessorModel.findOne({ index: professorIndex });
        if (!professor) {
            professor = await ProfessorModel.create({ index: professorIndex });
        }
            professor.totalTests++;
        if (hasSeenProfessor) {
            professor.trueResponses++;
        }
        await professor.save();
        res.json({ success: true });
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
})
app.get('/professors', async (req, res) => {
    try {
        // Fetch the professor data from the database
        const professors = await ProfessorModel.find();

        // Send the retrieved data as a response
        res.json(professors);
    } catch (error) {
        // Handle errors
        console.error('Error fetching professors:', error);
        res.status(500).json({ error: 'Internal Server Error' });
    }
})




app.listen(3001, () => {
    console.log("Server is running on http://localhost:3001")
})