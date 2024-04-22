import React, { useState, useEffect} from 'react';
import Signup from './components/SignUp.js';
import Login from './components/Login.js';
import About from './components/About.js';
import 'bootstrap/dist/css/bootstrap.min.css';
import { Routes, Route, BrowserRouter } from 'react-router-dom';
import './App.css';
import LieTest from './components/LieTest.js';
import Logout from './components/Logout.js';
import Home from './components/Home.js';
import InstructionsPage from './components/Instructions.js';
import Rankings from './components/Rankings.js';
import ResultsPage from './components/Results.js';

function App() {
  // const [results, setResults] = useState([])

  // useEffect(() => {
  //   fetchResults()
  // }, [])

  // const fetchResults = async () => {
  //   const response = await fetch("http://127.0.0.1:5000/results")
  //   const data = await response.json()
  //   setResults(data.results)
  //   console.log(data.results)
  // }

  return (
    <BrowserRouter >
      <Routes>
        <Route path="/signup" element={<Signup />} />
        <Route path="/login" element={<Login />} />
        <Route path="/lietest" element={<LieTest />} />
        <Route path='/logout' element={<Logout />} />
        <Route path='/home' element={<Home />} />
        <Route path="/" element={<About />} />
        <Route path="/instructions" element={<InstructionsPage />} />
        <Route path="/rankings" element={<Rankings />} />
        <Route path="/results" element={<ResultsPage />} />
      </Routes>
    </BrowserRouter>
  )
}

export default App;
