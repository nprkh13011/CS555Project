import React from 'react';
import Signup from './components/SignUp';
import Login from './components/Login';
import About from './components/About';
import 'bootstrap/dist/css/bootstrap.min.css';
import { Routes, Route, BrowserRouter } from 'react-router-dom';
import './App.css';
import LieTest from './components/LieTest';
import Logout from './components/Logout';
import Home from './components/Home';

function App() {
  return (
    <BrowserRouter >
      <Routes>
        <Route path="/signup" element={<Signup />} />
        <Route path="/login" element={<Login />} />
        <Route path="/lietest" element={<LieTest />} />
        <Route path='/logout' element={<Logout />} />
        <Route path='/home' element={<Home />} />
        <Route path="/" element={<About />} />
      </Routes>
    </BrowserRouter>
  )
}

export default App;
