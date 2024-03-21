import { useState } from 'react';
import '../components/Home.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import { Link, useNavigate } from 'react-router-dom';
import Logo from '../img/FibFinders_Logo.png';

const Home = () => {
    const navigate = useNavigate()
    
    return (
        <div className="d-flex justify-content-center align-items-center bg-white vh-100">
            <div className="peach p-3 rounded w-25 text-center teal">
            <img src={Logo} alt="FibFinders Logo" className="mb-3 rounded" style={{ maxWidth: "150px" }} />
            <h2>Home</h2>
            <div className="mb-3">
            <button className="btn btn-primary rounded" onClick={() => navigate('/signup')}>Sign Up</button>
            </div>
            <div className="mb-3">
            <button className="btn btn-primary rounded" onClick={() => navigate('/login')}>Login</button>
            </div>
        </div>
        </div>
    )
}

export default Home;