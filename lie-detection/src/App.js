import React from 'react';
import Signup from './components/SignUp';
import Login from './components/Login';
import Home from './components/Home';
import 'bootstrap/dist/css/bootstrap.min.css';
import { Routes, Route, BrowserRouter } from 'react-router-dom';
import './App.css';
import LieTest from './components/LieTest';
import Logout from './components/Logout';

function App() {
  return (
    <BrowserRouter >
      <Routes>
        <Route path="/signup" element={<Signup />} />
        <Route path="/login" element={<Login />} />
        <Route path="/lietest" element={<LieTest />} />
        <Route path='/logout' element={<Logout />} />
        <Route path="/" element={<Home />} />
      </Routes>
    </BrowserRouter>
  )
}

export default App;
