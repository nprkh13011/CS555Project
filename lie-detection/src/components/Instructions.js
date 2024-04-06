import React from 'react';
import { useNavigate } from 'react-router-dom';

const InstructionsPage = () => {
    const navigate = useNavigate()
    
    return (
        <div className="d-flex justify-content-center align-items-center vh-100">
            <div className="peach p-3 rounded w-50 h-70 text-center teal" style={{ width: '50%' }}>
                <h1 className="mb-4">How Does This Work?</h1>
                <p>You will be presented with images of professors and asked "Have you taken a class with this professor?"</p>
                <p>You will be given the option to choose "Yes" or "No".</p>
                <p>Afterwards, you will be asked "Would you recommend the class with the professor?" and again choose either "Yes" or "No".</p>
                <p>At the end, a ranking of professors will be displayed.</p>
                <div className="mb-3">
                    <button className="btn btn-success rounded" onClick={() => navigate('/lietest')}>Continue</button>
                </div>
            </div>
        </div>
    );
};

export default InstructionsPage;

